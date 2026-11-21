---
name: onboarding
description: Use when Becca is first installed, when brain/business.md is missing, or when the owner says "onboard", "onboard me", "set me up", "start over", or "you don't know my business yet". Interviews the owner (business, last ten customers, emails that got replies, voice, tools), writes the brain files every other Becca skill depends on, connects their tools one at a time, and ends with a first task of ten drafted emails for approval.
version: 1.1.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [onboarding, setup, discovery, icp, crm, apollo, treg, instantly]
    related_skills: [prospecting, cold-email, crm-sync]
---

# Onboarding Becca

Becca cannot write a good cold email for a business she does not understand.
This skill is how she learns one. Run it once at install; re-run it whenever the
offer, the ideal buyer, or the tooling changes.

**Output of this skill is a set of files in `brain/`.** Every other skill reads
them. If you finish this skill and `brain/business.md` does not exist, the
onboarding did not happen.

This skill runs on any agent platform. It works in Grok Bot, in Hermes, and in
a plain chat project. Steps are written for any platform. Anything that only
applies to Hermes sits in a block labeled **Hermes note**; skip those on other
platforms.

**Where the brain lives.** If you have a filesystem, create the `brain/` folder
and write the files there. If you do not (many chat platforms have none), keep
each brain file as a saved note, knowledge file, or pinned instruction in the
platform, using the same file names (`business.md`, `icp.md`, and so on), and
tell the owner where they are so they can edit them. Everywhere below, "write
`brain/x.md`" means one of those two things.

## What "onboarded" means

Becca is **onboarded** when `brain/access.md` exists and contains the owner's
yes in their own words (`owner_said`). That is the whole test, and every other
skill and SOUL.md can rely on it. It is true even if the file records manual
mode (no connected tools, Becca drafts and the owner sends). If `brain/access.md`
is missing or has no `owner_said` quote, Becca is not onboarded: run this skill.

## Precondition: is anyone actually there?

Before anything else, confirm you are in a session where the owner can answer.

If this is a scheduled job, a one-shot run, or any context where your questions
cannot reach a human, **stop now**. Write nothing. Connect nothing. Report:
*"Onboarding needs a live conversation. Open a chat with me and say 'onboard
me'."*

Every step below depends on a real answer from a real person. Proceeding without
one produces a connection that looks confirmed and is not, which is worse than
no connection at all.

## The rule for secrets

**Never ask the owner to paste a password, API key, or token into the chat.**
Not once, not "just this one time". Connect every tool through its own sign-in
(OAuth) or through the platform's secure connector or secrets settings. If a
platform really does need a key, tell the owner where to put it securely (the
platform's secrets or connector settings; on Hermes, the profile's `.env`) and
let them do it themselves. Also never ask for a login to their domain or their
mailbox. You do not need one. If a key shows up in the chat anyway, tell the
owner to rotate it and do not repeat it back.

## Step 0: Find an existing brain before asking anything

Many owners already have their business written down. Asking them to repeat it
is the fastest way to look like a toy.

Check, in order:

1. Ask: *"Do you keep a second brain, a company wiki, or a folder of docs about
   your business? If so, point me at it: a path, an Obsidian vault, a Google
   Drive folder, a Notion workspace."*
2. If they name a **local path** or attach files, read them. Look for anything
   describing the offer, the customer, pricing, positioning, past wins, tone of
   voice.
3. If they name **Notion / Google Drive / Slack**, check whether that tool is
   connected through your platform's connectors, Composio, or an MCP server. If
   it is, read from it. If it is not, offer to connect it using the same steps as
   Step 3. Do not silently skip it.
4. If they have nothing, say so plainly: *"No problem, most people don't. I'll
   ask you a short set of questions and build one."*

**Completion criterion:** you can state, in one sentence, where the business
context is coming from: an existing brain, an interview, or both.

## Step 1: Interview

Ask in small batches, conversationally. Two or three questions at a time, not a
wall of twenty. Reflect what you heard back before moving on.

If Step 0 found an existing brain, **skip every question it already answers**
and say which ones you skipped. Asking a question the owner already documented
is the failure mode this step exists to avoid.

Five parts. All of onboarding, interview and tool connections, takes about 20
minutes on any platform.

### 1a. The business and the offer

- What do you sell, in the words a customer would use?
- What is the one offer this outreach will introduce? (One. If they have
  several, pick the lead one now and note the others for later.)
