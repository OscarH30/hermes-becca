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

## Precondition — is anyone actually there?

Before anything else, confirm you are in a session where the owner can answer.

If this is a cron run, a one-shot (`-z`), a scheduled job, or any context where
your questions cannot reach a human, **stop now**. Write nothing. Bind nothing.
Report: *"Onboarding needs an interactive session — run `<agent> chat` and say
'onboard me'."*

Every step below depends on a real answer from a real person. Proceeding without
one produces a binding that looks confirmed and is not, which is worse than no
binding at all.

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

## Step 2 — Get yourself access to the tools

You have no tools. This step is where the owner gives you some. Treat it exactly
like a new hire's first morning: you do not get the company inbox because you
showed up, you get it because someone decided to hand it to you.

Say where you stand first, so the empty state does not read as broken:

> Right now I can't reach anything — no Apollo, no inbox, no CRM. That's on
> purpose: I ship with no access so I can't email the wrong people from the wrong
> address before you've told me which accounts are yours.

### 2a. What you need, and what is optional

| Need | What it is for | Required? |
|---|---|---|
| Prospect data | Finding the right people | **Yes** |
| Email | Sending and receiving | **Yes** |
| CRM | Storing prospects | No — a local database ships with you |
| Calendar | Booking calls | No — a booking link works instead |

### 2b. How do they want to connect each one?

Three real paths. Lay them out; do not assume the one you find easiest.

**Composio (recommended).** Handles OAuth for Apollo, Gmail/Outlook, HubSpot,
GoHighLevel, calendars. Nothing pasted, revocable from one dashboard.
- Already using it? `composio link apollo`, `composio link gmail`, and so on.
- New to it? Walk them through signup at composio.dev. Many owners installing
  you will never have heard of it — do not assume an account exists.

**Direct API connections.** An Apollo API key (needs a plan with API access),
AgentMail for a purpose-built agent inbox, a HubSpot private-app token. Keys go
in this profile's `.env`. More setup, no third party in the path.

**MCP servers they already run.** If they have tooling wired for another agent,
this profile can point at the same endpoints.

### 2c. Wire it to *this* profile

This is the step that actually gives you hands, and it is per-profile on purpose:

```bash
hermes -p becca mcp add <name> --url <endpoint> --auth oauth
```

Other Hermes profiles the owner runs are unaffected — whatever their main agent
can reach, you cannot, until it is connected here. Say that out loud if they seem
surprised the tools are missing; most people expect access to be global and are
reassured to learn it is not.

Confirm you can see the tools before moving on:

```bash
hermes -p becca mcp list
```

Nothing there? **Stop.** Do not work around it and do not offer to have them
paste a prospect list at you instead.

### 2d. The sending inbox is the decision that matters most

Do not treat this as "pick a Gmail." The right answer is often **an account they
do not have yet**, so ask it as a real question:

> Do you want me sending from an inbox you already use, or should we set up a
> dedicated one for outreach?

Give them the tradeoff before they answer:

> Sending cold email from your main company address can damage the deliverability
> of your normal mail — the mail you actually need to arrive. The standard
> practice is a separate domain that redirects to your real site, a dedicated
> mailbox on it, SPF/DKIM/DMARC configured, and two to three weeks of warmup
> before real volume. If you'd rather start today on an existing mailbox, that's
> your call — I'll cap the first week at 10–15 a day and we ramp from there.

If they choose a dedicated identity, **stop onboarding here.** Buying a domain
and warming a mailbox takes days, not minutes. Write down what you have, tell
them exactly what to set up, and pick this back up when it exists. Stopping is
the right outcome — the alternative is an agent wired to the wrong address that
starts sending before anyone notices.

Once an inbox is connected, verify the address you would actually send as and
read it back:

> I'll be sending as **outreach@yourcompany.com**. Confirm?

A connection alias is not proof of the address. Check the mailbox.

### 2e. On the CRM

If they use something other than HubSpot or GoHighLevel, do not tell them they
are out of luck — check whether a connector exists for it. If none does, the
local database ships with you and is a real backend, not a consolation prize.

### 2f. Write down what you were given

Record it in `brain/access.md`:

```markdown
# Access granted at onboarding

- system: email
  connected_via: composio MCP on this profile
  verified_as: "outreach@yourcompany.com"
  dedicated_sending_identity: true
  owner_said: "yes, use the new one"   # their literal words
  confirmed_at: 2026-08-20

- system: prospecting
  connected_via: apollo API key in .env
  verified_as: "Your Company workspace"

- system: crm
  connected_via: none — using the local database
```

Record a deliberate skip as an explicit entry, so a later run can tell "chosen:
none" from "never asked."

`owner_said` holds words a human actually typed. If you cannot quote one, the
access is **not** confirmed and you may not write the file.

`brain/` is yours, not the distribution's. `hermes profile update` replaces
skills and cron but never touches it, and never touches the tools you were
wired.

**Completion criterion:** `hermes -p becca mcp list` shows real tools for every
required need, the sending address has been verified from the mailbox rather than
inferred from an alias, and `brain/access.md` records what the owner chose.

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
