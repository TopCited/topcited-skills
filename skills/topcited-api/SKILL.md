---
name: topcited-api
description: Call the TopCited API (brands, competitors, site audits, monitoring, keyword/prompt recommendations, SEO/GEO analysis, pillar-cluster content, reports) with a personal API key. Use whenever the task involves reading or changing data in a TopCited account, or measuring a brand's visibility in search engines and AI assistants.
---

# TopCited API

TopCited measures and improves how visible a brand is in search engines (SEO) and
in AI assistants like ChatGPT, Claude, Gemini and Perplexity (GEO). This skill is
how an agent drives that platform over HTTP.

## Setup

| Variable | Required | Default |
|---|---|---|
| `TOPCITED_API_KEY` | yes | — |
| `TOPCITED_BASE_URL` | no | `https://api.topcited.ai` |
| `TOPCITED_UI_URL` | no | `https://topcited.ai` |

Get a key in the TopCited app under **Settings → Profile → API Key**. It is shown
once, starts with `tc_`, and acts as the signed-in user with full rights over
that account — generating a new one revokes the old one, and a key **expires 90
days** after it is generated. Key availability is currently limited; if the app
answers *"API keys are coming soon for your account"*, that account is not
enabled and the user should contact TopCited.

`TOPCITED_UI_URL` is only used to build deep links you show the user. It is a
separate host from the API — never derive one from the other. A call sent to the
UI host returns the web app's HTML instead of JSON, so an HTML response to an API
call means the base URL is wrong, not that the endpoint is missing.

## Making a call

Every call is `Authorization: Bearer $TOPCITED_API_KEY` against
`$TOPCITED_BASE_URL`:

```bash
curl -sS -H "Authorization: Bearer $TOPCITED_API_KEY" \
     -H "Content-Type: application/json" \
     "$TOPCITED_BASE_URL/api/v1/users/me"
```

A `scripts/tc-api.sh` helper sits next to this file and wraps that (it also turns
HTTP >= 400 into a non-zero exit):

```bash
scripts/tc-api.sh GET  /api/v1/users/me
scripts/tc-api.sh POST /api/v1/brands -d '{"name":"Acme","website":"https://acme.com"}'
```

**Always smoke-test with `GET /api/v1/users/me` before starting real work** — a
missing, revoked or expired key fails every subsequent call, and you want to find
that out before the user has invested time.

## Where to read next

Read the guide for a feature *before* calling it — the guides carry the when/why,
the worked examples, the credit cost, the UI deep-link pattern and the failure
modes. `references/endpoints/` is the generated schema reference: exact paths,
parameters and request-body fields, expanded model by model.

| Task | Guide | Schema |
|---|---|---|
| Who am I, what's my balance, what does a 402 mean | [references/auth-and-usage.md](references/auth-and-usage.md) | `users`, `auth`, `tasks` |
| Create / read the brand everything else hangs off | [references/brands.md](references/brands.md) | `brands` |
| Find and track competitors | [references/competitors.md](references/competitors.md) | `competitors` |
| Site audit: leads, health, manipulation check | [references/audit.md](references/audit.md) | `audit-requests`, `sci-defense` |
| Measure visibility across AI assistants over time | [references/monitoring.md](references/monitoring.md) | `monitoring` |
| Keyword, prompt and content-sentence recommendations | [references/recommendations.md](references/recommendations.md) | `keywords`, `prompts`, `content-sentences` |
| On-page SEO and GEO analysis / optimization | [references/seo-geo-analysis.md](references/seo-geo-analysis.md) | `seo`, `geo-optimizer`, `optimization` |
| Pillar/cluster content generation | [references/content-pillar-cluster.md](references/content-pillar-cluster.md) | `pillar-cluster` |
| Export a report for the user | [references/reports.md](references/reports.md) | `reports` |

## Rules that apply to every call

1. **Check the balance before spending.** Many operations consume T-coins (TopCited
   credits). Each guide has a Cost section. `GET /api/v1/users/me/coin-balance` is
   free and tells you what is left — call it before anything expensive, and tell
   the user the number before you spend it.
2. **HTTP 402 means credits are exhausted.** Do not retry, do not batch smaller, do
   not reach for a different endpoint that does the same thing. Explain it plainly
   and point the user at `{TOPCITED_UI_URL}/settings/billing`.
3. **Confirm before anything that creates, changes or costs.** Read-only lookups
   are exempt.
4. **Long-running work is asynchronous.** Most features return a run/task id and
   have their *own* polling endpoint (see the feature guide) rather than the
   generic `/api/v1/tasks`.
5. **Show your work.** After each step, give the user the matching
   `{TOPCITED_UI_URL}/...` deep link from the guide so they can see it themselves.
   The default locale is unprefixed — do not add `/en/`.

For the judgment calls behind any of this — what to actually change on a site, and
why — use the `seo-geo` skill. For an end-to-end engagement, use the
`visibility-workflow` skill.
