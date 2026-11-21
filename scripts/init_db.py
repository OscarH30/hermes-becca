#!/usr/bin/env python3
"""Create Becca's local prospect database.

Always run at onboarding. This is Becca's internal store, whether or not a CRM,
a CSV or a Google Sheet is connected. It holds the send log, the campaigns and
their approvals, and the dedupe index. It answers "have we already emailed this
person?" without a network call, which is what keeps Becca from emailing anyone
twice.

Safe to re-run: every statement is CREATE ... IF NOT EXISTS, and the migration
only adds columns that are missing. An existing prospects.db from an earlier
version is upgraded in place.

Usage:
    python3 scripts/init_db.py              create or upgrade prospects.db
    python3 scripts/init_db.py --db PATH    use a different database file
    python3 scripts/init_db.py --help       show this help (creates nothing)
"""
import argparse
import sqlite3
import sys
from pathlib import Path

DEFAULT_DB = Path(__file__).resolve().parent.parent / "prospects.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS prospects (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    email             TEXT NOT NULL UNIQUE COLLATE NOCASE,
    first_name        TEXT,
    last_name         TEXT,
    title             TEXT,
    company           TEXT,
    domain            TEXT COLLATE NOCASE,
    linkedin_url      TEXT,
    company_size      TEXT,
    industry          TEXT,
    location          TEXT,
    signal            TEXT NOT NULL,          -- why we reached out; never empty
    apollo_person_id  TEXT UNIQUE,
    crm_id            TEXT,                   -- id in HubSpot/GHL/etc, if synced
    status            TEXT NOT NULL DEFAULT 'new',
    sequence_step     INTEGER NOT NULL DEFAULT 0,
    next_action_at    TEXT,
    created_at        TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at        TEXT NOT NULL DEFAULT (datetime('now')),
    notes             TEXT
);

CREATE TABLE IF NOT EXISTS sends (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    prospect_id   INTEGER NOT NULL REFERENCES prospects(id) ON DELETE CASCADE,
    step          INTEGER NOT NULL,
    subject       TEXT NOT NULL,
    body          TEXT NOT NULL,
    sent_at       TEXT NOT NULL DEFAULT (datetime('now')),
    message_id    TEXT,
    thread_id     TEXT,
    provider      TEXT,
    status        TEXT NOT NULL DEFAULT 'sent'   -- sent | bounced | failed
);

