<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# monitoring

### GET /api/v1/monitoring/credit-forecast

Get Credit Forecast

Projected monitoring credit consumption this period vs available credits.

Returns the number of monitoring query-runs projected for this billing period
(``forecast_runs``), the remaining credits available (pool allowance minus
period spend, plus any purchased bundle balance), and whether the forecast
exceeds the available credits.

Responses: 200

### GET /api/v1/monitoring/gaps

Get Gaps

Get gap queries where competitors are mentioned but the customer brand is not.

Parameters:
- `query_set_id` in query (required)

Responses: 200, 422

### GET /api/v1/monitoring/mentions

Get Mentions

Get sentiment-aggregated mention data for a query set.

Parameters:
- `query_set_id` in query (required)

Responses: 200, 422

### GET /api/v1/monitoring/metrics/gaps

Get Gaps Metrics

Gap analysis metrics; day mode merges each set's latest batch per day.

``fill=true`` (day mode only) emits ``lost_query_count=0`` points with a
null ``batch_id`` for run-less days — a filled zero means "no data that
day", not "checked and found no gaps".

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query
- `bucket` in query
- `tz` in query
- `fill` in query

Responses: 200, 422

### GET /api/v1/monitoring/metrics/per-query

Get Per Query Metrics

Customer-brand metrics per query over the window (Query Tracking table).

One row per query of the selected set(s) — inactive and never-run queries
included (``total_runs=0``, metrics null). Formulas match
``/metrics/summary`` exactly (raw-count window aggregation), so per-query
numbers roll up to the brand-level summary: mention rate = mentioned runs
/ query runs, share of voice = customer mentioned runs / all brands'
mentioned runs on the query, sentiment is confidence-weighted, and
``avg_rank`` is search-only (null for LLM-only queries). ``brand_rank``
ranks the customer among brands by mentioned-run count on that query.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query

Responses: 200, 422

### GET /api/v1/monitoring/metrics/ranking

Get Ranking Metrics

Ranking metrics, per batch or per day.

Rank data is search-platform-only today: LLM answers carry no SERP
position, so ``avg_rank`` is null whenever the window/filters contain no
search runs. Multiple query sets pool their runs; ``fill=true`` (day mode
only) emits an empty point for run-less days.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query
- `bucket` in query
- `tz` in query
- `fill` in query

Responses: 200, 422

### GET /api/v1/monitoring/metrics/sentiment

Get Sentiment Metrics

Sentiment metrics for all brands, per batch or per day.

Multiple query sets pool their runs (confidence-weighted score sums the
numerator/denominator across the union). ``fill=true`` (day mode only)
emits an empty point for run-less days.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query
- `bucket` in query
- `tz` in query
- `fill` in query

Responses: 200, 422

### GET /api/v1/monitoring/metrics/source-citations

Get Source Citations

Return top-100 by-URL and by-domain source citations for a time window.

Brand matching is recomputed at request time against the customer's
current brand + competitor list (see spec §6). Multiple query sets pool
their source rows and union their brand/competitor name sets.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query

Responses: 200, 422

### GET /api/v1/monitoring/metrics/source-citations/hierarchy

Get Source Citations Hierarchy

Domain -> URL source-citation hierarchy for the Overview Sources card.

Same windowing/pooling/matching semantics as ``/metrics/source-citations``
(which stays unchanged for the current pages), but domains carry their
cited URLs nested, ``mentioned_count``/``url_count`` for the "N of M
cited pages" fraction, and competitor identity (id + icon/website) so
the client can render competitor logos. Top-100 domains, up to 50 URLs
listed per domain.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query

Responses: 200, 422

### GET /api/v1/monitoring/metrics/sources

Get Source Distribution

Return source-type distribution per brand over a time window.

Multiple query sets pool their mention counts.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query

Responses: 200, 422

### GET /api/v1/monitoring/metrics/summary

Get Metrics Summary

Per-brand aggregated stats over the window for the summary table.

Values are raw-count aggregates over the pooled window (union of the
selected query sets): mention rate = mentioned runs / total runs, share
of voice = brand's mentioned runs / all brands' mentioned runs, sentiment
is confidence-weighted, and ``avg_rank`` comes from search-platform runs
only (null for LLM-only data). With ``compare=true`` the response also
carries ``previous_window`` and per-row ``delta``.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query
- `compare` in query

Responses: 200, 422

### GET /api/v1/monitoring/metrics/visibility

Get Visibility Metrics

Visibility metrics (mention rate + share of voice), per batch or per day.

Multiple query sets (``query_set_ids``, or the active brand's sets when
no set param is given) are pooled over raw counts — mention rate is
mentioned runs / total runs of the union, never an average of per-set
rates. ``fill=true`` (day mode only) emits an empty point (``brands=[]``)
for run-less days.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `from` in query
- `to` in query
- `platforms` in query
- `bucket` in query
- `tz` in query
- `fill` in query

Responses: 200, 422

### GET /api/v1/monitoring/queries/recent

