# Becca — cold outreach SDR

Becca finds the right people, writes cold email that sounds like a person,
keeps your CRM current, works the inbox, and books calls.

She drafts; **you approve; then she sends.** That is the default and she does
not drift out of it.

---

## Install

```bash
hermes profile install github.com/OscarH30/hermes-becca --alias
```

Already running Hermes? Paste the install prompt into the session you have open
and it handles this for you. She installs as her **own profile**, alongside
whatever you already run — nothing you have is modified.

Then one thing before you talk to her: give the profile a model. Hermes profiles
carry their own credentials and do **not** inherit yours, which is exactly why no
API key ever ships inside a distribution. Skip this and you get a confusing
"No inference provider configured" error.

```bash
hermes -p becca setup --portal   # authenticate this profile
hermes -p becca model            # confirm or change the model
```

Now onboard her:

```bash
becca chat
```

Say **"onboard me"**.

> Requires Hermes >= 0.20.0 and git.

---

## She arrives with no access to anything

This is the part worth understanding before you start.

A freshly installed Becca can reach **nothing** — no Apollo, no inbox, no CRM,
no calendar. `hermes -p becca mcp list` comes back empty. That is not a broken
install: Hermes scopes tools per profile, so whatever you already connected to
your main agent is **not** connected to her.

**Onboarding is where you hand over the keys**, one at a time, the way you would
with a new hire. She will ask about your business, ask what you use, and wire
each tool to her profile — and she reads the sending address back to you from
the mailbox itself before a single draft is written.

Until that is done she cannot email the wrong people from the wrong address,
because she cannot email at all.

---

## What onboarding will connect

| Need | Options she'll offer | Required? |
|---|---|---|
| Prospect data | Composio → Apollo (recommended), or an Apollo API key | **Yes** |
| Email | Composio → Gmail/Outlook, AgentMail, or an MCP server you run | **Yes** |
| CRM | HubSpot, GoHighLevel, most others via Composio — or the built-in local database | No |
| Booking calls | Your Calendly/Cal.com link, or a connected calendar | No |

**New to Composio?** She'll walk you through signing up. It handles OAuth so
nothing gets pasted anywhere and access is revocable from one dashboard. Direct
API keys work too if you'd rather not use it.

**No CRM?** She ships with a real local prospect database — prospects, sends,
replies, statuses, suppression. Nothing is missing.

**Different CRM?** She'll check whether a connector exists for it during
onboarding. Close, Pipedrive, Salesforce, Zoho, Attio and many more work.

### One decision she'll push you on

Whether outreach should send from an inbox you already use, or a **dedicated
one**. She'll give you the deliverability tradeoff before you answer, and if you
choose a dedicated identity she will **stop onboarding** and tell you what to set
up — warming a domain takes days, not minutes. That is the correct outcome, not
a failure.

---

### Turn on her schedule

Cron jobs ship with the package but are **not** started automatically — Hermes
will not schedule someone else's jobs behind your back. Once you are happy after
onboarding:

```bash
hermes -p becca cron list      # see what she would run
hermes -p becca cron tick      # activate the schedule
```

---

## What she does on her own

| When | What |
|---|---|
| Weekdays 8:00 | Finds and qualifies new prospects in Apollo against your ICP |
| Weekdays 9:00 | Builds the day's batch, writes every email, **shows it to you** |
| Every 2 hours | Sweeps the inbox — opt-outs first, stops sequences on reply, drafts responses |

Change any of it: `becca` then *"run prospecting at 7 instead"*.

---

## Skills

| Skill | What it does |
|---|---|
| `onboarding` | Interviews you, reads your existing docs, connects tools, writes `brain/` |
| `prospecting` | Apollo search → enrich → qualify → dedupe → store |
| `cold-email` | Writes the email *(by [Corey Haines](https://github.com/coreyhaines31/marketingskills), MIT)* |
| `humanizer` | Strips the AI tells before you ever see a draft *(by [blader](https://github.com/blader/humanizer), MIT)* |
| `outreach-campaign` | Assembles the batch, gets approval, sends, schedules follow-ups |
| `inbox-triage` | Classifies replies, handles opt-outs, drafts responses |
| `crm-sync` | One interface over HubSpot / GoHighLevel / any Composio CRM / local |
| `booking` | Gets the call on the calendar |

---

## Her brain

Onboarding writes these into `~/.hermes/profiles/becca/brain/`. Edit them
directly any time — they are plain Markdown and she reads them on every run.

| File | What's in it |
|---|---|
| `business.md` | What you sell, pricing, proof, objections |
| `icp.md` | Who to target, and the trigger events worth searching for |
| `voice.md` | How you sound, and emails of yours that worked |
| `access.md` | What you connected her to, and the words you confirmed it with |
| `config.md` | Send caps, sequence spacing, autonomy, CRM choice |
| `suppression.md` | Never-contact list |
| `rules.md` | What she has learned from your corrections |

`brain/` is never committed and never leaves your machine.

---

## Before you send real volume

Cold email from your main company domain can damage the deliverability of your
normal mail. The standard practice:

1. A **separate domain** that redirects to your real site
2. A dedicated mailbox on it, with **SPF, DKIM, and DMARC** configured
3. **Two to three weeks of warmup** before real volume
4. Ramp slowly — 10-15/day at first

Skip the warmup and send fifty on day one and they land in spam. Becca will say
this to you during onboarding too.

You are responsible for complying with CAN-SPAM, GDPR, and any other law that
applies to you. Becca honors opt-outs immediately and permanently, but the
obligation is yours.

---

## Updating

```bash
hermes profile update becca
```

Your `brain/`, memories, sessions, `.env`, prospect database — **and the tools
you connected her to** — are never touched. Updates change how she works, never
what she can reach.

---

## Credits

Bundles two excellent MIT-licensed skills, unmodified:
[cold-email](https://github.com/coreyhaines31/marketingskills) by Corey Haines
and [humanizer](https://github.com/blader/humanizer) by blader.

Built on [Hermes Agent](https://hermes-agent.nousresearch.com) by Nous Research.
