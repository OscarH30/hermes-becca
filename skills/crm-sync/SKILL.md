---
name: crm-sync
description: Use whenever Becca needs to read or write a prospect, activity, campaign membership, or status change, or hand an Interested lead to the owner. The local database (or a tracker table where there is no filesystem) holds every prospect, send and campaign. The owner's CRM (Attio, HubSpot, GoHighLevel, Pipedrive, Salesforce, or any other the connector supports) receives only the lead-handoff record, with a CSV or Google Sheet fallback. Also runs the pre-send checks, including campaign approval.
version: 1.2.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [crm, crm-agnostic, lead-handoff, campaigns, csv, database, dedupe]
    related_skills: [prospecting, inbox-triage, outreach-campaign, onboarding]
---

# CRM sync

One interface, any CRM. Becca does not assume a particular CRM. The owner has
their own (or none), and `crm:` in `brain/config.md` says which: `none`, or the
name of whatever CRM the owner connected. Attio, HubSpot, GoHighLevel, Pipedrive,
and Salesforce are only examples of what that can be. Out of the box there is no
CRM: `crm: none` with `crm_fallback: csv`.

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

**The local record is always written, even when a CRM is connected. It is the
record of every prospect and every send.**

The local database (or the tracker table where there is no filesystem) is Becca's
send log and dedupe index. The owner's CRM receives only the lead-handoff record
(Interested, and optionally Referral and Question with booking intent). Pool
prospects, sends and campaign membership stay local. Never enroll a contact in a
CRM sequence, workflow, automation or campaign: those can email people, and the
owner has approved only the campaign they saw. Reading the CRM to dedupe is fine.

"Have I emailed this person before" has to be answerable offline, so the local
write must succeed whatever the CRM does. A missed dedupe means emailing someone
twice, which is the fastest way to lose a prospect and a domain's reputation at
once.

Write local first, then the handoff to the CRM. If the CRM write fails, use the
fallback, log it, keep going, and report the backlog at the end of the run. Never
drop the record.

## Backends

Use them in this order. The first two are the owner's own system. The last two
are Becca's own record: the local database always, and the tracker table where
there is no filesystem.

**1. The owner's connected CRM** (`crm:` is anything other than `none`). Reach it
through Composio or the platform's own connector, whichever onboarding connected.
This works for any CRM the connector supports. Do not guess field or tool names.
List what the connection offers, find the "create contact" and "create note"
operations (and a deal or pipeline operation if the owner uses one), confirm the
field mapping with the owner once, and write that mapping into `brain/config.md`
so it is stable from then on. Typical mapping for a handoff: the lead = a person
or contact, company = a company or account, the reply and the suggested next
step = a note or activity on the person (with the date, the campaign and the
bucket), stage = a status field, tag, or pipeline stage the owner chose. Do not
use any sequence, workflow or enrollment feature. Examples of the details that
differ by CRM, shown only as illustrations:

- Attio: person and company records, a note on the person, a status field or tag.
- HubSpot: Contact and Company, a note on the contact, `lifecyclestage` set to
  `lead` on create.
- GoHighLevel: Contact with tags, pipeline stage for status, a note. It
  requires the location ID on every call; if that is missing, stop and ask rather
  than writing into the wrong sub-account.
- Pipedrive, Salesforce, and any other: a person or lead with the same mapping.
  Search the connected tools for the CRM by name and discover the toolkit.

If the connection is missing or the write fails, use the fallback below. Never
drop the record.

**2. CSV or Google Sheet fallback** (`crm_fallback: csv` or `google_sheet`, at
`crm_fallback_location`). Used when `crm: none`, or when a push to the connected
CRM fails. Append one row per record with the same fields (see the lead-handoff
record below). A CSV is a file in the profile; a Google Sheet is written through
the connected Google tool. Never overwrite existing rows, only append. Tell the
owner where the file or sheet is.

**3. `local`**: SQLite at `prospects.db`, schema in `scripts/init_db.py` (safe to
re-run; it upgrades an older database). The internal store and send log, present
wherever the agent has a filesystem. It is always written, whatever else is
connected. A complete backend, not a placeholder: it holds prospects, sends,
replies, campaigns, campaign contacts, and status history.

**4. `tracker_table`**: for platforms with no filesystem (a chat-only project, for
example). A simple table kept in your brain notes, one row per prospect, with
these columns: company, contact name, title, email, source and date of the one
true fact, status (from the vocabulary below), campaign id and version, step sent,
date of each touch, next touch date, reply bucket, notes. Update it after every
send and every reply, and show the owner the current table when asked so they can
copy it into a spreadsheet. It does the same job as the local database and must be
checked the same way before every send. Keep a second small table of campaigns
(id, name, current version, approved version, status, approval email message id and
sent time, approval reply message id and time, approver, last handled message id,
contacts). Mark each prospect row with the version and the approved hash.

