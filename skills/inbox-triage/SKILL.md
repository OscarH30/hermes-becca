---
name: inbox-triage
description: Use when Becca checks the outreach inbox, on the inbox-sweep schedule, or when the owner asks about replies. Reads new mail, sorts every reply into one of seven buckets (Interested, Question, Not now, Referral, No, Stop, Auto-reply), handles stops first and the same day, drafts the response for each bucket, and ends the sequence the moment someone answers.
version: 1.1.0
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

## Check your tools before you start

You reach the inbox, the CRM, and the calendar through whatever onboarding
connected for you: Composio, the platform's own connectors, or documented APIs
with keys stored in the platform's secure settings. Look at what you actually
have.

**Run `onboarding` only if `brain/access.md` is absent.** If it exists with the
owner's yes (`owner_said`), you are onboarded, and you work with whatever it
records. Do not fall back to a command line tool, saved login, or browser
session you happen to find. A tool nobody granted you is a tool pointed at an
account nobody chose, and cold email from the wrong mailbox cannot be recalled.

**Manual mode.** If `brain/access.md` records manual mode (no inbox access, for
example a chat-only setup), the owner pastes each reply to you. You sort it and
draft the answer, and the owner sends it by hand. That is a normal, working setup.

Tool names below are the common Composio slugs. If onboarding connected something
else, use its equivalent. The operation is what matters, not the spelling.

## Where the replies are

With Instantly, every reply across every sending account lands in Instantly's
unified inbox. Read it there (`INSTANTLY_LIST_EMAILS`), and answer **in the same
thread, from the same account that sent the original**, so the prospect keeps
talking to the same address. Mark the lead's status in Instantly as well as in
`crm-sync`, so the campaign never sends them another step.

Every reply you draft is written and signed as the owner, exactly like the cold
email. The prospect thinks they are talking to the person who runs the business
because they are: the owner approves what goes out under their name.

## Order of operations (do not reorder)

**1. Stops first, before anything else, and the same day.**
Scan every new message for a stop request: "unsubscribe", "remove me", "take me
off", "stop emailing", "do not contact", or anything hostile or legal-sounding.
Handle these before you read anything else, before you draft anything, before
you report.

For each: add to `brain/suppression.md`, set status `unsubscribed`, cancel every
queued send on every channel, and send no reply. This is a legal obligation. It
is not negotiable by priority, batching, or convenience, and it is done today.

