---
name: booking
description: Use when a prospect wants to talk and Becca needs to get a call on the calendar. Prefers the owner's booking link, falls back to proposing real open slots from the connected calendar, and confirms the meeting into the owner's CRM. Interested leads go to the CRM for the owner's team through crm-sync.
version: 1.2.0
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

An Interested reply is also pushed to the owner's CRM through `crm-sync` (that is
`inbox-triage`'s job), and the owner's team takes over from there. This skill is
the booking part: the link, the times, the confirmation. Replies to prospects are
drafted and shown to the owner as before. That is separate from campaign
approval, which covers only the campaign emails.

## Check your tools before you start

You reach the inbox, the CRM, and the calendar through whatever onboarding
connected for you: the platform's own connector, or Composio. Keys live in the
platform's secure settings (on Hermes, the profile's `.env`), never in chat. Look
at what you actually have.

**Missing a tool this skill needs, and no `brain/access.md` with the owner's yes:
stop and run `onboarding`.** Do not fall back to a command line tool, saved login,
or browser session you happen to find. A tool nobody granted you is a tool
pointed at an account nobody chose, and cold email from the wrong mailbox cannot
be recalled. In manual mode (recorded in `brain/access.md`) you draft the reply
and the owner sends it.

Tool names below are the common Composio slugs. If onboarding connected something
else, use its equivalent. The operation is what matters, not the spelling.

## One rule for an Interested reply

1. **A booking link is set:** send it.
2. **No link, but a calendar is connected:** offer two specific times that you
   have checked are free.
3. **Neither:** draft the reply, flag it to the owner as needing a time, and let
   the owner fill it in.

Never propose a time you have not verified is free.

**1. Booking link (default, and usually best).**
If `booking_link` in `brain/config.md` (or `BECCA_BOOKING_LINK` where the
platform uses environment settings) is set, send it. No sign-in, no failure mode,
and it respects whatever buffers and hours the owner already configured in
Calendly or Cal.com. Do not over-engineer past this.

> Easiest is probably my calendar. Grab whatever works: <link>

**2. Offer two verified times from the connected calendar.**
Use the calendar the owner chose at onboarding, the one named in
`brain/config.md`. Never pick a different one: with several calendars connected
you would propose someone else's free time. Call the connected calendar tool
(through Composio or the platform connector, for example a "find free slots"
operation) to get the owner's open times.

Then offer **two** specific times, in **their** timezone, inferred from the
company location. Two, not five, because a menu is work.

> Would Thursday 10:15 or Friday 2:30 your time work? Happy to work around you.

When they pick one, create the event with the calendar tool's create-event
operation, including them as an attendee, a real title, and a one-line agenda in
the description so the owner walks in knowing the context.

**3. Hand it to the owner.**
If no calendar is connected and no link is set, draft the reply, flag it as
needing a time, and let the owner fill it in. Say so clearly rather than
inventing availability. Double-booking the owner is worse than a slower reply.

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

For a no-show: one follow-up, same day, assuming good faith, because things come up.
If that goes unanswered, set status back to `contacted`, note the no-show, and
leave it. Do not chase a third time.

**Completion criterion:** a booked call exists on the calendar, the prospect has
a written confirmation, the CRM shows `meeting_booked`, and the owner has the
context they need to run the call.
