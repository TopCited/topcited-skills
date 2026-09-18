<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# prompts

### GET /api/v1/brands/{brand_id}/prompt-recommendation-runs/latest

Get Latest Prompt Recommendation Run

Return the latest recommendation run for polling.

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### GET /api/v1/brands/{brand_id}/prompts

List Prompts

List the brand's prompts plus staged recommendations.

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### POST /api/v1/brands/{brand_id}/prompts

Add Prompt

Manually add a prompt (source='manual'). Free — no quota spend.

Parameters:
- `brand_id` in path (required)

Request body: `PromptCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### GET /api/v1/brands/{brand_id}/prompts/importable

List Importable Prompts

Historical Topic prompts for this brand that aren't in the library yet.

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### DELETE /api/v1/brands/{brand_id}/prompts/{prompt_id}

Delete Prompt

Delete a prompt (manual or recommended).

Parameters:
- `brand_id` in path (required)
- `prompt_id` in path (required)

Responses: 204, 422

### PATCH /api/v1/brands/{brand_id}/prompts/{prompt_id}

Update Prompt

Edit a customer prompt (source='manual'). Free — no quota spend.

Parameters:
- `brand_id` in path (required)
- `prompt_id` in path (required)

Request body: `PromptUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### POST /api/v1/brands/{brand_id}/prompts/{prompt_id}:accept

Accept Recommendation

Promote a staged recommendation into the customer prompt list.

Parameters:
- `brand_id` in path (required)
- `prompt_id` in path (required)

Responses: 201, 422

### POST /api/v1/brands/{brand_id}/prompts/{prompt_id}:add-to-topics

Add Prompt To Topics

Push a library prompt into one or more Topics as llm_prompt queries.

Parameters:
- `brand_id` in path (required)
- `prompt_id` in path (required)

Request body: `AddToTopicsRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### POST /api/v1/brands/{brand_id}/prompts:import

Import Prompts

Adopt selected historical Topic prompts into the library.

Parameters:
- `brand_id` in path (required)

Request body: `ImportRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### POST /api/v1/brands/{brand_id}/prompts:recommend

Recommend Prompts

Enqueue an async prompt recommendation run (spends 3 credits).

Parameters:
- `brand_id` in path (required)

Responses: 202, 422

## Request body schemas

### AddToTopicsRequest

- `query_set_ids`: `array<string (uuid)>` (required)

### ImportRequest

- `texts`: `array<string>` (required)

### PromptCreate

Manual prompt add. ``source`` is server-set — never client-settable.

- `text`: `string` (required)

### PromptUpdate

Edit prompt text. Only ``manual`` rows are patchable.

- `text`: `string` (required)
