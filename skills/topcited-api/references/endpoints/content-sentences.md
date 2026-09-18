<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# content-sentences

### GET /api/v1/brands/{brand_id}/content-sentence-runs/latest

Get Latest Content Sentence Run

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### GET /api/v1/brands/{brand_id}/content-sentences

List Content Sentences

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### DELETE /api/v1/brands/{brand_id}/content-sentences/{sentence_id}

Delete Content Sentence

Parameters:
- `brand_id` in path (required)
- `sentence_id` in path (required)

Responses: 204, 422

### POST /api/v1/brands/{brand_id}/content-sentences/{sentence_id}:accept

Accept Content Sentence

Parameters:
- `brand_id` in path (required)
- `sentence_id` in path (required)

Responses: 201, 422

### POST /api/v1/brands/{brand_id}/content-sentences:recommend

Recommend Content Sentences

Parameters:
- `brand_id` in path (required)

Request body: `ContentSentenceGenerateRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 202, 422

## Request body schemas

### ContentSentenceGenerateRequest

Topic mode needs exactly one of topic/keyword_id; competitor mode neither.

- `mode`: `string` (required)
- `topic`: `string | null` (optional)
- `keyword_id`: `string (uuid) | null` (optional)
