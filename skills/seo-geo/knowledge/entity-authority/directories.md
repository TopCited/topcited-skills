---
topic: Which directory types still matter for humans, search, and AI citation in 2026
stage-relevance: [5]
last-verified: 2026-08-20
sources:
  - https://developers.google.com/search/docs/advanced/guidelines/link-schemes
  - https://www.yext.com/blog/ai-visibility-in-2025-how-gemini-chatgpt-perplexity-cite-brands
  - https://www.averi.ai/ (accessed via search; primary report not directly fetched — flag for spot-check)
  - heuristic
---

# Directories and AI citation value

## In plain words
Not all directory listings are the same kind of win. Every listing gives a
brand a backlink and a consistency check, but only a narrower slice of
directories — the ones AI assistants actually pull from when answering
"what's the best tool for X" — carry real weight for showing up in AI
answers specifically. Knowing which tier a directory falls into stops effort
from going into low-value, generic listings first.

## What practitioners need to know

### Directories are not link spam by default
Google's link-spam policy (the "link schemes" documentation) defines link
spam as links created "primarily for the purpose of manipulating a site's
ranking" — examples include buying/selling links, excessive link exchanges,
and automated link-creation programs. It does **not** ban directory listings
as a format; a listing is fine when it's an editorially-curated business
listing rather than a manipulative scheme. The risk is in *how* a listing is
acquired (mass-submitted, paid purely for link-passing) rather than in
directories as a category. Pacing submissions and using consistent brand
fields (rather than mass-blasting dozens of directories in a day) lines up
with this "primarily for manipulation" test, even though Google does not
publish a specific submission-rate threshold *(inference from the primary
doc, not a stated Google threshold)*.

### The strongest evidence in this track: Yext's AI-citation dataset — and its scope
- Yext's "AI Citation Behavior Across Models" research (first-party, disclosed
  methodology) analyzed 6.8 million AI citations from 1.6 million queries per
  model, collected 2025-07-01 to 2025-08-31, across ChatGPT, Gemini, and
  Perplexity, spanning 4 intent quadrants and 4 industries (retail, financial
  services, healthcare, food service). Finding: **48.73% of ChatGPT citations
  came from third-party sites** (directories/review platforms such as Yelp,
  TripAdvisor, MapQuest); for subjective "what's the best…" queries the
  third-party/directory share rose to 46.3% even within that mix.
- **Scope limit — read this carefully before reusing the stat**: this dataset
  covers general local/consumer business categories (retail, financial
  services, healthcare, food service), not software/SaaS or AI-tool
  directories. **It is evidence that directories broadly matter for AI
  citation in the categories studied — it is not evidence for the value of
  AI-tool/SaaS directories specifically.** No independent study in this
  track measured citation rates for named AI-tool directories (There's An AI
  For That, Futurepedia, Toolify, FutureTools.io, TheSaaSDir, OpenTools,
  SaaSHub). Any claim that AI-tool directories are high-value is a
  heuristic inference from Yext's category-level pattern ("subjective
  queries pull heavily from third-party/directory sources"), not a
  directly-measured finding — the playbooks track separately confirmed it
  found zero direct evidence for that narrower claim.
- Averi (680M AI citations analyzed, early 2026, methodology not
  independently verified here) found only 11% domain overlap between
  ChatGPT's and Perplexity's citation sets — a directory cited by one
  assistant is not a reliable proxy for being cited by another. Averi also
  reports brands present on 4+ platforms are 2.8x more likely to appear in
  ChatGPT responses — directionally supportive of broad, consistent
  multi-directory presence, but "platforms" here conflates directories with
  social/review/press presence, and the source doesn't disentangle whether
  presence *causes* citation or already-cited brands simply get listed
  everywhere *(heuristic, causal direction unresolved — flag for
  spot-check)*.

### Directory tiers and what each is actually good for
- **AI-tool/SaaS directories** (There's An AI For That, Futurepedia,
  Toolify, FutureTools.io, TheSaaSDir, OpenTools, SaaSHub): the category most
  plausibly aligned with Yext's "subjective query → third-party citation"
  pattern, since these are exactly the kind of third-party source that
  answers "best X tool" questions draw from — but this is an analogy from
  Yext's findings, not a direct measurement of these named sites
  *(heuristic)*.
- **Review/comparison platforms** (G2, Capterra/GetApp, AlternativeTo,
  SaaSworthy): matter for human buyers (review-driven B2B purchase
  decisions, a well-documented pattern) and, consistent with Yext's
  subjective-query finding, plausibly for AI citation on comparison-style
  prompts *(heuristic, indirect)*.
- **Launch/startup directories** (Product Hunt, BetaList, Indie Hackers,
  Show HN): primarily human traffic and backlink/authority value at launch;
  weaker direct evidence of AI-citation value — Product Hunt is anecdotally
  cited in "best new AI tools" answers, but that's not a measured finding
  *(heuristic)*.
- **Generic/low-tier SEO directories** (F6S, StartupStash, and similar):
  no evidence found that generic directories carry meaningful AI-citation
  weight; their value is limited to backlink count and NAP-consistency
  reinforcement (see `brand-entity-sameas.md` for how weakly-evidenced that
  consistency effect itself is) *(heuristic — absence of positive evidence,
  not a documented negative finding)*.

### What to actually do
1. Prioritize category-relevant, higher-tier directories first (AI-tool/SaaS
   directories for an AI/SaaS product; review/comparison platforms next),
   not by directory count.
2. Don't present AI-tool-directory submissions to a user as "proven to drive
   AI citations" — the honest framing is "these are the third-party source
   *type* Yext's data shows AI assistants leaning on for subjective queries
   in the categories studied; no direct measurement exists yet for these
   specific sites."
3. Pace submissions — a handful of high-relevance listings first, generic
   volume directories spread over time — both because it avoids the
   link-spam pattern Google's policy targets and because low-tier
   directories are the weakest-evidenced tier here.
4. Keep identity fields (name, logo, tagline, URL) byte-identical across
   every listing, and treat each new listing as a candidate `sameAs` target
   per `brand-entity-sameas.md`.
5. Verify submissions land and stay accurate — a stale or rejected listing
   does not contribute the corroboration effect it's meant to.

## How this shows up in the workflow
Stage 5 (technical & entity fixes) uses this file to explain to the user
*why* directory submissions matter and which tiers are worth the effort,
scoped honestly to what the Yext/Averi data actually covers versus what's
inferred. The mechanics of picking and submitting to specific directories
live in `../playbooks/directories-playbook.md` (Stage 7).
