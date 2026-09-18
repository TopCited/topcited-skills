# SEO & GEO analysis

## What this is (tell the user)
"SEO" is being findable in Google/Bing search. "GEO" (Generative Engine
Optimization) is the newer cousin: being findable and quoted correctly by AI
assistants. This guide covers three related tools that check and improve
both: (1) a quick **URL analysis** that scores one page and checks whether
AI can actually "see" it, (2) a full **site audit** that crawls a whole site
and lists concrete issues to fix, and (3) the **GEO content optimizer**,
which rewrites a page's content (section by section or as a whole) to be
more citable by AI assistants, plus a related **content optimization**
pipeline for other rewrite strategies.

## When the workflow uses it
Stage 4 (Site audit): register the site, trigger an audit, translate the
issue list into plain language ranked by impact, and turn it into an
improvement plan the user approves item by item. Stage 5 (Technical & entity
fixes): the audit's findings drive the guided fixes in that stage. The GEO
optimizer and content optimization submissions support the content side of
Stage 5/6 — rewriting existing pages rather than drafting new ones (compare
[content-pillar-cluster.md](content-pillar-cluster.md), which generates new
pillar/cluster pages from scratch).

## Operations

### URL analysis (one page, no site registration needed)
| I want to… | Call | Reference |
|---|---|---|
| Analyze a single URL (score + AI-written findings) | `POST /api/v1/seo/analyze` | [endpoints/seo.md](endpoints/seo.md) |
| List saved analyses | `GET /api/v1/seo/analyses` | [endpoints/seo.md](endpoints/seo.md) |
| Get one saved analysis | `GET /api/v1/seo/analyses/{analysis_id}` | [endpoints/seo.md](endpoints/seo.md) |
| Delete a saved analysis | `DELETE /api/v1/seo/analyses/{analysis_id}` | [endpoints/seo.md](endpoints/seo.md) |
| Retry the AI-visibility check after a failure | `POST /api/v1/seo/analyses/{analysis_id}/ai-visibility` | [endpoints/seo.md](endpoints/seo.md) |

### Site audits (register a site, crawl it, list issues)
| I want to… | Call | Reference |
|---|---|---|
| Register a site | `POST /api/v1/seo/sites` | [endpoints/seo.md](endpoints/seo.md) |
| List registered sites | `GET /api/v1/seo/sites` | [endpoints/seo.md](endpoints/seo.md) |
| Trigger a new audit | `POST /api/v1/seo/sites/{site_id}/audit-runs` | [endpoints/seo.md](endpoints/seo.md) |
| List/get an audit run | `GET /api/v1/seo/sites/{site_id}/audit-runs`, `GET .../audit-runs/{run_id}` | [endpoints/seo.md](endpoints/seo.md) |
| List issues found by a run | `GET /api/v1/seo/sites/{site_id}/audit-runs/{run_id}/issues` | [endpoints/seo.md](endpoints/seo.md) |
| Mark an issue fixed/ignored | `PATCH /api/v1/seo/issues/{issue_id}` | [endpoints/seo.md](endpoints/seo.md) |
| List/get crawled pages | `GET /api/v1/seo/sites/{site_id}/pages`, `GET .../pages/{page_id}` | [endpoints/seo.md](endpoints/seo.md) |
| Delete a site (cascades pages/runs/issues) | `DELETE /api/v1/seo/sites/{site_id}` | [endpoints/seo.md](endpoints/seo.md) |

### GEO content optimizer
| I want to… | Call | Reference |
|---|---|---|
| Get plain-language labels for GEO features/methods | `GET /api/v1/geo-optimizer/labels` | [endpoints/geo-optimizer.md](endpoints/geo-optimizer.md) |
| Analyze a page (fetch + parse into blocks, no LLM yet) | `POST /api/v1/geo-optimizer/analyze` | [endpoints/geo-optimizer.md](endpoints/geo-optimizer.md) |
| Optimize the whole page (Mode 2, synchronous) | `POST /api/v1/geo-optimizer/runs/{run_id}/optimize` | [endpoints/geo-optimizer.md](endpoints/geo-optimizer.md) |
| Rewrite content in a publishing platform's voice (LinkedIn / Medium / Reddit) | same call, with body `{"platform": "linkedin"}` | [endpoints/geo-optimizer.md](endpoints/geo-optimizer.md) |
| Optimize / regenerate one block (Mode 1, synchronous) | `POST /api/v1/geo-optimizer/runs/{run_id}/blocks/{block_index}/optimize` | [endpoints/geo-optimizer.md](endpoints/geo-optimizer.md) |
| Run optimization in the background over selected sections | `POST /api/v1/geo-optimizer/runs/{run_id}/optimize-async` | [endpoints/geo-optimizer.md](endpoints/geo-optimizer.md) |
| List/get optimizer runs | `GET /api/v1/geo-optimizer/runs`, `GET /api/v1/geo-optimizer/runs/{run_id}` | [endpoints/geo-optimizer.md](endpoints/geo-optimizer.md) |

