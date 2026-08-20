---
name: inbox-triage
description: Use when Becca checks the outreach inbox, on the inbox-sweep cron, or when the owner asks about replies. Reads new mail, classifies every reply, handles opt-outs first, drafts responses that move interested prospects toward a booked call, and stops sequences the moment someone answers.
version: 1.0.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [inbox, replies, triage, objections, booking]
    related_skills: [crm-sync, booking, cold-email, humanizer]
---

# Working the inbox

A reply is the whole point. Handle it faster and better than the sequence that
earned it.

Read `accounts.gmail` from `brain/config.md` and pass `--account <word_id>` on
every call. Empty → stop and run `onboarding`. Reading the wrong inbox wastes a
run; replying from it is worse.

## Order of operations — do not reorder

**1. Opt-outs first, before anything else.**
Scan every new message for a stop request: "unsubscribe", "remove me", "take me
off", "stop emailing", "do not contact". Handle these before you read anything
else, before you draft anything, before you report.

For each: add to `brain/suppression.md`, set status `unsubscribed`, cancel any
queued sends, and send nothing but a one-line acknowledgement if a reply is
warranted at all. This is a legal obligation and it is not negotiable by
priority, batching, or convenience.

**2. Stop sequences for anyone who replied.**
Any human reply — positive, negative, confused, an out-of-office with a real
person's forward — sets status `replied` and cancels every queued follow-up for
that prospect. A follow-up that lands after someone answered makes the whole
operation look automated, because it is.

**3. Then triage the rest.**

## Classify every message

| Class | Signal | What you do |
|---|---|---|
| **Interested** | Wants to talk, asks how it works, asks price | Draft a reply that gets a time on the calendar. Highest priority. |
| **Objection** | Interested but blocked — timing, budget, incumbent | Draft an honest answer from `brain/business.md`. One rebuttal only. |
| **Referral** | "Talk to Dana instead" | Thank them, write the new contact in, open a fresh thread naming the referrer. |
| **Not now** | "Revisit in Q1" | Status `not_interested`, note the date, propose a reminder. Do not argue. |
| **Hard no** | Clear rejection | Status `not_interested`. One-line thanks or nothing. Never rebut. |
| **Auto-reply** | Out of office, no human content | Not a reply. Reschedule the step past their return date. Do not set `replied`. |
| **Bounce** | Delivery failure | Status `bounced`. Never retry. If bounces exceed 3% of a batch, stop and warn the owner — the list or the domain has a problem. |

Distinguishing an auto-reply from a real reply matters more than it sounds. Mark
an out-of-office as `replied` and you silently drop a live prospect.

## Drafting replies

Everything you draft goes to the owner for approval before sending, exactly as
with cold email — unless `autonomy: auto`, and even then, an objection about
pricing or a legal question always comes back for review.

**For interested replies:** match their energy, answer what they actually asked,
and make booking a single click. Use `BECCA_BOOKING_LINK` if set; otherwise
offer two concrete times in their timezone. Never make them do scheduling work.

**For objections:** answer the objection honestly and stop. One rebuttal, from
real material in `brain/business.md`. If the honest answer is "you're right,
we're not a fit," say that — it is worth more than a save.

Run every draft through `humanizer` first. A reply that reads like a template
undoes the email that earned it.

## Reporting

The `inbox-sweep` cron reports only what changed:

```
3 replies · 1 interested (Dana Reyes, Northwind) · 1 objection (pricing) · 1 opt-out
Drafted 2 responses — waiting on you
Sequences stopped: 3
```

Nothing new is a complete and acceptable report. Say "no new replies" and stop.
Never manufacture activity to look useful.