Get Recent Queries

Return the text of active queries the current user is monitoring.

Used by the New Run dialog to pre-populate topic suggestion chips so
they reflect what the user is already tracking.

Parameters:
- `limit` in query

Responses: 200, 422

### DELETE /api/v1/monitoring/queries/{query_id}

Delete Query

Hard-delete a single query.

Ownership is validated via the parent query set. Returns 404 if the
query does not exist or belongs to another customer. Returns 409
Conflict (code ``QUERY_HAS_RUNS``) if any monitoring runs still
reference the query; deactivate it via PATCH instead, or delete the
parent query set.

Parameters:
- `query_id` in path (required)

Responses: 204, 422

### PATCH /api/v1/monitoring/queries/{query_id}

Update Query

Update a single query.

Ownership is validated by walking ``query.query_set.customer_id``.
Returns 404 if the query does not exist **or** belongs to another
customer, to avoid leaking cross-tenant existence.

Parameters:
- `query_id` in path (required)

Request body: `QueryUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### GET /api/v1/monitoring/query-sets

List Query Sets

List query sets for the authenticated customer.

Each row carries ``query_count`` / ``active_query_count`` (from a grouped
COUNT, not the ``queries`` relationship) so the Topics filter can show
"N prompts" per set without a detail call per set.

Parameters:
- `skip` in query
- `limit` in query

Responses: 200, 422

### POST /api/v1/monitoring/query-sets

Create Query Set

Create a new query set for the authenticated customer.

Request body: `QuerySetCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### PATCH /api/v1/monitoring/query-sets/reorder

Reorder Query Sets

Persist a drag-reorder of the caller's query sets (topic groups).

``ordered_ids`` gets 0-based positions by list index. Every id must
belong to the caller (404 otherwise). A subset is allowed; unlisted sets
keep their old positions. List endpoints order by (position, created_at).

NOTE: registered before ``PATCH /query-sets/{query_set_id}`` so the
literal ``reorder`` segment is never parsed as a UUID.

Request body: `ReorderRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 204, 422

### DELETE /api/v1/monitoring/query-sets/{query_set_id}

Delete Query Set

Hard-delete a query set and cascade to queries, runs, and mentions.

Returns 204 on success, 404 if the query set does not exist or belongs
to another customer. For reversible removal, use ``PATCH`` with
``is_active=false`` instead.

Parameters:
- `query_set_id` in path (required)

Responses: 204, 422

### GET /api/v1/monitoring/query-sets/{query_set_id}

Get Query Set

Get a single query set by ID, including its full list of queries.

Parameters:
- `query_set_id` in path (required)

Responses: 200, 422

### PATCH /api/v1/monitoring/query-sets/{query_set_id}

Update Query Set

Update a query set.

Parameters:
- `query_set_id` in path (required)

Request body: `QuerySetUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### POST /api/v1/monitoring/query-sets/{query_set_id}/competitors:add-all

Add All Competitors To Query Set

Snapshot every current brand competitor into this query set.

Idempotent: rerunning is a no-op if the brand's competitors are already
linked. The ``tracks_all_competitors`` flag is left untouched -- callers
that want auto-tracking should patch the flag separately.

Parameters:
- `query_set_id` in path (required)

Responses: 200, 422

### POST /api/v1/monitoring/query-sets/{query_set_id}/queries

Add Queries

Add queries to a query set.

Parameters:
- `query_set_id` in path (required)

Responses: 201, 422

### PATCH /api/v1/monitoring/query-sets/{query_set_id}/queries/reorder

Reorder Queries

Persist a drag-reorder of the queries within one query set.

``ordered_ids`` must be a permutation of ALL the set's queries (active
and inactive) -- 400 ``QUERY_REORDER_MEMBERSHIP`` otherwise. Unknown or
cross-tenant query sets 404.

Parameters:
- `query_set_id` in path (required)

Request body: `ReorderRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 204, 422

### POST /api/v1/monitoring/query-sets/{query_set_id}/run

Trigger Run

Trigger a monitoring run for all queries in a query set.

Returns the batch_id which can be used to track the run's progress.
Task dispatch happens in a background task after the response (and DB
commit) completes, avoiding a race condition where workers see no row.

Parameters:
- `query_set_id` in path (required)

Responses: 202, 422

### DELETE /api/v1/monitoring/query-sets/{query_set_id}/runs

Clear Run History

Delete all monitoring runs for a query set, keeping the set itself.

Returns ``{"deleted": <count>}``; 404 if the query set does not exist or
belongs to another customer. Irreversible — clears run history + the brand
mentions and sources derived from those runs.

Parameters:
- `query_set_id` in path (required)

Responses: 200, 422

### POST /api/v1/monitoring/query-sets/{query_set_id}/suggest-queries

Suggest Queries

Suggest realistic monitoring queries via LLM.

Uses the query set's name, brands, and competitors as context. Mirrors
the `suggest_competitors` pattern in `app/api/routes/v1/competitors.py`.

Parameters:
- `query_set_id` in path (required)

Request body: `SuggestQueriesRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### POST /api/v1/monitoring/query-sets/{query_set_id}/suggest-query-pairs

