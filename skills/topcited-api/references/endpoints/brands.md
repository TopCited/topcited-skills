<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# brands

### GET /api/v1/brands

List Brands

List the current user's brands, newest first.

Responses: 200

### POST /api/v1/brands

Create Brand

Create a brand for the current user.

This is the onboarding submit. When the user has no active brand, the
new brand becomes active.

Request body: `BrandCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### GET /api/v1/brands/limits

Get Brand Limits

Return the current user's brand count and plan brand cap.

Cardinality caps are deliberately excluded from ``/users/me/usage``
(they come from the entity table, not the usage ledger), so the brand
cap is surfaced here for the UI to gate "Add brand" client-side.

Responses: 200

### DELETE /api/v1/brands/{brand_id}

Delete Brand

Delete a brand owned by the current user.

Competitors are deleted with the brand; query sets, reports, SEO data
and content submissions are detached (their ``brand_id`` becomes NULL).
The last remaining brand cannot be deleted (400). If the deleted brand
was active, the newest remaining brand becomes active.

Parameters:
- `brand_id` in path (required)

Responses: 204, 422

### PATCH /api/v1/brands/{brand_id}

Update Brand

Rename a brand and/or set its website.

Parameters:
- `brand_id` in path (required)

Request body: `BrandUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### GET /api/v1/brands/{brand_id}/competitor-keywords/dashboard

Get Competitor Keywords Dashboard

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### GET /api/v1/brands/{brand_id}/competitor-keywords/overlap

Get Competitor Keyword Overlap

Parameters:
- `brand_id` in path (required)

Responses: 200, 422

### POST /api/v1/brands/{brand_id}/competitor-keywords/scan-all

Scan All Competitor Keywords

Parameters:
- `brand_id` in path (required)

Responses: 202, 422

## Request body schemas

### BrandCreate

Body for POST /brands — the onboarding submit.

- `name`: `string` (required)
- `website`: `string | null` (optional)

### BrandUpdate

Body for PATCH /brands/{id} — rename and/or website change.

Both fields are optional, but at least one must be provided.

- `name`: `string | null` (optional)
- `website`: `string | null` (optional)