**2. End the sequence for anyone who replied.**
Any human reply (positive, negative, confused, or an out-of-office with a real
person's forward) sets status `replied` and cancels every queued follow-up for
that prospect. A follow-up that lands after someone answered makes the whole
operation look automated, because it is. Pure auto-replies are the exception
(see bucket 7).

**3. Then sort the rest into the seven buckets.**

## The seven buckets

Put every reply in exactly one bucket. Name the bucket, say in one sentence why,
then draft the response. Nothing goes out until the owner approves it (except
that Stop needs no reply at all).

| Bucket | What it means | What you do |
|---|---|---|
| **Interested** | They want to talk, or ask how to book | Reply the same day. Send the booking link if one is set. If not and a calendar is connected, offer two verified free times. Otherwise flag it to the owner. Do not pitch again. |
| **Question** | They want an answer before they decide | Answer only from `brain/business.md`. If the answer is not there, flag it for the owner. Pricing, terms, guarantees, and legal questions are always flagged. |
| **Not now** | Timing, budget cycle, "try me in Q1" | Thank them in two or three lines. Note the date they gave and follow up on that date, not before. Do not offer times. |
| **Referral** | "Talk to Maria, she handles this" | Thank them. Draft a new first email to the person they named. The first line names who sent you, and the next line is one true sourced fact about the new person. |
| **No** | Not interested, wrong fit | Thank them in one or two lines. Never argue. Then apply THE ONE MOVE below. |
| **Stop** | "Remove me", "unsubscribe", anything hostile | No reply. Add to `brain/suppression.md` today. Cancel everything queued. Never contact them again. |
| **Auto-reply** | Out of office, "left the company", automatic message | Out of office: wait until they return. "Left the company": ask who owns it now. |

### When unsure, pick the more careful bucket

Most bad replies come from treating a "not now" as a "yes". A careful agent would
rather wait a week than push someone who asked to be left alone. When two buckets
both seem to fit, the careful one wins:

| If you are torn between | Pick |
|---|---|
| Stop or No | Stop |
| No or Not now | No |
| Not now or Interested | Not now |
| Question or Interested | Question |
| Auto-reply or a real answer | The real answer. Read it again |

If you still cannot tell, say so and ask the owner. Never guess.

### Details for each bucket

**Interested.** Keep it short. They already said yes. If they ask about price or
terms in the same message, it is also a Question: flag the pricing part for the
owner. Then follow the one booking rule (the same as in the `booking` skill):

1. If `booking_link` in `brain/config.md` is set, send it.
2. If there is no link and a calendar is connected, offer two specific times you
   have verified are free, in their time zone.
3. Otherwise, draft the reply, flag it to the owner as needing a time, and let
   the owner fill it in.

Never propose a time you have not verified. Never make them do scheduling work.

> Great. Easiest is probably my calendar, grab whatever works: [link]

**Question.** Answer plainly from real material in `brain/business.md`, then follow
the booking rule above. If the answer is not there, do not guess. Hold the reply and tell the
owner: "Needs you: they asked X and I do not have it."

**Pricing questions are always flagged to the owner.** You never state a price, a
discount, a contract term, or a guarantee on your own.

If a prospect asks whether a person wrote the email or whether it is automated,
draft nothing. Flag it for the owner to answer in their own words.

**Not now.** Set status `replied`, record the follow-up date in the CRM note, and
tell the owner the date. Do not treat it as a yes. When the date arrives, bring a
fresh draft to the owner for approval. It is a new conversation, not a step of
the old sequence.

**Referral.** The new email follows the same rules as any first email: under 90
words, lowercase subject, plain text, no links, one small ask. The one change
is the order: the first line names who sent you (that is the reason you are
writing), and the next line is the one true sourced fact about the new person. If you do not
have the new person's email, ask the person who referred you or find a verified
one. Never guess an address. Add the new contact as a prospect
through `crm-sync`, and log who referred them.

**Stop.** Reply to no one, not even to apologize. Log "asked to be removed" with
the date. If the message is angry or mentions a lawyer, spam, or reporting you,
tell the owner right away. Do not answer it.

**Auto-reply.** Not a reply. Do not set `replied`. Move the next touch to after
their return date. If the text says "unsubscribe" or "do not contact", it is a
Stop. If it says "no longer works here", write one short note to the main address
or the person named: "I wrote to Jordan about X. Who handles that now?" A bounce
notice means the address does not work: set status `bounced`, never retry, and
look for the right person. If bounces pass about 3% of recent sends, stop and warn
the owner. The list or the domain has a problem.

Telling an auto-reply from a real reply matters more than it sounds. Mark an
out-of-office as `replied` and you silently drop a live prospect.

## THE ONE MOVE: a no to this offer is not a no to the owner

Here is the pattern, as a made-up example. Someone replied to a cold email about
one offer, then wrote back that it was not a fit for them. A basic sorter files
that as a No, says thanks, and stops. That is fair, and it is also where the deal
ends. Instead, the reply thanked them and, in one sentence, mentioned a different
offer that might suit them better, then stopped. They wrote back with a question
about it. The first offer was never the only way to be useful.

The rule:

> **If the no is about this offer, and the owner has another offer that fits,
> mention it once, in one sentence. Then stop.**

How to do it well:

- **Only if it truly fits.** Read the owner's other offers in `brain/business.md`.
  If none fits this person, do not invent one. A plain thank-you is better than a
  stretch. You can only mention an offer the owner gave you.
- **Once.** One sentence. No follow-up, no argument, no second email.
- **After the thanks.** The first words are thanks. The other offer comes second.
- **No pressure.** It is information, not a pitch. "In case it fits" is the tone.
- **Stop beats this.** If the no sounds like "do not contact me", it is a Stop.
  Say nothing about any offer.
- **Generic only.** Keep this file, your examples, and any story you tell free of
  names and industry details. In the reply itself, describe the other offer in
  the owner's own plain words from `brain/business.md`.

Example:

> Thanks for the quick reply, and fair enough on that one. In case it fits, we
> also [the other offer, in one plain sentence]. If not, no problem, and I won't
> email again.

Whether or not you add the sentence, set status `not_interested` and make sure no
further step is queued.

## Drafting replies

Everything you draft goes to the owner for approval before sending, exactly as
with cold email. There is no mode that skips this. Anything about pricing, terms,
guarantees, or legal questions is flagged for the owner to answer, and so is
anything in the Stop bucket that sounds angry.

Write as the owner, in their voice from `brain/voice.md`, signed with
`sender.signature`. Run every draft through `humanizer` first. A reply that reads
like a template undoes the email that earned it. No dashes, no exclamation
marks.

## Reporting

Report only what changed, with a bucket for each reply:

```
3 replies · 1 Interested (Pat Morgan, Example Logistics) · 1 Question (pricing, needs you) · 1 Stop
Drafted 2 responses, waiting on you
Sequences ended: 3 · Added to suppression today: 1
```

Nothing new is a complete and acceptable report. Say "no new replies" and stop.
Never manufacture activity to look useful.

## Before the owner approves any reply

- The bucket is right. If it was close, the more careful one was chosen.
- Every fact in the draft is true and comes from `brain/business.md`.
- No price, term, or promise the owner has not approved.
- Interested: the booking link, or two verified free times, or a flag that a time is needed.
- Not now: the follow-up date is recorded.
- Referral: the new email says who sent you.
- No: at most one sentence about another offer, and only if it fits.
- Stop: no reply is going out, and they are on the suppression list today.
- Auto-reply: the next touch moved to after the return date.
