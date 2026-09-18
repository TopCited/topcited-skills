<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# seo

### GET /api/v1/seo/analyses

List Url Analyses

List the current user's saved URL analyses, newest first.

Parameters:
- `skip` in query
- `limit` in query

Responses: 200, 422

### DELETE /api/v1/seo/analyses/{analysis_id}

Delete Url Analysis

Delete one of the current user's saved URL analyses.

Parameters:
- `analysis_id` in path (required)

Responses: 204, 422

### GET /api/v1/seo/analyses/{analysis_id}

Get Url Analysis

Get one saved URL analysis, including the full signals/issues payload.

Parameters:
- `analysis_id` in path (required)

Responses: 200, 422

### POST /api/v1/seo/analyses/{analysis_id}/ai-visibility

Request Ai Visibility

Re-run the AI-visibility check for an analysis (manual retry on failure).

The check runs automatically on every analyze (see ``analyze_url``), so this
endpoint exists only as a free retry for the error case. It is NOT separately
charged — the analyze already spent one ``url_analyses`` unit. If a verdict is
already pending or done it returns the row unchanged (no re-dispatch).

Parameters:
- `analysis_id` in path (required)

Responses: 200, 422

### POST /api/v1/seo/analyze

Analyze Url

Fetch a URL, extract SEO signals, and return an AI-written analysis.

Authenticated requests spend one ``url_analyses`` unit (subject to the
plan's cap) and have the analysis persisted to their history, so it
survives a page refresh and appears under ``/seo/analyses``. They also kick
off the AI-visibility check automatically: the row is saved with
``ai_visibility = pending`` and the background ``assess_ai_visibility`` task
is dispatched after commit, which renders the page and (if AI can't see it)
caps the score. The frontend polls until the verdict lands. No separate
charge — the visibility check is part of this analyze. Anonymous requests are
allowed, spend no quota, are not persisted, and run no visibility check.

Request body: `SeoAnalyzeRequest` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### PATCH /api/v1/seo/issues/{issue_id}

Update Issue

Update the fixed_status of a SEO issue (open / fixed / ignored).

Parameters:
- `issue_id` in path (required)

Request body: `SeoIssueUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### GET /api/v1/seo/site-audit/pages

List Site Audit Pages

Per-page audit cards for the Overview Site Audit row.

One card per distinct analyzed URL — each URL's latest saved analysis —
scoped to the caller's active brand (analyses saved before brands
existed are included). Returns ``{path, domain, score, checked_at,
high, medium, low}`` per page plus the total distinct-URL count.

Parameters:
- `sort` in query
- `limit` in query
- `offset` in query

Responses: 200, 422

### GET /api/v1/seo/sites

List Sites

List all registered sites for the authenticated user.

Parameters:
- `skip` in query
- `limit` in query

Responses: 200, 422

### POST /api/v1/seo/sites

Create Site

Register a new website for SEO auditing.

Request body: `SiteCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### DELETE /api/v1/seo/sites/{site_id}

Delete Site

Hard-delete a site and all associated pages, audit runs, and issues.

Parameters:
- `site_id` in path (required)

Responses: 204, 422

### GET /api/v1/seo/sites/{site_id}

Get Site

Get a single site by ID.

Parameters:
- `site_id` in path (required)

Responses: 200, 422

### PATCH /api/v1/seo/sites/{site_id}

Update Site

Update site metadata.

Parameters:
- `site_id` in path (required)

Request body: `SiteUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### GET /api/v1/seo/sites/{site_id}/audit-runs

List Audit Runs

List all audit runs for a site, newest first.

Parameters:
- `site_id` in path (required)
- `skip` in query
- `limit` in query

Responses: 200, 422

### POST /api/v1/seo/sites/{site_id}/audit-runs

Trigger Audit

Trigger a new SEO audit for a site.

Creates a SeoAuditRun with status=pending and dispatches the crawl
task via Taskiq after the DB transaction commits.  The Taskiq message
carries ``user_id`` and ``feature`` labels (and uses ``spend.ref_id`` as
the message task_id) so UsageRefundMiddleware can refund on terminal failure.

Parameters:
- `site_id` in path (required)

Responses: 202, 422

### GET /api/v1/seo/sites/{site_id}/audit-runs/{run_id}

Get Audit Run

Get a single audit run, including its summary.

Parameters:
- `site_id` in path (required)
- `run_id` in path (required)

Responses: 200, 422

### GET /api/v1/seo/sites/{site_id}/audit-runs/{run_id}/issues

List Issues

List all SEO issues for an audit run.

Parameters:
- `site_id` in path (required)
- `run_id` in path (required)
- `skip` in query
- `limit` in query

Responses: 200, 422

### GET /api/v1/seo/sites/{site_id}/pages

List Pages

List all pages crawled for a site.

Parameters:
- `site_id` in path (required)
- `skip` in query
- `limit` in query

Responses: 200, 422

### GET /api/v1/seo/sites/{site_id}/pages/{page_id}

Get Page

Get a single crawled page by ID.

Parameters:
- `site_id` in path (required)
- `page_id` in path (required)

Responses: 200, 422

## Request body schemas

### SeoAnalyzeRequest

- `url`: `string` (required)

### SeoIssueUpdate

- `fixed_status`: `string` (required)

### SiteCreate

- `domain`: `string` (required)
- `sitemap_url`: `string | null` (optional)
- `robots_url`: `string | null` (optional)
- `cms_type`: `string | null` (optional)
- `industry`: `string | null` (optional)
- `target_country`: `string | null` (optional)
- `target_language`: `string | null` (optional)

### SiteUpdate

- `domain`: `string | null` (optional)
- `sitemap_url`: `string | null` (optional)
- `robots_url`: `string | null` (optional)
- `cms_type`: `string | null` (optional)
- `industry`: `string | null` (optional)
- `target_country`: `string | null` (optional)
- `target_language`: `string | null` (optional)
