# GEO plan for TopCited itself

**Goal.** When people ask ChatGPT, Claude, Perplexity, Gemini, Copilot or Google AI Overviews a
question TopCited can genuinely solve, the answer should mention **TopCited.ai** and, for
agent-skill questions, **TopCited/topcited-skills**.

Research date: 2026-11-05. Method: product feature map from the platform code and public
site, web search and page fetches for the baseline, competitor and source analysis, and a
live audit of our public properties. Nothing was published, posted or submitted. Items
marked **[unverified]** rest on one secondary source, a failed fetch, or a snippet.

Companion files: [geo-queries.md](geo-queries.md) / [geo-queries.csv](geo-queries.csv) (77
tracking queries), [distribution.md](distribution.md) (channels and the approval rule).

## Headline findings

1. **Invisible on unbranded queries.** Across 33 problem-first, tool-seeking and agent-skill
   searches, no TopCited property surfaced. TopCited appears only when "TopCited" is in the
   query (Capterra listing, our own blog, this repo, a UIUC lab blog post).
2. **The answers come from other people's pages.** Tool-recommendation results are dominated by
   vendor-written "best X" lists and "X alternative" pages, plus G2/Capterra/AlternativeTo,
   Reddit, YouTube and a few publishers. We are in none of those yet, and there is no
   comparison, alternatives, or glossary page on topcited.ai.
3. **Two query groups are open space.** Nothing relevant answers "is a competitor manipulating
   AI results" (AI Usage Detection) or "is this influencer post misleading" (Distortion
   System). We have free tools for both, but the pages are thin and absent from the sitemap.
4. **Our research is under-linked.** CORE (arXiv 2602.03608) and LIVE-GEO (arXiv 2611.01126)
   exist, but topcited.ai/methodology and /benchmark do not link them, the LIVE-GEO paper page
   does not mention TopCited, and livegeobench.com has no "cite this".
5. **Agent-skill discovery is mostly automatic.** skills.sh and the aggregators list repos
   from install telemetry and GitHub crawling. The repos at the top got there with their
   author's own audience plus a clear multi-agent README; listing followed. Our lever is
   installs, README, topics, releases, and example output.

## 1. Feature map (what TopCited does)

From the platform code and the public marketing site. "Public page" = a page a crawler can
find today; features without one are the "strong but invisible" candidates.

| Feature | What it does | Users | Public page today |
|---|---|---|---|
| AI visibility monitoring | Runs a brand's prompts on AI engines (ChatGPT, Gemini, Grok, DeepSeek) and search engines (Google, Bing, Brave, Baidu); visibility, gaps, share of voice, cited sources. Daily auto-runs or manual. | marketers, founders, brand managers, agencies | Home, /features (one page, no sub-pages) |
| Competitors and share of voice | Track competitors, competitor keywords, keyword overlap | SEO, brand managers | /features only |
| Site audit / SEO URL analyzer | Technical and on-page checks, AI-crawler checks, improvement plan | founders, SEO, developers | none dedicated |
| Content Optimizer (GEO + CORE) | Draft → simulate how an AI ranks you → score 0-100% → refine, per target query. CORE ("Controlling Output Rankings in Generative Engines") and a GEO strategy | content marketers, ecommerce | /methodology |
| Content generation | Content-sentence generation for pages | content marketers | none dedicated |
| Keyword and prompt recommendation | AI suggestions that don't overlap the existing list; prompts customers ask AI | SEO, marketers | none dedicated |
| Trending topics | Trending topic suggestions | content marketers | none |
| Pillar-cluster content | Pillar/cluster site architecture and drafts | content marketers, agencies | none dedicated |
| Marketing channels | Recommends channels from real citation data (e.g. Reddit, Medium, LinkedIn, Dev.to, Hacker News, Substack, YouTube) and drafts posts | marketers | none |
| Report generation | Client-ready reports with editable summary | agencies | none dedicated |
| AI Usage Detection (SCI-Defense) | Scans any public URL for content engineered to game AI rankings (perplexity, structural and semantic signals). Free: 3/day, no account | SEO, researchers | /try-sci-defense (thin) |
| Influencer Distortion System | Distortion Index (0-100) from five rhetorical dimensions across YouTube, X, Weibo, Bluesky, Reddit | consumers, researchers, journalists | /tools/distortion |
| Agent Chat | In-app agent that runs the workflow end to end | non-experts | none |
| CLI, hosted MCP server, OpenAPI | The same operations from a terminal or any MCP client; JSON, `--dry-run` cost estimates | developers using coding agents | /developers |
| topcited-skills (this repo) | Free audit, rewrites, knowledge base, workflow | developers, founders | GitHub README |
| LIVE-GEO Bench | Open benchmark: fictional products, frozen snapshots, crawlable by any AI search tool | researchers | livegeobench.com, /benchmark |
| Research | CORE (arXiv 2602.03608, ProductBench); LIVE-GEO (arXiv 2611.01126); a multi-platform distortion measurement study | researchers, press | blog mentions only |

