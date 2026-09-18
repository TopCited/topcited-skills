---
topic: Keyword and search-intent research without enterprise tools (free-tool stack for small brands)
stage-relevance: [3, 6]
last-verified: 2026-08-20
sources:
  - https://www.20minutemarketing.com.au/blog/how-to-do-keyword-research-for-free-in-2026 (accessed 2026-08-20) [heuristic]
  - https://embertribe.com/blog/keyword-research (accessed 2026-08-20) [heuristic]
  - https://robizsolutions.com/how-to-do-keyword-research-2026-intent-first/ (accessed 2026-08-20) [heuristic]
  - https://www.jigsawkraft.com/post/how-to-do-keyword-research-step-by-step-guide-for-beginners-2026 (accessed 2026-08-20) [heuristic]
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
5. **Google Keyword Planner** (free with a Google Ads account, no ad spend
   required) — Google buckets exact search volume behind an ad-spend
   threshold, but the free tier still returns usable relative-volume bands.
   *(heuristic)*

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
reduced regardless of ranking position. One source attributes ~58.5% of
searches ending without a click to SparkToro (2026) and ~34.5% CTR loss on
head terms (10K+ monthly searches) when an AI Overview appears, attributing
the latter to a "Rand Fishkin 2026 zero-click report" — **these specific
percentages could not be independently verified against a primary source in
this research pass; treat them as heuristic/unverified attribution.** The
directional claim itself (AI Overviews suppress organic CTR on head terms)
is consistent with widely reported industry data through 2025–2026 and is
safe to state directionally without citing the precise numbers.

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
