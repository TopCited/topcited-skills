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

Users can update their own profile (email, full_name).
Role changes require admin privileges — for an API-key principal, the key
itself must also carry the admin grant (keys never inherit the owner's role).

Request body: `UserUpdate` — fields under [Request body schemas](#request-body-schemas)

Responses: 200, 422

### GET /api/v1/users/me/active-work

Get My Active Work

Return in-flight async work across monitoring, optimization, content, and SEO.

Responses: 200

### GET /api/v1/users/me/api-key

Get My Api Key Status

Report the caller's newest active (non-revoked, non-expired) API key.

Open to any authenticated principal — unlike POST, no admin gate:
checking whether you already have a key doesn't need elevated access.

Responses: 200

### POST /api/v1/users/me/api-key

Regenerate My Api Key

Mint a fresh self-service API key, revoking any of the caller's existing ones.

Gated: accounts not yet enabled for self-service keys are rejected with a
403. One active personal key per user — minting always revokes whatever was
active before, including the key used to make this call.

Responses: 200

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

Schema for updating a user.

- `email`: `string (email) | null` (optional)
- `password`: `string | null` (optional)
- `full_name`: `string | null` (optional)
- `is_active`: `boolean | null` (optional)
- `role`: `"admin" | "user" | null` (optional)
- `active_brand_id`: `string (uuid) | null` (optional)
