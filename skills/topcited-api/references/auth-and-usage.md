# Auth & usage

## What this is (tell the user)
Every action in a visibility session runs as you, authenticated by a personal
API key that carries full rights over your account — it's a credential to guard,
not a scoped read token. Before spending on anything expensive, we check your
remaining credit balance so you're never surprised by a blocked request.

## When the workflow uses it
Cross-cutting: every stage starts from a signed-in CLI, and `topcited usage`
should be checked before any credit-hungry step — most importantly before
Stage 6 (`pillar_clusters`, the priciest operation, whose cost scales with page
count — see [content-pillar-cluster.md](content-pillar-cluster.md)) and before a
large Stage 2/8 monitoring run (1 T-coin per query per engine — see
[monitoring.md](monitoring.md)).

## Commands
| I want to… | Command |
|---|---|
| Sign in (device flow) | `topcited auth login` (`--no-wait` then `--continue` without a live terminal) |
| Use an existing key (CI) | `TOPCITED_API_KEY=tc_…` or `echo "$KEY" \| topcited auth login --with-token` |
| Who am I, plan, key expiry | `topcited auth status` |
| Print the key for another tool | `topcited auth token --show` (bare key only, so `$(…)` works) |
| Forget this host's key | `topcited auth logout` |
| Plan, T-coin balance, quotas, monitoring forecast | `topcited usage` |
| Diagnose config / connectivity / version skew | `topcited doctor` |
| List background tasks | `topcited tasks list [--status] [--type]` · `topcited tasks show <id> [--wait]` |
| List this account's API keys (prefix, expiry, last use) | `topcited api /users/me/api-keys` |
| T-coin balance by bucket | `topcited api /users/me/coin-balance` |

## How sign-in behaves
- `auth login` prints a URL and a short code and waits while the user approves
  in the browser. It only opens a browser itself on a real terminal (not over
  SSH, in CI, or on headless Linux). In JSON mode the prompt arrives as a
  `{"device_authorization": …}` line on stderr — show the URL and code to the
  user verbatim.
- Approval mints an ordinary key named `topcited-cli on <hostname>`; logging in
  again on the same machine replaces it. Keys live in
  `~/.config/topcited/credentials.json` (mode 0600), one per API host.
  `TOPCITED_API_KEY` beats the stored key; `TOPCITED_BASE_URL` / `--base-url`
  picks the API host.
- Keys **expire 90 days** after creation; the CLI warns with fewer than 14 days
  left, and `auth status` shows the date. A key that worked last month can fail
  today with nothing else changed.
- An account can hold **5 active keys**. Sign-in at the cap exits 6 with a hint
  to revoke one in **Settings → Profile → API keys**.
- **A key can't manage keys.** Creating or revoking keys, or changing
  email/password, needs a signed-in browser session (an API key gets 403).
  `auth logout` only forgets the local copy — to revoke it, send the human to
  `{TOPCITED_UI_URL}/settings/profile`. Never try to rotate your own key
  mid-session.

## Reading the balance
`topcited usage` combines the plan, the T-coin balance, per-feature quotas and
this period's monitoring forecast in one view — the number to quote before a
spend is the T-coin `total_available`. The raw breakdown
(`topcited api /users/me/coin-balance`) separates plan allowance, carryover,
bonus and purchased balance; `topcited api /users/me/usage` gives one row per
plan feature (`feature`, `used`, `limit`, `reset_period`, `reset_at`).

## UI links
- `{TOPCITED_UI_URL}/settings/billing` — balance, plan, upgrade — where to send a
  user who hits exit 4.
- `{TOPCITED_UI_URL}/settings/profile` — API keys and sessions: create, list or
  revoke keys, including the one you're using.

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
Everything in this guide is free — checking who you are, what you've used, or
your balance never spends a credit. That's the point: check for free *before*
calling something that isn't.

**What exit 4 / HTTP 402 means, everywhere:** the plan's included usage for
that feature is used up. Don't retry as-is, don't batch smaller, don't call a
different command that does the same thing — the balance is genuinely
exhausted. Explain it in plain language and point the user at
`{TOPCITED_UI_URL}/settings/billing`.

## Failure modes
- Exit 3 on any command → the key is missing, expired or revoked; every command
  will fail the same way. Check `topcited auth status` (expiry date) before
  assuming an outage, then re-run `auth login` or ask the user for a fresh key.
- Exit 4 → see above. Expect it on any metered command across
  [monitoring.md](monitoring.md), [recommendations.md](recommendations.md),
  [seo-geo-analysis.md](seo-geo-analysis.md), [reports.md](reports.md),
  [content-pillar-cluster.md](content-pillar-cluster.md) and
  [ai-usage-detection.md](ai-usage-detection.md).
- An HTML page instead of JSON from `topcited api` → the base URL points at the
  web app, not the API. `topcited doctor` shows which base URL is in use and
  where it came from.
- `tasks` covers generic background tasks, but most features have their own job
  shape — use the feature command's `--wait` (or `topcited wait <job>`) rather
  than polling `/tasks` by hand.
