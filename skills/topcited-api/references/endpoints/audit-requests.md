<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# audit-requests

### POST /api/v1/audit-requests

Create Audit Request

Public endpoint — accepts a lead submission from the landing page form.
Submissions are rate-limited per IP.

Request body: `AuditRequestCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

## Request body schemas

### AuditRequestCreate

Incoming payload for a lead-form submission.

- `email`: `string (email)` (required)
- `name`: `string` (required)
- `industry`: `string | null` (optional)
- `needs`: `string | null` (optional)
- `budget`: `string | null` (optional)
- `source_page`: `string | null` (optional)
