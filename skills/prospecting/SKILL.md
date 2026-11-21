---
name: prospecting
description: Use when Becca needs to find new prospects, build a list, or run the daily prospecting job. Searches Apollo and/or treg.to against the ideal buyer profile, enriches and verifies contact details, dedupes against everyone already contacted, and writes qualified prospects into the CRM or local database.
version: 1.1.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [apollo, treg, prospecting, lead-generation, icp, enrichment]
    related_skills: [onboarding, crm-sync, cold-email]
---

# Prospecting with Apollo and treg.to

Turn `brain/icp.md` (the ideal buyer profile) into a list of real people with
real, verified email addresses, with nobody on it twice.

## Your data sources

**Apollo** is the main search: find the right companies, then the decision
makers inside them, with work emails.

**treg.to** sits beside it. It is a pay-per-call catalog of data tools for
agents: finding and verifying emails, company and person lookups, and local
business data. The price is shown before each call, and a new account gets a
small free credit. Use it to:

- **verify emails** before anyone goes on the list,
- **enrich companies** with facts that become the one true hook in the email,
- **cover local businesses** (trades, clinics, shops, restaurants and similar)
  that Apollo covers thinly.

If onboarding connected only one of the two, use that one. If both are
connected, search in Apollo first, then use treg.to for the gaps: prospects with
no verified email, and local businesses Apollo could not find.

**Connecting treg.to.** The setup line for the agent is:

```text
set up treg - https://treg.to/llms.txt
```

Follow what that page says. The owner creates the account at https://treg.to and
approves the connection in treg.to's own flow, and you never handle a login or
key in the chat. Do not guess treg.to tool or endpoint names; use the ones the
setup page and the connection actually show you.

**Spend rules for treg.to (and any other paid call):**

- Check the price before every call. If you cannot see a price, ask for it or
  do not call.
- Start with ten prospects, not a big list.
- Tell the owner the total before you run a batch and wait for their yes.
- Do not re-run a lookup you already have. Keep the answers with the prospect
  record.
- **Unattended runs:** a scheduled or automatic run may use treg.to only within
  `treg_daily_spend_cap` in `brain/config.md`. If it is 0 or missing, skip treg.to
  in unattended runs and use Apollo only. Spend above the cap needs the owner in
  the conversation.
- Record the source of every email and fact (Apollo, treg.to, the company's own
  site) with the prospect.

## Check your tools before you start

You reach Apollo, treg.to, the inbox, the CRM, and the calendar through
whatever onboarding connected: the platform's connectors, Composio, an MCP
server, or a documented API with a key kept in the platform's secure settings.
Look at what you actually have.

**If `brain/access.md` does not exist, stop and run `onboarding`.** That file,
with the owner's yes in it, is what "onboarded" means. Do not fall back to a CLI
you happen to find on the shell. A tool nobody granted you is a tool pointed at
an account nobody chose, and cold email from the wrong mailbox cannot be
recalled.

**If `brain/access.md` exists but a tool is not connected, that is manual mode,
not a reason to stop.** Ask the owner for ten companies or names to work from,
research them with web search, and use only emails the owner found or gave you.
Never guess an address.

Tool names below are the common Composio slugs for Apollo. If onboarding wired
something else, use its equivalent. The operation is what matters, not the
spelling. No shell is needed: you call the connected tool.

## Before you search

Read `brain/icp.md` and `brain/config.md`. If either is missing, stop and run
`onboarding`. Searching without an ICP produces a list that wastes sends.

## Step 1: Search organizations, then people

Two passes beat one. Find the right **companies** first, then the right
**people** inside them. It is far more precise than one broad people search,
and it costs fewer credits.

Translate the ideal buyer profile into filters. Its "who they are" section gives
industry, size, location and title. Its "reasons to reach out" section gives the
signals worth looking for.

**Connected tool path (recommended):** call the connected Apollo tool (through
Composio or the platform connector): `APOLLO_ORGANIZATION_SEARCH` first, then
`APOLLO_PEOPLE_SEARCH`, with the filters below.

