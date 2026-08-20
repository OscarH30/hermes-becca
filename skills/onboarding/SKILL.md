---
name: onboarding
description: Use when Becca is first installed, when brain/business.md is missing, or when the owner says "onboard", "set me up", "start over", or "you don't know my business yet". Interviews the owner, connects their tools, reads any existing second brain, and writes the brain/ files every other Becca skill depends on.
version: 1.0.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [onboarding, setup, discovery, icp, crm]
    related_skills: [prospecting, cold-email, crm-sync]
---

# Onboarding Becca

Becca cannot write a good cold email for a business she does not understand.
This skill is how she learns one. Run it once at install; re-run it whenever the
offer, the ICP, or the tooling changes.

**Output of this skill is a set of files in `brain/`.** Every other skill reads
them. If you finish this skill and `brain/business.md` does not exist, the
onboarding did not happen.

## Step 0 — Find an existing brain before asking anything

Many owners already have their business written down. Asking them to repeat it
is the fastest way to look like a toy.

Check, in order:

1. Ask: *"Do you keep a second brain, a company wiki, or a folder of docs about
   your business? If so, point me at it — a path, an Obsidian vault, a Google
   Drive folder, a Notion workspace."*
2. If they name a **local path**, read it. Look for anything describing the
   offer, the customer, pricing, positioning, past wins, tone of voice.
3. If they name **Notion / Google Drive / Slack**, check whether that tool is
   connected (`composio search "<tool>"`, or an MCP server). If it is, read from
   it. If it is not, offer to connect it — do not silently skip it.
4. If they have nothing, say so plainly: *"No problem — most people don't. I'll
   ask you about a dozen questions and build one."*

**Completion criterion:** you can state, in one sentence, where the business
context is coming from — an existing brain, an interview, or both.

## Step 1 — Interview

Ask these in small batches, conversationally. Two or three at a time, not a
wall of twenty. Reflect what you heard back before moving on.

If Step 0 found an existing brain, **skip every question it already answers**
and say which ones you skipped. Asking a question the owner already documented
is the failure mode this step exists to avoid.

**The business**
- What do you sell, in the words a customer would use?
- What does it cost, and how is it priced?
- What happens to a customer who buys — what changes for them?

**The customer**
- Who is the best-fit customer? Industry, company size, geography.
- Whose job title actually feels this problem? Who signs?
- What is going on at a company right when they become ready to buy? (This is
  the trigger event, and it is the single most valuable answer in the interview
  — push for specifics.)
- Who is a bad fit? Who should I never email?

**The proof**
- Name a customer result you can point to. Numbers if you have them.
- Why do people pick you over the obvious alternative?
- What do prospects push back on, and what's the honest answer?

**The voice**
- Formal or casual with your customers?
- Anything you would never say? Words you hate?
- Do you have past emails that worked? (Ask for two or three. They are worth
  more than every style question above combined.)

**The rules**
- How many emails a day are you comfortable sending?
- Do you want to approve every batch, or approve the template and let me run?
  (Default is approve-every-batch. Say so.)
- Anyone or any company I must never contact?

## Step 2 — Connect the tools

Work through these four in order. For each, state what it is for, whether it is
required, and both connection paths. Never make the owner guess.

| Need | Recommended | Alternative | Required? |
|---|---|---|---|
| Find prospects | `composio link apollo` | `APOLLO_API_KEY` in `.env` | Yes |
| Send & receive email | `composio link gmail` (or `outlook`) | `AGENTMAIL_API_KEY` | Yes |
| Store prospects | `composio link hubspot` / `gohighlevel` | local database (built in) | No |
| Book calls | a booking link in `BECCA_BOOKING_LINK` | `composio link googlecalendar` | No |

**On the CRM:** if the owner uses a CRM that is not HubSpot or GoHighLevel, do
not tell them they are out of luck. Run `composio search "<their CRM> create
contact"`. Composio covers most of them. If theirs is genuinely unsupported,
say so and use the local database — it is a real fallback, not a consolation
prize.

**On email, be honest about deliverability.** Say this out loud, in plain
language, before they connect anything:

> Sending cold email from your main company domain can hurt the deliverability
> of your normal mail. The standard practice is a separate domain that
> redirects to your real site, a dedicated mailbox on it, SPF/DKIM/DMARC set
> up, and two to three weeks of warmup before real volume. If you skip the
> warmup and send fifty on day one, they land in spam and the domain is burned.

Then ask which they want. If they want to start today on an existing mailbox,
that is their call — cap the first week at 10-15/day and tell them why.

**Completion criterion:** for each of the four rows, you can state either
"connected via X" or "deliberately skipped, because Y."

## Step 3 — Write the brain

Create these files. Be concrete; vague files produce vague email.

**`brain/business.md`** — what they sell, pricing, the transformation, proof
points with real numbers, competitors and the honest differentiator, common
objections and answers. Mark anything you inferred rather than heard as
`[INFERRED]` so it can be corrected later.

**`brain/icp.md`** — industries, company size, geography, target titles, and the
trigger events. Write the trigger events as things you could actually search for
in Apollo (hiring for a role, recent funding, headcount growth, a tech change).
End with an explicit exclusion list.

**`brain/voice.md`** — tone, words to use, words to never use, sign-off, and any
example emails they gave you, quoted verbatim. Verbatim examples matter more
than your description of them.

**`brain/config.md`** — the operating rules, as a machine-readable block:

```yaml
autonomy: approve        # approve | auto
daily_send_cap: 20
daily_prospect_target: 25
sequence_steps: 3
sequence_spacing_days: [0, 3, 5]
crm: local              # local | hubspot | gohighlevel | <composio toolkit>
email_provider: gmail   # gmail | outlook | agentmail
booking_link: ""
send_window: "09:00-16:00"
timezone: "America/Chicago"
```

**`brain/suppression.md`** — never-contact list. Seed it with everyone they
named in the interview, plus their own domain.

**`brain/rules.md`** — start it with a single line: `# Learned rules` and a note
that Becca appends here as she learns what works. It will fill up on its own.

## Step 4 — Initialize storage

Run `scripts/init_db.py` to create the local prospect database. Do this even
when a CRM is connected — it is Becca's send log and dedupe index, and it is
what makes "never email the same person twice" true.

## Step 5 — Prove it works, then hand back

Do not end onboarding with a summary. End it with evidence:

1. Pull **three** real prospects from Apollo against the ICP you just wrote.
2. Write **one** complete cold email to the best of them, run it through the
   `humanizer` skill, and show it.
3. Say what you would do tomorrow morning without being asked, and which cron
   jobs are scheduled to do it.
4. Ask one question: *"Does that email sound like you?"* Their answer is the
   most valuable correction you will get all week — write it into
   `brain/voice.md` before you do anything else.

**Completion criterion:** the owner has read a real email to a real prospect
from their real ICP, and you have written their reaction into the brain.