## The lead-handoff record

When someone replies Interested (and optionally a Referral or Question with
booking intent), `inbox-triage` asks for this record. The owner's team takes over
from the CRM, so give them everything they need to act without opening the inbox.

| Field | What goes in it |
|---|---|
| name | The person who replied |
| company | Their company |
| email | The address they replied from |
| campaign name and id | For example "Second-site warehouses, 21 Nov", `C20261121-1` |
| reply text | The reply, verbatim |
| bucket | Interested, Referral, or Question |
| suggested next step | One line, for example "send the booking link" or "answer the pricing question" |

Write it to the owner's connected CRM as a person plus a note (and a deal or stage
if the owner uses one). If `crm: none` or the push fails, append the same row to
the CSV or Google Sheet. Then record in the local database that the reply was
pushed, and the CRM record id if there is one, so it is never pushed twice. List
every pushed lead in the daily summary. No secrets go into a CRM note, a CSV, or
the chat.

## Campaign fields

The campaign version fields live in the local record, not in the CRM. Each
prospect that enters a campaign carries: the campaign id, the campaign version it
was included in, and the approved hash of its words (the approval covers exactly
those words). The campaign itself carries its name, status, current version and
approved version, the approval email message id and sent time, the approval reply
message id and time, the approver address, the last handled message id and last
checked time, and the Instantly campaign id. Write them to the local record. Put
only the campaign name and id on the CRM record or note when a lead is handed
off.

## Status vocabulary

Use exactly these. A status outside this list breaks the reporting.

**Contact status**

| Status | Means |
|---|---|
| `new` | Qualified, researched, not yet contacted, not in an open campaign |
| `queued` | In an approved campaign, not yet sent |
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

A contact chosen for a campaign that is still waiting for approval stays at `new`
in this vocabulary. It is held in that campaign (see below) and is not eligible
for another one. It becomes `queued` only when its campaign is approved.

**Campaign status** (one per campaign)

| Status | Means |
|---|---|
| `drafting` | Being built and written. Nothing shown yet |
| `awaiting_approval` | The approval email was sent, waiting for the owner's reply |
| `revising` | The owner asked for changes. Next version in progress |
| `approved` | A valid approval was received. Not yet loaded |
| `loading` | A lock set right before the Instantly upload, so two jobs never load the same campaign twice |
| `launched` | Loaded into Instantly (or sending started) |
| `held` | Unapproved after `approval_reminder_days`, reminder sent. No new campaign until the owner replies |
| `completed` | Every touch went out or was cancelled |
| `cancelled` | Abandoned. Its contacts go back to the pool |

A campaign is `approved` only through the approval gate in `outreach-campaign`.
Nothing else may set it: not a CRM stage change, not a note, not a prospect's
reply.

## Before every send

Query the local record (database or tracker table) for the email address and
confirm all of:
- **the contact's campaign is `approved`, `loading` or `launched`, and the contact
  is in the campaign version the owner approved** (its version equals the
  campaign's approved version and its approved hash matches the words). A contact
  may be loaded only if its campaign is approved. A campaign that is `drafting`,
  `awaiting_approval`, `revising`, `held`, or `cancelled` loads nothing
- not present with any terminal status
- not on `brain/suppression.md` and not in the database `suppression` table
  (the file is the master list and the table mirrors it; write both, check both)
- **first touches only:** the contact's status is `new` (or `queued` in this
  approved campaign). Anything else, including `contacted` imported from the
  owner's brain, is not eligible for a first touch. Also no send logged to this
  address in the last 48 hours (this catches the same person arriving from two
  lists)
- **follow-ups (touch 2 and 3):** the previous touch is logged, the spacing in
  `sequence_spacing_days` has elapsed (touch 2 goes out 2 days after touch 1), and
  there is no reply, stop, or bounce
- daily cap in `brain/config.md` not yet reached for that inbox

If any check fails, skip the prospect and say which check caught it. These
checks are cheap and the failure they prevent is expensive.

When building a campaign (before it is shown to the owner), run the same checks
except the campaign status one. Contacts that fail are held back with a reason,
and `outreach-campaign` lists them in the approval email.

**Completion criterion:** every prospect in an approved campaign has passed all
the checks, and the count sent equals the count that passed.
