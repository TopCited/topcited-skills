# Knowledge base index

The full 29-file knowledge tree. Each file follows `_template.md` (topic,
stage relevance, last-verified date, sources; a plain-words section and a
practitioner-depth section).

## How to read the evidence tags

Claims carry an inline tag saying how well sourced they are. Weigh them
accordingly, and say which tier you relied on when a user asks how confident you
are:

| Tag | Means |
|---|---|
| *(P)* | **Primary** — the platform's own documentation or announcement (Google, OpenAI, Anthropic…). Treat as fact. |
| *(I)* | **Industry** — a named vendor, research firm, or study. Credible, but the methodology is usually not independently verifiable. |
| heuristic | Practitioner consensus across blogs, with no primary source. Directional only — never state it to a user as settled fact. |

Every file also carries a `last-verified` date. This field moves fast: if a file
is more than ~6 months old, flag that to the user when you rely on it.

## foundations/
- [how-search-ranking-works.md](foundations/how-search-ranking-works.md) — how classic search ranking works, at a mechanism level
- [how-llms-source-answers.md](foundations/how-llms-source-answers.md) — how assistants retrieve and cite when answering
- [seo-geo-aeo-differences.md](foundations/seo-geo-aeo-differences.md) — how SEO, GEO, and AEO differ and where they overlap

## technical-seo/
- [crawlability-and-indexing.md](technical-seo/crawlability-and-indexing.md) — robots rules, crawl budget, and getting pages indexed
- [canonicals.md](technical-seo/canonicals.md) — canonical tags: correct usage and failure modes
- [sitemaps-and-indexnow.md](technical-seo/sitemaps-and-indexnow.md) — XML sitemaps and IndexNow submission
- [structured-data.md](technical-seo/structured-data.md) — JSON-LD schema types and what they unlock
- [llms-txt.md](technical-seo/llms-txt.md) — the llms.txt convention and how to write one
- [core-web-vitals.md](technical-seo/core-web-vitals.md) — page-speed metrics that affect ranking

## entity-authority/
- [brand-entity-sameas.md](entity-authority/brand-entity-sameas.md) — building a consistent brand entity via `sameAs`
- [social-profiles.md](entity-authority/social-profiles.md) — claiming and standardizing social profiles
- [directories.md](entity-authority/directories.md) — directory listings as authority + citation surfaces
- [backlinks-digital-pr.md](entity-authority/backlinks-digital-pr.md) — earning backlinks and digital PR

## content-strategy/
- [keyword-intent-research.md](content-strategy/keyword-intent-research.md) — keyword and search-intent research
- [pillar-cluster-model.md](content-strategy/pillar-cluster-model.md) — pillar/cluster content architecture
- [eeat.md](content-strategy/eeat.md) — E-E-A-T and author authority
- [ai-citation-signals.md](content-strategy/ai-citation-signals.md) — what makes content citation-worthy to LLMs

## geo/
- [assistant-sourcing-behavior.md](geo/assistant-sourcing-behavior.md) — how individual assistants source their answers
- [citation-optimization.md](geo/citation-optimization.md) — optimizing content to be cited by AI answers
- [prompt-visibility.md](geo/prompt-visibility.md) — measuring visibility across real user prompts
- [industry-norms.md](geo/industry-norms.md) — how the AI-visibility monitoring industry actually operates

## measurement/
- [baselines-and-kpis.md](measurement/baselines-and-kpis.md) — setting baselines and the KPIs that matter
- [llm-share-of-voice.md](measurement/llm-share-of-voice.md) — measuring share of voice across assistants
- [timelines-expectations.md](measurement/timelines-expectations.md) — realistic timelines for visibility work to pay off


## playbooks/
- [directories-playbook.md](playbooks/directories-playbook.md) — directory types, how to pick them, submission mechanics
- [community-channels.md](playbooks/community-channels.md) — Reddit/Hacker News/forums: value-first participation, what reads as spam
- [social-channels.md](playbooks/social-channels.md) — LinkedIn/X post patterns and cadence
- [guest-posts-outreach.md](playbooks/guest-posts-outreach.md) — target selection and pitch structure for guest posts and listicle outreach