**Platform-targeted rewrites.** Whole-page optimize takes an optional
`platform` — `"linkedin"`, `"medium"`, or `"reddit"` — which swaps in a
per-platform writing directive: LinkedIn gets a professional, first-person,
insight-led voice with no hype or hashtags; Medium gets long-form essayistic
narrative with analogies; Reddit gets plain-spoken, community-first prose with
no marketing tone. It tunes **tone, voice and structure only — never length**
(the rewriter enforces its own word budget, and a length instruction here would
fight it). Omit the field for a generic GEO rewrite. This is the parameter
behind the platform tiles in the optimizer UI, and it's how you serve a "rewrite
this for LinkedIn" request. The chosen platform is echoed back on the run
(`platform` on the response and on list items).

Note that `analyze` accepts raw `content` as well as a `url`, so pasted text —
not just a live page — can be run through a platform-targeted rewrite.

### Content optimization (submission pipeline)
| I want to… | Call | Reference |
|---|---|---|
| Submit content for optimization | `POST /api/v1/optimization/submissions` | [endpoints/optimization.md](endpoints/optimization.md) |
| Submit content handed off from a SEO analysis | `POST /api/v1/optimization/submissions/from-seo` | [endpoints/optimization.md](endpoints/optimization.md) |
| Submit a CORE-strategy request (always async) | `POST /api/v1/optimization/core/submit` | [endpoints/optimization.md](endpoints/optimization.md) |
| List/get submissions | `GET /api/v1/optimization/submissions`, `GET /api/v1/optimization/submissions/{submission_id}` | [endpoints/optimization.md](endpoints/optimization.md) |
| List available strategies | `GET /api/v1/optimization/strategies` | [endpoints/optimization.md](endpoints/optimization.md) |
| Delete a submission | `DELETE /api/v1/optimization/submissions/{submission_id}` | [endpoints/optimization.md](endpoints/optimization.md) |

## Example
```bash
scripts/tc-api.sh POST /api/v1/seo/analyze -d '{"url": "https://acmecoffee.com/blog/best-espresso-machines"}'
```
Returns the score/issues immediately. If the caller is authenticated, the
row is saved and an AI-visibility check is kicked off in the background
(`result.ai_visibility.status` starts `"pending"`) — poll
`GET /api/v1/seo/analyses/{analysis_id}` until it settles.

```bash
scripts/tc-api.sh POST /api/v1/seo/sites -d '{"url": "https://acmecoffee.com"}'
scripts/tc-api.sh POST /api/v1/seo/sites/$SITE_ID/audit-runs
```
The audit run starts `pending`/`running`; poll
`GET /api/v1/seo/sites/{site_id}/audit-runs/{run_id}` (with `$SITE_ID` and
the returned run id) until terminal, then list issues.

```bash
scripts/tc-api.sh POST /api/v1/geo-optimizer/analyze -d '{"url": "https://acmecoffee.com/blog/best-espresso-machines"}'
```
Returns a run in `analyzed` status with content split into blocks and a
detected mode (whole-page vs per-block). Then either:
```bash
scripts/tc-api.sh POST /api/v1/geo-optimizer/runs/$RUN_ID/optimize
```
(Mode 2, synchronous — waits for the LLM call and returns the optimized
page), or optimize one block at a time (Mode 1 — call the block endpoint
again with the same `block_index` to regenerate it), or hand a longer job to
the background with `optimize-async` and poll `GET /runs/{run_id}`.

To rewrite pasted text in a target platform's voice, analyze the `content`
directly and pass `platform` to the whole-page optimize:
```bash
scripts/tc-api.sh POST /api/v1/geo-optimizer/analyze -d '{"content": "Our new espresso machine..."}'
scripts/tc-api.sh POST /api/v1/geo-optimizer/runs/$RUN_ID/optimize -d '{"platform": "linkedin"}'
```
The rewritten copy comes back in `rewritten_content_md`.

