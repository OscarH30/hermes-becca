# Becca, your outreach agent

If you are an AI agent reading this: open AGENT-SETUP.md and follow it.
Raw URL: https://raw.githubusercontent.com/OscarH30/hermes-becca/main/AGENT-SETUP.md

Becca is the agent's name. Tell your agent: **set up the outreach agent from https://github.com/OscarH30/hermes-becca**

That one sentence is the whole start. Your agent reads this repo, installs the
skills, and walks you through setup by asking about your business. Becca finds
the right people, writes cold email that sounds like a person, works the inbox,
hands interested leads to your CRM, and books calls.

**Every email goes out in your name, not hers.** She writes as you, the owner or
CEO, and signs with your signature. Each weekday she builds one campaign of up to
50 contacts and emails it to you. **You approve that campaign by replying, then
she sends it** (or you send by hand). Nothing is loaded or sent without your
approval of that specific campaign. That is the rule and she does not drift out
of it.

---

## How it works

1. **Brain.** She asks whether you already have a company brain (Notion, Google
   Drive, GBrain, Obsidian, a local folder, any knowledge base). If you do, she
   pulls your business context and existing contacts from it. If you do not, she
   interviews you and builds a starter brain.
2. **Contacts.** Every weekday she finds people who match your ideal buyer and
   your offer (treg.to, Apollo), skips anyone already in your brain, your CRM or
   your do-not-contact list, and researches each one for one true, sourced fact.
3. **Write.** She writes a custom first email per contact (under 90 words, one
   small ask) plus a day 3 and a day 7 follow-up, in your voice. Three touches,
   then stop.
4. **Daily campaign approval by email.** She builds one new campaign of up to 50
   contacts and emails you one approval email: who they are, every contact with
   its custom first email, and the plan. You reply **APPROVE** (from your approval
   address, to that email), or reply with changes and she revises and resends.
   Only then does it load into Instantly and send, within the daily cap.
5. **Replies to your CRM.** Replies come back in Instantly and are sorted into
   seven buckets. Interested leads go to your CRM (or a Google Sheet or CSV if
   you have none) and are listed in the daily summary. Your team takes it from
   there. The CRM gets only your hot leads. Every prospect and every send stays in
   her own database, so nothing in your CRM can be emailed by accident.

How big is a campaign? Up to 50 is the ceiling. Each contact gets three emails,
so the real number is about (sending inboxes x daily cap per inbox) / 3 new
contacts a day. Onboarding works it out with you, and each approval email says
what the campaign was sized to.

---

## Get set up

Pick the one that matches your agent.

### Grok Bot

1. Open Grok Bot and start a chat with your bot (or create a new one for this).
2. Paste the sentence above: *set up the outreach agent from
   https://github.com/OscarH30/hermes-becca*
3. It reads `AGENT-SETUP.md` in this repo, saves the skills and rules as its own
   instructions or knowledge, and then runs `onboarding`.
4. Answer the questions (about 20 minutes). It starts by asking about your
   company brain, then your CRM and the email address where your daily campaign
   goes. It walks you through connecting each tool below, one at a time, using
   the connection options in your bot's own settings.

A bot that cannot check email on its own has no schedule. After you reply to
the approval email, tell it **"check my approval"** and it looks for your reply
then.

Menu names in Grok Bot change over time. If the agent points you at a settings
page, look for the closest match to what it describes. If your bot has no
connectors, it works in manual mode: it drafts, you send. If your bot cannot
read links, use the no-tools steps below.

### Hermes Agent

```bash
hermes profile install github.com/OscarH30/hermes-becca --alias
hermes -p becca setup --portal   # give this profile a model
becca chat
```

Then say **"onboard me"**. Becca installs as her own profile alongside whatever
you already run. Nothing you have is modified. Hermes profiles carry their own
credentials, so skip `setup --portal` and you will see "No inference provider
configured". Needs Hermes 0.20.0 or newer and git.

### Claude Projects, ChatGPT Projects or GPTs (no tools)

For agents that cannot open links or connect tools:

1. On this page choose **Code > Download ZIP**, then unzip it.
2. Create a new project (or GPT).
3. Open `AGENT-SETUP.md`, find the "Job description" section, and copy only what
   is inside the code box. Paste it into the project's instructions.
4. Upload these files as project files. Eight of them are named `SKILL.md`, so
   rename each one to its folder name first (`onboarding.md`, `cold-email.md`,
   and so on) or they will collide:
   - `SOUL.md`
   - the eight skills: `onboarding`, `prospecting`, `cold-email`, `humanizer`,
     `inbox-triage`, `outreach-campaign`, `crm-sync`, `booking`
   - the five files in `skills/cold-email/references/`
   If your plan limits how many files you can upload, add them in this order:
   Job description (instructions box), `SOUL.md`, onboarding, cold-email,
   prospecting, humanizer, inbox-triage, then the rest.
5. Turn on web search. If there is none, paste each prospect's website text into
   the chat and tell the agent to use only that.
6. Start a chat and say **"onboard me"**.
7. At the end of onboarding, the agent shows you your brain notes. Save them as
   `brain.md` and upload it to the project. Whenever the agent shows you a new
   version, replace the old file. These projects forget between chats, and this
   file is how she remembers your business.

