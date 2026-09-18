<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# pillar-cluster

### GET /api/v1/pillar-cluster/runs

List Runs

Parameters:
- `limit` in query
- `before` in query

Responses: 200, 422

### POST /api/v1/pillar-cluster/runs

Create Run

Parameters:
- `Idempotency-Key` in header

Request body: `RunCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### GET /api/v1/pillar-cluster/runs/{task_id}

Get Run

Parameters:
- `task_id` in path (required)

Responses: 200, 422

### POST /api/v1/pillar-cluster/runs/{task_id}/cancel

Cancel Run

Parameters:
- `task_id` in path (required)

Responses: 202, 422

### GET /api/v1/pillar-cluster/runs/{task_id}/export.zip

Export Zip

Parameters:
- `task_id` in path (required)
- `mode` in query

Responses: 200, 422

### GET /api/v1/pillar-cluster/runs/{task_id}/outputs/draft

Get Draft

Parameters:
- `task_id` in path (required)

Responses: 200, 422

### GET /api/v1/pillar-cluster/runs/{task_id}/outputs/pages

List Pages

Parameters:
- `task_id` in path (required)

Responses: 200, 422

### GET /api/v1/pillar-cluster/runs/{task_id}/outputs/pages/{slug}

Get Page

Parameters:
- `task_id` in path (required)
- `slug` in path (required)

Responses: 200, 422

### POST /api/v1/pillar-cluster/runs/{task_id}/replay

Replay Run

Parameters:
- `task_id` in path (required)

Request body: `ReplayRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 202, 422

### GET /api/v1/pillar-cluster/trending-topics

Get Trending Topics

Parameters:
- `topic` in query

Responses: 200, 422

## Request body schemas

### ReplayRequest

POST /runs/{id}/replay request body.

- `from_stage`: `"research" | "scrape" | "analyze" | "draft" | "generate"` (required)

### RunCreate

POST /runs request body.

At least one of a non-empty ``topic``, non-empty ``keyword_ids``, or
``topology`` must be supplied. ``topic`` (optionally plus keyword ids)
triggers ArchitectStage to derive a topology; ``topology`` runs the
architect in passthrough mode. Topic and topology together are rejected.

- `topic`: `string | null` (optional)
- `keyword_ids`: `array<string (uuid)> | null` (optional)
- `topology`: `array<PillarSpec> | null` (optional)
- `voice_profile`: `VoiceProfile | null` (optional)
- `model_overrides`: `map<string, string> | null` (optional)
- `token_budget`: `integer | null` (optional)
- `language`: `string` (optional, default `"en"`)
- `platform`: `"reddit" | "linkedin" | "medium" | "zhihu" | null` (optional)
- `content_type`: `string` (optional, default `"educational"`)

### PillarSpec

Spec for a single page in the pillar-cluster topology.

- `slug`: `string` (required)
- `title`: `string` (required)
- `target_keywords`: `array<string>` (required)
- `role`: `"pillar" | "cluster"` (required)
- `parent_slug`: `string | null` (optional)

### VoiceProfile

Placeholder for milestone E (voice calibration). No fields today.

_No documented fields._
