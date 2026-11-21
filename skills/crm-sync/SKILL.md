---
name: crm-sync
description: Use whenever Becca needs to read or write a prospect, lead, activity, or status change. Routes to Attio, HubSpot, GoHighLevel, any Composio-supported CRM, the built-in local database, or a simple tracker table for platforms with no filesystem, and keeps the local send log authoritative for dedupe regardless of which CRM is in use.
version: 1.1.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [crm, attio, hubspot, gohighlevel, database, dedupe]
    related_skills: [prospecting, inbox-triage, onboarding]
---

# CRM sync

One interface, six backends (local, tracker table, Attio, HubSpot, GoHighLevel, or any other Composio-supported CRM). Read `crm:` in `brain/config.md` to know which.

## Check your tools before you start

You reach prospect data, the inbox, the CRM, and the calendar through whatever
onboarding connected for you: the platform's own connector, or Composio. Keys
live in the platform's secure settings (on Hermes, the profile's `.env`), never
in chat. Look at what you actually have. In manual mode (recorded in
`brain/access.md`) the owner pastes data to you and you keep the record in the
local database or the tracker table.

**Missing a tool this skill needs, and no `brain/access.md` with the owner's yes:
stop and run `onboarding`.** Do not fall back to a command line tool, saved login,
or browser session you happen to find. A tool nobody granted you is a tool
pointed at an account nobody chose, and cold email from the wrong mailbox cannot
be recalled.

Tool names below are the common Composio slugs. If onboarding connected something
else, use its equivalent. The operation is what matters, not the spelling.

## The rule that matters most

**The local record is always written, even when a CRM is connected.**

The CRM is the owner's system of record. The local database (or the tracker table
where there is no filesystem) is Becca's send log and dedupe index. If a CRM write
fails because of a rate limit, an expired sign-in, or the network, the local write
must still succeed, because "have I emailed this person before" has to be
answerable offline. A missed dedupe means emailing someone twice, which is the
fastest way to lose a prospect and a domain's reputation at once.

Write local first, then the CRM. If the CRM write fails, log it, keep going, and
report the backlog at the end of the run. Never drop the record.

## Backends

**`local`**: SQLite at `prospects.db`, schema in `scripts/init_db.py`. Present
wherever the agent has a filesystem. A complete backend, not a placeholder: it
holds prospects, sends, replies, and status history.

**`tracker_table`**: for platforms with no filesystem (a chat-only project, for
example). A simple table kept in your brain notes, one row per prospect, with
these columns: company, contact name, title, email, source and date of the one
true fact, status (from the vocabulary below), step sent, date of each touch, next
touch date, reply bucket, notes. Update it after every send and every reply, and
show the owner the current table when asked so they can copy it into a
spreadsheet. It does the same job as the local database and must be checked the
same way before every send.

**`attio`**: through the connected tool (Composio or the platform connector). Map:
prospect → Person, company → Company, each send and each reply → a note on the
Person (with the date, the touch number, and the bucket for replies). Status goes
in a status field or tag the owner chose. Do not guess field or tool names. List
what the connection offers, confirm the mapping with the owner once, and write it
into `brain/config.md`.

**`hubspot`**: call the connected tool (through Composio or the platform
connector) to create and update records. Map: prospect → Contact, company →
Company, each send → an Email engagement on the contact timeline. Set
`lifecyclestage` to `lead` on create.

**`gohighlevel`**: call the connected tool (through Composio or the platform
connector). Map: prospect → Contact with tags, status → pipeline stage, each send
→ a note. GHL requires the location ID on every call; if it is missing, stop and
ask rather than writing into the wrong sub-account.

**Any other CRM**: do not give up. Search the connected tools for the CRM by name
and look for a "create contact" operation. Composio covers Close, Pipedrive,
Salesforce, Zoho, Copper and many more. Discover the toolkit, confirm the field
mapping with the owner once, then write the mapping into `brain/config.md` so it
is stable from then on.

## Status vocabulary

Use exactly these. A status outside this list breaks the reporting.

| Status | Means |
|---|---|
| `new` | Qualified, not yet contacted |
| `queued` | In an approved batch, not yet sent |
| `contacted` | Step 1 sent |
| `follow_up_1` / `follow_up_2` | Later sequence steps sent |
| `replied` | Any human reply. **Sequence stops immediately.** For a "Not now" reply, also record the follow-up date in the note |
| `meeting_booked` | Call on the calendar |
| `not_interested` | Explicit no. Never contact again |
| `unsubscribed` | Opt-out. Added to suppression, never contact again |
| `bounced` | Hard bounce. Never retry |
| `disqualified` | Wrong fit, discovered after the fact |

`replied`, `not_interested`, `unsubscribed`, and `bounced` are all terminal for
automation. No sequence continues past any of them, ever.

## Before every send

Query the local record (database or tracker table) for the email address and
confirm all of:
- not present with any terminal status
- not on `brain/suppression.md`
- **first touches only:** no send logged to this address in the last 48 hours
  (this catches the same person arriving from two lists)
- **follow-ups (touch 2 and 3):** the previous touch is logged, the spacing in
  `sequence_spacing_days` has elapsed (touch 2 goes out 2 days after touch 1), and
  there is no reply, stop, or bounce
- daily cap in `brain/config.md` not yet reached for that inbox

If any check fails, skip the prospect and say which check caught it. These
checks are cheap and the failure they prevent is expensive.

**Completion criterion:** every prospect in an approved batch has passed all
four checks, and the count sent equals the count that passed.
