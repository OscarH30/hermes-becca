---
name: crm-sync
description: Use whenever Becca needs to read or write a prospect, lead, activity, or status change. Routes to HubSpot, GoHighLevel, any Composio-supported CRM, or the built-in local database, and keeps the local send log authoritative for dedupe regardless of which CRM is in use.
version: 1.0.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [crm, hubspot, gohighlevel, database, dedupe]
    related_skills: [prospecting, inbox-triage, onboarding]
---

# CRM sync

One interface, four backends. Read `crm:` in `brain/config.md` to know which.

## The rule that matters most

**The local database is always written, even when a CRM is connected.**

The CRM is the owner's system of record. The local database is Becca's send log
and dedupe index. If a CRM write fails — rate limit, expired token, network —
the local write must still succeed, because "have I emailed this person before"
has to be answerable offline. A missed dedupe means emailing someone twice,
which is the fastest way to lose a prospect and a domain's reputation at once.

Write local first, then the CRM. If the CRM write fails, log it, keep going, and
report the backlog at the end of the run. Never drop the record.

## Backends

**`local`** — SQLite at `prospects.db`, schema in `scripts/init_db.py`. Always
present. A complete backend, not a placeholder: it holds prospects, sends,
replies, and status history.

**`hubspot`** — `composio execute "HUBSPOT_CREATE_CONTACT"` etc., or the REST API
with `HUBSPOT_ACCESS_TOKEN`. Map: prospect → Contact, company → Company, each
send → an Email engagement on the contact timeline. Set `lifecyclestage` to
`lead` on create.

**`gohighlevel`** — `composio execute "GOHIGHLEVEL_CREATE_CONTACT"`, or the REST
API with `GHL_API_KEY` + `GHL_LOCATION_ID`. Map: prospect → Contact with tags,
status → pipeline stage, each send → a note. GHL requires the location ID on
every call; if it is missing, stop and ask rather than writing into the wrong
sub-account.

**Any other CRM** — do not give up. Run:
```bash
composio search "<crm name> create contact"
```
Composio covers Close, Pipedrive, Salesforce, Zoho, Attio, Copper and many more.
Discover the toolkit, confirm the field mapping with the owner once, then write
the mapping into `brain/config.md` so it is stable from then on.

## Status vocabulary

Use exactly these. A status outside this list breaks the reporting.

| Status | Means |
|---|---|
| `new` | Qualified, not yet contacted |
| `queued` | In an approved batch, not yet sent |
| `contacted` | Step 1 sent |
| `follow_up_1` / `follow_up_2` | Later sequence steps sent |
| `replied` | Any human reply — **sequence stops immediately** |
| `meeting_booked` | Call on the calendar |
| `not_interested` | Explicit no. Never contact again |
| `unsubscribed` | Opt-out. Added to suppression, never contact again |
| `bounced` | Hard bounce. Never retry |
| `disqualified` | Wrong fit, discovered after the fact |

`replied`, `not_interested`, `unsubscribed`, and `bounced` are all terminal for
automation. No sequence continues past any of them, ever.

## Before every send

Query the database for the email address and confirm all of:
- not present with any terminal status
- not on `brain/suppression.md`
- no send logged in the last 48 hours
- daily cap in `brain/config.md` not yet reached

If any check fails, skip the prospect and say which check caught it. These
checks are cheap and the failure they prevent is expensive.

**Completion criterion:** every prospect in an approved batch has passed all
four checks, and the count sent equals the count that passed.
