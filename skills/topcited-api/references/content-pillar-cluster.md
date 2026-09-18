# Content (pillar/cluster)

## What this is (tell the user)
A "pillar and cluster" is a content structure: one in-depth "pillar" page that
covers a topic thoroughly, plus several shorter "cluster" articles that each
go deep on one sub-question and link back to the pillar. It's the content
structure both search engines and AI assistants treat as a sign of real
expertise — one thin page rarely earns trust, a well-linked cluster does.
This feature generates a full pillar/cluster set — topic research, an
outline, drafts, and publish-ready pages — from a topic or a handful of your
tracked keywords.

## When the workflow uses it
Stage 6 (Content strategy & generation): once competitor keywords (Stage 3)
and the site audit / improvement plan (Stage 4) exist, start a run from a
topic the brand should own, or hand it a topic derived from keyword
research. The user reviews drafts in the TopCited UI before anything is
published anywhere.

## Operations
| I want to… | Call | Reference |
|---|---|---|
| Start a pillar/cluster run | `POST /api/v1/pillar-cluster/runs` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| List past runs | `GET /api/v1/pillar-cluster/runs` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| Check a run's status/progress | `GET /api/v1/pillar-cluster/runs/{task_id}` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| Cancel a run in progress | `POST /api/v1/pillar-cluster/runs/{task_id}/cancel` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| Redo a run from a specific stage (research/scrape/analyze/draft/generate) | `POST /api/v1/pillar-cluster/runs/{task_id}/replay` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| Read the combined draft (all pages, one markdown stream) | `GET /api/v1/pillar-cluster/runs/{task_id}/outputs/draft` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| List the generated pages (pillar + clusters) | `GET /api/v1/pillar-cluster/runs/{task_id}/outputs/pages` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| Read one generated page | `GET /api/v1/pillar-cluster/runs/{task_id}/outputs/pages/{slug}` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| Download everything as a zip | `GET /api/v1/pillar-cluster/runs/{task_id}/export.zip` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |
| Get trending-topic ideas to seed a run | `GET /api/v1/pillar-cluster/trending-topics` | [endpoints/pillar-cluster.md](endpoints/pillar-cluster.md) |

**Platform-formatted output.** A run takes an optional `platform` —
`"linkedin"`, `"medium"`, `"zhihu"`, or `"reddit"` — paired with
`content_type` (default `"educational"`). A configured (platform,
content_type) cell reshapes the generated post: its title rule, body rule,
hashtag rule, page count, whether FAQ JSON-LD is skipped, and the outline the
analyze stage produces. LinkedIn, for example, becomes a single 135-150 word
page opening with a 5W1H question, and skips the FAQ JSON-LD; Zhihu titles
run 15-30 Chinese characters. This is separate from the GEO optimizer's
`platform` (see the SEO & GEO guide), which only nudges voice on content that
already exists — this one drives layout for content being generated.

**Only three cells are configured**: `("linkedin"|"zhihu"|"medium",
"educational")`. `platform: "reddit"` is a valid enum value with **no spec
behind it**, and so is any `content_type` other than `"educational"` — those
requests are accepted and run, but `get_format_spec` returns `None` and the
pipeline falls back to the default long-form behavior with no platform
shaping at all. Don't promise a user Reddit-formatted output; if they want
Reddit voice on existing copy, that's the GEO optimizer, which does have a
Reddit directive.

`cancel` and `replay` are the two follow-up `POST`s beyond create/list/get:
`cancel` stops a run that hasn't reached a terminal state yet; `replay`
re-runs from a named stage (`research`, `scrape`, `analyze`, `draft`, or
`generate`) on a run that has already finished, failed, or was cancelled —
there is no separate "regenerate" or "confirm" endpoint, replay covers both.

## Example
```bash
scripts/tc-api.sh POST /api/v1/pillar-cluster/runs \
  -d '{"topic": "espresso machine buying guide", "language": "en"}'
```
Returns `{"task_id", "status": "pending", "created_at", "updated_at", ...}`.
Instead of `topic` you can pass `keyword_ids` (from the keyword
recommendations guide) or a pre-built `topology` (a list of pillar/cluster
specs) — supply exactly one of the three, not a combination of `topic` and
`topology`.

