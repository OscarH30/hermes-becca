#!/usr/bin/env python3
"""Create Becca's local prospect database.

Always run at onboarding, even when a CRM is connected. This database is the
send log and dedupe index -- it answers "have we already emailed this person?"
without a network call, which is what keeps Becca from emailing anyone twice.

Safe to re-run: every statement is CREATE ... IF NOT EXISTS.
"""
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "prospects.db"

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
    classification TEXT,   -- interested | objection | referral | not_now | hard_no | auto_reply | bounce
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

CREATE INDEX IF NOT EXISTS idx_prospects_status  ON prospects(status);
CREATE INDEX IF NOT EXISTS idx_prospects_email   ON prospects(email);
CREATE INDEX IF NOT EXISTS idx_prospects_domain  ON prospects(domain);
CREATE INDEX IF NOT EXISTS idx_prospects_next    ON prospects(next_action_at);
CREATE INDEX IF NOT EXISTS idx_sends_prospect    ON sends(prospect_id);
CREATE INDEX IF NOT EXISTS idx_suppression_email ON suppression(email);
CREATE INDEX IF NOT EXISTS idx_suppression_domain ON suppression(domain);

-- Keep updated_at honest without the agent having to remember.
CREATE TRIGGER IF NOT EXISTS trg_prospects_touch
AFTER UPDATE ON prospects
FOR EACH ROW
BEGIN
    UPDATE prospects SET updated_at = datetime('now') WHERE id = NEW.id;
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


def main() -> int:
    conn = sqlite3.connect(DB)
    try:
        conn.executescript(SCHEMA)
        conn.commit()
        tables = [
            r[0]
            for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            )
        ]
    finally:
        conn.close()
    print(f"Becca's prospect database ready: {DB}")
    print(f"Tables: {', '.join(tables)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
