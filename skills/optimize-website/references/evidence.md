# What the research says (use it to set expectations)

Strength: **strong** = controlled or consistently replicated; **moderate** = observational or one good
study; **weak/contradicted** = mixed or null. Full table with sources: the repo's
[GEO plan](../../../docs/geo-plan.md#6-research-backed-rules).

| Lever | Strength | Note |
|---|---|---|
| Page matches the query (same terms in title, intro, headings) | strong | Prompt alignment is the largest page-level predictor in a 2.1M-citation study (preprint) and a controlled SIGIR'26 study |
| Visible price/specs/dates; not stale; no contradictions or hedging | strong (commerce) | Missing price and old timestamps were gatekeepers in the controlled study |
| Answer in the first 2-3 sentences / top third | moderate | Median cited passage sits about a third down the page |
| Named, sourced statistics and quotations | mixed | Helped in the original GEO paper's simulated engine; unverifiable numbers get flagged on the live web (LIVE-GEO) |
| Keyword stuffing | contradicted | Negative in the GEO paper |
| Third-party mentions, reviews, roundups, communities | moderate | Strongest correlate of AI mentions; correlation, not proof |
| FAQ blocks, heavy structure, length | weak/contradicted | Vanish once domain is controlled |
| JSON-LD for citation lift | contradicted | Null in a 1,885-page difference-in-differences study |
| llms.txt for citation lift | contradicted | No correlation across ~300k domains; rarely fetched |
| Persuasive hidden text / prompt-injection style content | works in labs, policy risk | Do not recommend |

Never promise citations: engines disagree with each other and answers change run to run.