**Direct API path:** `POST https://api.apollo.io/api/v1/mixed_companies/search`
then `mixed_people/search`, with `X-Api-Key: $APOLLO_API_KEY`.

Use industry, employee-count range, location, and the target titles as filters.
Where a trigger event in the ICP maps to an Apollo filter (recent funding,
headcount growth, hiring for a role), use it. Trigger-filtered
lists reply at multiples of unfiltered ones, which is the whole reason the ICP
asks for triggers.

**Known Apollo behavior, so you do not waste a run:**
- Paginate with `page` / `per_page`; `per_page` tops out around 100.
- `q_keywords` must be a **string**. An array fails validation.
- Over-constrained filters silently return `total_entries: 0`. When that
  happens, loosen **one** filter at a time and say which one you loosened. Never
  quietly widen everything at once and hand over a list that no longer
  matches the ICP.
- `APOLLO_ORGANIZATION_SEARCH` can return 403 even when auth is fine. Fall back
  to `APOLLO_ORGANIZATION_ENRICHMENT` on known domains.
- Thin results for local businesses are normal. Try treg.to for those (Step 2b)
  instead of loosening the ICP.

## Step 2: Enrich

Search results usually lack a usable email. Enrich the shortlist:

Call the connected Apollo tool (through Composio or the platform connector),
`APOLLO_BULK_PEOPLE_ENRICHMENT`, with the shortlist.

Batches of **10 or fewer**. Dedupe inputs first. Merge results back by Apollo
person ID, not by name. Names collide.

For anyone bulk enrichment misses, retry individually with
`APOLLO_PEOPLE_ENRICHMENT` using the strongest identifier you have.

### Step 2b: Verify and fill gaps with treg.to

Use treg.to for three jobs, and only for prospects that are still in play:

1. **Verify** every email you plan to use, including Apollo's. Only addresses
   that come back verified go forward. "Unknown" or "risky" gets checked another
   way or dropped.
2. **Find** a work email for a good-fit person Apollo has no verified email for.
3. **Enrich** the company (and the person, if needed) with facts that could
   become the one true hook, and local business data for the businesses Apollo
   covers thinly.

Check the price first, start with ten prospects, and give the owner the total
before a bigger batch. Pick the treg.to tool that does the job from what the
connection shows you. Do not invent names. Save what it returned, and where it
came from, on the prospect record.

## Step 3: Qualify, and be willing to throw work away

Drop a prospect when any of these is true. Do not soften these. A padded list
is worse than a short one, because it burns sends and domain reputation.

- No verified business email. Apollo's `email_status` is not `verified` and
  treg.to could not verify it either: drop.
- Personal domain (`@gmail`, `@yahoo`, `@hotmail`) when a business email exists.
- Already in the database with any status. **Check every time.**
- On `brain/suppression.md`.
- Same domain as a prospect already in today's batch (one person per company
  per batch, unless the owner asked otherwise).
- Title does not actually match the ICP. "Close enough" titles are how a list
  quietly stops being an ICP list.

Report honest counts: *found N, verified M, qualified K, dropped J and why.* The
owner should always be able to see the attrition, and for paid lookups, what
they cost.

## Step 4: Write them down

For each qualified prospect, write a record through the `crm-sync` skill with:
name, title, company, domain, email, LinkedIn, company size, industry, the
**specific trigger or signal you found**, the Apollo person ID (if any), the source of the email, and status
`new`.

The signal field is not optional. It is what the cold email is built on, and a
prospect with an empty signal field is a prospect nobody can write a good email
to. If you could not find one, either find one or drop the prospect.

**Completion criterion:** every qualified prospect is in the database with a
non-empty signal, and the counts you reported reconcile with what is stored.

## Daily run

Where scheduled jobs are available (on Hermes, the daily prospecting cron job),
this skill runs against `daily_prospect_target` in `brain/config.md`. Elsewhere,
the owner can ask for it any time. It reports:

```
Prospected 25, verified 19, qualified 16, dropped 9
Top signal: 6 companies hiring ops roles this month
Ready for outreach: 16
```

If a run returns far fewer than target two days running, say so and suggest
widening a specific ICP dimension. A quietly shrinking list is a problem the
owner needs to know about.