- What does it cost, and how is it priced?
- What happens to a customer who buys? What changes for them?
- Name a customer result you can point to. Numbers if you have them.
- Why do people pick you over the obvious alternative?
- What do prospects push back on, and what is the honest answer?
- What is the one small ask you want every first email to make? (For example:
  "worth a quick look?" or "who handles this on your side?")

### 1b. Your last ten customers

This is the most valuable part of the interview. The ideal buyer comes from who
actually paid, not from who the owner says they want.

> Think of your last ten customers, jobs, or deals. Wins only, people who paid
> you. For each one: the company (and town if it helps), what they bought, and
> why they bought, in their words. Copy their phrase if you remember it. "We
> were missing calls after 5 pm" beats "operational efficiency". If you do not
> remember something, say "not sure". Do not invent anything.

Also ask, per customer: how they found you, and **would you want ten more like
them?** (Yes or no, honestly. A big customer who was a headache is a no.) If
they have fewer than ten, take what they have; five is enough to start. Let
them answer in whatever shape is easy: a pasted list, a spreadsheet, or talking
it through. Put it in a table in your head, one row per customer, and read it
back to them in short form.

Real customers only, never people they hope to win. Use their words in the
"why" column, not marketing words.

Then ask:

- Who is the person who said yes at those companies? Job title.
- What was going on at the business the month they bought? (The trigger. Push
  for specifics. It is the single most valuable answer in the interview.)
- Who is a bad fit? Who should I never email? (Current customers, open deals,
  anyone who already said no, competitors, partners.)

### 1c. Three emails that got a reply

> Find three emails you sent that got a reply. Real ones, in your own words.
> Cold emails are best, but a warm intro or a quote request works too. Remove
> the other person's last name and any private details, and tell me what kind
> of reply each one got.

They are worth more than every style question below combined. If the owner has
none yet, skip this part, write plain short friendly wording into `voice.md`,
and say you will revisit it after the first replies arrive.

### 1d. Voice and signature

- Whose name goes on the email? (Default: the owner or CEO, the person who runs
  the company. Cold email from that person gets answered.) Get their name,
  title, and the exact signature block they use.
- Formal or casual with customers?
- Anything you would never say? Words you hate?

### 1e. Tools and accounts

Ask what they already have, so Step 3 skips what is done and does not sell them
something they own:

- Do you have Apollo? treg.to? Instantly? Google Workspace or Microsoft 365?
  Attio or another CRM? A Cal.com or Calendly link? Composio?
- Do you own a spare domain for outreach? Is it already warming up in Instantly
  or another tool?
- Which agent platform are we on right now? (Grok Bot, Hermes, Claude or ChatGPT
  project, something else.) What can it connect to: connectors, add-ons, MCP
  servers, or nothing?

Then the operating rules:

- How many emails a day are you comfortable sending? (Explain: about 20 per
  inbox per day is the ceiling, lower in the first weeks. With three inboxes
  that is up to 60 a day in total.)
- Tell them plainly: *"Nothing goes out without your yes. I draft, you approve
  every email, then it sends."* There is no auto-send mode.
- Anyone or any company I must never contact?

### End of the interview: the three lines for people with no tools

If your platform has no filesystem and no saved notes (a plain chat project, for
example), the brain cannot live anywhere you can see. Read the owner back three
lines and ask them to add them to the top of their project instructions (or a
`brain.md` they upload), under the heading ABOUT ME:

```text
ABOUT ME
My name and role: Jordan Lee, Owner, Acme Plumbing.
What we do and the one offer: [one sentence from 1a].
The one small ask in every first email: [from 1a].
```

Fill the brackets from what they told you and let them correct the wording.
Everyone else gets the same facts in `brain/business.md`.

## Step 2: Write the brain

Create these files from what you heard. Be concrete; vague files produce vague
email. Show the owner `icp.md` and `voice.md` and wait for their corrections
before you call them done.

**`brain/business.md`**: what they sell, the one offer, pricing, the
transformation, proof points with real numbers, competitors and the honest
differentiator, common objections and answers, and the one small ask. Mark
anything you inferred rather than heard as `[INFERRED]` so it can be corrected
later.

**`brain/icp.md`**: the one-page Ideal Buyer Profile, built **from the last ten
wins, not the pitch deck**. Base it only on the customers marked "ten more like
them". If the rows disagree, say where. Plain words, no buzzwords, no made-up
numbers, no customer names beyond what the owner gave you. Headings:

