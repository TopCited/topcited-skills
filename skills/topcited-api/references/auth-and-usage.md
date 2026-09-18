# Auth & usage

## What this is (tell the user)
Every action in a visibility session runs as you, authenticated by a
personal API key. Before spending on anything expensive, we check your
remaining credit balance so you're never surprised by a blocked request.
This guide covers how a session proves who it is, how to check what's left
on the plan, and what it means when a call is refused for running out of
credits.

## When the workflow uses it
Cross-cutting: every stage authenticates the same way, and `GET
/users/me/usage` should be checked before any credit-hungry step — most
importantly before Stage 6 (`pillar_clusters`, 62 T-coins/run) and before
triggering a large Stage 2/8 monitoring run (1 T-coin per query per engine —
see [monitoring.md](monitoring.md)).

## Operations
| I want to… | Call | Reference |
|---|---|---|
| Smoke-test the session / get the current user | `GET /api/v1/users/me` | [endpoints/users.md](endpoints/users.md) |
| Check remaining credit balance per feature | `GET /api/v1/users/me/usage` | [endpoints/users.md](endpoints/users.md) |
| Check T-coin balance broken down by bucket | `GET /api/v1/users/me/coin-balance` | [endpoints/users.md](endpoints/users.md) |
| Check the caller's own API-key status | `GET /api/v1/users/me/api-key` | [endpoints/users.md](endpoints/users.md) |
| See in-flight async work across all features | `GET /api/v1/users/me/active-work` | [endpoints/users.md](endpoints/users.md) |
| List background tasks (generic) | `GET /api/v1/tasks` | [endpoints/tasks.md](endpoints/tasks.md) |
| Get one background task by id | `GET /api/v1/tasks/{task_id}` | [endpoints/tasks.md](endpoints/tasks.md) |

`GET /api/v1/auth/me` also returns the current user and exists for
session-authenticated UI clients. For an API-key caller, `GET /users/me` is
the one to use. The rest of the `/auth` surface (login, register, password
reset, invites) is UI-facing and out of scope for an API-key agent — do not
call it.

## Example
Every call carries `Authorization: Bearer $TOPCITED_API_KEY`. The
`scripts/tc-api.sh` helper next to this skill's `SKILL.md` does that for you,
so you never construct the header by hand. The key is created by the account
owner in the TopCited app under **Settings → Profile → API Key** and starts
with the `tc_` prefix.

Smoke-test a session at the start of every run:
```bash
scripts/tc-api.sh GET /api/v1/users/me
```
A `200` with the user's profile confirms the key is live; a non-2xx means
the key is missing, revoked, or expired — stop and tell the user rather than
proceeding into a workflow that will fail partway through.

Before an expensive step, check the balance and say something concrete:
```bash
scripts/tc-api.sh GET /api/v1/users/me/usage
```
Returns one `UsageSnapshot` (`feature`, `used`, `limit`, `reset_period`,
`reset_at`) per plan feature. For the shared T-coin pool specifically (which
is what most features draw from — see the cost notes in each other guide),
`GET /api/v1/users/me/coin-balance` is more precise: it separates plan
allowance, carryover, bonus, and purchased balance and sums them into
`total_available` — that total is the number to tell the user before a
62-credit pillar/cluster run or a large monitoring run.

## UI links
- `{TOPCITED_UI_URL}/settings/billing` — credit balance, plan, and the
  upgrade flow — this is where to send a user who hits a 402.
- `{TOPCITED_UI_URL}/settings/profile` — the user's own API-key status and
  session management. This is where a human goes to create, see or regenerate
  the key you are authenticating with.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
Everything in this guide is a free read — checking who you are, what you've
used, or your balance never spends a credit. The point of `GET /me/usage`
and `GET /me/coin-balance` is precisely to let you check for free *before*
calling something that isn't.

**What a 402 means, everywhere in this API:** every metered endpoint across
every other guide raises the same `QuotaExceededError`, which the global
exception handler maps to HTTP 402 Payment Required.
When you see a 402, the correct response is always the same: don't retry the
call as-is, explain to the user in plain language that their plan's included
usage for that feature is used up, and point them at
`{TOPCITED_UI_URL}/settings/billing` to add credits or upgrade. Do not try
to work around a 402 by retrying, batching smaller, or calling a different
endpoint that does the same thing — the balance is genuinely exhausted.

## Failure modes
- Missing/invalid/revoked/expired `TOPCITED_API_KEY` → every call fails, not
  just one endpoint. `GET /users/me` at session start is the fastest way to
  catch this before the user has invested time in a longer workflow.
- 402 anywhere → see "What a 402 means" above. It is not specific to one
  feature; expect it on any of the metered calls documented across
  [content-pillar-cluster.md](content-pillar-cluster.md),
  [monitoring.md](monitoring.md), [recommendations.md](recommendations.md),
  [seo-geo-analysis.md](seo-geo-analysis.md), [reports.md](reports.md), and
  the `sci_defense` check in [audit.md](audit.md).
- `POST /users/me/api-key` (regenerate) is still being rolled out: accounts
  that are not enabled for it get a 403 with "API keys are coming soon for
  your account." Regenerating also **revokes the key you are currently using**,
  so never call it mid-session — leave key management to the human in
  `{TOPCITED_UI_URL}/settings/profile`.
- `GET /tasks` / `GET /tasks/{task_id}` cover generic background-task
  tracking, but most features in this API have their **own** dedicated
  polling endpoint instead (pillar/cluster's `GET /runs/{task_id}`,
  monitoring's `GET /runs`, the recommendation runs'
  `.../latest` endpoints, geo-optimizer's `GET /runs/{run_id}`) — check the
  relevant feature guide first; fall back to the generic `/tasks` endpoints
  only if a feature-specific one isn't documented.
