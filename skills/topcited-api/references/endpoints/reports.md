<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# reports

### GET /api/v1/reports/

List Reports

List reports for the authenticated customer.

Parameters:
- `skip` in query
- `limit` in query

Responses: 200, 422

### POST /api/v1/reports/generate

Generate Report

Generate a new report for the authenticated customer.

One ``reports`` quota unit (10 T-coins) is spent at route entry.
On internal failure the spend is refunded; user/validation errors keep
the spend so callers cannot probe the service for free.

Request body: `ReportCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### GET /api/v1/reports/{report_id}

Get Report

Get a single report by ID.

Parameters:
- `report_id` in path (required)

Responses: 200, 422

### GET /api/v1/reports/{report_id}/download/html

Download Html

Download report as a self-contained HTML file.

Parameters:
- `report_id` in path (required)
- `theme` in query

Responses: 200, 422

### GET /api/v1/reports/{report_id}/download/pdf

Download Pdf

Download report as PDF (rendered via Playwright).

Parameters:
- `report_id` in path (required)
- `theme` in query

Responses: 200, 422

### GET /api/v1/reports/{report_id}/view

View Report

Return rendered HTML view of the report.

Parameters:
- `report_id` in path (required)
- `theme` in query

Responses: 200, 422

## Request body schemas

### ReportCreate

Schema for requesting a new report.

- `report_type`: `"geo_audit"` (optional, default `"geo_audit"`)
- `params`: `object | null` (optional)