In this mode there is no email channel and no scheduled run. Becca shows you the
full campaign in chat, you approve it by typing a message of your own that names
the campaign id (pasted text never counts), and you paste and send by hand. Everything else, the research, the voice, the
three-touch sequence and the reply sorting, works the same.

---

## The tools I use

Sign up for these, connect them to your agent, and go. Onboarding goes through
them in this order, one at a time: Apollo and/or treg.to, Instantly (with Google
Workspace inboxes on lookalike domains), the email channel she uses to send you
the daily campaign, your CRM (whichever one you use), Cal.com or Calendly, then
Composio as the connector layer where your platform supports it. You connect
each app on its own sign-in page. You never paste a password or API key into the
chat.

You will need paid plans for some of these tools, and a domain registrar to buy
the lookalike sending domain. Check each tool's pricing page before you sign up.

| Tool | Sign up | Job | Required | How your agent connects it |
|---|---|---|---|---|
| Apollo | https://www.apollo.io | find decision makers and work emails | Yes (or treg.to) | through your platform's connector settings, or through Composio |
| treg.to | https://treg.to | pay-per-call research tools: verify emails, enrich companies, local business data | Recommended | you send `set up treg - https://treg.to/llms.txt`; the agent follows that page and you approve the connection |
| Instantly | https://instantly.ai | send from warmed lookalike domains, sequences, reply inbox | Yes for sending at scale (or send by hand from Gmail at first) | through your platform's connector settings, or through Composio |
| Google Workspace | https://workspace.google.com | inboxes on your lookalike sending domains | Yes for Instantly | you create the inboxes, then connect them to Instantly yourself |
| Your CRM (any: Attio, HubSpot, GoHighLevel, Pipedrive, or a Google Sheet) | your own CRM's site | receives interested leads with the reply and a suggested next step | Optional (a CSV or Google Sheet otherwise) | through your platform's connector settings, or through Composio |
| Composio | https://composio.dev | connects Apollo, Instantly, your CRM, Gmail to your agent through secure sign-in (OAuth) | Recommended for Hermes; optional elsewhere | you make an account, then connect each app on Composio's own connect page (OAuth, or a key you enter there), never in chat |
| Cal.com | https://cal.com | booking link for interested replies (Calendly also works) | Optional | you give your public booking link, nothing else |

The email channel for your daily campaign is separate from the warmed Instantly
inboxes. It can be your own connected Gmail or Outlook, AgentMail, or your
platform's own email. If none is available, she shows the campaign in chat
instead, which is a fallback.

If a tool needs a key and offers no sign-in, the agent tells you where to put it
securely (in Hermes, the profile's `.env` file; elsewhere, the platform's
secrets or connector settings). Never in the chat.

---

## What you get

| What the class promised | What does it | Skill |
|---|---|---|
| An outreach agent with a job description it follows every time | the rules in `SOUL.md` and the job description in `AGENT-SETUP.md` | all of them |
| A one-page ideal buyer profile built from your last ten wins, not your pitch deck | the onboarding interview, saved as `brain/icp.md` | `onboarding` |
| Ten researched cold emails, under 90 words, one small ask | your first campaign is ten contacts: find, verify and research them, write and score the drafts, and email them to you for approval. Daily campaigns after that are about 50 | `prospecting`, `cold-email`, `humanizer`, `outreach-campaign` |
| A three-touch sequence that follows up without sounding pushy | day 1, day 3, day 7, then stop. One campaign approval covers all three touches | `cold-email`, `outreach-campaign` |
| A reply playbook | sorts every reply into seven buckets: Interested, Question, Not now, Referral, No, Stop, Auto-reply | `inbox-triage` |
| A checklist for protecting your main email address | lookalike domains, SPF, DKIM, DMARC, warmup, daily caps | `outreach-campaign`, `onboarding` |
| Research tools for real facts and real emails | treg.to and Apollo lookups, with the price checked first | `prospecting` |
| Interested leads in your CRM | name, company, email, campaign, the reply and a suggested next step pushed to your CRM (or a CSV or Google Sheet). Only hot leads go there. The local database stays the record of every prospect and send | `crm-sync` |
| Calls on the calendar | your booking link on interested replies | `booking` |

---

## She arrives with no access to anything

A fresh Becca can reach nothing: no Apollo, no inbox, no CRM, no calendar. That
is not a broken install. It is the design. Onboarding is where you give
her access, one tool at a time, the way you would with a new hire, and you do it
on each tool's own sign-in page. It takes about 20 minutes. She asks about your
company brain first, then which CRM you use and which email address your daily
campaign should go to. She connects each tool, and reads the sending address
back to you from the mailbox itself before a single draft is written. Until
sending is connected she cannot email anyone, so she cannot email the wrong
people from the wrong address.

On Hermes, tools are scoped per profile, so whatever your main agent can reach is
not connected to her. `hermes -p becca mcp list` comes back empty until
onboarding is done.

### Two decisions she will push you on

**Whose name is on the email.** Yours, by default. She records your name, title
and exact signature, and reads them back before she writes anything.

