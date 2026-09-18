# Recommendations (keywords, prompts, content sentences)

## What this is (tell the user)
Three related tools that each ask an AI to suggest something the brand
should be tracking or saying, based on what we already know about the brand
and its competitors: **keyword recommendations** (search terms worth
targeting), **prompt recommendations** (the conversational questions people
ask AI assistants, worth adding to monitoring), and **content sentences**
(specific factual statements about the brand worth planting in content so AI
assistants can quote them back accurately). All three follow the same
pattern: start an async run, poll for the result, then accept the
suggestions you want one at a time — nothing is added to the brand's real
list until you accept it.

## When the workflow uses it
Supports Stage 3 (Competitor research) and Stage 2/8 (Baseline & ongoing
monitoring): keyword and prompt recommendations turn competitor and brand
research into a starting query set instead of the user inventing questions
from scratch. Content sentences support Stage 6 (Content strategy &
generation): specific claims worth working into pillar/cluster drafts so AI
assistants have something quotable and accurate to cite.

## Operations

### Keyword recommendations
| I want to… | Call | Reference |
|---|---|---|
| List the brand's keywords (saved + staged) | `GET /api/v1/brands/{brand_id}/keywords` | [endpoints/keywords.md](endpoints/keywords.md) |
| Manually add a keyword (free) | `POST /api/v1/brands/{brand_id}/keywords` | [endpoints/keywords.md](endpoints/keywords.md) |
| Start a keyword recommendation run | `POST /api/v1/brands/{brand_id}/keywords:recommend` | [endpoints/keywords.md](endpoints/keywords.md) |
| Poll the latest recommendation run | `GET /api/v1/brands/{brand_id}/keyword-recommendation-runs/latest` | [endpoints/keywords.md](endpoints/keywords.md) |
| Accept a staged recommendation | `POST /api/v1/brands/{brand_id}/keywords/{keyword_id}:accept` | [endpoints/keywords.md](endpoints/keywords.md) |
| Refresh difficulty/volume/CPC for the brand's keywords | `POST /api/v1/brands/{brand_id}/keywords:difficulty` | [endpoints/keywords.md](endpoints/keywords.md) |
| Delete a keyword | `DELETE /api/v1/brands/{brand_id}/keywords/{keyword_id}` | [endpoints/keywords.md](endpoints/keywords.md) |

### Prompt recommendations
| I want to… | Call | Reference |
|---|---|---|
| List the brand's prompt library (saved + staged) | `GET /api/v1/brands/{brand_id}/prompts` | [endpoints/prompts.md](endpoints/prompts.md) |
| Manually add a prompt (free) | `POST /api/v1/brands/{brand_id}/prompts` | [endpoints/prompts.md](endpoints/prompts.md) |
| Start a prompt recommendation run | `POST /api/v1/brands/{brand_id}/prompts:recommend` | [endpoints/prompts.md](endpoints/prompts.md) |
| Poll the latest recommendation run | `GET /api/v1/brands/{brand_id}/prompt-recommendation-runs/latest` | [endpoints/prompts.md](endpoints/prompts.md) |
| Accept a staged recommendation | `POST /api/v1/brands/{brand_id}/prompts/{prompt_id}:accept` | [endpoints/prompts.md](endpoints/prompts.md) |
| Push a library prompt into one or more Topics (monitoring query sets) | `POST /api/v1/brands/{brand_id}/prompts/{prompt_id}:add-to-topics` | [endpoints/prompts.md](endpoints/prompts.md) |
| List historical Topic prompts not yet in the library | `GET /api/v1/brands/{brand_id}/prompts/importable` | [endpoints/prompts.md](endpoints/prompts.md) |
| Import historical Topic prompts into the library (free) | `POST /api/v1/brands/{brand_id}/prompts:import` | [endpoints/prompts.md](endpoints/prompts.md) |
| Delete a prompt | `DELETE /api/v1/brands/{brand_id}/prompts/{prompt_id}` | [endpoints/prompts.md](endpoints/prompts.md) |

