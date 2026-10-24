# Content (pillar/cluster)

## What this is (tell the user)
A "pillar and cluster" is a content structure: one in-depth "pillar" page that
covers a topic thoroughly, plus several shorter "cluster" articles that each go
deep on one sub-question and link back to the pillar. It's the structure both
search engines and AI assistants treat as a sign of real expertise. This feature
generates a full set — topic research, an outline, drafts and publish-ready pages
— from a topic or a handful of your tracked keywords.

## When the workflow uses it
Stage 6 (Content strategy & generation): once competitor keywords (Stage 3) and
the improvement plan (Stage 4) exist, start a run from a topic the brand should
own. The user reviews drafts in the TopCited app before anything is published.

## Calls
*Internal* — not in the public spec and no CLI verb yet; everything below works
via `topcited api` but may change.

| I want to… | Call |
|---|---|
| Start a run | `topcited api -X POST /pillar-cluster/runs -d '{"topic": "espresso machine buying guide", "language": "en"}'` |
| List runs | `topcited api /pillar-cluster/runs` |
| Check status/progress | `topcited api /pillar-cluster/runs/<task_id>` |
| Cancel a run in progress | `topcited api -X POST /pillar-cluster/runs/<task_id>/cancel` |
| Redo from a stage | `topcited api -X POST /pillar-cluster/runs/<task_id>/replay -d '{"from_stage": "draft"}'` |
| Read the combined draft | `topcited api /pillar-cluster/runs/<task_id>/outputs/draft` |
| List / read generated pages | `topcited api /pillar-cluster/runs/<task_id>/outputs/pages` · `…/outputs/pages/<slug>` |
| Download everything as a zip | see **Lifecycle** below (binary — not through `topcited api`) |
| Trending-topic ideas | `topcited api /pillar-cluster/trending-topics` |

**Inputs.** Supply exactly one of `topic`, `keyword_ids` (from
[recommendations.md](recommendations.md)), or `topology` (pre-built
pillar/cluster specs: `slug`, `title`, `target_keywords`, `role`
`pillar|cluster`, `parent_slug`) — never `topic` and `topology` together. A run
generates 1–30 pages (one pillar, the rest clusters). Send an `Idempotency-Key` header
(`-H "Idempotency-Key: <uuid>"`) so a retried create doesn't start — and pay for
— a second run.

**Platform-formatted output.** An optional `platform` (`linkedin`, `medium`,
`zhihu`) with `content_type: "educational"` reshapes the generated post — title
and body rules, hashtags, page count, the outline, and whether FAQ JSON-LD is
included. LinkedIn, for example, becomes a single 135–150-word page opening with a
5W1H question; Zhihu titles run 15–30 Chinese characters. Only those three
`(platform, "educational")` combinations are configured: `reddit`, or any other
`content_type`, is accepted but silently falls back to default long-form output.
For Reddit voice on existing copy, use the GEO optimizer
([seo-geo-analysis.md](seo-geo-analysis.md)) instead.

**Lifecycle.** Runs are long (research → scrape → analyze → draft → generate).
Poll the run until `status` is `completed`, `failed`, or `cancelled` — there's no
webhook; tell the user to check back rather than wait live. `cancel` only works
on a run that isn't terminal; `replay` (from `research`, `scrape`, `analyze`,
`draft`, or `generate`) only on one that is.

**Export.** `topcited api` treats response bodies as text, so fetch the zip with
curl and the CLI's key:

```bash
curl -fsS -H "Authorization: Bearer $(topcited auth token --show)" \
  -o pillar-cluster-export.zip \
  "https://api.topcited.ai/api/v1/pillar-cluster/runs/<task_id>/export.zip"
```

(use your `TOPCITED_BASE_URL` host if it's overridden). The default
`mode=generated` holds the finished pages; `?mode=full` adds every intermediate
artifact.

## UI links
- `{TOPCITED_UI_URL}/pillar-cluster` — run list, "New run" dialog, Trending
  topics tab.
- `{TOPCITED_UI_URL}/pillar-cluster/{task_id}` — one run: stage timeline, draft
  preview, pages, export.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
The **most credit-hungry operation in the workflow** — and not flat:

```
cost = <your plan's pillar_clusters base cost> + 40 × (pages − 1)
```

The base is per plan, so **don't quote a number from memory**: read the plan and
balance with `topcited usage`, compute the figure for the number of pages you're about
to request, and state it before starting the run. `cancel` doesn't refund;
`replay` continues the same run without a new charge. Reading runs, outputs,
exports and trending topics is free.

## Failure modes
- Exit 4 on create → the `pillar_clusters` allowance is used up; explain, don't
  retry, point at billing.
- HTTP 422 on create → none, or a forbidden combination, of
  `topic`/`keyword_ids`/`topology`; pick exactly one.
- Exit 5 on `runs/<task_id>` → wrong or someone else's run id; re-list.
- Cancel on a terminal run, or replay on a running one → refused; check `status`
  first.
- Outputs requested before their stage finished → refused or empty; read
  `current_stage` first, and tell the user partial runs have partial outputs.
- A `failed` or `budget_exceeded` run keeps its charge — salvage it with
  `replay` from the last good stage rather than paying for a fresh run.
