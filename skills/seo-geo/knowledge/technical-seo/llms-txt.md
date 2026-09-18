---
topic: llms.txt spec status, real-world adoption, and whether it actually affects AI citation
stage-relevance: [4, 5]
last-verified: 2026-08-20
sources:
  - https://llmstxt.org/
  - https://www.pravinkumar.co/blog/w3c-llms-txt-standard-proposal-june-2026-webflow-2026
  - https://www.rankability.com/data/llms-txt-adoption/
  - https://codersera.com/blog/llms-txt-complete-guide-2026/
  - https://ultrascout.ai/article/princeton-research-geo-deep-dive
---

# llms.txt

## In plain words
llms.txt is a proposed markdown file, hosted at `/llms.txt`, meant to give AI
tools a clean, curated summary of a site instead of making them parse full
HTML pages. It's cheap to add and a growing number of sites do it. But the
evidence that it actually increases how often AI assistants cite you is thin,
contradictory, and in one widely repeated case appears to be a misattributed
statistic — treat it as low-cost hygiene, not a proven growth lever.

## What practitioners need to know
- **Spec status**: proposed by Jeremy Howard, published 2024-09-03, spec
  pages last updated through 2026-08-10. Format: a markdown file with a
  required H1 (project/brand name), an optional blockquote summary, then
  H2-delimited sections of annotated links. It's deliberately positioned as
  **complementary** to robots.txt/sitemap.xml, not a replacement.
  It **remains a community proposal, not a ratified standard**, governed
  informally via GitHub and Discord.
  - One source claims a W3C standardization proposal in June 2026 — this is
    **unverified against a primary W3C source**; do not state "W3C is
    standardizing llms.txt" as settled fact. (heuristic)
  - A separate source flatly claims "major LLM crawlers don't fetch it yet"
    as of an April 2026 cutoff — also not independently confirmed against
    OpenAI/Anthropic/Google crawler documentation. (heuristic)
- **Notable adopters**: OpenAI, Anthropic, and Gemini publish their own
  llms.txt for developer docs; Mintlify auto-generates one for hosted docs
  sites; Chrome Lighthouse now includes an llms.txt audit check.
- **Adoption data (Rankability tracker, disclosed methodology, monthly
  re-scan, Tranco top-1000 sample, checks `/llms.txt` and `/llms-full.txt`,
  counts only real HTTP 200 plain-text responses)**: as of June 2026, **8.7%**
  of the top 1,000 sites (87/1000) publish llms.txt. Of the 549 domains that
  were actually reachable content sites (451 were infra/CDN domains),
  adoption is **15.8%**. 15 sites also publish `llms-full.txt`. Adoption was
  roughly flat (8–10%) across low/mid/high-traffic tiers — **not** concentrated
  only among tech/AI companies.
- **Debunk: the "23% more AI citations" / "Princeton GEO-bench" claim is
  likely a misattribution.** One industry summary attributes a finding that
  llms.txt sites earn 23% more AI citations (across ChatGPT Search,
  Perplexity, Google AI Mode vs matched controls) to "Princeton's
  GEO-bench." This could not be verified against the actual GEO-bench paper
  (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande). That
  original paper — independently corroborated across three separate
  summaries — evaluated nine *content* optimization methods (statistics
  citation, quotations, fluency, etc.) across ~10,000 queries / 9 datasets /
  7 domains, and **llms.txt is not part of that study at all**. Do not cite
  the 23% figure to Princeton/GEO-bench in any downstream material; it looks
  like a misattribution or conflation with a different, unnamed 2026
  follow-on study.
- **Countervailing negative claim**: a separate, unattributed practitioner
  claim states an XGBoost model trained on AI-citation features *improved*
  when the llms.txt variable was dropped, implying its presence is noise
  rather than signal for citation prediction. No disclosed
  authorship/methodology/sample — treat as anecdotal. (heuristic)
- **Honest framing**: llms.txt in 2026 is a low-cost, low-yield bet with
  clear optionality — implementation cost is roughly half a day, and shipping
  one is increasingly a hygiene norm (especially for dev-tool/SaaS sites,
  given IDE-agent ecosystems already consume similar files) independent of
  whether it measurably moves AI citations. (heuristic, reasonable consensus
  framing) Do not promise brand owners a citation lift from adding it — the
  strongest claimed uplift figure appears misattributed, and the only
  disclosed-methodology adoption data says nothing about whether adoption
  correlates with citation outcomes.

## How this shows up in the workflow
Stage 4 (site audit) checks whether `/llms.txt` exists and is well-formed.
Stage 5 (technical/entity fixes) adds it as a low-cost, low-risk hygiene item
alongside other technical fixes — framed to brand owners as "worth doing
because it's cheap and increasingly normal," not as a promised AI-citation
lever, given the thin and partly-misattributed evidence base.