### Content sentences
| I want to… | Call | Reference |
|---|---|---|
| List the brand's content sentences (saved + staged) | `GET /api/v1/brands/{brand_id}/content-sentences` | [endpoints/content-sentences.md](endpoints/content-sentences.md) |
| Start a content-sentence generation run | `POST /api/v1/brands/{brand_id}/content-sentences:recommend` | [endpoints/content-sentences.md](endpoints/content-sentences.md) |
| Poll the latest run | `GET /api/v1/brands/{brand_id}/content-sentence-runs/latest` | [endpoints/content-sentences.md](endpoints/content-sentences.md) |
| Accept a staged sentence | `POST /api/v1/brands/{brand_id}/content-sentences/{sentence_id}:accept` | [endpoints/content-sentences.md](endpoints/content-sentences.md) |
| Delete a sentence | `DELETE /api/v1/brands/{brand_id}/content-sentences/{sentence_id}` | [endpoints/content-sentences.md](endpoints/content-sentences.md) |

## Example
```bash
scripts/tc-api.sh POST /api/v1/brands/$BRAND_ID/keywords:recommend
```
Returns `202` with a run object (`{"id", "status": "pending", ...}`). Poll:
```bash
scripts/tc-api.sh GET /api/v1/brands/$BRAND_ID/keyword-recommendation-runs/latest
```
until `status` is terminal, then accept the ones the user wants:
```bash
scripts/tc-api.sh POST /api/v1/brands/$BRAND_ID/keywords/$KEYWORD_ID:accept
```
Prompt recommendations follow the identical create → poll → accept shape at
`prompts:recommend` / `prompt-recommendation-runs/latest` /
`prompts/{id}:accept`. `POST /prompts:recommend` optionally takes a body
narrowing the run (e.g. seeding from a specific keyword or topic) — check
`PromptRecommendRequest` in [endpoints/prompts.md](endpoints/prompts.md)
if the user wants a scoped run rather than the brand-wide default.

Content sentences require a body:
```bash
scripts/tc-api.sh POST /api/v1/brands/$BRAND_ID/content-sentences:recommend \
  -d '{"mode": "topic", "topic": "coffee subscription services"}'
```
then the same poll/accept pattern via `content-sentence-runs/latest` and
`content-sentences/{id}:accept`.

## UI links
- `{TOPCITED_UI_URL}/keywords` — keyword library + recommendation flow.
- `{TOPCITED_UI_URL}/prompts` — prompt library + recommendation flow *and*
  the content-sentences panel, both rendered on the same page — there is no
  separate content-sentences route.
- `{TOPCITED_UI_URL}/competitor-keywords` — the competitor-keyword
  dashboard/overlap views that keyword recommendations are grounded in (see
  [brands.md](brands.md) for the brand-scoped endpoints behind it).

Default locale (`en`) is unprefixed — don't add `/en/`.

## Cost & quota
Each `:recommend` run spends a fixed T-coin amount at route entry, refunded
automatically only if the background task fails to dispatch or the run
fails internally — not refunded just because the user doesn't like the
suggestions:
- Keyword recommendations: 3 T-coins per run.
- Prompt recommendations: 3 T-coins per run.
- Content sentences: 3 T-coins per run (same rate as prompt recommendations
  by design).

Manually adding, editing, or deleting a keyword/prompt is free — only the
LLM-driven `:recommend` run and `keywords:difficulty` refresh are metered.
`keywords:difficulty` spends 1 `keyword_difficulty` credit (3 T-coins) but
**only if** any of the brand's keywords are stale against a 45-day TTL
cache — a Refresh click that finds everything fresh returns `200
{"status": "up_to_date"}` with no charge.
`accept`, `:add-to-topics`, and `:import` are all free — accepting a
suggestion doesn't cost anything beyond the original recommendation run.

## Failure modes
- All three `:recommend` calls are **asynchronous** — `202` means "queued,"
  not "done." Poll the matching `.../latest` endpoint; there is no
  per-run-id GET, only "the latest run for this brand," so starting a second
  run before the first finishes replaces what polling returns.
- 402 from any `:recommend` call → the relevant credit feature is exhausted;
  explain in plain language, don't retry, point to billing.
- A recommendation run landing `failed` still consumed the credit unless the
  failure happened before/during dispatch (auto-refunded) — a run that
  completes but produces zero usable suggestions is not automatically
  refunded; treat that as a normal (if disappointing) outcome, not a bug.
- Accepting the same recommendation twice, or accepting a stale/wrong
  `{keyword_id}`/`{prompt_id}`/`{sentence_id}`, 404s — re-fetch the list
  endpoint to get current staged ids before retrying an accept.
- `prompts:import` only surfaces prompts already used in an existing
  monitoring Topic that aren't yet in the library — if the user has no
  monitoring history yet, `GET .../prompts/importable` returns empty; that's
  expected, not an error.