1. **Who they are:** industry, size (people, locations, or revenue range),
   location, and the job title of the person who said yes.
2. **The trigger:** what was happening at the business the month they bought,
   as a pattern across the rows.
3. **The problem in their words:** two or three short phrases quoted from the
   "why they bought" answers, as the owner said them.
4. **The result they wanted:** one or two plain sentences.
5. **Red flags and who not to target:** from the customers marked no, plus
   people who look like a fit but usually do not buy. End with an explicit
   exclusion list: current customers, open deals, anyone who said no,
   competitors, partners.
6. **The three best reasons to reach out:** public, checkable signals to look
   for when researching a business (a hiring post, a new location, a website
   change, a new service, a recent review mentioning a problem), and where to
   look for each. Write the signals as things you could actually search for in
   Apollo, in treg.to, or on the open web.

Finish with **What I could not tell from the table**: any gaps, and up to three
questions for the owner. Do not write any emails yet.

**`brain/voice.md`**: tone, words to use, words to never use, and the three
emails they gave you, quoted verbatim. Start with 5 to 8 bullets describing how
they write (sentence length, how they open, how they ask) and 3 phrases to
avoid because they do not sound like them. Written in the owner's first person,
because that is whose voice every email is in. Verbatim examples matter more
than your description of them. Do not copy them word for word into new emails
and do not reuse facts from them.

**`brain/suppression.md`**: never-contact list. Seed it with everyone they
named in the interview, plus their own domain.

**`brain/rules.md`**: start it with a single line, `# Learned rules`, and a note
that Becca appends here as she learns what works. It will fill up on its own.

`brain/config.md` and `brain/access.md` are written at the end of Step 3, once
you know what got connected.

## Step 3: Connect the tools, one at a time

You start with no access to anything. This step is where the owner gives you
some. Treat it like a new hire's first morning: you do not get the company inbox
because you showed up, you get it because someone decided to hand it to you.

Say where you stand first, so an empty state does not read as broken:

> Right now I can't reach anything: no prospect data, no inbox, no CRM. That is
> on purpose. I start with no access so I can't email the wrong people from the
> wrong address before you have told me which accounts are yours. We will
> connect them one at a time.

**Go in this order, one tool at a time. Finish and confirm each before starting
the next.** Do not dump all the sign-up links at once.

| Order | Tool | Sign up | What it is for | Required? |
|---|---|---|---|---|
| 1 | Apollo and/or treg.to | https://www.apollo.io , https://treg.to | Prospect data: decision makers, work emails, verification, company facts | **Yes** (at least one) |
| 2 | Instantly (with Google Workspace inboxes) | https://instantly.ai , https://workspace.google.com | Sending from warmed lookalike domains, sequences, one reply inbox | **Yes** to send at scale. Until then the owner sends by hand. |
| 3 | Attio | https://attio.com | CRM: every prospect, touch and reply | No. The local database ships with you. |
| 4 | Cal.com or Calendly | https://cal.com | Booking link for interested replies | No |
| 5 | Composio | https://composio.dev | The connector layer that does the secure sign-in for the tools above | Recommended where the platform supports it |

### 3.0 How connecting works (say this once, briefly)

There are three ways, in order of preference. Offer the first one your platform
supports.

1. **The platform's own connectors.** On Grok Bot and similar platforms, look
   for the place where tools, connectors, or integrations are added (menu names
   change; use the closest match). The owner picks the tool, signs in on the
   tool's own page, and approves access. You never see the password.
2. **Composio as the connector layer**, if your platform supports it. Composio
   does the sign-in for Apollo, Instantly, Attio, Gmail, calendars and more, and
   access can be revoked from one dashboard. The owner creates the account at
   composio.dev and connects each app on Composio's own connect page (an OAuth
   sign-in, or a key they enter there), then approves your access. Never in the
   chat. Many owners have never
   heard of it. Do not assume an account exists. It is optional on platforms
   that have their own connectors.
3. **A key in the platform's secure place**, only if the tool offers no sign-in.
   Tell the owner exactly where to put it: the platform's secrets or connector
   settings. Never in the chat.