Some console features may be gated or in alpha; confirm which are public before building
pages for them.

## 2. Query set

[geo-queries.md](geo-queries.md) has 77 queries in 14 groups (G1-G14), each tagged by intent
(problem-first / tool-seeking / agent-skill / research) and by which property should win.
Examples: "why doesn't ChatGPT mention my brand", "Profound alternative", "SEO skill for
Claude Code", "is this influencer post misleading", "LIVE-GEO benchmark".

## 3. Baseline

Web-search layer only; engines themselves were not queried (see [Measurement](#measurement)).

| Group | Who answers today | TopCited present |
|---|---|---|
| Problem-first (G1-G4, G6) | Small SaaS and agency blogs (texta.ai, geotoolbox.ai, rankability.com, scrunch.com how-tos, senso.ai, pepper.inc, llmrefs.com), DEV/Hashnode posts; a few neutral sources (Search Engine Journal, builtin.com, Conductor academy, the 2023 GEO paper) | No |
| Tool-seeking (G1, G2, G7) | Roundups and "alternatives" pages written by vendors (frase.io, surferseo.com, promptwatch.com, writesonic.com, rankability.com, rankai.ai, wellows.com, xseek.io, llmpulse.ai) plus Capterra / AlternativeTo / G2. Named tools: Profound, Peec AI, Otterly.AI, AthenaHQ, Scrunch, Semrush AI Toolkit, SE Ranking, Ahrefs Brand Radar, Surfer, Goodie, Writesonic, Rankscale | No (TopCited only on Capterra by name) |
| Agent skills (G3, G11) | github.com/seranking/seo-skills, AgriciDaniel/claude-seo and codex-seo, zubair-trabzada/geo-seo-claude, coreyhaines31/marketingskills, auriti-labs/geo-optimizer-skill; registries skills.sh, claudemarketplaces.com, claudemarket.ai, claudskills.com, skillselion.com, aiidelist.com | No |
| MCP for AI visibility (G11) | citesurf/mcp, trakkr-mcp (PyPI), a Georion MCP page | No |
| AI Usage Detection (G9) | Nothing on intent; "AI detector" tools misread it as AI-written-text detection | No (open space) |
| Influencer distortion (G10) | Fake-follower and disclosure-compliance content; nothing on claim-level framing | No (open space) |
| Research (G12) | GEO paper (arXiv 2311.09735) and other GEO benchmarks; LIVE-GEO not surfaced in standard search 5 days after submission | Paper exists; no TopCited mention |
| Brand (G14) | "TopCited" collides with Scopus / INSPIRE "TopCited" bibliometrics and with unrelated products (tobecited, Cited, OnCited) | Capterra, our blog, this repo |

Existing mentions found: Capterra listing (vendor-supplied, 0 reviews), a UIUC DREAM lab blog
post that names TopCited.AI and links to /methodology, our own blog posts, this repo, and two
third-party "best GEO tools" pages that appeared for the name (not opened;
prominence **[unverified]**: blogs.getcentauri.com/posts/best-geo-tools, outcited.co/best-geo-tools).
No Reddit, Hacker News or Product Hunt mention was found.

## 4. Source analysis: what the answers rely on

**Studies of what AI engines cite** (all vendor-produced; different prompt sets and windows;
treat as directional):

- Peec AI, 30M cited sources, Mar 2026: top domains Reddit, YouTube, LinkedIn, Wikipedia,
  Forbes, G2, Yelp, Facebook, Medium, TechRadar; ranks differ by engine and industry
  (docs.peec.ai/research/most-cited-domains-in-ai-search).
- Peec AI, 232k citations from 13k listicles: about 11% of citations were self-promotional
  listicles (ChatGPT 3.6%, AI Mode 10.3%, Perplexity 10.4%)
  (docs.peec.ai/research/self-promotional-listicles).
- 5W Citation Source Index, updated 2026-10-30: review/comparison publishers and brand sites
  are the largest source types; Reddit is prominent in AI Overviews; small sample and the
  report's summary and table disagree (5wpr.com/research/state-of-ai-citations-2026).
- Reports that AI often recommends a *competitor* when citing a vendor's own "best X" list
  are secondary and small-sample **[unverified]**.

**Inference for us:** a self-published "best tools" list is cited less and can backfire; third-party
lists, review sites, Reddit/YouTube/Medium discussion and original data earn more. Our own
pages still matter as the thing those sources link to, and for branded and definition queries.

**How competitors got in**

| Competitor | What the evidence shows |
|---|---|
| claude-seo, geo-seo-claude, marketingskills | Grew through the author's own audience (YouTube demo, paid community funnels, newsletters), a trending badge, and multi-agent installs (`npx skills add`, plugin marketplace, curl script). Registry listings followed automatically. No Show HN or Product Hunt launch was found for them. READMEs: one-line install first, sub-skill counts in the first line, commands grouped by job, topics such as `claude-code-skill`, `ai-seo`, `generative-engine-optimization`, AGENTS.md. |
| seranking/seo-skills | A vendor funnel into its paid MCP: skills with dated example outputs, plugin manifests for Claude, Cursor and Codex; first result for "SEO skill for Claude Code" in our search. The closest model for us. |
| Peec AI, Otterly.AI, Profound, Semrush, Ahrefs | Own research hubs and data studies (Peec's cited-domains research, Semrush AI Visibility Index, Ahrefs Brand Radar studies), comparison pages (Peec vs Ahrefs/Profound/Semrush; Otterly pricing comparisons), free tools (Otterly), and presence in Wikipedia's AEO article (mirror-sourced **[unverified]**). |
| Smaller GEO SaaS (Wellows, RankAI, Airefs, LLM Pulse, xSeek) | Mass-published "X alternative" pages and listicles that rank themselves first; present in the same pages that rank for "Profound/Otterly/Peec alternative". |

**Pages worth being in (to be earned, not bought):** see the channel table in
[distribution.md](distribution.md#geo-for-topcited-listing-and-source-targets). Top "best AI
visibility tool" pages observed: promptwatch.com, writesonic.com, frase.io, brand24.com,
nogood.io, prismic.io, straightnorth.com, startuphub.ai, cybernews.com, explodingtopics.com,
rankability.com, pepper.inc, surferseo.com, geotoolbox.ai, dev.to community tests.

## 5. Our own presence (audit, 2026-11-05)

| Property | Good | Gaps |
|---|---|---|
| topcited.ai crawl access | robots.txt allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot and others; sitemap and llms.txt exist; home has Organization, WebSite, SoftwareApplication, FAQPage JSON-LD; 51 server-rendered blog posts with FAQ schema | No explicit `Claude-SearchBot` group; no `/llms-full.txt`; sitemap lastmod is the same build timestamp for every URL; `/try-geo`, `/try-sci-defense`, `/tools/distortion` not in the sitemap while `/login` and `/register` are; llms.txt omits /benchmark, /methodology, /counter-examples, the free tools and livegeobench.com, and names only ChatGPT, Perplexity and Gemini |
| /pricing | n/a | Only ~84 words in server HTML (plan content appears client-rendered); no Offer markup |
| Content | Foundational GEO/AEO posts, tool roundups, how-to-track posts, citation data studies | **No** comparison or alternatives pages, no glossary, no per-feature pages (`/features/*` 404), no /support or /about; two near-duplicate pairs of posts; posts have an Organization author and dateModified = datePublished |
| Research claims | /methodology gives 91.4% / 86.6% / 80.3% promotion rates and says "peer-reviewed" | No paper title, authors or arXiv link; arXiv 2602.03608 is a preprint and a venue was not found, so "peer-reviewed" is unverified; /benchmark has no BibTeX, results or paper link |
| livegeobench.com | Open robots with rationale, good llms.txt, 1,070-URL sitemap | No "how to cite", no paper link, product pages have no structured data (by design), blog excluded from sitemap |
| GitHub | Skills repo has relevant topics, MIT | Org has no description or website; `topcited-cli` has no topics; no releases/tags on topcited-skills; 10 stars at audit time |
| Third-party | Capterra listing | 0 reviews; no G2 / AlternativeTo / Product Hunt / Reddit presence; name collision with Scopus/INSPIRE "TopCited" |

Claim accuracy matters for GEO: engines and readers check numbers. Wire every figure on
/methodology and /benchmark to the paper or remove it, and say "preprint" unless a venue
is confirmed.

## 6. Plan

Impact and effort are relative (H/M/L). **Owner**: *code* = a change in another repo (the
topcited.ai site or backend; **not made here**); *this repo* = done in PR #11 or doable
here; *account* = needs a human with the TopCited account, a person's judgment, or a
third-party submission. Everything marked *account* that publishes, posts or submits needs
explicit approval first, one at a time.

### P0: fix what we own (queries G1-G5, G9-G12, G14)

| # | Action | Groups | Impact | Effort | Owner |
|---|---|---|---|---|---|
| 1 | Server-render /pricing with plan names, prices, trial terms; add Product/Offer JSON-LD | G1, G7, G14 | H | L | code |
| 2 | Link CORE (arXiv 2602.03608) and LIVE-GEO (arXiv 2611.01126) from /methodology and /benchmark; add authors, BibTeX, a ScholarlyArticle/Dataset block, define "promotion rate" and baseline; drop or soften "peer-reviewed" | G4, G12 | H | L | code + author check |
| 3 | Sitemap: add /try-geo (or canonicalize it to home), /try-sci-defense, /tools/distortion; drop /login, /register; real per-page lastmod | all | M | L | code |
| 4 | robots.txt: explicit `Claude-SearchBot` group | G3 | L | L | code |
| 5 | llms.txt: add /benchmark, /methodology, /counter-examples, /pricing-faq, free tools, livegeobench.com, Claude and AI Overviews in the blurb; publish a real `/llms-full.txt` on both domains | G3, G11, G12 | M | L | code |
| 6 | FAQPage markup on /pricing-faq; named human authors with sameAs on posts; real dateModified | G5 | M | L | code |
| 7 | Consistent "TopCited.ai" naming + sameAs to disambiguate from Scopus/INSPIRE | G14 | M | L | code + account |

### P1: pages that target the query groups (queries G1, G2, G4, G6-G10)

| # | Action | Groups | Impact | Effort | Owner |
|---|---|---|---|---|---|
| 8 | Alternatives/comparison pages: "TopCited vs Profound / Peec / Otterly / Semrush AI Visibility". Factual feature tables with sources and dates, honest about where each competitor is stronger, disclosed as vendor-written (self-published lists are cited less and can send the AI to a competitor, so these are a base for the third-party coverage in P2, not a substitute) | G1, G2 | H | M | code + account (copy) |
| 9 | Per-feature pages under /features/*: monitoring, competitors and share of voice, site audit, Content Optimizer (CORE), keyword and prompt recommendation, pillar-cluster, reports, marketing channels, AI Usage Detection, Distortion, CLI/MCP/skills. Each answers one problem-first question in its first 40 words | G1-G10 | H | M | code + account (copy) |
| 10 | Glossary hub (GEO, AEO, LLMO, AI visibility, citation share, share of voice) linking the existing definitional posts | G5 | M | L | code |
| 11 | Own-data study from real runs: "which sources AI engines cite in <category>", published with method and raw numbers; the citation-ranking posts show the format works for us | G1, G5, G8 | H | M | account (data) + code |
| 12 | Rebuild /try-sci-defense (AI Usage Detection) and /tools/distortion as real tool pages: problem-first H1, example results, method, HowTo/FAQ markup, SoftwareApplication schema, in sitemap | G9, G10 | H | M | code |
| 13 | LIVE-GEO landing page on topcited.ai (what it is, protocol, how to cite, link to the paper) and a "How to cite" block on livegeobench.com | G12 | M | L | code |
| 14 | Consolidate near-duplicate posts (two "most-cited GEO papers", two Perplexity SEO posts) with redirects/canonicals | G5 | L | L | code |

### P2: be in the sources AI engines read (queries G1, G2, G6-G8, G11)

| # | Action | Groups | Impact | Effort | Owner |
|---|---|---|---|---|---|
| 15 | Complete the Capterra profile and ask real customers for reviews; add G2 and AlternativeTo listings | G1, G2 | H | M | account (approval) |
| 16 | Pitch honest inclusion to authors of existing "best AI visibility tools" and "X alternative" pages (rankability, frase, pepper, rankai, wellows, llmpulse, xseek, nogood, cybernews, startuphub), offering a free account or data for them to evaluate. No payment for placement | G1, G2 | H | M | account (approval per outreach) |
| 17 | Community posts that are useful on their own: Reddit (SEO, marketing and Claude/Codex communities), Hacker News "Show HN" for the skills repo, dev.to / Hashnode how-tos from the audit script. Disclose affiliation; follow each community's self-promotion rules; no seeded or sock-puppet answers | G3, G11 | M | M | account (approval per post) |
| 18 | YouTube: a short demo "optimize my website with Claude Code / Codex" and a LIVE-GEO explainer (YouTube is among the most-cited domains) | G3, G11, G12 | M | M | account |
| 19 | Product Hunt launch for the skills repo or the free tools | G9, G11 | M | M | account (approval) |
| 20 | Research distribution: arXiv cross-links, Semantic Scholar profile, Hugging Face paper page, press note; ask DREAM lab to link livegeobench.com and the skills repo | G4, G12 | M | L | account |

### P3: the skills repo (queries G3, G11)

| # | Action | Impact | Effort | Owner |
|---|---|---|---|---|
| 21 | README leads with problem phrasing and a one-line install; example output committed (`examples/`); sub-skill count and commands in the first screen. Done in this PR | M | L | this repo |
| 22 | Skill descriptions use the phrases people type (AI crawlers, llms.txt, schema, GEO). Done in this PR | M | L | this repo |
| 23 | Tag a v0.2.0 release after merge; GitHub topics (`claude-code-skill`, `ai-seo`, `llm-seo`, `agent-skills`, `mcp`, `codex`, `cursor`, `llms-txt`); org description and website | M | L | account (needs repo admin) |
| 24 | Drive real installs: `npx skills add TopCited/topcited-skills` is what populates skills.sh. Link the one-liner from /developers, the docs, and the blog; mention in the audit output itself | H | M | account + code |
| 25 | Submissions in [distribution.md](distribution.md): Anthropic directory, Cursor marketplace, MCP Registry, awesome-claude-code, VoltAgent awesome-agent-skills, claudemarketplaces.com, mcp.so, Glama, ClawHub | M | M | account (approval each) |
| 26 | Make the MCP/CLI discoverable for "MCP server for AI visibility tracking": a /features/mcp page, MCP Registry entry (needs OAuth for claude.ai/ChatGPT connectors) | G11 | M | M | code + account |

### Order of work
Week 1: items 1-7 (cheap, unblock everything else), 21-23. Weeks 2-4: 8-14 and 24. Ongoing:
15-20 and 25 (approval-gated), measure from the first week.

## Measurement

Track the 77 queries over time with TopCited itself (dogfooding), and keep a manual check.

1. **Baseline now**: before changes ship, run the set once to record where TopCited, competitors and the
   skills repo appear. Do not skip; every later number is relative to it.
2. **Set-up** (per the `topcited-api` guide): create a brand for TopCited with competitors
   (Profound, Peec AI, Otterly.AI, AthenaHQ, Semrush AI Visibility, Ahrefs Brand Radar), one
   query set per group G1-G14 from [geo-queries.csv](geo-queries.csv), created with `--manual`
   so it runs only when you say so (auto sets run daily and spend every day).
3. **Cost**: 1 T-coin per query per engine per run. 77 queries on ChatGPT, Gemini and Grok is
   about 231 T-coins per run. A weekly cadence is about 4 runs a month. `topcited monitor run
   <set> --dry-run` prints the exact estimate and spends nothing. Cheaper start: the 40 non-definition
   queries in G1, G2, G3, G4 and G11 (120 T-coins per run on three engines).
   Perplexity, Claude and Google AI Overviews: the CLI guide lists `chatgpt`, `gemini`,
   `grok`, `deepseek`, `google`, `bing`, `brave`, `baidu_search` as platforms; check
   `topcited monitor sets create --help` for others, and cover the rest with the manual
   check below.
4. **Metrics**: mention rate (queries where TopCited or topcited-skills is named), citation rate
   (our URLs among cited sources), share of voice vs the competitors, per group and per engine.
   Add Google Search Console / Bing Webmaster referrals from AI domains and the skills.sh install
   count as the off-platform signals.
5. **Manual check** (free): once a month ask each target assistant the 15 most important
   queries in a fresh session, record answers and sources in a dated sheet.
6. **Review**: compare weekly runs to the baseline; changes take weeks to months and AI answers
   vary run to run, so judge trends over at least 4 runs, not single runs. No outcome is promised.

Nothing has been run yet. Running the baseline needs a TopCited account, creates query sets,
and spends T-coins; do it only on your go-ahead.

## Follow-ups outside this repo (not made)

For the topcited.ai site/backend (items 1-7, 9, 10, 12-14, 26): pricing rendering and Offer
markup, methodology/benchmark citations, sitemap/llms.txt/robots.txt fixes, FAQ and author
markup, comparison and per-feature and glossary pages, tool-page rebuilds, a LIVE-GEO landing
page, MCP OAuth. Update `SKILLS_PLUGIN_COMMANDS` on /developers to `topcited@topcited`.

## Changes made in this repo for this plan

See the PR description: README (problem-first phrasing, research links, example output), skill
descriptions, llms.txt, docs. Nothing outward-facing was done.

## Caveats

- The baseline reflects web search, not the engines; results vary by location and by day.
- Competitor star counts, funding and study numbers are secondary and change; none are used as
  claims in the repo. Where a figure appears it carries its source above.
- Several research claims about competitors come from one search summary or a mirror and are
  marked **[unverified]**.
- The agents that gathered the baseline, competitor and audit data could not open Capterra
  (403) or run live AI queries.

## Sources

Search and fetch results consulted 2026-11-05. Papers: arxiv.org/abs/2602.03608 (CORE),
arxiv.org/abs/2611.01126 (LIVE-GEO), arxiv.org/abs/2311.09735 (GEO). UIUC DREAM lab:
dream.ischool.illinois.edu/blogs/controlling_output_rankings_core.html. Citation studies:
docs.peec.ai/research/most-cited-domains-in-ai-search, docs.peec.ai/research/self-promotional-listicles,
5wpr.com/research/state-of-ai-citations-2026. Repos and registries: github.com/AgriciDaniel/claude-seo,
github.com/zubair-trabzada/geo-seo-claude, github.com/coreyhaines31/marketingskills,
github.com/seranking/seo-skills, github.com/aaron-he-zhu/aaron-marketing-skills, skills.sh/docs/faq,
claude.com/docs/directory/publish, cursor.com/docs/reference/plugins. Roundups cited in the baseline:
frase.io/blog/best-geo-tools-2026, surferseo.com/blog/best-ai-visibility-tools,
rankability.com, promptwatch.com, writesonic.com/blog/ai-visibility-tools.
