# Monitoring

## What this is (tell the user)
We regularly ask Google and the AI assistants (ChatGPT, Gemini, and similar)
the questions your customers actually ask, and track whether your brand
shows up in the answers — and where your competitors do instead. A "query
set" (shown in the UI as a "Topic") is a themed group of those questions;
each question in it is a "query." Running the set fires every query at every
configured engine and records who got mentioned, how prominently, and with
what sentiment.

## When the workflow uses it
Stage 2 (Baseline monitoring): right after the brand brief exists, derive an
initial keyword/prompt set, create query sets, and trigger the first run —
this is the "before photo," deliberately early so improvement later is
measurable. Stage 8 (Review & ongoing monitoring): much later, refine the
query sets with everything learned since, compare the new numbers against
that Stage 2 baseline, and leave a recurring check-in routine running.

## Operations
| I want to… | Call | Reference |
|---|---|---|
| Create a query set (Topic) | `POST /api/v1/monitoring/query-sets` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| List query sets | `GET /api/v1/monitoring/query-sets` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Get one query set (with its queries) | `GET /api/v1/monitoring/query-sets/{query_set_id}` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Update a query set | `PATCH /api/v1/monitoring/query-sets/{query_set_id}` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Delete a query set | `DELETE /api/v1/monitoring/query-sets/{query_set_id}` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Snapshot all brand competitors into a set | `POST /api/v1/monitoring/query-sets/{query_set_id}/competitors:add-all` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Get LLM-suggested queries for a set | `POST /api/v1/monitoring/query-sets/{query_set_id}/suggest-queries` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Get LLM-suggested keyword+prompt pairs for a set | `POST /api/v1/monitoring/query-sets/{query_set_id}/suggest-query-pairs` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Add queries to a set | `POST /api/v1/monitoring/query-sets/{query_set_id}/queries` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Edit a query | `PATCH /api/v1/monitoring/queries/{query_id}` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Delete a query | `DELETE /api/v1/monitoring/queries/{query_id}` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Trigger a run for every query in a set | `POST /api/v1/monitoring/query-sets/{query_set_id}/run` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| List runs | `GET /api/v1/monitoring/runs` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| See a run's captured sources | `GET /api/v1/monitoring/runs/{run_id}/sources` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Clear a set's run history | `DELETE /api/v1/monitoring/query-sets/{query_set_id}/runs` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Check projected credit spend vs balance | `GET /api/v1/monitoring/credit-forecast` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Read mention rate / share of voice over time | `GET /api/v1/monitoring/metrics/visibility` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Read the summary table (per-brand aggregates) | `GET /api/v1/monitoring/metrics/summary` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Read per-query metrics (the Query Tracking table) | `GET /api/v1/monitoring/metrics/per-query` | [endpoints/monitoring.md](endpoints/monitoring.md) |
| Find "gap" queries (competitors mentioned, you aren't) | `GET /api/v1/monitoring/gaps` | [endpoints/monitoring.md](endpoints/monitoring.md) |

Beyond these there are several more `metrics/*` read endpoints (ranking,
sentiment, source distribution, source citations) — same query/date/platform
filter shape throughout; browse [endpoints/monitoring.md](endpoints/monitoring.md)
for the full list rather than treating the table above as exhaustive.

## Example
```bash
scripts/tc-api.sh POST /api/v1/monitoring/query-sets \
  -d '{"name": "Espresso machines"}'
```
Returns the query set with its `id`. Then add queries:
```bash
scripts/tc-api.sh POST /api/v1/monitoring/query-sets/$SET_ID/queries \
  -d '[{"text": "best espresso machine for beginners", "query_type": "llm_prompt"}, {"text": "espresso machine reviews", "query_type": "search_keyword"}]'
```
`query_type` routes the query to the right engine(s) — valid values are
`llm_prompt` (runs against AI assistants), `search_keyword` (runs against
Google/Bing), and `universal` (runs against both).
Then trigger a run:
```bash
scripts/tc-api.sh POST /api/v1/monitoring/query-sets/$SET_ID/run
```
Returns `{"batch_id", "runs_created"}` — `runs_created` is one run per
(query × platform × method) combination, not per query. Runs execute
asynchronously; poll `GET /api/v1/monitoring/runs` (with `?query_set_id=`)
and watch for the newest batch to move out of `running`, or read
`GET /api/v1/monitoring/metrics/summary` (same `query_set_id` filter) once
done.

## UI links
- `{TOPCITED_UI_URL}/monitoring` — the single-page Query Tracking view:
  topic groups, query CRUD, trigger-run, and every metrics chart/table live
  here.
- `{TOPCITED_UI_URL}/monitoring?topics={query_set_id}` — deep link straight
  to one query set (Topic) with it pre-selected in the filter. The legacy
  `/monitoring/[id]` route still works but only redirects to this form —
  link here directly.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
Every monitoring run charges **1 T-coin per query per engine** — not per
query set and not per click of "Run": `trigger_run` creates one
`MonitoringRun` row per (query × platform × method) combination, and each
row is charged independently when its own async task executes.
So a 5-query set tracked on 2 engines costs up to 10 T-coins per run — tell
the user this multiplies with query-set size and engine count before they
trigger a large set for the first time. If a plan has no `monitoring_runs`
feature configured the charge fails open (not charged, not blocked) rather
than erroring — a legacy-plan edge case, not something to rely on.
`GET /credit-forecast` projects this period's expected spend from the user's
active query-set configuration against their remaining credit balance —
check it before triggering a big first run and relay `exceeds: true` as "this
run may not complete before your credits run out."
`suggest-queries` and `suggest-query-pairs` each spend one `suggestions`
credit (2 T-coins) per call, win-or-lose — a failed/empty LLM result is
refunded automatically, a successful one is not, even if the user doesn't
like the suggestions.
All CRUD on query sets/queries, listing runs, and every `metrics/*` read is
free.

## Failure modes
- `POST .../run` is **asynchronous**: it returns `202` with a `batch_id`
  immediately, before any query has actually run. There is no single "run
  complete" endpoint — poll `GET /runs` filtered to the batch/query set, or
  watch the metrics endpoints, and tell the user results trickle in rather
  than arriving all at once.
- `POST .../run` 400s with `QUERY_SET_EMPTY` if every query in the set is
  inactive or filtered out by platform/query-type routing — add at least one
  runnable query first.
- A run can land as `SKIPPED` (not `failed`) if the credit balance ran out
  mid-batch — some queries in the same batch may have run and others not;
  don't assume a partial batch means nothing happened.
- `DELETE /queries/{query_id}` 409s (`QUERY_HAS_RUNS`) if the query has run
  history — deactivate it via `PATCH` (`is_active: false`) instead of
  deleting, or delete the whole query set if it truly needs to go away.
- `GET /runs` (and every `metrics/*` endpoint) 400s if neither
  `query_set_id`/`query_set_ids` is given and the caller has no active
  brand — there's no default scope to fall back to; make sure a brand is
  active first.
- 422 from any of the bucketed metrics endpoints → malformed date window
  (`from`/`to` given alone, `from` after `to`, span over 365 days) or
  `fill=true` combined with `bucket=batch` (`fill` only applies in `day`
  mode) — fix the query params rather than retrying as-is.