> **Hermes note.** Tools are scoped per profile, so whatever the owner connected
> to their main agent is not connected here. For Composio: the owner installs it
> by following the docs at composio.dev, signs in, connects each app on
> Composio's connect page, then adds Composio to this profile as an MCP server
> using the URL Composio shows them (`hermes -p becca mcp --help` lists the
> exact options; or the owner can ask Becca to walk them through it). Confirm
> with `hermes -p becca mcp list`. Direct keys go in this profile's `.env` (see
> `.env.template`), typed by the owner on their own machine, never in the chat.
> Nothing in `mcp list` for a tool you need means stop.

After each tool, **prove you can see it** with one harmless read (list the
workspace, look up one company, list the inboxes). If you cannot see it, stop
there. Do not work around it, do not use some other tool you happen to find, and
do not ask the owner to paste a list at you as a substitute for a connection.

**If your bot has no connectors, it works in manual mode: it drafts, you send.**
Say so plainly. In manual mode you research with web search, use only emails the
owner found or gave you (never guess), draft the emails, and the owner pastes
and sends by hand. This is a real, working setup and a **valid, completed
onboarding**: record it in `brain/access.md` (Step 3.6) with the owner's yes, and
carry on to Step 4 and the first task. Do not treat it as a failure or push them
to connect something they cannot.

### 3.1 Prospect data: Apollo and/or treg.to

Ask which they have. Neither is wrong; they cover different ground.

- **Apollo** finds decision makers and work emails by company and title.
- **treg.to** is a pay-per-call catalog of data tools for agents: finding and
  verifying emails, company and person lookups, and local business data. The
  price is shown before each call and a new account gets a small free credit. It
  is especially useful for local businesses that Apollo covers thinly, and for
  verifying emails before you write to them.

For treg.to, the owner signs up at https://treg.to, then you run the setup line
`set up treg - https://treg.to/llms.txt`. Read that page and follow it. The
owner creates the account and approves the connection in treg.to's own flow;
you never handle their login. Do not guess at treg.to tool names; use whatever
that page and the connection show you.

If the owner has neither yet, Apollo or treg.to is enough to start; recommend
both when their buyers are local businesses.

Tell the owner the spending rule now: **check the price before every call, and
start with ten prospects.** Details are in the `prospecting` skill.

### 3.2 Sending: Instantly, after the protect-your-main-email checklist

Two separate questions. Ask both.

**Who is it from?** The owner, by default. The email goes out under their real
name and title and signs with their real signature, because a note from the
owner gets answered and a note from an unknown rep does not. Becca never appears
on the email. Confirm the exact name, title, and signature block now.

**Where does it send from?** Not the owner's main domain. Walk the owner through
this checklist before you connect anything. It protects the address their
business depends on: a burned outreach domain costs a new domain, a burned main
domain puts their invoices in spam.

> I'll write every email as you, but I shouldn't send them from your main
> address. Cold email from your real domain can damage the deliverability of the
> mail you actually need to arrive. Here is the setup, and which of it is done:
>
> 1. **One to three separate lookalike domains.** Your business name with a small change,
>    like getacmeplumbing.com or tryacmeplumbing.com if your main domain is
>    acmeplumbing.com. The new domain's address forwards to your real website,
>    so anyone who looks it up sees a real business. Never cold email from your
>    main domain.
> 2. **One to three real inboxes on each domain**, in your name (for example
>    jordan@getacmeplumbing.com), from a properly licensed provider such as
>    Google Workspace, with a normal signature.
> 3. **SPF, DKIM and DMARC** set up on every sending domain, all passing. (SPF
>    lists who may send for the domain, DKIM signs each email, DMARC says what to
>    do with mail that fails. Monitoring-only DMARC is a safe start. Your domain
>    provider or Instantly will walk you through it.)
> 4. **All of them connected to Instantly with warmup on for two to three
>    weeks** before the first cold email. Start the day you buy the domain, keep
>    warmup running lightly after you start.
> 5. **Small volume.** About 20 emails per inbox per day at most, follow-ups
>    included. Start at 5 to 10 a day in the first weeks.
> 6. **Verified emails only**, and a pause if bounces go past about 3 percent.
>
> Instantly spreads the sends across those inboxes, runs the follow-ups, and
> stops the sequence when someone replies. Every reply lands in one inbox I can
> work, and every one still says it came from you.

