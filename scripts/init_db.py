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

-- One row per daily campaign, posted in the owner's chat for approval. status: drafting | awaiting_approval | revising |
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
    approval_channel          TEXT,                 -- where the campaign was posted for review: grok_bot_chat | telegram | imessage | slack | whatsapp | discord | hermes_chat | other (1.5.0 databases may hold gmail | outlook | agentmail | platform_email | chat here; kept as is)
    approval_owner_identity   TEXT,                 -- the owner's immutable id in that channel (user id, member id or number; a handle only as a label); only their typed message counts as approval
    approval_message_ref      TEXT,                 -- channel-neutral reference to the last message of the posted campaign (the one with the closing line) (message id, link or timestamp)
    approval_sent_at          TEXT,                 -- when the campaign was posted for review
    approval_reply_ref        TEXT,                 -- reference to the owner's approval message
    approved_by               TEXT,                 -- the owner identity the approval message came from (1.5.0 databases hold a sender email address here; kept as is)
    approved_at               TEXT,
    approved_version          INTEGER,              -- the version the owner approved; load only this one
    reminder_sent_at          TEXT,                 -- reset to NULL on every new version
    reminder_ref              TEXT,                 -- reference to the one reminder Becca posted; reset on every new version; never counts as an approval
    last_handled_ref          TEXT,                 -- high-water mark by time: newest owner message in the approval channel already handled; skip anything at or before it
    last_checked_at           TEXT,                 -- when the approval channel was last checked for this campaign
    parts_posted              INTEGER,              -- how many numbered messages the campaign was posted in
    -- Legacy email columns from 1.5.0. Kept so an existing database upgrades
    -- without losing anything. Becca 1.6.0 no longer writes them.
    approval_email            TEXT,                 -- LEGACY (1.5.0): the address the old emailed approval was sent to
    approval_message_id       TEXT,                 -- LEGACY (1.5.0): RFC Message-ID of the old emailed campaign; see approval_message_ref
    approval_reply_message_id TEXT,                 -- LEGACY (1.5.0): Message-ID of the approval reply; see approval_reply_ref
    reminder_message_id       TEXT,                 -- LEGACY (1.5.0): Message-ID of the reminder; see reminder_ref
    last_handled_message_id   TEXT,                 -- LEGACY (1.5.0): see last_handled_ref
    load_error                TEXT,                 -- why the last load failed, with the date; tell the owner once, do not retry hourly
    instantly_campaign_id     TEXT,
    launched_at               TEXT,                 -- empty means never launched; only then may crash recovery cancel it
    created_at                TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at                TEXT NOT NULL DEFAULT (datetime('now'))
);

-- The contacts in a campaign and the exact words shown to the owner for approval.
-- version is the campaign version the words were last shown in. approved_hash is
-- a hash of the words shown (email, subject_1..3, body_1..3), set when
-- the campaign is posted for review. At load time only rows with state included, version
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
    subject_2    TEXT,
    body_2       TEXT,
    subject_3    TEXT,
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
# development (campaigns.reminder_message_id, campaign_contacts.subject_2 and
# subject_3 among them), plus the channel-neutral approval columns added in
# 1.6.0. Each is added only if it is missing, so this is safe on a new
# database and on an old one. Nothing here ever drops or rewrites a column.
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
    ("campaigns", "reminder_message_id", "TEXT"),
    ("campaign_contacts", "version", "INTEGER"),
    ("campaign_contacts", "approved_hash", "TEXT"),
    ("campaign_contacts", "subject_2", "TEXT"),
    ("campaign_contacts", "subject_3", "TEXT"),
    # Added in 1.6.0: campaign approval happens in chat. These are
    # channel-neutral. The 1.5.0 email columns stay in place as legacy and are
    # never dropped.
    ("campaigns", "approval_owner_identity", "TEXT"),
    ("campaigns", "approval_message_ref", "TEXT"),
    ("campaigns", "approval_reply_ref", "TEXT"),
    ("campaigns", "reminder_ref", "TEXT"),
    ("campaigns", "last_handled_ref", "TEXT"),
    ("campaigns", "parts_posted", "INTEGER"),
]

# Indexes on migrated columns must be created after the migration.
POST_MIGRATION = """
CREATE INDEX IF NOT EXISTS idx_sends_campaign ON sends(campaign_id);
CREATE INDEX IF NOT EXISTS idx_replies_campaign ON replies(campaign_id);
"""


# Copy 1.5.0 references into the channel-neutral columns, only where the new
# column is still empty. The old columns are left untouched. approved_by and
# approval_channel keep their 1.5.0 values as they are. The old email address is
# deliberately not copied into approval_owner_identity: an email address is not
# the owner's identity in a chat channel, and onboarding records that fresh.
BACKFILL = [
    ("approval_message_ref", "approval_message_id"),
    ("approval_reply_ref", "approval_reply_message_id"),
    ("reminder_ref", "reminder_message_id"),
    ("last_handled_ref", "last_handled_message_id"),
]


def migrate(conn: sqlite3.Connection) -> list:
    added = []
    for table, column, decl in MIGRATIONS:
        existing = {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}
        if column not in existing:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {decl}")
            added.append(f"{table}.{column}")
    conn.executescript(POST_MIGRATION)
    campaign_cols = {row[1] for row in conn.execute("PRAGMA table_info(campaigns)")}
    for new, old in BACKFILL:
        if new in campaign_cols and old in campaign_cols:
            conn.execute(
                f"UPDATE campaigns SET {new} = {old} "
                f"WHERE {new} IS NULL AND {old} IS NOT NULL"
            )
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
