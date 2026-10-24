# SEO & GEO analysis

## What this is (tell the user)
"SEO" is being findable in Google/Bing search. "GEO" (Generative Engine
Optimization) is the newer cousin: being findable and quoted correctly by AI
assistants. This guide covers the tools that check and improve both: a full
**site audit** that crawls a whole site and lists concrete issues, a quick
**URL analysis** that scores one page and checks whether AI can "see" it, and the
**GEO content optimizer** plus **content optimization** submissions, which
rewrite existing content to be more citable.

## When the workflow uses it
Stage 4 (Site audit): audit the site, translate the issue list into plain
language ranked by impact, and turn it into an improvement plan the user approves
item by item. Stage 5: the audit findings drive the guided fixes. Stages 5/6: the
optimizer and submissions rewrite existing pages (compare
[content-pillar-cluster.md](content-pillar-cluster.md), which drafts new ones).

## Site audits
| I want to… | Command |
|---|---|
| Estimate, then audit a site | `topcited audit run example.com --dry-run` → `topcited audit run https://example.com --wait --yes` |
| Show a run's summary and issues | `topcited audit show <run-id> [--site example.com]` |
| List audit runs | `topcited audit list [--site example.com]` |
| Raw issues / site records | `topcited api /seo/sites/<site_id>/audit-runs/<run_id>/issues` · `topcited api /seo/sites` · `topcited api /seo/sites/<site_id>` |

`audit run` registers the site on first use and reuses it after that.

*Internal* (works via `topcited api`, may change): mark an issue fixed/ignored
(`PATCH /seo/issues/<issue_id>`), list crawled pages
(`GET /seo/sites/<site_id>/pages`), delete a site (`DELETE /seo/sites/<site_id>`,
cascades pages, runs and issues).

## URL analysis — *internal*
One page, no site registration. Works via `topcited api`, may change:

```bash
topcited api -X POST /seo/analyze -d '{"url": "https://acmecoffee.com/blog/best-espresso-machines"}'
```

The score and findings return immediately; for a signed-in caller the analysis
is saved and an AI-visibility check starts in the background
(`result.ai_visibility.status` = `pending`). Poll
`topcited api /seo/analyses/<analysis_id>` until it settles; retry a failed
check with `POST /seo/analyses/<analysis_id>/ai-visibility` (free).

## GEO content optimizer — *internal*
Works via `topcited api`, may change.

1. `topcited api -X POST /geo-optimizer/analyze -d '{"url": "…"}'` (or
   `{"content": "…"}` for pasted text) — fetches and splits the content into
   blocks and **detects** the mode: whole-page or per-block. No LLM yet.
2. Then, per the detected mode:
   - whole page: `POST /geo-optimizer/runs/<run_id>/optimize` (synchronous;
     rewritten copy in `rewritten_content_md`);
   - one block: `POST /geo-optimizer/runs/<run_id>/blocks/<block_index>/optimize`
     (call again to regenerate);
   - longer jobs: `POST /geo-optimizer/runs/<run_id>/optimize-async` with
     `selected_block_indices`, then poll `GET /geo-optimizer/runs/<run_id>`.

**Platform-targeted rewrites.** Whole-page `optimize` takes an optional
`{"platform": "linkedin" | "medium" | "reddit"}`: LinkedIn gets a professional,
first-person, insight-led voice with no hype or hashtags; Medium gets long-form
essayistic narrative; Reddit gets plain-spoken, community-first prose. It tunes
tone, voice and structure only — never length. Only whole-page `optimize` accepts
it: the block endpoint takes no body and `optimize-async` silently drops it. A
re-run overwrites the stored `platform` — omitting it writes `null`, so send it
again to regenerate the same variant.

## Content optimization submissions
In the public spec, via `topcited api`:

| I want to… | Call |
|---|---|
| List strategies | `topcited api /optimization/strategies` |
| Submit content | `topcited api -X POST /optimization/submissions -d '{"input_content": "…", "output_mode": "…", "strategy_id": "…"}'` |
| List / get submissions | `topcited api /optimization/submissions` · `topcited api /optimization/submissions/<id>` |

Small submissions (≤2,000 words) come back processed; larger ones run async —
poll the submission. The result is in the submission's `output_data` (there is no
download endpoint). *Internal*: `POST /optimization/submissions/from-seo`
(hand-off from a URL analysis) and `POST /optimization/core/submit` (CORE
strategy, always async).

## UI links
- `{TOPCITED_UI_URL}/seo` — URL analysis and the site list;
  `{TOPCITED_UI_URL}/seo/analyses/{id}` — one saved analysis.
- `{TOPCITED_UI_URL}/seo/{siteId}` — a site's pages;
  `{TOPCITED_UI_URL}/seo/{siteId}/audit/{runId}` — one audit run's issues.
- `{TOPCITED_UI_URL}/geo-optimizer` — the GEO optimizer.
- `{TOPCITED_UI_URL}/optimization` and `{TOPCITED_UI_URL}/optimization/{id}` —
  submissions. (`/try-geo` is a public demo — not this.)

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
- Site audit: **9 T-coins** per crawl (`seo_audits`). `--dry-run` can't estimate
  it yet (it shows the balance) — quote 9 yourself.
- URL analysis: **1 T-coin** (`url_analyses`); the follow-up AI-visibility check
  and its retry are free.
- Optimization submissions: **7 T-coins** each (`optimizations`), refunded on
  internal failure, not on validation errors.
- GEO optimizer: free during beta (one async run at a time per user). Metering
  may arrive before GA — quote only what `topcited usage` shows today.
- Listing and reading sites, runs, issues, analyses and submissions is free.

## Failure modes
- Exit 4 → that feature's allowance is used up; explain, don't retry, point at
  billing.
- Exit 7 from `audit run --wait` → the crawl is still going; `topcited wait <job>`.
  Don't treat the issue list as final until the run is terminal.
- Exit 6 from `optimize-async` → you already have a GEO run in flight; wait for
  it (or its 1-hour lock) rather than starting another.
- A submission whose `deletable` is `false` (task still active) can't be deleted
  yet — wait for a terminal status.
