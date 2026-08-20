---
name: outreach-campaign
description: Use for the daily outreach run, when the owner says "send today's batch", or when building or advancing an email sequence. Assembles the day's batch, writes each email, humanizes it, presents the batch for approval, sends what was approved, and schedules follow-ups.
version: 1.0.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [campaign, sending, sequences, batching, approval]
    related_skills: [cold-email, humanizer, crm-sync, prospecting]
---

# Running the daily batch

This skill is the orchestration. `cold-email` writes the words; this decides who
gets them, when, and whether they go out at all.

## Resolve your accounts first

Every `{{ACCOUNT:<toolkit>}}` below is a placeholder. Read `brain/accounts.md`
and substitute the `word_id` recorded there.

If `brain/accounts.md` is missing, or the toolkit you need has no entry, **stop
and run `onboarding`.** Never substitute a default and never guess.

A binding without an `owner_said` quote is **not** a valid binding — treat it as
absent. It means something wrote the file without a human confirming it. An unpinned
call lands in whichever account the platform happens to pick — which may belong
to an entirely different company.


## Step 1 — Assemble the batch

Read `brain/config.md` for `daily_send_cap`, `sequence_steps`,
`sequence_spacing_days`, and `send_window`.

The batch is built from two pools, and **follow-ups come first**:

1. **Due follow-ups** — prospects at `contacted` or `follow_up_1` whose spacing
   has elapsed and who have not replied. These outperform first touches, so they
   get the capacity first.
2. **New first touches** — prospects at `new`, best-signal first, filling the
   remaining capacity up to the cap.

Run every prospect through the pre-send checks in `crm-sync`. Report anyone
dropped and why.

## Step 2 — Write

For each prospect, use the `cold-email` skill, feeding it: the prospect's role
and company, the **specific signal** from their record, the offer and proof from
`brain/business.md`, and the tone rules from `brain/voice.md`.

Then run every draft through `humanizer`. No exceptions, including follow-ups.

**Follow-ups are not reminders.** Each step adds something — a different angle, a
relevant result, a shorter ask. Never send "just bumping this" or "following up
on my last email." A follow-up with no new content is a reason to unsubscribe.

## Step 3 — Present for approval

This is the default and the whole batch stops here. Show:

```
Batch for Wed 20 Aug — 18 emails (12 first touch, 6 follow-up)
Cap: 20 · Window: 09:00-16:00 CT

 1. Dana Reyes · VP Ops · Northwind Logistics · hiring 3 dispatchers
    Subj: your dispatch hiring
    > Saw you're adding three dispatchers this quarter...
    [full body]

 2. ...
```

Full body for every email, not a summary. The owner is approving the actual
words, and a summary makes approval meaningless.

Then ask plainly: *send all, edit some, or hold?* Handle edits by rewriting and
re-showing that email. Corrections the owner makes are signal — append the
pattern to `brain/voice.md` so you stop making that mistake.

**Only skip this step when `autonomy: auto` is set in `brain/config.md`** — and
even then, stop for approval on a template used for the first time or a new
segment.

## Step 4 — Send

**Confirm the outbound identity first.** Read the `gmail` binding and `sending_address` from `brain/accounts.md`. If either is empty, stop — do not send
from a default account. Owners often have several mailboxes connected, and cold
email from the wrong one reaches real people from an address that never agreed
to send it. Verify the address the provider will actually send as, and that it
matches `sending_address`. A mismatch stops the run.

Send through the configured provider — Gmail/Outlook via Composio (always with
`--account {{ACCOUNT:gmail}}`), or AgentMail.

- Space sends across the `send_window`. Do not fire 20 emails in 40 seconds;
  it is the most obvious automation signal there is.
- Send in the owner's business hours, in the prospect's timezone where known.
- Plain text. No tracking pixels, no link shorteners, no images — all three hurt
  deliverability and all three are visible to anyone technical.
- **Log every send the moment it happens.** A send that isn't logged will be
  sent again.

Stop the entire run and tell the owner immediately if: a send fails
authentication, bounces exceed 3% of the batch, or the provider returns a rate
limit. Do not push through an error — a burned domain takes weeks to recover
and the owner would always rather stop.

## Step 5 — Schedule and report

Queue the next step per `sequence_spacing_days`. Report:

```
Sent 18/18 · 0 bounces · next follow-ups Fri (6)
Week: 74 sent · 9 replies (12.2%) · 3 meetings
```

Reply rate is the number that matters. Track it weekly, and if it drops below
about 3%, say so and propose a specific change — a tighter segment, a different
trigger, a shorter email. Do not just keep sending.

**Completion criterion:** every approved email is sent and logged, every
follow-up is queued, and the counts in the report reconcile with the database.