**Where it sends from.** Not your main domain. She recommends one to three
lookalike domains, one to three inboxes on each in your name, all connected to
Instantly and warmed for two to three weeks. If they are not ready she records
`sending: pending`, tells you what is left to set up, and carries on with the
other tools and the first task. She loads and sends nothing until Instantly
shows warmed inboxes and you have approved that specific campaign by email. In
the meantime you can send the first ten by hand.

---

## Before you send real volume

Cold email from your main company domain can damage the deliverability of your
normal mail. The standard practice:

1. One to three **lookalike domains** that redirect to your real site.
2. One to three inboxes on each, **in your name**, with **SPF, DKIM and DMARC**.
3. All of them in **Instantly**, with **two to three weeks of warmup**.
4. About 20 emails per inbox per day at most, verified emails only. Pause if
   bounces pass about 3 percent.
5. A real sender, a real address and an easy opt-out on every email. Stops are
   honored the same day.

You are responsible for complying with CAN-SPAM, GDPR and any other law that
applies to you. Becca honors opt-outs immediately and permanently, but the
obligation is yours.

---

## Hermes extras

### Turn on her schedule

Cron jobs ship with the package but are not started automatically. Once you are
happy after onboarding:

```bash
hermes -p becca cron list      # see what she would run
hermes -p becca cron tick      # activate the schedule
```

| When | What |
|---|---|
| Weekdays 8:00 | Daily prospecting: finds and researches contacts that match your ideal buyer profile and your offer |
| Weekdays 9:00 | Daily campaign for approval: builds one campaign of up to 50 contacts, writes every email, **emails it to you for approval** |
| Weekdays, hourly | Campaign approval check: looks for your approval reply and only reports when something changed. Loads and sends only a campaign you approved, from your approval address |
| Every 2 hours | Inbox sweep: opt-outs first, stops sequences on reply, drafts responses, sends interested leads to your CRM |

She builds a new campaign only when none is waiting for your approval. If you
have not replied after 3 days she sends one reminder, then holds.

Change any of it: `becca` then *"run prospecting at 7 instead"*.

### Updating

```bash
hermes profile update becca
```

Your `brain/`, memories, sessions, `.env`, prospect database and the tools you
connected are never touched. Updates change how she works, never what she can
reach.

Coming from 1.4.0? After the update, tell Becca **"upgrade my database"**. She
runs `scripts/init_db.py` (safe to re-run, it keeps your data) and asks the
approval questions again: your approval email, your CRM and your campaign size.

---

## Skills

| Skill | What it does |
|---|---|
| `onboarding` | Starts from your company brain (or builds one), asks your CRM and approval email, connects your tools, writes `brain/` |
| `prospecting` | Search, enrich, verify, dedupe, store |
| `cold-email` | Writes the email *(adapted from [Corey Haines](https://github.com/coreyhaines31/marketingskills), MIT)* |
| `humanizer` | Strips the AI tells before you see a draft *(by [blader](https://github.com/blader/humanizer), MIT)* |
| `outreach-campaign` | Builds the daily campaign, emails it to you for approval, loads and sends only what you approved, schedules follow-ups |
| `inbox-triage` | Sorts replies, handles opt-outs, drafts responses |
| `crm-sync` | Pushes interested leads to whatever CRM you use (Attio, HubSpot, GoHighLevel, Pipedrive and others), or to a CSV or Google Sheet |
| `booking` | Gets the call on the calendar |

## Her brain

Onboarding writes these files. In Hermes they live in
`~/.hermes/profiles/becca/brain/`; elsewhere your agent keeps them as project
files or saved notes. They are plain Markdown. Edit them any time.

| File | What is in it |
|---|---|
| `business.md` | What you sell, proof, objections |
| `icp.md` | Your ideal buyer profile and the trigger events worth searching for |
| `voice.md` | How you sound, and emails of yours that worked |
| `access.md` | What you connected, and the words you confirmed it with |
| `config.md` | Send caps, sequence spacing, bounce pause, your approval email, campaign size, your CRM and the CSV or Google Sheet fallback |
| `suppression.md` | Never-contact list |
| `rules.md` | What she has learned from your corrections |

`brain/` is never committed to this repo.

---

## Version

**1.5.0** starts onboarding from your company brain, adds a daily campaign of
up to 50 contacts that is emailed to you and sent only after you reply APPROVE
for that campaign, and pushes interested leads to whatever CRM you use (or a CSV
or Google Sheet).

**1.4.0** added the one-line start for any agent, `AGENT-SETUP.md`, a named
tools list with treg.to, the day 1, 3, 7 sequence, and the seven reply buckets.

## Credits

Bundles two MIT-licensed skills. The cold-email skill is adapted from work by
[Corey Haines](https://github.com/coreyhaines31/marketingskills). The humanizer
skill is by [blader](https://github.com/blader/humanizer), unmodified.
Runs on [Hermes Agent](https://hermes-agent.nousresearch.com) by Nous Research,
and works in any agent that can read these files.

---

Built by Vindex Consulting. vindexconsulting.com. Taught at the Cold Email Masterclass.
