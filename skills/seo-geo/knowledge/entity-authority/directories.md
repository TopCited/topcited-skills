---
topic: Which directory types still matter for humans, search, and AI citation in 2026
stage-relevance: [5]
last-verified: 2026-10-24
sources:
  - https://developers.google.com/search/docs/essentials/spam-policies#link-spam (updated 2026-08-28)
  - https://www.yext.com/blog/ai-visibility-in-2025-how-gemini-chatgpt-perplexity-cite-brands (2025-10-29)
  - Yext press release, Business Wire, 2025-10-09 ("86% of AI citations come from brand-managed sources")
  - https://www.tryprofound.com/blog/ai-platform-citation-patterns (Profound, 680M citations, 2025-06-05)
  - https://www.averi.ai/how-to/chatgpt-vs.-perplexity-vs.-google-ai-mode-the-b2b-saas-citation-benchmarks-report-(2026) (Averi, 2026-01-07 — secondary aggregator)
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
Google's spam policies define link spam as "creating links to or from a site
primarily for the purpose of manipulating search rankings" — examples
include buying/selling links, excessive link exchanges, automated
link-creation programs, and, explicitly, **"low-quality directory or
bookmark site links."** *(P)* It does **not** ban directory listings as a
format; a listing is fine when it's an editorially-curated business listing
rather than a manipulative scheme. The risk is in *how* a listing is
acquired (mass-submitted, paid purely for link-passing) rather than in
directories as a category. Pacing submissions and using consistent brand
fields (rather than mass-blasting dozens of directories in a day) lines up
with this "primarily for manipulation" test, even though Google does not
publish a specific submission-rate threshold *(inference from the primary
doc, not a stated Google threshold)*.

### The strongest evidence in this track: Yext's AI-citation dataset — and its scope
- Yext's AI-citation research (first-party, disclosed methodology) analyzed
  6.8 million AI citations across 1.6 million responses, collected
  2025-07-01 to 2025-08-31, across ChatGPT, Gemini, and Perplexity, spanning
  4 intent quadrants and 4 industries (retail, financial services,
  healthcare, food service). Finding: **48.73% of ChatGPT citations came
  from third-party sites** (directories/review platforms such as Yelp,
  TripAdvisor, MapQuest), while Gemini drew 52.15% from brand-owned sites;
  Yext puts the directory share for subjective "what's the best…" queries
  at 46.3%. *(I)* Yext's own headline cuts the other way: it reports **86%
  of citations come from brand-managed sources** — websites 44%, *listings*
  42% — because it counts a brand's directory listings as brand-managed.
  Either way, listings a brand controls are a large share of what AI cites.
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
- Cross-engine overlap is low: only ~11% of cited domains are shared
  between ChatGPT and Perplexity (reported by Averi's Jan 2026 aggregator
  report, citing a third-party analysis; consistent with TopCited internal
  research) — a directory cited by one assistant is not a reliable proxy
  for being cited by another. *(I)* (The large citation dataset often cited
  alongside it — 680M citations — is Profound's Aug 2024–Jun 2025 analysis,
  not Averi's. A widely repeated "brands on 4+ platforms are 2.8x more
  likely to appear in ChatGPT" figure could not be found in the Averi
  report and should not be cited.)

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
scoped honestly to what the Yext data actually covers versus what's
inferred. The mechanics of picking and submitting to specific directories
live in `../playbooks/directories-playbook.md` (Stage 7).
