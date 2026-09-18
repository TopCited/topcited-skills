<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# geo-optimizer

### POST /api/v1/geo-optimizer/analyze

Analyze

Fetch + parse into blocks + detect mode, then persist an 'analyzed' run.

Request body: `AnalyzeRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### GET /api/v1/geo-optimizer/labels

Get Labels

Return plain-language labels for GEO features and methods.

Responses: 200

### GET /api/v1/geo-optimizer/runs

List Runs

List the caller's recent optimization runs, newest first.

Parameters:
- `seo_analysis_id` in query
- `source` in query

Responses: 200, 422

### GET /api/v1/geo-optimizer/runs/{run_id}

Get Run

Fetch one of the caller's optimization runs.

Parameters:
- `run_id` in path (required)

Responses: 200, 422

### POST /api/v1/geo-optimizer/runs/{run_id}/blocks/{block_index}/optimize

Optimize Block

Mode 1: optimize a single block (call again to Regenerate).

Parameters:
- `run_id` in path (required)
- `block_index` in path (required)

Responses: 200, 422

### POST /api/v1/geo-optimizer/runs/{run_id}/optimize

Optimize Run

Mode 2: optimize the whole page content for an analyzed run.

Parameters:
- `run_id` in path (required)

Request body: `OptimizeRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### POST /api/v1/geo-optimizer/runs/{run_id}/optimize-async

Optimize Run Async

Start a background GEO run over selected sections. Beta: per-user lock, no quota.

Parameters:
- `run_id` in path (required)

Request body: `OptimizeAsyncRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 202, 422

## Request body schemas

### AnalyzeRequest

Body for POST /geo-optimizer/analyze.

- `url`: `string | null` (optional)
- `content`: `string | null` (optional)
- `target_queries`: `array<string>` (optional)
- `source`: `string` (optional, default `"standalone"`)
- `seo_analysis_id`: `string (uuid) | null` (optional)

### OptimizeAsyncRequest

Body for POST /geo-optimizer/runs/{id}/optimize-async.

- `selected_block_indices`: `array<integer> | null` (optional)

### OptimizeRequest

Body for POST /geo-optimizer/runs/{id}/optimize (whole-page, Mode 2).

- `platform`: `"linkedin" | "medium" | "reddit" | null` (optional)
