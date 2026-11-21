---
name: outreach-campaign
description: Use for the daily outreach run, when the owner says "send today's batch", or when building or advancing an email sequence. Checks the sending domain is safe, assembles the day's batch, writes each email, humanizes and scores it, presents the batch for approval, sends only what was approved, and schedules the day 3 and day 7 follow-ups.
version: 1.1.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [campaign, sending, sequences, batching, approval, deliverability]
    related_skills: [cold-email, humanizer, crm-sync, prospecting, inbox-triage]
---

# Running the daily batch

This skill is the orchestration. `cold-email` writes the words; this decides who
gets them, when, from where, and whether they go out at all.

**Nothing is sent without the owner's yes.** Drafting is not permission. Silence
is not permission. There is no mode that skips this. The owner approves all three
touches for a prospect together, before the first email goes out.

## Check your tools before you start

You reach the prospect data, the inbox, the CRM, and the calendar through
whatever onboarding connected for you: Composio, the platform's own connectors,
or documented APIs with keys stored in the platform's secure settings. Look at
what you actually have.

**Run `onboarding` only if `brain/access.md` is absent.** If it exists with the
owner's yes (`owner_said`), you are onboarded, and you work with whatever it
records. Do not fall back to a command line tool, saved login, or browser
session you happen to find. A tool nobody granted you is a tool pointed at an
account nobody chose, and cold email from the wrong mailbox cannot be recalled.

**Manual mode.** If `brain/access.md` records manual mode (no sending tool, for
example a chat-only setup), you still write and score the batch. The owner reads
it and sends each email by hand from the sending mailbox, then tells you what went
out so you can log it.

Tool names below are the common Composio slugs. If onboarding connected something
else, use its equivalent. The operation is what matters, not the spelling.

## Step 0: Protect the owner's main email

Cold email goes out from a separate sending domain, never the owner's main one.
If cold email goes wrong, mailbox providers distrust the domain it came from. If
that is the main domain, the owner's invoices and customer replies start landing
in spam. A burned outreach domain costs a new domain. A burned main domain costs
the business.

Before the first send, and again whenever something changes, confirm each item.
If any one is not true, stop and tell the owner what to fix.

**Setup (once)**

- **Separate lookalike domains.** One to three domains that are clearly the
  owner's but not the main one (for example `getacmeplumbing.com` if the main
  domain is `acmeplumbing.com`), forwarding to the real website. One to three
  real mailboxes on each domain, with the owner's real name. Properly licensed business mailboxes (such as
  Google Workspace), not a cheap bulk reseller.
- **SPF, DKIM, and DMARC** set up on every sending domain and showing as passing.
  Check with the sending tool's test or a free checker. (SPF lists who may send
  for the domain, DKIM signs each email, DMARC says what to do with mail that
  fails.) A monitoring-only DMARC setting is a safe start.
- **Never ask for a login** to the owner's domain, registrar, or mailbox. You do
  not need one. The owner does the DNS steps, with the sending tool's help.

**Warm up (two to three weeks before the first cold email)**

- Warmup is on for every sending mailbox and has run for **two to three weeks**.
  A brand new mailbox has no reputation. Do not skip this to save time; waiting is
  cheaper than replacing a domain.
- Keep warmup on, lightly, after sending starts.

**Every day**

- **About 20 emails per inbox per day, at most.** Follow-ups count toward it.
  Start lower in the first weeks (5 to 10 per inbox per day). Spread sends across
  the working day. `daily_send_cap` in `brain/config.md` is **per inbox, per day**.
  Never exceed it, and never exceed 20 even if the cap is set higher. The batch
  size for a day is the cap times the number of sending inboxes.
- **Verified emails only.** Every address was checked before it enters a batch
  (see `prospecting`). No bought or rented lists. No "unknown" or "risky"
  addresses until verified another way. Never guess an address.
- **Watch the bounces.** If bounces pass **about 3%**, pause the whole campaign.
  Do not send more until the list is checked and the cause is found. Remove every
  bounced address the same day. If anyone calls the email spam, pause, re-read
  what was sent, and fix it first.
- **Keep the email simple.** Plain text, no images, no attachments, no links in the
  first email, no open or click tracking, an honest subject. Each email carries
  its own fact about its own business, never one copy sent to hundreds.

**Be a good sender**

