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

**Then three one-time steps.** Do them in order — the first two are what make
the agent able to think at all, and skipping them produces a confusing
"No inference provider configured" error.

```bash
# 1. Authenticate this profile with a model provider.
#    Each Hermes profile carries its own credentials — that is deliberate,
#    and it is why no API key ever ships inside a distribution.
hermes -p becca setup --portal

# 2. Confirm the model. The package defaults to Nous Portal; if you are on
#    Anthropic, OpenAI, or anything else, pick it here.
hermes -p becca model

# 3. Add your tool credentials (all optional — see the table below).
cp ~/.hermes/profiles/becca/.env.EXAMPLE ~/.hermes/profiles/becca/.env
```

Then:

```bash
becca chat
```

Say **"onboard me"** and she takes it from there.

> Requires Hermes >= 0.20.0 and git.

### Turn on her schedule

Cron jobs ship with the package but are **not** started automatically — Hermes
will not schedule someone else's jobs behind your back. Review and activate:

```bash
hermes -p becca cron list      # see what she would run
hermes -p becca cron tick      # activate the schedule
```

---

## What she needs connected

Two paths for everything. **Composio is recommended** — managed OAuth, no keys
pasted anywhere. Direct API keys work if you would rather not use Composio.

| Need | Recommended | Alternative | Required? |
|---|---|---|---|
| Find prospects | `composio link apollo` | `APOLLO_API_KEY` | **Yes** |
| Send & receive email | `composio link gmail` / `outlook` | `AGENTMAIL_API_KEY` | **Yes** |
| Store prospects | `composio link hubspot` / `gohighlevel` | built-in local database | No |
| Book calls | `BECCA_BOOKING_LINK` (your Calendly/Cal.com link) | `composio link googlecalendar` | No |

**No CRM?** Becca ships with a real local prospect database — prospects, sends,
replies, statuses, suppression. Nothing is missing.

**Different CRM?** Onboarding runs `composio search "<your CRM> create contact"`
and wires it up. Close, Pipedrive, Salesforce, Zoho, Attio and many more work.

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

Your `brain/`, memories, sessions, `.env`, and prospect database are never
touched.

---

## Credits

Bundles two excellent MIT-licensed skills, unmodified:
[cold-email](https://github.com/coreyhaines31/marketingskills) by Corey Haines
and [humanizer](https://github.com/blader/humanizer) by blader.

Built on [Hermes Agent](https://hermes-agent.nousresearch.com) by Nous Research.