To generate the same topic formatted for a specific platform:
```bash
scripts/tc-api.sh POST /api/v1/pillar-cluster/runs \
  -d '{"topic": "espresso machine buying guide", "platform": "linkedin", "content_type": "educational"}'
```

```bash
scripts/tc-api.sh GET /api/v1/pillar-cluster/runs/$TASK_ID
```
Poll this until `status` is `completed`, `failed`, or `cancelled` — there is
no webhook. Tell the user this is a long-running job (research, scraping,
analysis, drafting, and page generation are separate stages) and check back
rather than waiting synchronously.

```bash
scripts/tc-api.sh GET /api/v1/pillar-cluster/runs/$TASK_ID/export.zip > pillar-cluster-export.zip
```
Downloads the full archive (`mode=generated` by default; pass `?mode=full`
for every intermediate artifact too) — this is what to hand the user once
they've reviewed and approved the drafts. Redirect to a file as shown; the
binary body must not print to the terminal.

## UI links
- `{TOPCITED_UI_URL}/pillar-cluster` — the run list + "New run" dialog,
  including the Trending topics tab that backs `GET /trending-topics`.
- `{TOPCITED_UI_URL}/pillar-cluster/{task_id}` — a single run's detail page
  (stage timeline, draft preview, page list, export).

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
Pillar/cluster runs are the **most credit-hungry operation in the whole
workflow**, against 1–10 T-coins for everything else (SEO audit 9, report 10,
URL analysis 1, optimization 7, monitoring run 1).

**The cost is not flat — it scales with the number of pages you ask for:**

```
cost = <your plan's pillar_clusters base cost> + 40 × (target_page_count − 1)
```

`target_page_count` is 1–30 (1 pillar page, the rest clusters), so a large
run costs many times a single-page one. The base is a per-plan value, not a
constant, so **do not quote a fixed number from memory** — read the user's
plan cost and balance from `GET /api/v1/users/me/coin-balance` (free), compute
the figure for the page count you are about to request, and state that number
before calling `POST /runs`. A wasted run is expensive to redo.
`cancel` and `replay` do not spend additional quota — the original run's
charge stands; cancelling doesn't refund it, and replaying continues the
same run rather than starting a fresh metered one.
The output-retrieval endpoints (`outputs/draft`, `outputs/pages`,
`export.zip`) and `GET /runs`, `GET /runs/{task_id}` are free reads.
`GET /trending-topics` is also free (Redis-cached, no LLM call per request).

## Failure modes
- All run-lifecycle calls are **asynchronous** — `POST /runs` returns
  `pending` immediately (or `201`/`200` on idempotent re-submit via the
  `Idempotency-Key` header). Poll `GET /runs/{task_id}` for progress; do not
  assume the run finished just because the create call succeeded.
- 402 from `POST /runs` → plan's `pillar_clusters` credit balance is
  exhausted; explain in plain language, don't retry, point to billing.
- 422 on create → none of `topic`/`keyword_ids`/`topology` was supplied, or
  both `topic` and `topology` were supplied together — pick exactly one input
  shape.
- 404-shaped `RunNotOwnedError` on any `runs/{task_id}` call → wrong,
  cross-tenant, or malformed `task_id`; re-list runs and confirm the id.
- Cancel on a run already in a terminal state (`completed`/`failed`/
  `cancelled`/`timeout`/`budget_exceeded`) → 4xx `RunStateError`; check
  status first, don't blind-retry cancel.
- Replay on a run that is still `pending`/`running` → 4xx `RunStateError`;
  replay only applies to terminal runs.
- `outputs/draft` / `outputs/pages` before the relevant stage has completed
  → `RunStateError` ("Draft stage not yet completed" / empty page list);
  read `current_stage` from the run snapshot before fetching outputs, and
  set the user's expectation that partial runs have partial outputs.
- A `failed` or `budget_exceeded` run does not silently refund — mention to
  the user that a run consumed the credit even if it didn't finish; `replay`
  from the last-good stage is the way to salvage it rather than paying for a
  fresh run from scratch.