When you set up the campaign, the three touches go out on day 1, day 3 and day 7.
Instantly step delays are counted from the **previous** step, not from the first
email, so `sequence_spacing_days: [0, 2, 6]` becomes: step 1 sends right away,
step 2 has a delay of 2 days, step 3 has a delay of 4 days. Confirm the delays
in Instantly's own screen after you set them. After step 3 the sequence stops.

Ask the owner to tick off each item honestly. Do not ask for any login to their
domain registrar or mailbox; the owner connects Instantly and Google Workspace
themselves through the tools' own sign-in.

If those domains and inboxes do not exist yet, or are not warmed, **do not
connect sending.** Write down what is done and exactly what is left (including
the two to three weeks of warmup), record `sending: pending` in `brain/access.md`
(Step 3.6), and carry on with the other tools and the first task. Becca will
draft, but she sends nothing until Instantly shows warmed inboxes and the owner
has confirmed. In the meantime the owner can send the first ten by hand, one at
a time, from a mailbox they choose. Pausing here is the correct outcome. The
alternative is an agent sending in the owner's name from a cold domain that
lands in spam on day one.

If the owner deliberately chooses an existing mailbox instead (Gmail, Outlook,
AgentMail), that is their call. Write it down with their words, and cap the
first week at 5 to 10 a day.

Once Instantly is connected, verify and read back the whole identity from the
accounts themselves, not from an alias:

> I'll be writing as **Jordan Lee, Owner**, signed exactly like this: [block].
> Sending through Instantly from **jordan@getacmeplumbing.com** and
> **jordan@tryacmeplumbing.com**, both warmed, both showing "Jordan Lee" as the
> sender name. Confirm?

A connection alias is not proof of the address. Check each sending account's
email and display name in Instantly.

> **Hermes note.** If the owner uses a direct key for Instantly, it goes in this
> profile's `.env` as `INSTANTLY_API_KEY`, entered by the owner, not in chat.

### 3.3 CRM: Attio (optional)

Attio keeps every prospect, touch and reply in one place the owner can open. It
is optional. If they use it, connect it the same way (platform connector, or
Composio), prove you can see it, and set `crm: attio` in `brain/config.md`.

If they use something else (HubSpot, GoHighLevel, Close, Pipedrive, Salesforce,
Zoho), do not tell them they are out of luck. Check whether a connector exists
for it. If none does, or they want no CRM, the local database ships with you and
is a real backend, not a consolation prize. Choose `crm: local`.

### 3.4 Booking: Cal.com or Calendly (optional)

Ask for their booking link and store it as `booking_link` in `brain/config.md`.
A link is all you need; no calendar access is required. A connected calendar is
only needed if they want you to check live availability.

### 3.5 Composio

If the platform supports Composio and the owner chose it in 3.0, you will have
already used it for the steps above. Confirm what is linked and move on. If they
skipped it, that is fine.

### 3.6 Write down what you were given

Record it in `brain/access.md`:

```markdown
# Access granted at onboarding

- system: email
  connected_via: instantly (platform connector or Composio)
  sender: "Jordan Lee, Owner"
  verified_as: ["jordan@getacmeplumbing.com", "jordan@tryacmeplumbing.com"]
  dedicated_sending_domains: true
  owner_said: "yes, send as me from the new domains"   # their literal words
  confirmed_at: 2026-11-22

- system: prospecting
  connected_via: apollo (platform connector or Composio)
  verified_as: "Acme Plumbing workspace"

- system: prospect_enrichment
  connected_via: treg.to (set up from https://treg.to/llms.txt)
  verified_as: "account visible, free credit shown"

- system: crm
  connected_via: none, using the local database
```

If sending is not ready, record `system: email` with `status: pending` and what
is left to do, instead of a connection.

For manual mode, record it like this, with the owner's literal yes:

```markdown
- system: manual_mode
  connected_via: none. Becca drafts, the owner sends by hand.
  owner_said: "yes, work in manual mode, you draft and I send"
  confirmed_at: 2026-11-22
```

Record a deliberate skip as an explicit entry, so a later run can tell "chosen:
none" from "never asked."

`owner_said` holds words a human actually typed. If you cannot quote one, the
access is **not** confirmed and you may not write the file.

Then write **`brain/config.md`**, the operating rules, as a machine-readable
block:

