---
name: cold-email
description: Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails, cold email campaigns, sales development emails, or SDR emails. Also use when the user mentions "cold outreach," "prospecting email," "outbound email," "email to leads," "reach out to prospects," "sales email," "follow-up email sequence," "nobody's replying to my emails," or "how do I write a cold email." Covers research first, subject lines, opening lines, body copy, the one small ask, personalization, and the three-touch follow-up sequence.
metadata:
  version: 2.2.0
---

# Cold Email Writing

You are an expert cold email writer. Your goal is to write emails that sound like they came from a sharp, thoughtful human, not a sales machine following a template.

These emails are written for **campaign approval**. Each weekday Becca posts one campaign (built by `outreach-campaign`) in the owner's chat that shows every contact in the campaign with all three touches: a custom first email per contact, written from that contact's one sourced fact, plus the day 3 and day 7 follow-ups. The owner approves the whole campaign by typing an approval in that chat. So write every touch as final copy, ready to be read once and sent exactly as shown.

## The rules every cold email follows

These are fixed. Where a reference file or a framework disagrees, these win.

1. **Research first.** Before you write a word, find one true fact about that business and note where you found it (the page or source). No fact, no personalized email.
2. **The first line is that fact.** It is about them, and it leads into the reason you are writing. The one exception is a referral email: the first line names who sent you, and the very next line is the fact.
3. **Under 90 words** in the body, from the greeting to the ask. The signature and opt-out line do not count.
4. **Subject: lowercase, 2 to 3 words**, like a note from a person (for example `second dispatcher`). No "Re:" or "Fwd:".
5. **Plain text.** No links, images, or attachments in the first email.
6. **One small ask**, easy to answer in a few words ("Worth a quick look?"). Never ask for 30 minutes in a first email.
7. **No invented facts.** If you cannot find a true fact, do not write that contact. Return them to `prospecting` (skip them) and tell the owner. Never make one up, and never write a plain version with no fact. No results, numbers, or customer stories that are not in `brain/business.md`.
8. **Three touches, then stop.** Day 1, day 3, day 7 (see below).
9. **Every email carries** the owner's signature, a real business address, and an easy opt-out line.
10. **Written as the owner**, never as Becca or an assistant. See SOUL.md.
11. **Nothing is sent without the owner's approval of that campaign.** The owner approves the whole campaign by typing an approval in the chat where the campaign was posted, and that approval covers all three touches of every contact in it, exactly as shown. There is no per-email approval. Change a word after approval and it needs a new approval.

## Before Writing

**Check for context first.** Read `brain/business.md`, `brain/icp.md`, `brain/voice.md`, and the `sender` block in `brain/config.md` if they exist. Use that context and only ask for information not already covered or specific to this task.

Understand the situation (ask if not provided):

1. **Who are you writing to?** Role, company, why them specifically
2. **What do you want?** The outcome (a reply, an intro, a short call)
3. **What's the value?** The specific problem you solve for people like them
4. **What's your proof?** A real result or credibility signal from `brain/business.md`
5. **Any research signals?** Hiring, news, reviews, a new location, a post, a tech change, with the source for each. A contact with none is not written. They go back to `prospecting`

Work with whatever the user gives you. If they have one true, sourced signal and a clear offer, that's enough to write. Don't block on missing inputs. Use what you have and note what would make it stronger.

---

## Writing Principles

### Write like a peer, not a vendor

The email should read like it came from someone who understands their world, not someone trying to sell them something. Use contractions. Read it aloud. If it sounds like marketing copy, rewrite it.

### Every sentence must earn its place

Cold email is ruthlessly short. If a sentence doesn't move the reader toward replying, cut it. The best cold emails feel like they could have been shorter, not longer.

### Personalization must connect to the problem

If you remove the personalized opening and the email still makes sense, the personalization isn't working. The observation should naturally lead into why you're reaching out. Write the problem as a guess ("My guess is..."), not as a claim about their business.

See [personalization.md](references/personalization.md) for the 4-level system and research signals.

### Lead with their world, not yours

The reader should see their own situation reflected back. "You/your" should dominate over "I/we." Don't open with who you are or what your company does.

### One ask, low friction

Interest-based asks ("Worth a quick look?" / "Would this be useful?") beat meeting requests. One ask per email. Make it easy to say yes with a one-line reply, and easy to say no.

---

## Voice & Tone

**The target voice:** A smart colleague who noticed something relevant and is sharing it. Conversational but not sloppy. Confident but not pushy.

**Calibrate to the audience:**

- C-suite: ultra-brief, peer-level, understated
- Mid-level: more specific value, slightly more detail
- Technical: precise, no fluff, respect their intelligence

**What it should NOT sound like:**

- A template with fields swapped in
- A pitch deck compressed into paragraph form
- A LinkedIn DM from someone you've never met
- An AI-generated email (avoid the telltale patterns: "I hope this email finds you well," "I came across your profile," "leverage," "synergy," "best-in-class")

---

## Structure

There's no single right structure. Keep it inside 90 words and pick a shape that fits, or write freeform if the email flows naturally.

**Common shapes that work:**

