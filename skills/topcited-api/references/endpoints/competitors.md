<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# competitors

### GET /api/v1/brands/{brand_id}/competitors

List Competitors

List the brand's competitors, newest first.

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### POST /api/v1/brands/{brand_id}/competitors

Create Competitor

Create a competitor under one of the user's brands.

Parameters:
- `brand_id` in path (required)

Request body: `CompetitorCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### POST /api/v1/brands/{brand_id}/competitors:bulk

Bulk Create Competitors

Atomically create a batch of competitors. All-or-nothing on collision.

Parameters:
- `brand_id` in path (required)

Responses: 201, 422

### POST /api/v1/brands/{brand_id}/competitors:suggest

Suggest Competitors

Return LLM-suggested competitors based on brand context.

Spends one `suggestions` quota unit (50/period free, 1 T-coin paid). Empty
results are refunded; over-cap callers get 402 before the LLM call.

Parameters:
- `brand_id` in path (required)

Request body: `SuggestCompetitorsRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### DELETE /api/v1/competitors/{competitor_id}

Delete Competitor

Delete a competitor.

Parameters:
- `competitor_id` in path (required)

Responses: 204, 422

### GET /api/v1/competitors/{competitor_id}

Get Competitor

Fetch a single competitor owned by the current user.

Parameters:
- `competitor_id` in path (required)

Responses: 200, 422

### PATCH /api/v1/competitors/{competitor_id}

Patch Competitor

Partially update a competitor.

Parameters:
- `competitor_id` in path (required)

Request body: `CompetitorUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### POST /api/v1/competitors/{competitor_id}/keyword-scans

Trigger Keyword Scan

Parameters:
- `competitor_id` in path (required)

Responses: 202, 422

### GET /api/v1/competitors/{competitor_id}/keyword-scans/latest

Get Latest Keyword Scan

Parameters:
- `competitor_id` in path (required)

Responses: 200, 422

### GET /api/v1/competitors/{competitor_id}/keywords

List Competitor Keywords

Parameters:
- `competitor_id` in path (required)

Responses: 200, 422

## Request body schemas

### CompetitorCreate

Body for creating a competitor.

- `name`: `string` (required)
- `website`: `string | null` (optional) — Raw user input (may include path/query). CompetitorService normalizes via normalize_website() to a scheme+host origin (<=500 chars) before storage.
- `description`: `string | null` (optional)
- `aliases`: `array<string>` (optional)
- `icon_url`: `string | null` (optional)

### CompetitorUpdate

Body for partial competitor update.

- `name`: `string | null` (optional)
- `website`: `string | null` (optional) — Raw user input (may include path/query). CompetitorService normalizes via normalize_website() to a scheme+host origin (<=500 chars) before storage.
- `description`: `string | null` (optional)
- `aliases`: `array<string> | null` (optional)
- `icon_url`: `string | null` (optional)

### SuggestCompetitorsRequest

Optional overrides for :suggest. All fields default to brand-derived values.

- `query`: `string | null` (optional)
- `product_name`: `string | null` (optional)
- `product_description`: `string | null` (optional)