## UI links
- `{TOPCITED_UI_URL}/seo` — the URL-analysis panel and the site list.
- `{TOPCITED_UI_URL}/seo/analyses/{id}` — a single saved URL analysis.
- `{TOPCITED_UI_URL}/seo/{siteId}` — a registered site's page list.
- `{TOPCITED_UI_URL}/seo/{siteId}/audit/{runId}` — a single audit run's
  issue list.
- `{TOPCITED_UI_URL}/geo-optimizer` — the GEO content optimizer.
- `{TOPCITED_UI_URL}/optimization` — the content-optimization submission
  list; `{TOPCITED_UI_URL}/optimization/{id}` for a single submission;
  `{TOPCITED_UI_URL}/optimization/sci-defense` is the manipulation-check tool
  covered in [audit.md](audit.md), not this guide.
- `{TOPCITED_UI_URL}/try-geo` — a public/unauthenticated GEO demo page, out
  of scope for an authenticated agent session (listed only so you don't
  confuse it with `/geo-optimizer`).

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
- `POST /seo/analyze`: 1 T-coin (`url_analyses`) when authenticated;
  anonymous callers spend nothing, aren't persisted, and get no AI-visibility
  check. The automatic AI-visibility check that follows a saved analysis is
  **not** separately charged, and its manual retry (`.../ai-visibility`) is
  free too.
- `POST .../audit-runs`: 9 T-coins (`seo_audits`) per triggered crawl.
- The GEO optimizer (`analyze`, `optimize`, block `optimize`,
  `optimize-async`) is **free during beta** — deliberate policy: no quota for
  now, per-user concurrency lock only; metering may be introduced before GA,
  so do not assume it stays free. `analyze` does no LLM work (fetch + block-split + persist).
  `optimize` operations run the same engine as `/optimization` submissions,
  which are metered. Do not tell the user what it will cost after beta —
  quote only what `GET /api/v1/users/me/usage` reports today. You can only
  have one async GEO run going at once (a per-user lock with a 1-hour TTL).
- `POST /optimization/submissions`, `.../submissions/from-seo`, and
  `.../core/submit` each spend 7 T-coins (`optimizations`) at route entry,
  refunded on internal failure (`InternalError`/`ExternalServiceError`) but
  **not** refunded for user errors (validation, rate limit) — small
  submissions (≤2000 words) process synchronously and return the result
  immediately; larger ones and all CORE submissions are dispatched async.
- Everything else here (listing/getting/deleting sites, pages, audit runs,
  issues, analyses, submissions, strategies, geo-optimizer labels) is a free
  read.

## Failure modes
- 402 from `/seo/analyze` (authenticated), `.../audit-runs`, or any
  `/optimization/submissions*`/`core/submit` call → the relevant credit
  feature is exhausted; explain in plain language, don't retry, point to
  billing.
- `/seo/analyze` is synchronous for the score itself but the AI-visibility
  verdict is async — read `result.analysis_id`, then poll
  `GET /seo/analyses/{analysis_id}` for `ai_visibility.status` to move past
  `pending`; don't block on it in the same call.
- `.../audit-runs` and site/page listing are async crawls — `trigger_audit`
  returns `202` immediately; poll the run, don't assume issues exist until
  status is terminal.
- `AlreadyExistsError` (409-shaped) from `optimize-async` → the user already
  has a GEO run in flight; wait for it to finish (or its 1-hour lock to
  expire) rather than starting a second one.
- `platform` is accepted **only** by whole-page `optimize`. The block endpoint
  takes no body at all, and `optimize-async` accepts only
  `selected_block_indices` — a platform sent to either is silently dropped and
  the rewrite comes back generic. If a user wants platform-targeted output,
  route them through the synchronous whole-page call.
- Re-running `optimize` on a run **overwrites** its stored `platform` with
  whatever the new body carries — omitting the field writes `null`, not "keep
  the previous one". To regenerate the same LinkedIn variant, send `platform`
  again.
- `geo-optimizer` Mode 1 vs Mode 2 is **auto-detected** by `analyze`, not
  chosen by the caller — call `optimize` for whole-page mode or the
  block-scoped `blocks/{block_index}/optimize` for per-block mode based on
  what the analyzed run reports, not by guessing.
- `optimization/submissions/{submission_id}/download` is explicitly **not implemented**
  (`501`) — don't build a flow around it; direct the user to the submission
  response's `output_data` instead.
- `optimization/submissions` `deletable: false` (with
  `not_deletable_reason: "task_active"` or `"job_in_progress"`) blocks
  `DELETE` — wait for the submission to reach a terminal status before
  retrying the delete.