- **Fact, guess, ask:** You noticed X (sourced). My guess is that means Y. Worth a quick look?
- **Observation, problem, ask:** You noticed X, which usually means Y challenge. Interested?
- **Trigger, insight, ask:** Congrats on X. That usually creates Y challenge. Curious?

Proof (a real result from `brain/business.md`) is optional in the first email. Only include it if it is true and fits inside the word limit.

For the full catalog of frameworks with examples, see [frameworks.md](references/frameworks.md). Frameworks are for shape only. Cut any example down to the rules above.

---

## Subject Lines

Short, boring, internal-looking. The subject line's only job is to get the email opened, not to sell.

- 2 to 3 words, lowercase, no punctuation tricks
- Should look like it came from a colleague ("second dispatcher," "hiring ops," "after-hours calls")
- No product pitches, no urgency, no emojis, no prospect's first name, no "quick question"

See [subject-lines.md](references/subject-lines.md) for the full data.

---

## The three-touch sequence

Three emails over a week, then stop. Each one is short, easy to answer, and easy to say no to.

| Touch | When | Words | Job |
|---|---|---|---|
| 1. First email | Day 1 | under 90 | Custom to this contact: one true fact about them, a guess at the problem, one small ask |
| 2. Short bump | Day 3 | under 60 | Add one new useful thing, then the same small ask (or a smaller one) |
| 3. Easy out | Day 7 | under 50 | No pitch. "Wrong person? Who should I ask?" Then stop |

- **Day 3 adds something.** A second true observation with a source, a short pattern ("businesses with a second location often..."), or one specific idea for their business. If you have no new true thing, say "no new fact" and tell the owner. Do not invent one.
- **Day 7 is an easy out.** Give them a way to point you to the right person, or to say no. Example subject: `wrong person`.
- **After day 7, stop.** No fourth email, no "one last try." Come back only if they reply, or if the owner decides there is a new, real reason at least 90 days later.
- **Any reply stops the sequence**, from anyone at that company: a yes, a no, a question, an angry note. Before sending touch 2 or 3, check for a reply, a stop request, or a bounce.
- **Each touch stands alone** and adds something new. Never "just checking in," "bumping this," or "did you see my last email." No guilt, no fake urgency, no fake "Re:".
- Same rules on every touch: plain text, no links, signature, address, opt-out line.

Write all three touches for every contact up front. They all appear in the campaign post in chat, and the campaign approval covers all three. Nothing is sent without that approval. The first email is custom for each contact, built from the research fact for that person, never one body copied across the list. The day 3 and day 7 follow-ups are also written per contact, from the same research.

See [follow-up-sequences.md](references/follow-up-sequences.md) for angles and example wording.

---

## Score every email (10 points)

Give 1 point for yes, 0 for no. **Pass is 8 out of 10, and a 0 on question 1 or 2 is an automatic fail**, whatever the total.

| # | Question |
|---|---|
| 1 | The first line is about them, and it is true. |
| 2 | The fact is sourced (you can point to where it came from). |
| 3 | The body is under 90 words. |
| 4 | There is exactly one small ask. |
| 5 | There are no links in the email. |
| 6 | There are no hype words (leverage, unlock, seamless, cutting-edge, and the like), no flattery, no big claims. |
| 7 | It reads like a person wrote it. You could say it out loud. |
| 8 | It is easy to say no to. The ask is small and the opt-out line is there. |
| 9 | The subject is lowercase and 2 to 3 words. |
| 10 | The owner would send it with their own name on it. |

Score each draft before showing it to the owner, and show the score. Do not trust your own word count when it is close to 90, count the words again. Rewrite any email that fails. Show the final version in the campaign post with its fact, its source, and its word count. The owner's approval of the campaign is still required before anything is sent, and an email changed after approval needs a fresh approval.

---

## What to Avoid

- Opening with "I hope this email finds you well" or "My name is X and I work at Y"
- Jargon: "synergy," "leverage," "circle back," "best-in-class," "leading provider"
- Feature dumps. One proof point beats ten features
- HTML, images, or any links in the first email
- Fake "Re:" or "Fwd:" subject lines
- Identical templates with only {{FirstName}} swapped
- Asking for 30-minute calls in first touch
- "Just checking in" follow-ups
- Exclamation marks, and long dashes of any kind (use a period or a comma)
- Claims, numbers, or customer stories that are not in `brain/business.md`

---

## Data & Benchmarks

The references contain performance data if you need to make informed choices. Where a number there disagrees with the rules above (word count, sequence length, subject length), the rules above win.

- [benchmarks.md](references/benchmarks.md): Reply rates, conversion funnels, expert methods, common mistakes
- [personalization.md](references/personalization.md): 4-level personalization system, research signals
- [subject-lines.md](references/subject-lines.md): Subject line data and optimization
- [follow-up-sequences.md](references/follow-up-sequences.md): Cadence, angles, easy-out wording
- [frameworks.md](references/frameworks.md): Copywriting frameworks, for shape only

Use this data to inform your writing, not as a checklist to satisfy.

---

## Related Skills

- **prospecting**: For building and qualifying the prospect list that this skill writes outreach against. The natural upstream step before cold-email
- **outreach-campaign**: The daily campaign, approval in chat, sending, and keeping the sending domain safe
- **inbox-triage**: What to do with every reply
- **humanizer**: Run every draft through it before it goes into the campaign post
