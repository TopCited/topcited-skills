<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# optimization

### POST /api/v1/optimization/core/submit

Submit Core

Submit a CORE optimization request.

The CORE strategy is always processed asynchronously via a background task.
It creates a content submission and a pipeline Task that tracks the
iterative Generator -> Synthesizer -> Optimizer loop.

One ``optimizations`` quota unit is spent at route entry — same as the
synchronous ``/submissions`` endpoint. The quota ref_id is wired onto the
Taskiq message so UsageRefundMiddleware refunds it on terminal task
failure. CORE has no synchronous processing path, so (mirroring ``submit``)
RateLimitError / ValidationError are user errors and keep the spend.

Request body: `CORESubmissionCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 202, 422

### GET /api/v1/optimization/strategies

List Strategies

List all available optimization strategies.

Responses: 200

### GET /api/v1/optimization/submissions

List Submissions

List content submissions for the authenticated customer.

Parameters:
- `skip` in query
- `limit` in query

Responses: 200, 422

### POST /api/v1/optimization/submissions

Submit

Submit content for optimization.

Small submissions (<=2000 words) are processed synchronously.
Larger submissions are queued for background processing.
Task dispatch happens in a background task after the response (and DB
commit) completes, avoiding a race condition where workers see no row.

One ``optimizations`` quota unit is spent at route entry. For async
submissions the UsageRefundMiddleware refunds on terminal task failure.
For sync submissions this route refunds on InternalError / ExternalServiceError /
LLMError (internal failures). ValidationError is user error and is NOT refunded.

Request body: `SubmissionCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### POST /api/v1/optimization/submissions/from-seo

Submit From Seo

Create an optimization submission from Website Optimization (SEO) extracted content.

Request body: `SeoOptimizationHandoffCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 201, 422

### DELETE /api/v1/optimization/submissions/{submission_id}

Delete Submission

Hard-delete a content submission.

Parameters:
- `submission_id` in path (required)

Responses: 204, 422

### GET /api/v1/optimization/submissions/{submission_id}

Get Submission

Get a single content submission by ID.

Parameters:
- `submission_id` in path (required)

Responses: 200, 422

### GET /api/v1/optimization/submissions/{submission_id}/download

Download Submission

Download optimized content as a document. Not yet implemented.

Parameters:
- `submission_id` in path (required)

Responses: 200, 422

### POST /api/v1/optimization/submissions/{submission_id}/publish

Mark Published

Mark a submission as published (Phase 2 hook).

Parameters:
- `submission_id` in path (required)

Responses: 200, 422

## Request body schemas

### CORESubmissionCreate

Schema for creating a CORE optimization submission.

Cross-field validation ensures target_item_id refers to an actual
candidate, and content_strategy is one of the supported values.

- `query`: `string` (required)
- `candidates`: `array<CORECandidateItem>` (required)
- `target_item_id`: `string` (required)
- `output_mode`: `"advice" | "rewrite"` (optional, default `"rewrite"`)
- `content_strategy`: `string` (optional, default `"reasoning"`)
- `max_iterations`: `integer` (optional, default `10`)
- `target_k`: `integer` (optional, default `1`)

### SeoOptimizationHandoffCreate

Create an optimization submission sourced from Website Optimization (SEO).

- `output_mode`: `"advice" | "rewrite"` (optional, default `"rewrite"`)
- `url_analysis_id`: `string (uuid) | null` (optional)
- `site_id`: `string (uuid) | null` (optional)
- `page_id`: `string (uuid) | null` (optional)
- `audit_run_id`: `string (uuid) | null` (optional)

### SubmissionCreate

Schema for creating a new content submission.

- `input_type`: `string` (optional, default `"text"`)
- `input_content`: `string` (required)
- `output_mode`: `"advice" | "rewrite"` (required)
- `strategy_id`: `string (uuid) | null` (optional)
- `vertical`: `string | null` (optional)
- `category`: `string | null` (optional)

### CORECandidateItem

A single candidate item for the CORE optimization pipeline.

- `id`: `string` (required)
- `title`: `string` (required)
- `text`: `string` (required)
