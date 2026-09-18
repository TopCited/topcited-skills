<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# sci-defense

### POST /api/v1/sci-defense/analyze

Analyze Url

Fetch a URL and run the SCI-Defense pipeline on its content.

Returns a verdict (clean/suspicious/manipulated) with per-dimension
scores from the PPL, SIS, and ICD detectors.

One sci_defense quota unit is spent at route entry via enforce_quota.
On pipeline failure the spend is refunded; SSRF/422 user errors are not.

Request body: `SCIDefenseRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### POST /api/v1/sci-defense/public-analyze

Public Analyze Url

Unauthenticated URL analysis with per-IP daily rate limit.

Rate-limited to SCI_DEFENSE_PUBLIC_DAILY_LIMIT analyses per IP per UTC day.
Uses the same fetch+pipeline as the authenticated endpoint.

Request body: `SCIDefenseRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

## Request body schemas

### SCIDefenseRequest

- `url`: `string (uri)` (required) — URL of the page to analyze