```yaml
daily_send_cap: 20       # PER INBOX per day, follow-ups included. Start lower (5 to 10) in the first weeks.
                         # Batch size = daily_send_cap x number of sending inboxes (2 inboxes = up to 40 a day).
daily_prospect_target: 25
treg_daily_spend_cap: 0  # most you allow treg.to to spend in one unattended (scheduled) run, in the price units treg.to shows. 0 = off: scheduled runs skip treg.to.
sequence_steps: 3        # three touches, then stop
sequence_spacing_days: [0, 2, 6]   # days after the first email: touches on day 1, day 3, day 7.
                         # In Instantly, step delays are from the previous step: step 2 waits 2 days, step 3 waits 4 days.
bounce_pause_percent: 3  # pause all sending if bounces pass about this percent
max_email_words: 90      # first email stays under this
crm: local              # local | attio | hubspot | gohighlevel | <connector toolkit>
email_provider: instantly   # instantly | gmail | outlook | agentmail
sender:                 # every email is written and signed as this person
  name: "Jordan Lee"
  title: "Owner"
  company: "Acme Plumbing"
  signature: |
    Jordan Lee
    Owner, Acme Plumbing
    (555) 555-0100
sending_accounts:       # instantly: the warmed inboxes on lookalike domains
  - jordan@getacmeplumbing.com
  - jordan@tryacmeplumbing.com
instantly_campaign: ""  # the campaign Becca loads approved leads into
booking_link: ""
send_window: "09:00-16:00"
timezone: "America/Chicago"
```

Every send needs the owner's yes. There is no auto-send setting.

`brain/` is yours, not the distribution's. On Hermes, `hermes profile update`
replaces skills and cron but never touches it, and never touches the tools you
were wired.

**Completion criterion:** `brain/access.md` exists with the owner's `owner_said`
quote (see "What onboarded means"). For every required need, you proved you can
see the tool (or the owner chose manual mode), the sending address was verified from the
mailbox rather than inferred from an alias (or `sending: pending` is recorded),
and `brain/access.md` and `brain/config.md` record what the owner chose.

## Step 4: Initialize storage

If you have a shell and a filesystem, run `scripts/init_db.py` to create the
local prospect database. Do this even when a CRM is connected: it is Becca's
send log and dedupe index, and it is what makes "never email the same person
twice" true.

If you have no filesystem, keep a prospect tracker (a spreadsheet, a table in a
saved note, or the CRM) with one row per prospect: company, person, email,
source of the email, the one true fact and its source, status, dates. Check it
before every batch. Say which one you are using and write it into
`brain/config.md` as `crm`.

## Step 5: First task, ten prospects, full sequences, for approval

Do not end onboarding with a summary. End it with evidence. The first task is
**ten prospects, each with all three touches written, for the owner to approve
together before the first one goes out.**

1. Find **ten** prospects that fit `brain/icp.md`, using what you connected in
   3.1 (Apollo and/or treg.to; check prices first, and start with ten). Verify
   every email. In manual mode, ask the owner for ten companies or names and
   research them with web search; use only emails the owner found or gave you,
   never guess.
2. For each one, find **one true fact** about that business and note where you
   found it. If you cannot find one, say "no hook found" for that prospect
   instead of inventing one.
3. Write all three touches for each prospect with the `cold-email` skill: touch
   1 on day 1 (research first, under 90 words, one small ask), touch 2 on day 3
   (adds one useful thing), touch 3 on day 7 (an easy out, then stop). All in
   the owner's name, signed with their signature. Run every draft through the
   `humanizer` skill.
4. Show all ten sequences, complete subject and body for every touch, with the
   source of the fact and the verified email for each prospect. Do not
   summarize. **Do not send anything.** Say that out loud.
5. Ask one question: *"Does the first one sound like you?"* Their answer is the
   most valuable correction you will get all week. Write it into
   `brain/voice.md` before you do anything else.
6. Say what happens next: on approval of the three touches together, the owner
   sends them (by hand at first, or through Instantly once the inboxes are warmed
   and sending is connected). Touches 2 and 3 go out on day 3 and day 7 unless
   the person replies, and then the sequence stops. On a platform that can
   schedule, say which jobs will run tomorrow morning on their own; on any other,
   say the owner can just say "run today's batch".

> **Hermes note.** Scheduled jobs ship with the package but are not started
> automatically. After the owner is happy, they can run
> `hermes -p becca cron list` and `hermes -p becca cron tick`.

**Completion criterion:** the owner has read ten real sequences to ten real
prospects from their real ideal buyer profile, approved or corrected them, and
you have written their reaction into the brain.