Suggest Query Pairs

Suggest search keywords and LLM prompts in one metered call.

Grounded in the query set's name, brands, competitors, the brand's website,
and an optional product description (read defensively so it upgrades for
free once #549 lands a confirmed positioning column). Both lists come from
a single LLM call wrapped in one ``spend_for_suggestion`` so the dialog
charges exactly one metered unit per open / Regenerate.

Parameters:
- `query_set_id` in path (required)

Request body: `SuggestQueryPairsRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### GET /api/v1/monitoring/runs

List Runs

List monitoring runs, newest first, pooled across the scoped query sets.

Scope follows the same convention as the metrics endpoints: ``query_set_ids``
(comma-separated) aggregates several sets into one history, ``query_set_id``
remains the single-set form, and giving neither defaults to every query set
of the caller's active brand — which is a 400 when the caller has no active
brand, since there is then no clean scope to fall back to.

Unlike the metrics endpoints, the date window is **opt-in**: omitting
``from``/``to`` means all time rather than a default window, so an existing
caller that never passed dates keeps seeing its whole history.

Parameters:
- `query_set_id` in query
- `query_set_ids` in query
- `provider` in query
- `platforms` in query
- `method` in query
- `from` in query
- `to` in query
- `skip` in query
- `limit` in query

Responses: 200, 422

### GET /api/v1/monitoring/runs/{run_id}/sources

Get Run Sources

Return all sources captured by a single monitoring run.

404 if the run does not exist or belongs to another customer.

Parameters:
- `run_id` in path (required)

Responses: 200, 422

### GET /api/v1/monitoring/share-of-voice

Get Share Of Voice

Get share-of-voice metrics for a query set.

Parameters:
- `query_set_id` in query (required)

Responses: 200, 422

### GET /api/v1/monitoring/topic-suggestions

Get Topic Suggestions

Return LLM-generated content topic suggestions based on the user's queries.

Spends one `suggestions` quota unit per non-empty generation. Returns `[]`
without spending when the user has no active monitoring queries; refunds
(net zero) when the LLM call fails and yields no topics.

Responses: 200

## Request body schemas

### QuerySetCreate

Schema for creating a new query set.

- `name`: `string` (required)
- `brands`: `array<string>` (optional, default `[]`)
- `competitor_ids`: `array<string (uuid)> | null` (optional)
- `tracks_all_competitors`: `boolean` (optional, default `false`)
- `run_mode`: `"auto" | "manual"` (optional, default `"auto"`)
- `schedule_cron`: `string` (optional, default `"0 0 * * *"`)
- `schedule_timezone`: `string` (optional, default `"UTC"`)
- `platforms`: `array<"chatgpt" | "gemini" | "grok" | "google" | "bing" | "brave" | "deepseek" | "baidu_search">` (required)
- `methods_per_platform`: `map<string, "api" | "browser">` (optional, default `{}`)

### QuerySetUpdate

Schema for updating an existing query set.

- `name`: `string | null` (optional)
- `brands`: `array<string> | null` (optional)
- `competitor_ids`: `array<string (uuid)> | null` (optional)
- `tracks_all_competitors`: `boolean | null` (optional)
- `run_mode`: `"auto" | "manual" | null` (optional)
- `paused`: `boolean | null` (optional)
- `schedule_cron`: `string | null` (optional)
- `schedule_timezone`: `string | null` (optional)
- `platforms`: `array<"chatgpt" | "gemini" | "grok" | "google" | "bing" | "brave" | "deepseek" | "baidu_search"> | null` (optional)
- `methods_per_platform`: `map<string, "api" | "browser"> | null` (optional)
- `is_active`: `boolean | null` (optional)

### QueryUpdate

Schema for updating an existing query.

All fields are optional; only fields explicitly set on the request
(``model_dump(exclude_unset=True)``) will be applied.

- `text`: `string | null` (optional)
- `query_type`: `"llm_prompt" | "search_keyword" | "universal" | null` (optional)
- `category`: `string | null` (optional)
- `priority`: `string | null` (optional)
- `is_active`: `boolean | null` (optional)

### ReorderRequest

Ordered id list for the two reorder endpoints.

Positions are assigned by list index (0-based). Ids must be unique; the
endpoint-specific services validate ownership / membership.

- `ordered_ids`: `array<string (uuid)>` (required)

### SuggestQueriesRequest

Request body for auto-suggesting queries for a query set.

- `query_type`: `"llm_prompt" | "search_keyword" | "universal"` (required)

### SuggestQueryPairsRequest

Request body for the combined keyword + prompt suggestion endpoint.

A single call funds one metered ``suggestions`` unit and returns both
lists, so the Add Queries dialog never double-charges or half-populates.

- `keyword_count`: `integer` (optional, default `2`)
- `prompt_count`: `integer` (optional, default `5`)
