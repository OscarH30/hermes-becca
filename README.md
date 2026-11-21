# Becca, your outreach agent

If you are an AI agent reading this: open AGENT-SETUP.md and follow it.
Raw URL: https://raw.githubusercontent.com/OscarH30/hermes-becca/main/AGENT-SETUP.md

Becca is the agent's name. Tell your agent: **set up the outreach agent from https://github.com/OscarH30/hermes-becca**

That one sentence is the whole start. Your agent reads this repo, installs the
skills, and walks you through setup by asking about your business. Becca finds
the right people, writes cold email that sounds like a person, keeps your
records current, works the inbox, and books calls.

**Every email goes out in your name, not hers.** She writes as you, the owner or
CEO, and signs with your signature. She drafts, **you approve, then she sends**
(or you send by hand). That is the default and she does not drift out of it.

---

## Get set up

Pick the one that matches your agent.

### Grok Bot

1. Open Grok Bot and start a chat with your bot (or create a new one for this).
2. Paste the sentence above: *set up the outreach agent from
   https://github.com/OscarH30/hermes-becca*
3. It reads `AGENT-SETUP.md` in this repo, saves the skills and rules as its own
   instructions or knowledge, and then runs `onboarding`.
4. Answer the questions (about 20 minutes). It walks you through connecting each
   tool below, one at a time, using the connection options in your bot's own
   settings.

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

In this mode Becca drafts and you paste and send by hand. Everything else, the
research, the voice, the three-touch sequence and the reply sorting, works the
same.

---

## The tools I use

Sign up for these, connect them to your agent, and go. Onboarding goes through
them in this order, one at a time: Apollo and/or treg.to, Instantly (with Google
Workspace inboxes on lookalike domains), Attio, Cal.com or Calendly, then
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
| Attio | https://attio.com | CRM: every prospect, touch and reply | Optional (built-in local database otherwise) | through your platform's connector settings, or through Composio |
| Composio | https://composio.dev | connects Apollo, Instantly, Attio, Gmail to your agent through secure sign-in (OAuth) | Recommended for Hermes; optional elsewhere | you make an account, then connect each app on Composio's own connect page (OAuth, or a key you enter there), never in chat |
| Cal.com | https://cal.com | booking link for interested replies (Calendly also works) | Optional | you give your public booking link, nothing else |

If a tool needs a key and offers no sign-in, the agent tells you where to put it
securely (in Hermes, the profile's `.env` file; elsewhere, the platform's
secrets or connector settings). Never in the chat.

---

## What you get

| What the class promised | What does it | Skill |
|---|---|---|
| An outreach agent with a job description it follows every time | the rules in `SOUL.md` and the job description in `AGENT-SETUP.md` | all of them |
| A one-page ideal buyer profile built from your last ten wins, not your pitch deck | the onboarding interview, saved as `brain/icp.md` | `onboarding` |
| Ten researched cold emails, under 90 words, one small ask | find, verify and research prospects, then write and score the drafts | `prospecting`, `cold-email`, `humanizer` |
| A three-touch sequence that follows up without sounding pushy | day 1, day 3, day 7, then stop | `cold-email`, `outreach-campaign` |
| A reply playbook | sorts every reply into seven buckets: Interested, Question, Not now, Referral, No, Stop, Auto-reply | `inbox-triage` |
| A checklist for protecting your main email address | lookalike domains, SPF, DKIM, DMARC, warmup, daily caps | `outreach-campaign`, `onboarding` |
| Research tools for real facts and real emails | treg.to and Apollo lookups, with the price checked first | `prospecting` |
| Every prospect, touch and reply on record | Attio, another CRM, or the built-in local database | `crm-sync` |
| Calls on the calendar | your booking link on interested replies | `booking` |

---

## She arrives with no access to anything

A fresh Becca can reach nothing: no Apollo, no inbox, no CRM, no calendar. That
is not a broken install. It is the design. Onboarding is where you give
her access, one tool at a time, the way you would with a new hire, and you do it
on each tool's own sign-in page. It takes about 20 minutes. She asks about your
business, asks what you use, connects each tool, and reads the sending address
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
other tools and the first task. She sends nothing until Instantly shows warmed
inboxes and you confirm. In the meantime you can send the first ten by hand.

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
| Weekdays 8:00 | Finds and qualifies new prospects against your ideal buyer profile |
| Weekdays 9:00 | Builds the day's batch, writes every email, **shows it to you** |
| Every 2 hours | Sweeps the inbox, opt-outs first, stops sequences on reply, drafts responses |

Change any of it: `becca` then *"run prospecting at 7 instead"*.

### Updating

```bash
hermes profile update becca
```

Your `brain/`, memories, sessions, `.env`, prospect database and the tools you
connected are never touched. Updates change how she works, never what she can
reach.

---

## Skills

| Skill | What it does |
|---|---|
| `onboarding` | Interviews you, connects your tools, writes `brain/` |
| `prospecting` | Search, enrich, verify, dedupe, store |
| `cold-email` | Writes the email *(adapted from [Corey Haines](https://github.com/coreyhaines31/marketingskills), MIT)* |
| `humanizer` | Strips the AI tells before you see a draft *(by [blader](https://github.com/blader/humanizer), MIT)* |
| `outreach-campaign` | Assembles the batch, gets approval, sends, schedules follow-ups |
| `inbox-triage` | Sorts replies, handles opt-outs, drafts responses |
| `crm-sync` | One interface over Attio, HubSpot, GoHighLevel, other CRMs, or the local database |
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
| `config.md` | Send caps, sequence spacing, bounce pause, CRM choice |
| `suppression.md` | Never-contact list |
| `rules.md` | What she has learned from your corrections |

`brain/` is never committed to this repo.

---

## Version

**1.4.0** adds the one-line start for any agent (Grok Bot, Hermes, Claude and
ChatGPT projects), `AGENT-SETUP.md`, a named tools list with treg.to and Attio,
a first task of ten drafts for approval, the day 1, 3, 7 sequence, and the
seven reply buckets.

## Credits

Bundles two MIT-licensed skills. The cold-email skill is adapted from work by
[Corey Haines](https://github.com/coreyhaines31/marketingskills). The humanizer
skill is by [blader](https://github.com/blader/humanizer), unmodified.
Runs on [Hermes Agent](https://hermes-agent.nousresearch.com) by Nous Research,
and works in any agent that can read these files.

---

Built by Vindex Consulting. vindexconsulting.com. Taught at the Cold Email Masterclass.
