---
name: prospecting
description: Use when Becca needs to find new prospects, build a list, or run the daily prospecting job. Searches Apollo against the ICP, enriches for verified contact details, dedupes against everyone already contacted, and writes qualified prospects into the CRM or local database.
version: 1.0.0
author: Vindex Consulting
license: MIT
metadata:
  hermes:
    tags: [apollo, prospecting, lead-generation, icp, enrichment]
    related_skills: [onboarding, crm-sync, cold-email]
---

# Prospecting with Apollo

Turn `brain/icp.md` into a list of real people with real email addresses, with
nobody on it twice.

## Check your tools before you start

You reach Apollo, the inbox, the CRM, and the calendar through whatever
onboarding wired into this profile — MCP servers, or documented APIs using keys
in `.env`. Look at what you actually have.

**Missing a tool this skill needs → stop and run `onboarding`.** Do not fall back
to a CLI you happen to find on the shell. A tool nobody granted you is a tool
pointed at an account nobody chose, and cold email from the wrong mailbox cannot
be recalled.

Tool names below are the common Composio slugs. If onboarding wired something
else, use its equivalent — the operation is what matters, not the spelling.

## Before you search

Read `brain/icp.md` and `brain/config.md`. If either is missing, stop and run
`onboarding`. Searching without an ICP produces a list that wastes sends.

## Step 1 — Search organizations, then people

Two passes beat one. Find the right **companies** first, then the right
**people** inside them — it is far more precise than one broad people search,
and it costs fewer credits.

**Composio path (recommended):**
```bash
composio execute "APOLLO_ORGANIZATION_SEARCH" -d '{...}'
composio execute "APOLLO_PEOPLE_SEARCH" -d '{...}'
```

**Direct API path:** `POST https://api.apollo.io/api/v1/mixed_companies/search`
then `mixed_people/search`, with `X-Api-Key: $APOLLO_API_KEY`.

Translate the ICP into filters: industry, employee-count range, location, and
the target titles. Where a trigger event in the ICP maps to an Apollo filter —
recent funding, headcount growth, hiring for a role — use it. Trigger-filtered
lists reply at multiples of unfiltered ones, which is the whole reason the ICP
asks for triggers.

**Known Apollo behavior, so you do not waste a run:**
- Paginate with `page` / `per_page`; `per_page` tops out around 100.
- `q_keywords` must be a **string**. An array fails validation.
- Over-constrained filters silently return `total_entries: 0`. When that
  happens, loosen **one** filter at a time and say which one you loosened —
  never quietly widen everything at once and hand over a list that no longer
  matches the ICP.
- `APOLLO_ORGANIZATION_SEARCH` can return 403 even when auth is fine. Fall back
  to `APOLLO_ORGANIZATION_ENRICHMENT` on known domains.

## Step 2 — Enrich

Search results usually lack a usable email. Enrich the shortlist:

```bash
composio execute "APOLLO_BULK_PEOPLE_ENRICHMENT" -d '{...}'
```

Batches of **10 or fewer**. Dedupe inputs first. Merge results back by Apollo
person ID, not by name — names collide.

For anyone bulk enrichment misses, retry individually with
`APOLLO_PEOPLE_ENRICHMENT` using the strongest identifier you have.

## Step 3 — Qualify, and be willing to throw work away

Drop a prospect when any of these is true. Do not soften these — a padded list
is worse than a short one, because it burns sends and domain reputation.

- No verified business email. Apollo's `email_status` is not `verified` → drop.
- Personal domain (`@gmail`, `@yahoo`, `@hotmail`) when a business email exists.
- Already in the database with any status. **Check every time.**
- On `brain/suppression.md`.
- Same domain as a prospect already in today's batch — one person per company
  per batch, unless the owner asked otherwise.
- Title does not actually match the ICP. "Close enough" titles are how a list
  quietly stops being an ICP list.

Report honest counts: *found N, verified
M, qualified K, dropped J and why.* The owner should always be able to see the
attrition.

## Step 4 — Write them down

For each qualified prospect, write a record through the `crm-sync` skill with:
name, title, company, domain, email, LinkedIn, company size, industry, the
**specific trigger or signal you found**, the Apollo person ID, and status
`new`.

The signal field is not optional. It is what the cold email is built on, and a
prospect with an empty signal field is a prospect nobody can write a good email
to. If you could not find one, either find one or drop the prospect.

**Completion criterion:** every qualified prospect is in the database with a
non-empty signal, and the counts you reported reconcile with what is stored.

## Daily run

The `daily-prospecting` cron job runs this skill against
`daily_prospect_target` in `brain/config.md`. It reports:

```
Prospected 25 · verified 19 · qualified 16 · dropped 9
Top signal: 6 companies hiring ops roles this month
Ready for outreach: 16
```

If a run returns far fewer than target two days running, say so and suggest
widening a specific ICP dimension. A quietly shrinking list is a problem the
owner needs to know about.
