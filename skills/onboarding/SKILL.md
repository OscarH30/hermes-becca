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

## Resolve your accounts first

Every `{{ACCOUNT:<toolkit>}}` below is a placeholder. Read `brain/accounts.md`
and substitute the `word_id` recorded there.

If `brain/accounts.md` is missing, or the toolkit you need has no entry, **stop
and run `onboarding`.** Never substitute a default and never guess. An unpinned
call lands in whichever account the platform happens to pick — which may belong
to an entirely different company.


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

## Step 2 — Decide, together, what you are allowed to touch

You arrive with no accounts. This step is where the owner grants you each one,
deliberately. Until `brain/accounts.md` exists you must not read an inbox, spend
an Apollo credit, or touch a calendar.

Work through the four needs below. For each: say what it is for, whether it is
required, and offer both connection paths. Never make the owner guess, and never
pick an account for them.

| Need | Recommended | Alternative | Required? |
|---|---|---|---|
| Find prospects | `composio link apollo` | `APOLLO_API_KEY` in `.env` | Yes |
| Send & receive email | `composio link gmail` / `outlook` | `AGENTMAIL_API_KEY` | Yes |
| Store prospects | `composio link hubspot` / `gohighlevel` | local database (built in) | No |
| Book calls | a booking link | `composio link googlecalendar` | No |

For every toolkit, list what already exists before assuming anything:

```bash
composio connections list --toolkit gmail
```

Show every result with alias and status. Ask which one — and always offer the
third option: *"or would you rather connect a different one first?"* If they
want a new connection, wait while they run `composio link`.

### The sending inbox is the decision that matters most

Do not treat this as "pick a Gmail." Ask it as a real question, because the
right answer is often **a new account they do not have yet**:

> Do you want me sending from an inbox you already use, or should we set up a
> dedicated one for outreach?

Then give them the honest tradeoff before they answer:

> Sending cold email from your main company address can damage the
> deliverability of your normal mail — the mail you actually need to arrive.
> The standard practice is a separate domain that redirects to your real site,
> a dedicated mailbox on it, SPF/DKIM/DMARC configured, and two to three weeks
> of warmup before real volume. If you'd rather start today on an existing
> mailbox, that's your call — I'll cap the first week at 10–15 a day and we
> ramp from there.

If they choose a dedicated identity, **stop onboarding at this point.** Buying a
domain and warming a mailbox takes days, not minutes. Write down what you have
so far, tell them exactly what to set up, and pick this back up when it exists.
Stopping is the right outcome — the alternative is an agent wired to the wrong
address that starts sending before anyone notices.

Once an inbox is chosen, verify the address the provider will actually send as,
and read it back:

> I'll be sending as **outreach@yourcompany.com**. Confirm?

An alias in a connection list is not proof of the address. Check the mailbox.

### On the CRM

If they use a CRM that is not HubSpot or GoHighLevel, do not tell them they are
out of luck. Run `composio search "<their CRM> create contact"` — Composio covers
Close, Pipedrive, Salesforce, Zoho, Attio, Copper and more. If theirs genuinely
is not supported, say so and use the local database, which is a real backend and
not a consolation prize.

### Write the binding

Create `brain/accounts.md`. This is what turns you from inert into operational:

```markdown
# Account bindings
Written by onboarding. Every skill resolves {{ACCOUNT:...}} from here.

- toolkit: gmail
  word_id: gmail_example-handle
  verified_as: "outreach@yourcompany.com"
  method: composio
  dedicated_sending_identity: true
  owner_said: "yes, that's the right one"   # their literal words
  confirmed_at: 2026-08-20

- toolkit: apollo
  word_id: apollo_example-handle
  verified_as: "Your Company workspace"
  method: composio

- toolkit: crm
  word_id: ""            # empty = local database
  verified_as: "local"
```

Record a toolkit the owner deliberately skipped as an explicit empty binding, so
a later run can tell "chosen: none" apart from "never asked."


### The confirmation cannot be fabricated

`owner_said` holds the owner's **actual words**, quoted. If you cannot quote
something a human really typed in this session, the binding is **not confirmed**
and you may not write the file. Do not fill the field from inference, do not
paraphrase silence into agreement, and never write a confirmation date for a
confirmation that did not happen.

Every downstream skill trusts this field. A fabricated confirmation is not a
tidy-looking record — it is an agent operating on an account nobody approved.

`brain/` is yours, not the distribution's — `hermes profile update` never touches
it, so an update can never silently unwire or re-point you.

**Completion criterion:** `brain/accounts.md` exists; every required toolkit has
a binding the owner chose out loud; and the sending address has been verified
from the mailbox rather than inferred from an alias.

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
