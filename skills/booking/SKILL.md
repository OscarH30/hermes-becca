---
name: booking
description: Use when a prospect wants to talk and Becca needs to get a call on the calendar. Prefers the owner's booking link, falls back to proposing real open slots from the connected calendar, and confirms the meeting into the CRM.
version: 1.0.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [calendar, scheduling, calendly, booking, meetings]
    related_skills: [inbox-triage, crm-sync]
---

# Getting the call booked

The moment someone says yes, every extra step loses some of them. Your job is to
remove the steps.

## Check your tools before you start

You reach Apollo, the inbox, the CRM, and the calendar through whatever
onboarding wired into this profile — MCP servers, or documented APIs using keys
in `.env`. Look at what you actually have.

**Missing a tool this skill needs → stop and run `onboarding`.** Do not fall back
to a CLI you happen to find on the shell. A tool nobody granted you is a tool
pointed at an account nobody chose, and cold email from the wrong mailbox cannot
be recalled.

Tool names below are the common Composio slugs. If onboarding wired something
else, use its equivalent — the operation is what matters, not the spelling.

## Three paths, in order of preference

**1. Booking link (default, and usually best).**
If `BECCA_BOOKING_LINK` or `booking_link` in `brain/config.md` is set, send it.
No API, no auth, no failure mode, and it respects whatever buffers and hours the
owner already configured in Calendly or Cal.com. Do not over-engineer past this.

> Easiest is probably my calendar — grab whatever works: <link>

**2. Propose real times from the connected calendar.**
Better for senior prospects, who often will not click a scheduling link.

```bash
composio execute "GOOGLECALENDAR_FIND_FREE_SLOTS" -d '{...}'
```

Use `accounts.googlecalendar` from `brain/config.md`; never the default — with
several calendars connected you would propose someone else's free time.

Then offer **two** specific times, in **their** timezone, inferred from the
company location. Two, not five — a menu is work.

> Would Thursday 10:15 or Friday 2:30 your time work? Happy to work around you.

When they pick one, create the event with `GOOGLECALENDAR_CREATE_EVENT`,
including them as an attendee, a real title, and a one-line agenda in the
description so the owner walks in knowing the context.

**3. Hand it to the owner.**
If no calendar is connected and no link is set, draft the reply, flag it as
needing a time, and let the owner fill it in. Say so clearly rather than
inventing availability. Never propose a slot you have not verified is free —
double-booking the owner is worse than a slower reply.

## Always

- **Confirm in writing.** After booking, a short confirmation with the time,
  timezone, duration, and how to join.
- **Update the record.** Status `meeting_booked`, with date and time, through
  `crm-sync`.
- **Stop the sequence.** Already handled by `replied`, but verify it.
- **Give the owner context.** Before the call, they should have: who, company,
  the signal you originally reached out about, and what the prospect actually
  said. Put it in the calendar description at booking time, not later.

## When they reschedule or no-show

Reschedules are normal. Offer new times once, cheerfully, no guilt.

For a no-show: one follow-up, same day, assuming good faith — things come up.
If that goes unanswered, set status back to `contacted`, note the no-show, and
leave it. Do not chase a third time.

**Completion criterion:** a booked call exists on the calendar, the prospect has
a written confirmation, the CRM shows `meeting_booked`, and the owner has the
context they need to run the call.
