<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# keywords

### GET /api/v1/brands/{brand_id}/keyword-recommendation-runs/latest

Get Latest Keyword Recommendation Run

Return the latest recommendation run for polling.

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### GET /api/v1/brands/{brand_id}/keywords

List Keywords

List keywords with latest run summary and competitor overlap.

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### POST /api/v1/brands/{brand_id}/keywords

Add Keyword

Manually add a keyword (source='manual'). Free — no quota spend.

Fire-and-forget a free async KD fetch for the new word so its
difficulty/volume/CPC populate the global cache without blocking the add.

Parameters:
- `brand_id` in path (required)

Request body: `KeywordCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### DELETE /api/v1/brands/{brand_id}/keywords/{keyword_id}

Delete Keyword

Delete a keyword (manual or recommended).

Parameters:
- `brand_id` in path (required)
- `keyword_id` in path (required)

Responses: 204, 422

### PATCH /api/v1/brands/{brand_id}/keywords/{keyword_id}

Update Keyword

Edit a customer keyword (source='manual'). Free — no quota spend.

Parameters:
- `brand_id` in path (required)
- `keyword_id` in path (required)

Request body: `KeywordUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### POST /api/v1/brands/{brand_id}/keywords/{keyword_id}:accept

Accept Recommendation

Promote a staging recommendation into the customer keyword list.

Parameters:
- `brand_id` in path (required)
- `keyword_id` in path (required)

Responses: 201, 422

### POST /api/v1/brands/{brand_id}/keywords:difficulty

Refresh Keyword Difficulty

Refresh KD/volume/CPC for the brand's keywords — charges only if needed.

Gathers the brand's keyword texts (read-only, ownership-checked) and checks
whether any are stale/missing against the 45-day TTL cache BEFORE spending
anything. If every keyword is already fresh, returns 200 {"status":
"up_to_date"} with no quota spend and no dispatch — a Refresh click that would
be a genuine no-op must not cost a T-coin. Otherwise spends one
``keyword_difficulty`` unit (``enforce_quota``'s own check-and-spend logic,
called directly here rather than via ``Depends`` so the charge can be
conditional on the staleness check above), dispatches the async KD fetch, and
returns 202 {"status": "accepted"} — the ref_id + feature label let
``UsageRefundMiddleware`` refund the spend if the task later fails.

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### POST /api/v1/brands/{brand_id}/keywords:recommend

Recommend Keywords

Enqueue an async keyword recommendation run.

Spends one ``keyword_recommendations`` unit before dispatch. On task failure
the worker + UsageRefundMiddleware refund the spend via ``ref_id``.

Parameters:
- `brand_id` in path (required)

Responses: 202, 422

## Request body schemas

### KeywordCreate

Manual keyword add. ``source`` is server-set — never client-settable.

- `text`: `string` (required)

### KeywordUpdate

Edit customer keyword text. Only ``manual`` rows are patchable.

- `text`: `string` (required)
