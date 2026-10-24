---
topic: Keyword and search-intent research without enterprise tools (free-tool stack for small brands)
stage-relevance: [3, 6]
last-verified: 2026-10-24
sources:
  - https://www.20minutemarketing.com.au/blog/how-to-do-keyword-research-for-free-in-2026 (accessed 2026-08-20) [heuristic]
  - https://embertribe.com/blog/keyword-research (accessed 2026-08-20) [heuristic]
  - https://robizsolutions.com/how-to-do-keyword-research-2026-intent-first/ (accessed 2026-08-20) [heuristic]
  - https://www.jigsawkraft.com/post/how-to-do-keyword-research-step-by-step-guide-for-beginners-2026 (accessed 2026-08-20) [heuristic]
  - https://support.google.com/google-ads/answer/7337243 (Keyword Planner access requirements, accessed 2026-10-24) [primary]
  - https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/ (2026-06-09) [industry, disclosed methodology]
  - https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/ (2024-07-02) [industry, disclosed methodology]
  - https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/ (2026-02-04) [industry, disclosed methodology]
  - https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ (2025-07-22) [industry, disclosed methodology]
---

# Keyword and intent research on a free-tool budget

## In plain words
You don't need an Ahrefs or Semrush seat to figure out what to write about.
Google itself will tell you what people search for, for free, if you know
where to look — autocomplete, the "People Also Ask" boxes, the related
searches at the bottom of a results page, and (best of all) Search Console,
which shows the searches your own site is *already* getting. Combine those
with a simple "what does the searcher want to do next" classification, and
you have a workable keyword list without paying for anything.

## What practitioners need to know

### The free-tool stack (heuristic, but converged across many independent 2026 guides)
1. **Google Autocomplete** — type a seed term into the search box; every
   suggestion is a real query someone has typed. *(heuristic)*
2. **People Also Ask (PAA)** — the expandable question boxes on a live SERP;
   each question is a candidate content angle or FAQ entry. *(heuristic)*
3. **Related Searches** at the bottom of the results page — adjacent-intent
   expansion from a seed term. *(heuristic)*
4. **Google Search Console** (free, requires only site verification) — shows
   actual impressions/clicks/queries your site already gets, including
   queries you rank for with no dedicated page. This is the highest-signal
   free source because it's your own real traffic, not a modeled estimate.
   *(heuristic, but structurally the strongest source in the stack — it's
   ground truth, not an inference)*
5. **Google Keyword Planner** (free with a Google Ads account; Google
   requires completing account setup with billing information, but no
   active ad spend) — accounts without meaningful spend see volume as
   ranges (e.g. 100–1K, 1K–10K) rather than exact numbers, which is still a
   usable relative-volume signal. *(primary for access; heuristic for the
   range behavior)*

### Classifying intent without a tool
Bucket every harvested query by what the searcher wants to *do* next, not
just the words they typed: informational ("how to fix a leaking tap") versus
transactional/high-intent-now ("emergency plumber Ringwood"). For a small or
new site, prioritize lower-volume, higher-intent long-tail phrases over head
terms — head terms are both more competitive and increasingly zero-click.
*(heuristic — this four-way informational/navigational/commercial/
transactional framing is the long-standing practitioner default, still
dominant in 2026 guides)*

### Check for zero-click SERP features before committing content budget
Before investing in a full article for a query, check whether it already
triggers an AI Overview or featured snippet — those clicks are structurally
reduced regardless of ranking position. The sourced numbers *(industry,
disclosed methodology)*:
- **Zero-click share**: SparkToro (Rand Fishkin, 2026-06-09, Similarweb
  panel) found **68.01%** of US Google searches ended without a click to
  the open web in Jan–Apr 2026, up from 60.45% on the same panel in 2024.
  (An often-repeated "58.5%" figure is SparkToro/Datos's *2024* study, not
  2026.)
- **CTR loss when an AI Overview appears**: Ahrefs' 2026-02-04 update (300K
  keywords, Search Console data, Dec 2023 vs Dec 2025) found position-1 CTR
  **58% lower** on queries with an AI Overview; its Apr 2025 study had put
  the drop at 34.5% (the "34.5%" figure is Ahrefs', not a Fishkin report).
  Seer Interactive measured ~61% lower organic CTR on AI Overview queries
  (Sept 2025).
- **Behavioral data**: Pew (2025-07-22, 900 US adults' browsing) found users
  clicked a traditional result on 8% of visits with an AI summary vs 15%
  without, and clicked a link inside the summary only 1% of the time.

### End-to-end workflow (synthesized from multiple convergent 2026 guides)
1. Brainstorm seed topics from the brand's actual products, services, and
   real expertise.
2. Expand each seed via Autocomplete + PAA + Related Searches.
3. Pull Search Console for queries already getting impressions with no
   dedicated page — these are the fastest wins, since you're already almost
   ranking.
4. Classify every harvested query by intent.
5. Bundle same-intent queries onto one target page — this is also the seed
   of the pillar-cluster model (see `pillar-cluster-model.md`).
6. Use Keyword Planner volume bands plus a manual SERP look (who currently
   ranks, is there an AI Overview) as a cheap difficulty proxy, since a free
   stack has no keyword-difficulty score.
7. Revisit quarterly — intent and SERP features shift.
*(heuristic — synthesized workflow, not a single documented spec)*

### A note on source quality
No primary/documented methodology exists for this topic — Google doesn't
publish a "how to do keyword research" spec, and Search Console/Keyword
Planner are tools, not guidance documents. Everything above is convergent
practitioner consensus, which is the normal state of this craft, not a gap
specific to this research pass.

## How this shows up in the workflow
Stage 3 (competitor research) uses this to harvest and classify the query
set a competitor is capturing. Stage 6 (content) uses it to pick which
queries a new piece of content should target and to decide, per query,
whether a full article is worth writing given the SERP's zero-click risk.
