<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# users

### GET /api/v1/users/avatar/{user_id}

Get Avatar

Get user avatar image.

Parameters:
- `user_id` in path (required)

Responses: 200, 422

### GET /api/v1/users/me

Read Current User

Get current user.

Returns the authenticated user's profile including their role.

Responses: 200

### PATCH /api/v1/users/me

Update Current User

Update current user.

Users can update their own profile (email, full_name, password).
`role` is not part of UserUpdate, so it can never be set here — a `role`
key in the body is ignored.

Changing `email`, `password` or `is_active` requires a signed-in session:
called with an API key, those fields are rejected with a 403. Other fields
(`full_name`, `active_brand_id`) can be changed with a key.

Request body: `UserUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### GET /api/v1/users/me/active-work

Get My Active Work

Return in-flight async work across monitoring, optimization, content, and SEO.

Responses: 200

### GET /api/v1/users/me/api-key

Get My Api Key Status

Deprecated: use `GET /users/me/api-keys`.

Report the caller's newest active (non-revoked, non-expired) API key.

Responses: 200

### POST /api/v1/users/me/api-key

Regenerate My Api Key

Deprecated: use `POST /users/me/api-keys`.

Responses: 200

### GET /api/v1/users/me/api-keys

List My Api Keys

List the caller's non-revoked API keys (expired ones included), newest first.
Works with an API key. Each entry: `id`, `prefix`, `is_admin`, `created_at`,
`expires_at`, `last_used_at` — the secret itself is never returned.

Responses: 200

### POST /api/v1/users/me/api-keys

Create My Api Key

Mint a new API key for the caller. The raw key is returned exactly once.

Open to every signed-in user on any plan: plan quotas, not the mint,
decide what the key can do. The key carries the owner's role (never
admin for a customer) and expires after 90 days. 409 at the active-key
cap (5); 403 when called with an API key.

Responses: 201

### DELETE /api/v1/users/me/api-keys/{key_id}

Revoke My Api Key

Revoke one of the caller's keys. 404 if it isn't theirs or is already
revoked. 403 when called with an API key.

Parameters:
- `key_id` in path (required)

Responses: 204, 422

### POST /api/v1/users/me/avatar

Upload Avatar

Upload or replace avatar image for the current user.

Responses: 200, 422

### GET /api/v1/users/me/coin-balance

Get My Coin Balance

Return the user's T-coin balance broken down by bucket.

Buckets, in the meter's fixed draw order: plan allowance (period-windowed
pool), carryover, bonus, purchased. ``bundle_balance`` is kept as an alias
of ``purchased_balance`` for API compatibility.

Responses: 200

### GET /api/v1/users/me/dashboard/metric-highlights

Get My Metric Highlights

Return top metric highlight charts for the dashboard.

Responses: 200

### GET /api/v1/users/me/saved-time

Get My Saved Time

Return lifetime and last-30-days saved-hours totals for the current user.

Responses: 200

### GET /api/v1/users/me/tutorials

Get My Tutorials

Return the current user's tutorial seen-state map.

Keys absent from ``seen`` are unseen and should auto-play on the
matching feature page.

Responses: 200

### POST /api/v1/users/me/tutorials/{key}

Record My Tutorial View

Record a monotonic tutorial-view transition.

Idempotent: an illegal transition (e.g. completed->exited) is a no-op
and the effective stored status is returned. Never errors on transition
legality, so the frontend can fire-and-forget.

Parameters:
- `key` in path (required)

Request body: `TutorialViewUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### POST /api/v1/users/me/upgrade-requests

Submit Upgrade Request

Create or bump an upgrade request for (user, feature).

Idempotent on ``(user_id, feature)`` — re-submitting the same feature
bumps ``triggered_at`` and updates ``intent_text`` if provided.

Request body: `UpgradeRequestCreate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### GET /api/v1/users/me/usage

Get My Usage

Return one UsageSnapshot per feature on the user's plan.

Counter features use ``UsageMeter.get_usage``; the monitoring budget uses
a projected monthly run count from the user's active query-set configuration.

Responses: 200

### TutorialViewUpdate

Request body for POST /users/me/tutorials/{key}.

- `status`: `"exited" | "completed"` (required)
- `step_index`: `integer | null` (optional)

### UpgradeRequestCreate

Body for POST /me/upgrade-requests.

- `feature`: `string` (required)
- `intent_text`: `string | null` (optional)

### UserUpdate

Schema for a user updating their own profile.

- `email`: `string (email) | null` (optional)
- `password`: `string | null` (optional)
- `full_name`: `string | null` (optional)
- `is_active`: `boolean | null` (optional)
- `active_brand_id`: `string (uuid) | null` (optional)