CREATE TABLE IF NOT EXISTS replies (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    prospect_id   INTEGER NOT NULL REFERENCES prospects(id) ON DELETE CASCADE,
    received_at   TEXT NOT NULL DEFAULT (datetime('now')),
    classification TEXT,   -- interested | question | not_now | referral | no | stop | auto_reply | bounce
    body          TEXT,
    handled       INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS suppression (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    email       TEXT COLLATE NOCASE,
    domain      TEXT COLLATE NOCASE,
    reason      TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS status_history (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    prospect_id  INTEGER NOT NULL REFERENCES prospects(id) ON DELETE CASCADE,
    from_status  TEXT,
    to_status    TEXT NOT NULL,
    changed_at   TEXT NOT NULL DEFAULT (datetime('now')),
    reason       TEXT
);

-- One row per daily campaign. status: drafting | awaiting_approval | revising |
-- approved | loading | launched | held | completed | cancelled
-- (loading is a lock set right before the Instantly upload so two jobs never
-- load the same campaign twice)
CREATE TABLE IF NOT EXISTS campaigns (
    id                        TEXT PRIMARY KEY,     -- e.g. C20261121-1
    name                      TEXT,
    version                   INTEGER NOT NULL DEFAULT 1,
    status                    TEXT NOT NULL DEFAULT 'drafting',
    segment_note              TEXT,                 -- who this campaign targets and how they were found
    contact_count             INTEGER NOT NULL DEFAULT 0,
    approval_email            TEXT,                 -- the owner's address the approval went to
    approval_channel          TEXT,                 -- gmail | outlook | agentmail | platform_email | chat
    approval_sent_at          TEXT,
    approval_message_id       TEXT,
    approval_reply_message_id TEXT,
    approved_by               TEXT,                 -- verified sender address of the approval reply
    approved_at               TEXT,
    approved_version          INTEGER,              -- the version the owner approved; load only this one
    reminder_sent_at          TEXT,                 -- reset to NULL on every new version
    last_handled_message_id   TEXT,                 -- newest approval-thread message already handled; never replay an older one
    last_checked_at           TEXT,                 -- when the approval inbox was last read for this campaign
    load_error                TEXT,                 -- why the last load failed, with the date; tell the owner once, do not retry hourly
    instantly_campaign_id     TEXT,
    launched_at               TEXT,
    created_at                TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at                TEXT NOT NULL DEFAULT (datetime('now'))
);

-- The contacts in a campaign and the exact words shown to the owner for approval.
-- version is the campaign version the words were last shown in. approved_hash is
-- a hash of the words shown (email, subject_1, body_1, body_2, body_3), set when
-- the approval email is sent. At load time only rows with state included, version
-- equal to campaigns.approved_version, and a matching approved_hash are loaded.
CREATE TABLE IF NOT EXISTS campaign_contacts (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_id  TEXT NOT NULL REFERENCES campaigns(id) ON DELETE CASCADE,
    prospect_id  INTEGER NOT NULL REFERENCES prospects(id) ON DELETE CASCADE,
    state        TEXT NOT NULL DEFAULT 'included',  -- included | held_back | removed | loaded
    held_reason  TEXT,
    fact         TEXT,
    fact_source  TEXT,
    subject_1    TEXT,
    body_1       TEXT,
    body_2       TEXT,
    body_3       TEXT,
    word_count   INTEGER,
    version      INTEGER,
    approved_hash TEXT,
    UNIQUE (campaign_id, prospect_id)
);

CREATE INDEX IF NOT EXISTS idx_prospects_status  ON prospects(status);
CREATE INDEX IF NOT EXISTS idx_prospects_email   ON prospects(email);
CREATE INDEX IF NOT EXISTS idx_prospects_domain  ON prospects(domain);
CREATE INDEX IF NOT EXISTS idx_prospects_next    ON prospects(next_action_at);
CREATE INDEX IF NOT EXISTS idx_sends_prospect    ON sends(prospect_id);
CREATE INDEX IF NOT EXISTS idx_suppression_email ON suppression(email);
CREATE INDEX IF NOT EXISTS idx_suppression_domain ON suppression(domain);
CREATE INDEX IF NOT EXISTS idx_campaigns_status  ON campaigns(status);
CREATE INDEX IF NOT EXISTS idx_cc_campaign       ON campaign_contacts(campaign_id);
CREATE INDEX IF NOT EXISTS idx_cc_prospect       ON campaign_contacts(prospect_id);

-- Keep updated_at honest without the agent having to remember.
CREATE TRIGGER IF NOT EXISTS trg_prospects_touch
AFTER UPDATE ON prospects
FOR EACH ROW
BEGIN
    UPDATE prospects SET updated_at = datetime('now') WHERE id = NEW.id;
END;

-- Keep campaigns.updated_at honest (used to spot a campaign left in drafting
-- or revising by a crash).
CREATE TRIGGER IF NOT EXISTS trg_campaigns_touch
AFTER UPDATE ON campaigns
FOR EACH ROW
BEGIN
    UPDATE campaigns SET updated_at = datetime('now') WHERE id = NEW.id;
END;

-- Record every status change so reporting can reconstruct the funnel.
CREATE TRIGGER IF NOT EXISTS trg_status_history
AFTER UPDATE OF status ON prospects
FOR EACH ROW WHEN OLD.status IS NOT NEW.status
BEGIN
    INSERT INTO status_history (prospect_id, from_status, to_status)
    VALUES (NEW.id, OLD.status, NEW.status);
END;
"""


# Columns added after v1.4.0, plus columns added to the new tables during 1.5.0
# development. Each is added only if it is missing, so this is safe on a new
# database and on an old one.
MIGRATIONS = [
    ("sends", "campaign_id", "TEXT"),
    ("replies", "campaign_id", "TEXT"),
    ("replies", "pushed_to_crm", "INTEGER DEFAULT 0"),
    ("replies", "crm_record_id", "TEXT"),
    ("prospects", "signal_source", "TEXT"),
    ("prospects", "researched_at", "TEXT"),      # when the fact was last checked; pool freshness
    # Added during 1.5.0 development: only needed on a database created by an
    # early 1.5.0 build. A fresh or 1.4.0 database already has them.
    ("campaigns", "last_handled_message_id", "TEXT"),
    ("campaigns", "last_checked_at", "TEXT"),
    ("campaigns", "load_error", "TEXT"),
    ("campaign_contacts", "version", "INTEGER"),
    ("campaign_contacts", "approved_hash", "TEXT"),
]

# Indexes on migrated columns must be created after the migration.
POST_MIGRATION = """
CREATE INDEX IF NOT EXISTS idx_sends_campaign ON sends(campaign_id);
CREATE INDEX IF NOT EXISTS idx_replies_campaign ON replies(campaign_id);
"""


def migrate(conn: sqlite3.Connection) -> list:
    added = []
    for table, column, decl in MIGRATIONS:
        existing = {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}
        if column not in existing:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {decl}")
            added.append(f"{table}.{column}")
    conn.executescript(POST_MIGRATION)
    return added


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Create or upgrade Becca's local prospect database. "
        "It is the internal store and send log, whether or not a CRM or CSV is connected. "
        "Safe to re-run."
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=DEFAULT_DB,
        help=f"database file to create or upgrade (default: {DEFAULT_DB})",
    )
    args = parser.parse_args(argv)
    db = args.db

    conn = sqlite3.connect(db)
    try:
        conn.executescript(SCHEMA)
        added = migrate(conn)
        conn.commit()
        tables = [
            r[0]
            for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            )
        ]
    finally:
        conn.close()
    print(f"Becca's prospect database ready: {db}")
    print(f"Tables: {', '.join(tables)}")
    if added:
        print(f"Columns added: {', '.join(added)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