- A real sender name (the owner's), a real business address, and an easy opt-out
  line in every email, for example: *If this is not relevant, reply "stop" and I
  will not email you again.* Rules are stricter in the EU, the UK, and Canada,
  where permission is often needed before marketing email at all. If the owner
  will email there, tell them to check the local rules first. This is not legal
  advice.
- **Honor every stop the same day.** Add the person to `brain/suppression.md`,
  cancel everything queued, and never email them again from any tool. Keep one
  suppression list in one place and check it before every send. Current
  customers, open deals, and earlier no's belong on it too.

**Weekly check (five minutes).** Bounces as a percent of sends, any stop or spam
or angry replies and whether each was handled, SPF/DKIM/DMARC still passing,
daily volume stayed under the limit. If anything looks wrong, pause first, then
find out why. More volume never fixes a deliverability problem.

## Step 1: Assemble the batch

Read `brain/config.md` for `daily_send_cap`, `sequence_steps`,
`sequence_spacing_days`, and `send_window`.

The sequence is **three touches, then stop**: day 1, day 3, day 7. In days since
the first email that is 0, 2, and 6, so `sequence_steps` is 3 and
`sequence_spacing_days` should read `[0, 2, 6]`. If `brain/config.md` says
anything different, show the owner the difference and ask before sending.

Instantly works differently: its step delays are relative to the previous step,
not to the first email. So `[0, 2, 6]` means step 2 has a delay of 2 days and
step 3 has a delay of 4 days (2 + 4 = 6 days after the first email).

The batch is built from two pools, and **follow-ups come first**:

1. **Due follow-ups.** Prospects at `contacted` or `follow_up_1` whose spacing has
   elapsed and who have not replied. These outperform first touches, so they get
   the capacity first.
2. **New first touches.** Prospects at `new`, best-signal first, filling the
   remaining capacity. The batch size is `daily_send_cap` (per inbox) times the
   number of sending inboxes. Start small: ten prospects for the very
   first batch.

Run every prospect through the pre-send checks in `crm-sync`, including the
suppression list and the verified-email rule above. Report anyone dropped and
why.

## Step 2: Write

For each prospect, use the `cold-email` skill, feeding it: the prospect's role
and company, the **one true, sourced fact** from their record, the offer and proof
from `brain/business.md`, and the tone rules from `brain/voice.md`.

**Write it as the owner.** First person as `sender.name`, signed with
`sender.signature` verbatim, with the business address and the opt-out line.
Never as Becca, never "on behalf of", never a mention of an assistant or AI. See
SOUL.md.

**Write all three touches now.** The owner approves the whole sequence for a
prospect at once: the first email (day 1, under 90 words), the bump (day 3, under
60 words, one new useful thing), and the easy out (day 7, under 50 words, "wrong
person? who should I ask?"). Then nothing more.

Then run every draft through `humanizer`. No exceptions, including follow-ups.
Then score each first email with the 10-point check in `cold-email`. Fix any
that fail before the owner sees them.

**Follow-ups are not reminders.** Each step adds something or gives an easy out.
Never send "just bumping this" or "following up on my last email."

## Step 3: Present for approval

This is the default and the whole batch stops here. Show:

```
Batch for Wed 20 Aug: 18 emails (12 first touch, 6 follow-up)
From: Jordan Lee, Owner, via Instantly (jordan@getacmeplumbing.com, jordan@tryacmeplumbing.com)
Cap: 20 per inbox · Window: 09:00-16:00 CT · Warmup: on, week 3

 1. Pat Morgan · Operations Manager · Example Logistics · hiring 3 dispatchers
    Source: their careers page, seen 18 Aug
    Subj: second dispatcher   Words: 61   Score: 10/10
    > Saw you're adding three dispatchers this quarter...
    [full body, signature, address, opt-out line]
    Day 3: [full body]
    Day 7: [full body]

 2. ...
```

Full body for every email, not a summary. The owner is approving the actual
words, and a summary makes approval meaningless.

Then ask plainly: *send all, edit some, or hold?* Handle edits by rewriting and
re-showing that email. Corrections the owner makes are signal. Append the
pattern to `brain/voice.md` so you stop making that mistake.

**Never skip this step.** There is no mode where the batch goes out without the
owner's yes. That yes covers all three touches for each prospect together; it
is given before the first email is sent. If the owner changes a touch later, show
the new version and get a fresh yes before it goes out.

## Step 4: Send

Send through the configured provider in `brain/config.md`, and only what the
owner approved.

**Instantly (`email_provider: instantly`).** You do not send email one by one.
You load approved leads into `instantly_campaign` and Instantly sends:

- Before the first load, read the campaign back and check it: the sending
  accounts are exactly `sending_accounts`, every one shows `sender.name` as the
  display name, stop-on-reply is on, open and link tracking are off, the daily
  limit per account is at or under 20 and at or under `daily_send_cap`, warmup is
  on, and the schedule matches `send_window`. Anything different, stop and tell
  the owner.
- The campaign's steps are thin templates (`{{subject_1}}` / `{{body_1}}`, and
  so on). Each lead carries its own approved words as custom variables, so every
  email is the one the owner read. Add them with `INSTANTLY_ADD_LEADS_BULK`,
  duplicate-skip on, then check the uploaded count matches. A "success" can
  still upload zero.
- Log every lead the moment Instantly accepts it. A lead that is not logged will
  be loaded again.

**Gmail / Outlook / AgentMail, or by hand.** Send each approved email through the
connected account, from the verified sending address, with `sender.name` as the
display name. In a chat-only setup the owner pastes and sends each one.

- Space sends across the `send_window`. Do not fire 20 emails in 40 seconds. It
  is the most obvious automation signal there is.
- Send in the owner's business hours, in the prospect's timezone where known.
  Tuesday to Thursday mornings are the best days to start a sequence.
- Plain text. No tracking pixels, no link shorteners, no images. All three hurt
  deliverability.
- **Log every send the moment it happens.** A send that is not logged will be
  sent again.

**Stop the entire run and tell the owner immediately if:** a send fails
authentication, bounces pass about 3% of the batch, or the provider returns a rate
limit. Do not push through an error. A burned domain takes weeks to recover and
the owner would always rather stop.

## Step 5: Schedule and report

Queue the next step per `sequence_spacing_days` (day 3, then day 7). Before each
follow-up goes out, re-check for a reply, a stop, or a bounce. After day 7, the
prospect is done. Report:

```
Sent 18/18 · 0 bounces (0%) · next follow-ups Fri (6)
Week: 74 sent · 9 replies (12.2%) · 3 meetings
```

Reply rate is the number that matters. Track it weekly, and if it drops below
about 3%, say so and propose a specific change: a tighter segment, a different
trigger, a shorter email. Do not just keep sending.

**Completion criterion:** every approved email is sent and logged, every
follow-up is queued, no stop request is more than a day old, and the counts in the
report reconcile with the database.
