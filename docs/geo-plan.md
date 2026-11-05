# GEO plan for TopCited itself (v2)

**Goal.** When people ask ChatGPT, Claude, Perplexity, Gemini, Copilot or Google AI Overviews a
question TopCited can genuinely solve, the answer should mention **TopCited.ai** and, for
agent-skill questions, **TopCited/topcited-skills**.

Round 1 (2026-11-05): feature map, 77 tracking queries, web-search baseline, source analysis, audit
of our own presence. Round 2 (same day): competitor playbooks read page by page, documented case
studies, what the GEO research says, and a free real-AI baseline. Nothing was published, posted or
submitted. Source keys like `[PEEC-L]` are listed in [Sources](#sources). **[unverified]** means a
single secondary source, a snippet, or a failed fetch.

Companion files: [geo-queries.md](geo-queries.md) / [.csv](geo-queries.csv) (77 queries),
[geo-baseline/](geo-baseline/README.md) (raw answers), [geo-manual-check.md](geo-manual-check.md)
(steps for the engines not queried), [distribution.md](distribution.md) (channels, approval rule).

## What changed in v2

- **Moved up:** original data with a downloadable dataset (was #11), claim accuracy on
  /methodology (was #2), earned third-party coverage and reviews (#15, #16), YouTube (#18).
- **Moved down:** llms.txt and FAQ/JSON-LD work (#5, #6) because controlled studies show no
  citation lift; comparison pages (#8) because self-published lists are cited least and can send the
  AI to a competitor; Product Hunt (#19) because no vendor evidence was found.
- **New:** answer-first rewrite of key pages, a controlled-experiment series with a public tracker, a
  "what do coding agents recommend" study, co-published research with an independent party, a customer
  case study with a hard number, more example outputs in this repo, an evidence-calibrated skill.
- **Corrected:** the plan now treats schema and llms.txt as hygiene, not growth levers.

## Headline findings

1. **Invisible on unbranded queries, on every engine we could test.** 0 of 14 unbranded queries
   mentioned TopCited or topcited-skills on Claude with web search or on Codex with live search; the
   branded query was answered correctly on both (Claude from Capterra, Codex from topcited.ai)
   `[BASE]`. The round-1 web-search check (33 queries) agreed.
2. **The answers come from other people's pages.** Tool-recommendation results are vendor-written
   lists and "alternative" pages, review sites, Reddit and YouTube `[R1-BASE][PEEC-D][AHR-LISTS]`.
3. **Earned mentions beat our own pages.** Branded web mentions correlate with AI mentions at
   0.66 to 0.71, backlinks and Domain Rating at 0.2 to 0.33 `[AHR-BRAND]`; self-promotional lists are
   about 11% of listicle citations and 3.6% on ChatGPT `[PEEC-L]`.
4. **Schema and llms.txt are not citation levers.** Null in a 1,885-page difference-in-differences
   test `[AHR-SCHEMA]` and across about 300k domains `[SER-LLMS]`; Google says it uses neither `[GOOG]`.
5. **What the controlled evidence supports:** match the question, show price/specs/dates, keep claims
   verifiable, put the answer early `[SPRK][MD]`; unverifiable numbers get flagged on the live web `[LIVE]`.
6. **Open space exists** for AI Usage Detection and misleading-influencer queries `[R1-BASE][BASE]`, and
   competitors' original-data programmes (Peec, Otterly, Profound, Semrush, Ahrefs) are the visible
   playbook, but none releases a downloadable dataset `[COMP]`.
7. **Our research is under-linked and our claims need tightening.** /methodology and /benchmark do not
   link the CORE or LIVE-GEO papers, and the newer LIVE-GEO paper shows CORE's gains are model-dependent
   (Claude API ranked CORE last) `[LIVE][AUDIT]`.

## 1. Feature map (what TopCited does)

From the platform code and public site. "Public page" = a page a crawler can find today.

| Feature | What it does | Users | Public page today |
|---|---|---|---|
| AI visibility monitoring | Runs a brand's prompts on AI engines (ChatGPT, Gemini, Grok, DeepSeek) and search engines (Google, Bing, Brave, Baidu); visibility, gaps, share of voice, cited sources. Daily auto-runs or manual | marketers, founders, brand managers, agencies | Home, /features (one page) |
| Competitors, share of voice | Competitor tracking, competitor keywords, overlap | SEO, brand managers | /features only |
| Site audit / SEO URL analyzer | Technical and on-page checks incl. AI-crawler checks | founders, SEO, developers | none dedicated |
| Content Optimizer (GEO + CORE) | Draft, simulate how an AI ranks you, score 0-100%, refine, per target query | content marketers, ecommerce | /methodology |
| Content generation | Content-sentence generation | content marketers | none dedicated |
| Keyword and prompt recommendation | Suggestions that don't overlap the existing list | SEO, marketers | none dedicated |
| Trending topics | Trending topic suggestions | content marketers | none |
| Pillar-cluster content | Pillar/cluster architecture and drafts | content marketers, agencies | none dedicated |
| Marketing channels | Recommends channels from real citation data (Reddit, Medium, LinkedIn, Dev.to, Hacker News, Substack, YouTube) and drafts posts | marketers | none |
| Report generation | Client-ready reports with editable summary | agencies | none dedicated |
| AI Usage Detection (SCI-Defense) | Scans a public URL for content engineered to game AI rankings. Free: 3/day, no account | SEO, researchers | /try-sci-defense (thin) |
| Influencer Distortion System | 0-100 Distortion Index from five rhetorical dimensions across YouTube, X, Weibo, Bluesky, Reddit | consumers, researchers, journalists | /tools/distortion |
| Agent Chat | In-app agent that runs the workflow end to end | non-experts | none |
| CLI, hosted MCP, OpenAPI | The same operations from a terminal or MCP client | developers | /developers |
| topcited-skills (this repo) | Free audit, rewrites, knowledge base, workflow | developers, founders | GitHub README |
| LIVE-GEO Bench | Open benchmark: fictional products, frozen snapshots, crawlable by any AI search tool | researchers | livegeobench.com, /benchmark |
| Research | CORE (arXiv 2602.03608), LIVE-GEO (arXiv 2611.01126), a multi-platform distortion measurement study | researchers, press | blog mentions only |

Some console features may be gated or in alpha; confirm which are public before building pages.

## 2. Query set

[geo-queries.md](geo-queries.md): 77 queries, 14 groups (G1-G14), tagged by intent (problem-first,
tool-seeking, agent-skill, research) and by which property should win.

## 3. Baseline

### 3a. Web-search layer (round 1)

| Group | Who answers today | TopCited present |
|---|---|---|
| Problem-first (G1-G4, G6) | Small SaaS and agency blogs (texta.ai, geotoolbox.ai, rankability.com, scrunch.com how-tos, senso.ai, pepper.inc, llmrefs.com), DEV/Hashnode; few neutral sources `[R1-BASE]` | No |
| Tool-seeking (G1, G2, G7) | Vendor roundups and "alternatives" pages plus Capterra / AlternativeTo / G2. Named: Profound, Peec AI, Otterly.AI, AthenaHQ, Scrunch, Semrush, SE Ranking, Ahrefs Brand Radar, Surfer, Goodie, Writesonic, Rankscale `[R1-BASE]` | No (only on Capterra by name) |
| Agent skills (G3, G11) | seranking/seo-skills, AgriciDaniel/claude-seo and codex-seo, zubair-trabzada/geo-seo-claude, coreyhaines31/marketingskills, auriti-labs/geo-optimizer-skill; registries skills.sh, claudemarketplaces.com, claudemarket.ai, claudskills.com, skillselion.com, aiidelist.com `[R1-BASE]` | No |
| MCP for AI visibility (G11) | citesurf/mcp, trakkr-mcp (PyPI), a Georion MCP page `[R1-BASE]` | No |
| AI Usage Detection (G9), Distortion (G10) | Nothing on intent; "AI detector" tools read it as AI-written-text detection; influencer content is about fake followers and disclosure `[R1-BASE]` | No (open space) |
| Research (G12) | GEO paper and other benchmarks; LIVE-GEO not surfaced 5 days after submission `[R1-BASE]` | No |
| Brand (G14) | "TopCited" collides with Scopus / INSPIRE bibliometrics and unrelated products `[AUDIT]` | Capterra, our blog, this repo |

### 3b. Real AI baseline (free, 2026-11-05)

15 queries from [geo-queries.csv](geo-queries.csv) plus "what is TopCited.ai", sent verbatim, one run each,
to **Claude** (`claude -p` with web search) and **Codex** (`codex --search exec`, header reported model
`gpt-6.1-sol`). No TopCited T-coins spent. Raw answers: [geo-baseline/](geo-baseline/). `[BASE]`

| Result | Claude + web | Codex + search |
|---|---|---|
| Unbranded queries mentioning TopCited / topcited-skills | **0 / 14** | **0 / 14** |
| "what is TopCited.ai" | Yes, described from the Capterra listing and warned the $29 price came from a third-party directory | Yes, described from topcited.ai |
| Competitors named across the 14 (answers containing the name) | Profound 5, Otterly 5, Semrush 5, Peec 4, Ahrefs 4, Athena 3, Scrunch 2, Goodie 2, SE Ranking 1, geo-seo-claude 1, Rankscale 1 | Peec 2, Otterly 2, Ahrefs 2, Profound 1, Semrush 1, others 0 |
| Skills repos named | geo-seo-claude once; claude-seo 0 | none |

Observations:
- Claude's "best AI visibility tracker" answer said most "best of" pages are vendor-written and their
  rankings and prices conflict, then grouped tools by budget (Otterly cheapest, Peec mid-market, Profound
  enterprise) `[BASE]`. Codex's pick was Peec for marketing teams and Otterly for budget `[BASE]`.
- Both CLIs read agent-skill queries (SEO audit skill, GEO plugin for Cursor, MCP server) as build
  requests, and "is this influencer post misleading" and "LIVE-GEO benchmark" as needing input. These
  rows are weak proxies; use the chat products via [geo-manual-check.md](geo-manual-check.md).
- These are coding-agent CLIs, one run per query; answers vary between runs `[SPARK]`.
- Not queried: ChatGPT app, Perplexity, Gemini, Copilot, Google AI Overviews. Manual steps are in
  [geo-manual-check.md](geo-manual-check.md). TopCited's own monitoring would cover several of these but
  spends T-coins; see [Measurement](#9-measurement).

For context, AuthorityTech's vendor-name ledger (a competitor; 1,583 answers, 2026-07-08 to 11-02)
counted Profound named in 338, Semrush 273, Peec 263, Otterly 262, Ahrefs 191, Scrunch 91, Athena 76,
and Profound by engine in 151 of 360 Gemini answers but 26 of 405 ChatGPT answers `[AUTH]` (related
party, treat as indicative). Engines differ, so test each separately.

## 4. Competitor playbooks

Read page by page; "index only" = seen on a listing, not opened. `[COMP]` unless noted.

| Vendor | Content engine | Original-data assets | Listings / community | Gap we can use |
|---|---|---|---|---|
| **Profound** | Blog with named authors, research hub, AEO report, podcast, events, webinars | 11.8B-citation study across 29 industries and 8 models with method and per-industry table (2026-07-30); "half-life of an AI citation is 11 days" (index only); "Claude and Claude Code are distinct answer engines", 24,135 responses (index only); "Open in ChatGPT/Claude" buttons | G2 (~1,100 reviews, snippet); named in claude-seo as an extension; podcasts, LinkedIn startups list | No comparison pages or free tools in its nav; no dataset download |
| **Peec AI** | ~4 posts a month (43 in Jan-Oct 2026), named researchers, machine-readable `.md` research pages | 30M-source most-cited domains (top 10 only, no shares); 232k-citation self-promotional listicle study with method; citation-rate benchmarks; SIXT case study (+320% citations, index only) | G2 (small review count, snippet); MCP page | Admits single-vertical, vendor-data caveats; no dataset |
| **Otterly.AI** | 2-3 posts a week; most extensive experiment programme: 17+ data studies, 9 controlled "GEO experiments", public tracker | "We updated only the date on 10 articles: citations +31.5%" (title, index only); 617,985-citation content-type study; country "AI Search Index" series | G2 ~4.8 (snippet); public API; Claude Skill gated to paid plans | Its Claude skill is not free; no open dataset |
| **Semrush** | Original research under its blog; AI Visibility Index microsite | 126M-prompt AI Visibility Index (2026-06-26, with Adobe executives quoted); most-cited-domains study (thin method, no download) | G2 comparison pages | Method thinly explained; no dataset |
| **Ahrefs** | Research on its blog; free AI Visibility Checker; Brand Radar with public pricing | 75K-brand correlation study (mentions 0.664 vs backlinks 0.218), with caveat "correlation not causation"; schema and llms.txt studies `[AHR-BRAND][AHR-SCHEMA][AHR-LLMS]` | Press release (snippet) | Charts, no downloadable data |
| **Scrunch** | Roundup on its own domain, prompt generator | Research collaboration with Bain & Company (index only) | G2 ~4.6 (snippet); $15M Series A (Mayfield, snippet) | Third-party co-branding is its credibility lever |
| **AthenaHQ** | Posts every few days, `/comparison/[competitor]` pages | "Science of AI Citation" claims (index only, unverified methodology) | $2.2M seed (snippet) | Byline "AthenaHQ Labs" only |

**Skill repos** `[SKILLREPOS]`

| Repo | README and install | Levers |
|---|---|---|
| AgriciDaniel/claude-seo | Plugin marketplace + install script; sample audit; topics `ai-seo`, `claude-code-skill`; extensions list incl. Profound and SE Ranking | Author's own paid community and YouTube behind it; GitHub trending badge |
| coreyhaines31/marketingskills | Nine install methods; foundation `product-marketing` skill read by the others; 20 topics; partners table | Author's newsletter, agency and training audience |
| zubair-trabzada/geo-seo-claude | One `/geo audit` command running subagents (snippet) | Star history shows bursts tied to GitHub trending, not steady growth |
| seranking/seo-skills | 25 committed example runs; CONTRIBUTING asks for a before/after example on improvement PRs | Vendor funnel into its paid MCP; small reach |
| aaron-he-zhu/aaron-marketing-skills | Translated READMEs, listing badges for skills.sh, ClawHub and others | Sibling repos, Discussions tab |

skills.sh has no submission form; skills appear from `npx skills add owner/repo` telemetry and rank by
installs `[SKILLS-FAQ]`. Awesome lists: travisvn/awesome-claude-skills takes fork-and-PR and lists no SEO
skills today; hesreallyhim/awesome-claude-code says only collaborators open PRs; VoltAgent and Composio
lists could not be read **[unverified]**. No PR that added claude-seo or marketingskills to an awesome list
was found `[SKILLREPOS]`.

**How listing on "best tool" pages works:** the pages that rank are vendor-written. SE Ranking's "Profound
alternatives" ranks itself first with no stated method or conflict disclosure `[COMP]`. Peec measured that
self-promotional listicles are about 11% of listicle citations (ChatGPT 3.6%, AI Mode 10.3%, Perplexity
10.4%) and advises against the tactic `[PEEC-L]`. Ahrefs found "best X" lists are 43.8% of cited page types
and that higher rank on a third-party list means more recommendation; 34% of ChatGPT software responses
that recommended a publisher cited the publisher's own list `[AHR-LISTS]`. Top cited domains in AI search
include Reddit, YouTube, LinkedIn, Wikipedia, Forbes, G2, Yelp, Facebook, Medium, TechRadar `[PEEC-D]`.

**What to copy, beat, skip**

- **Copy:** named-stat research with a stated method and the number in the title (Otterly, Peec, Ahrefs);
  controlled experiments with a public tracker (Otterly); repeatable series (Otterly country index);
  machine-readable `.md` copies of studies (Peec); "Open in ChatGPT/Claude" buttons (Profound); a free
  tool that previews visibility (Ahrefs); worked example outputs in the skills repo (SE Ranking);
  third-party validation inside the data (Scrunch+Bain, Profound+Kevin Indig, Semrush+Adobe) `[COMP]`.
- **Beat:** release the dataset (CSV/JSON, licence, prompts) where Ahrefs, Semrush, Profound give charts
  only; state limits and prompt selection where Semrush is thin; publish a head-to-head with a disclosed
  method and conflict of interest instead of a "best of"; a fully free open skill where Otterly's is
  gated `[COMP]`.
- **Skip for now:** self-promotional listicles as the main play `[PEEC-L]`; chasing a funding/PR story;
  a paid community first (large repos had audiences before the repo; inference) `[COMP]`.

## 5. Case studies

No independent, rigorously measured case of a small devtool going from absent to cited in unbranded
AI answers was found. Evidence is vendor self-reports, correlational studies, one revealed-preference
study of coding agents, and open-source growth stories `[CASES]`.

| Case | Finding | Confidence |
|---|---|---|
| Claude Code default picks (Amplifying, Feb 2026) | 2,430 responses, 20 categories: Stripe 91.4%, shadcn/ui 90.1%, Vercel 76.8%, Resend 62.7%; Prisma 79% (Sonnet 4.5) to 0% (Opus 4.6) with Drizzle 21% to 100%. Authors say picks reflect training data, RLHF and system prompt `[AMP]` | High for what it measures |
| Vercel (self-reported) | ChatGPT refers "around 10%" of new signups (from 4.8% a month earlier, 1% six months earlier); advice: original data, SSR/static HTML, JSON-LD, seed Reddit/GitHub/HN/Stack Overflow, 30/90/180-day refresh. No attribution to one tactic `[VERCEL]` | Medium |
| Ahrefs 75k brands | YouTube mentions ~0.737, branded web mentions 0.66-0.71, branded anchors 0.51-0.63, DR 0.27-0.33, pages on site ~0.19; brands with DR above 40 only; correlation `[AHR-BRAND]` | Medium |
| SparkToro/Gumshoe variance | 2,961 prompts, 12 run 60-100 times: same brand list under 1%, same order under 0.1%; visibility percentage steadier than rank `[SPARK]` | Medium-high |
| Seer Interactive | Google page-one rank correlates ~0.65 with GPT-4o brand mentions; backlinks weak; GPT-4o only `[SEER]` | Medium |
| Ramp via Profound | AP visibility 3.2% to 22.2% in a month; vendor case, no method or date `[CASES]` | Low-medium |
| Gumlet via DerivateX | Entity consistency, glossary, G2/PeerSpot reviews, "alternative" clusters; claims AI-referred traffic is 20% of inbound revenue; agency self-report `[CASES]` | Low |
| Resend, Firecrawl, AFFiNE | Open-source distribution (react-email; open core and integrations; concentrated Reddit/HN/Product Hunt launch). Growth documented by investors/founders; no source ties them to AI picks; survivorship bias `[CASES]` | Medium (growth), low (AI link) |
| Context7, skills.sh / agent-browser | Tools that fix agent pain spread fast through MCP/skills; cause of agent-browser's surge unattributed `[CASES]` | Medium |
| Supabase agent-skills | A vendor skills repo with small uptake: vendor skills alone don't produce a rush **[unverified]** `[CASES]` | Low |
| Tailwind (counter-case) | Default pick, yet docs traffic and revenue fell sharply (press reports) **[unverified]**: being picked is not commercial success `[CASES]` | Medium |

**Strongest tactics for a small GEO/devtool company, by evidence** `[CASES]`:
1. Earn third-party mentions where engines pull from (correlation 0.66-0.71; Vercel advice).
2. Get placed in third-party "best X" lists; publish only a few honest comparison pages yourself.
3. Ship runtime context for coding agents: MCP server, CLI, skills listed on skills.sh.
4. Publish a focused open-source tool with a conversion-oriented README.
5. Concentrate launches (HN, Reddit, Product Hunt) and answer comments; evidence is self-reported and one
   preprint reportedly finds Show HN has no advantage after controls **[unverified]**.
6. Answer first; static/server-rendered HTML.
7. Entity consistency plus review/profile presence (G2, directories) (agency self-report).
8. Rank in Google for target queries (Seer).
9. Original data, quotes, citations, refreshed on a cadence (Vercel; GEO paper).
10. Measure with fixed prompt panels repeated many times; report visibility %, not rank (SparkToro).

**Not supported:** llms.txt for citation lift; vendor before/after numbers as proof; tracking rank in AI
answers; content volume (page count ~0.19); backlinks as the main lever; displacing a coding-agent
default through content alone; assuming AI visibility pays off commercially; relying on one platform
(a reported 91% of citations appear on only one of three platforms is **[unverified]**) `[CASES]`.

## 6. Research-backed rules

### What the research says

| Source | What was tested | Key findings and limits |
|---|---|---|
| Original GEO paper (KDD 2024, peer-reviewed) `[GEO24]` | 9 rewrite methods on GEO-bench; simulated engine (gpt-3.5-turbo over top-5 Google results) plus a 200-query Perplexity subset; metrics PAWC and a GPT-3.5 judge | Quotation Addition +39.5% PAWC, Statistics Addition +29.2%, Fluency +26.7%, Cite Sources +26.2%, Keyword Stuffing -9.2%. Perplexity: Cite Sources +11.2% PAWC but -23.1% subjective. Helps low-ranked sites (+97 to +115%) and hurts rank-1 (-20 to -30%). "Up to 40%" is an upper bound; simulated engine; text and tables differ slightly |
| CORE (preprint, arXiv 2602.03608, v2 21 Oct 2026; no venue found) `[CORE]` | Amazon ProductBench, 15 categories x 200 products, target placed last of 10; GPT-4o, Gemini-2.5, Claude-4, Grok-3; black-box rewriting of the target item | Average promotion 91.4% Top-5, 86.6% Top-3, 80.3% Top-1 vs 0% baseline; review-style text rated 4.6/5 fluency and detected as optimised 18.4% of the time; uses ranking feedback loops, i.e. persuasive rank manipulation. Authors note manipulation risk |
| LIVE-GEO (preprint, arXiv 2611.01126, 31 Oct 2026) `[LIVE]` | 80 fictional brands, original page plus five GEO rewrites published live, prices frozen, order randomised; consumer engines and API models | Top-1: CORE 76.3% (ChatGPT), 67.5% (Grok), 66.3% (Gemini); Original 2.5%, 0%, 10%. **Claude API reversed**: Original 44.9%, CORE 2.6%. E-GEO, AgenticGEO, C-SEO, Statistics Addition near baseline on consumer engines. Engines agree on the top product for only 48.8-66.3% of brands. Same method ranged 73.8% to 93.8% by candidate order. Numerical-faithfulness check flagged 86 of 400 rewrites (all 80 Statistics Addition). Authors: aggregate gains partly survive the live web; most brand-level gains do not. Limits: fictional brands, CORE tuned with live ChatGPT feedback, so the margin is not independent |
| Sprinklr, SIGIR'26 (peer-reviewed) `[SPRK]` | 252,000 controlled trials, 6 models; two pages differing in one of 18 factors | Gatekeepers (odds ratio above 100): off-topic content, missing price, old timestamp, lower list position. Moderate: completeness, trust cues (hedging, no evidence, contradictions), competitive comparison. No reliable effect: formatting and structure; promotional tone and social proof in only 2-3 models. Limits: two candidates, product reviews |
| Moore & Dunne (preprint) `[MD]` | ~2.1M citations, 19 B2B SaaS workspaces, 10,042 pages | Prompt-to-page alignment is the largest page-level predictor (beta +0.37); domain authority dominates (about 6x); FAQ, TL;DR and structured data effects shrink to zero with domain controls; median cited passage about a third down the page. Observational, one vertical |
| Zhang et al. (preprint) `[ZHG]` | 602 prompts, 21,143 citations, ChatGPT/AIO/Perplexity | Influential pages are longer with more headings and lists; Q&A format -5.7%. Descriptive, constructed metric, conflicts with `[SPRK][MD]` |
| Chen et al. (preprint) `[CHEN]` | 1,000 consumer prompts, 4 engines vs Google | AI answers lean on earned media (e.g. 81.9% earned, 18.1% brand for GPT automotive US; 92.1% earned for electronics); social near zero in AI answers; low overlap with Google results |
| E-GEO, AgenticGEO, AutoGEO (preprints) `[EGEO][AGEO][AUTOGEO]` | Prompt-optimised rewriting on benchmarks | Strong in-benchmark gains; near baseline on live engines in LIVE-GEO. AutoGEO's shared rules: cite credible sources, comprehensive coverage, factual accuracy, neutral tone, logical structure, clear language, up-to-date information |
| Ahrefs schema test `[AHR-SCHEMA]` | 1,885 pages that added JSON-LD vs 4,000 matched controls, difference-in-differences | ChatGPT +2.2%, AI Mode +2.4% (indistinguishable from zero), AI Overviews -4.6%. Pages already had 100+ AIO citations |
| llms.txt `[AHR-LLMS][SER-LLMS][GOOG]` | Ahrefs 137,210 domains (97% of valid files got zero requests); SE Ranking ~300k domains (no correlation) | No measured citation lift; Google says it uses neither llms.txt nor special markup for AI features. Measures fetches or correlation, not causation |
| Freshness `[AHR-FRESH]` | 17M citations | Cited URLs average 1,064 days old vs 1,432 for organic (ChatGPT strongest, AI Overviews the exception). Snippet only |

### Rules for our pages (checkable)

| # | Rule | Strength |
|---|---|---|
| 1 | Answer the target question in the first 2-3 sentences (about 40 words); keep key facts in the top third `[MD]` | moderate |
| 2 | Match the exact query phrasing in title, intro, headings `[MD][SPRK]` | strong |
| 3 | State price, specs, availability in visible text (not only images or schema) `[SPRK]` | strong for product pages |
| 4 | Visible published and last-updated dates; update only when content changes; refresh key pages on a schedule `[SPRK][AHR-FRESH][VERCEL]` | moderate |
| 5 | Named, dated, **verifiable** statistics with links; drop numbers we cannot source `[GEO24][LIVE]` | mixed |
| 6 | No keyword stuffing; neutral, specific tone `[GEO24][SPRK]` | strong against stuffing |
| 7 | Remove hedging, contradictions, unsupported claims `[SPRK]` | moderate |
| 8 | Comparison tables/explicit alternatives where users are choosing `[SPRK][ZHG]` | weak-moderate |
| 9 | Cover the topic fully with definitions, steps, numbers, code `[AUTOGEO][ZHG]` | weak-moderate |
| 10 | Do not add FAQ blocks, structure or length for their own sake `[SPRK][MD][GOOG]` | moderate (negative rule) |
| 11 | JSON-LD only where it matches visible content and serves rich results, not as a citation tactic `[AHR-SCHEMA][GOOG]` | strong that it is not a lever |
| 12 | Real authorship and first-hand data (tests, screenshots) `[GOOG]` | weak for citation |
| 13 | Server-rendered text; allow search/answer crawlers; check Bing and Brave indexing (retrieval-layer claims are blog-sourced, **[unverified]**) `[GOOG][VERCEL]` | inference |
| 14 | Earn third-party mentions; never buy or fake them `[CHEN][AHR-BRAND][GOOG]` | moderate (correlational) |
| 15 | Measure on a fixed prompt panel with repeated runs per engine `[LIVE][SPARK]` | method |

### Rules for the README / skill repo
Almost no study tests READMEs, topics, stars or AGENTS.md as recommendation drivers; items below are inference
from the page rules unless a source is shown.

1. First sentence says what it does and for whom, in query wording (`[MD][SPRK]`, inference).
2. What / install / one example in the first screen (`[MD]` position finding, inference).
3. Exact, working install commands, several hosts (`[SKILLS-FAQ][SKILLREPOS]`).
4. One committed example input and output (`[SKILLREPOS]` SE Ranking; `[ZHG]`).
5. Descriptive headings; "when to use / not use" and a short comparison (`[SPRK]`, inference).
6. Versions, dates, release notes (`[SPRK][AHR-FRESH]`, inference).
7. GitHub topics and description (no study; competitor practice `[SKILLREPOS]`).
8. Keep AGENTS.md short and non-obvious; context files raised agent cost 20%+ with no significant success
   gain (task-success study, not discoverability) `[AGENTSMD]`.
9. llms.txt optional hygiene, no expected lift `[AHR-LLMS][SER-LLMS][GOOG]`.
10. Earn stars, third-party mentions and real usage (popularity bias in LLM library choice `[LIBPOP]`).
11. No hidden instructions or prompt-injection text aimed at AI readers: it works in labs `[CORE][LIVE]` but
    violates Google's policy `[GOOG]`, and is not what we want to be known for.

### Not supported by the evidence
Guaranteed citations; llms.txt or schema as citation levers; structure/FAQ as independent drivers;
prompt-tuned GEO rewriting working on live engines; GEO-paper gains transferring to production engines;
an "ideal" length; any one claim about which index feeds which engine (blog-sourced); causal readings of
brand-mention correlations; any README/topics/stars effect on recommendations.

## 7. Our own presence (audit, 2026-11-05) `[AUDIT]`

| Property | Good | Gaps |
|---|---|---|
| topcited.ai crawl access | robots.txt allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot and others; sitemap and llms.txt exist; home has Organization, WebSite, SoftwareApplication, FAQPage JSON-LD; 51 server-rendered blog posts | No explicit `Claude-SearchBot` group; no `/llms-full.txt`; sitemap lastmod identical for every URL; `/try-geo`, `/try-sci-defense`, `/tools/distortion` missing from the sitemap while `/login` and `/register` are; llms.txt omits /benchmark, /methodology, /counter-examples, the free tools and livegeobench.com and names only ChatGPT, Perplexity, Gemini |
| /pricing | n/a | ~84 words in server HTML (plan content client-rendered); no Offer markup |
| Content | Foundational GEO/AEO posts, tool roundups, how-to-track posts, citation data studies | No comparison or alternatives pages, no glossary, no per-feature pages (`/features/*` 404), no /support or /about; two near-duplicate pairs of posts; Organization author, dateModified = datePublished |
| Research claims | /methodology gives 91.4% / 86.6% / 80.3% promotion rates and says "peer-reviewed" | No paper title, authors or arXiv link; CORE is a preprint with no venue found; the site says validated on four models while the newer LIVE-GEO paper shows the Claude API ranking CORE last on the live web `[LIVE]`; /benchmark has no BibTeX, results or paper link |
| livegeobench.com | Open robots with rationale, good llms.txt, 1,070-URL sitemap | No "how to cite", no paper link, product pages have no structured data (by design), blog excluded from sitemap |
| GitHub | Skills repo has relevant topics, MIT | Org has no description or website; `topcited-cli` has no topics; no releases/tags on topcited-skills; 10 stars at audit time |
| Third-party | Capterra listing, a UIUC DREAM lab post linking /methodology | 0 reviews; no G2 / AlternativeTo / Product Hunt / Reddit presence; name collision with Scopus/INSPIRE |

Claim accuracy matters for GEO: engines and readers check numbers. Wire every figure on /methodology and
/benchmark to its paper, say "preprint" unless a venue is confirmed, and describe CORE's results with
LIVE-GEO's model-dependence included.

## 8. Plan (v2, re-prioritised)

Impact and effort: H/M/L. **Owner**: *code* = change in the topcited.ai site or backend (another repo, not
made here); *this repo*; *account* = needs a person with the TopCited account or a third-party submission.
Anything that publishes, posts or submits needs your explicit approval first, one at a time.
"Old #" = number in plan v1; "Δ" = change and why. Status as of the end of this PR.

### P0: fix what we own (queries G1-G5, G9-G12, G14)

| # | Old | Action | Groups | Impact / effort | Owner | Status | Δ and evidence |
|---|---|---|---|---|---|---|---|
| 1 | 1 | Server-render /pricing with plans, prices, trial terms; add Offer markup for rich results only | G1, G7, G14 | H / L | Code | Not started | Kept. Crawlable text matters (AI crawlers largely skip JS `[VERCEL]`); markup is not a citation lever `[AHR-SCHEMA]` |
| 2 | 2 | Link CORE and LIVE-GEO from /methodology and /benchmark; authors, BibTeX, define "promotion rate"; say "preprint"; state CORE's model-dependence (Claude API reversed) | G4, G12, G14 | H / L | Code + author check | Not started | **Up.** Newer paper contradicts a blanket "validated on four models" reading `[LIVE]`; unverifiable claims are penalised `[LIVE][SPRK]` |
| 3 | 3 | Sitemap: add /try-geo (or canonicalize), /try-sci-defense, /tools/distortion; drop /login, /register; real lastmod | all | M / L | Code | Not started | Kept. Real dates matter for freshness `[AHR-FRESH][SPRK]` |
| 4 | 4 | robots.txt: explicit `Claude-SearchBot` group | G3 | L / L | Code | Not started | Kept |
| 5 | 5 | Update topcited.ai llms.txt (benchmark, methodology, free tools, Claude in blurb) | G3, G11, G12 | L / L | Code | Not started | **Down.** No measured citation lift `[AHR-LLMS][SER-LLMS][GOOG]`; `/llms-full.txt` dropped |
| 6 | 6 | Visible named authors with real sameAs, honest last-updated dates; **drop FAQPage markup as a citation tactic** | G5 | M / L | Code | Not started | **Down/reframed.** FAQ and schema null `[AHR-SCHEMA][MD]`; freshness and authorship kept `[SPRK][GOOG]` |
| 7 | 7 | Consistent "TopCited.ai" naming + sameAs | G14 | M / L | Code + account | Not started | Kept |
| 8 | new | Answer-first rewrite of home, /features, pricing-faq and top blog posts by the page rules in section 6 (first 40 words, query phrasing, sourced stats, dates) | G1-G5 | H / M | Code + account (copy) | Not started | **New** `[MD][SPRK][GEO24]` |

### P1: pages and data that target the query groups

| # | Old | Action | Groups | Impact / effort | Owner | Status | Δ and evidence |
|---|---|---|---|---|---|---|---|
| 9 | 8 | Honest head-to-head pages (vs Profound / Peec / Otterly / Semrush) with disclosed method and conflict of interest; not "best of" lists | G1, G2 | M / M | Code + account (copy) | Not started | **Down from H.** Self-promo lists ~11% of citations, 3.6% on ChatGPT, and can lead to a competitor `[PEEC-L][AHR-LISTS]`; a base for outreach, not a substitute |
| 10 | 9 | Per-feature pages under /features/*, each answering one problem-first question up front | G1-G10 | H / M | Code + account (copy) | Not started | Kept `[MD][SPRK]` |
| 11 | 10 | Glossary hub linking existing definitional posts | G5 | M / L | Code | Not started | Kept |
| 12 | 11 | Original data study from real runs, numbers in the title, stated method and limits, prompts published, **plus a downloadable CSV/JSON with licence and a machine-readable `.md` copy** | G1, G5, G8 | H / M | Account (data) + code | Not started | **Up.** The visible playbook of Peec, Otterly, Profound, Semrush, Ahrefs `[COMP]`; none releases data, so the dataset is the differentiator |
| 13 | new | Controlled-experiment series with a public tracker (e.g. our own date, sourcing and structure tests; LIVE-GEO results) | G4, G5, G12 | H / M | Account (data) + code | Not started | **New.** Otterly's programme `[COMP]`; must use fixed prompts and repeated runs `[SPARK][LIVE]` |
| 14 | new | "What do coding agents recommend for SEO/GEO?" revealed-preference study, using this repo and our baseline as seed | G3, G11 | M / M | Account + this repo | Not started | **New.** Amplifying's design `[AMP]`; Profound's Claude-Code study angle `[COMP]` |
| 15 | 12 | Rebuild /try-sci-defense and /tools/distortion as tool pages (problem-first H1, example results, method, in sitemap); cross-link from every study | G9, G10 | H / M | Code | Not started | Kept. Open space `[R1-BASE][BASE]`; free-tool model `[COMP]` |
| 16 | 13 | LIVE-GEO landing page on topcited.ai and "how to cite" on livegeobench.com; link the dataset | G12 | M / L | Code | Not started | Kept |
| 17 | 14 | Consolidate near-duplicate posts | G5 | L / L | Code | Not started | Kept |

### P2: be in the sources AI engines read (every outward step needs your approval)

| # | Old | Action | Groups | Impact / effort | Owner | Status | Δ and evidence |
|---|---|---|---|---|---|---|---|
| 18 | 15 | Complete Capterra; get real customer reviews; add G2 and AlternativeTo early | G1, G2 | H / M | Account | Not started | **Up.** G2 is a top-10 cited domain `[PEEC-D]`; rivals' review counts are small `[COMP]` |
| 19 | 16 | Pitch honest inclusion to authors of "best AI visibility tools" and "alternative" pages; no paid placement | G1, G2 | H / M | Account | Not started | **Up.** "Best X" lists are 43.8% of cited page types, rank on third-party lists drives recommendation `[AHR-LISTS]` |
| 20 | 18 | YouTube: "optimize my website with Claude Code/Codex" demo and a LIVE-GEO explainer | G3, G11, G12 | M / M | Account | Not started | **Up.** YouTube mentions had the highest correlation (~0.737) `[AHR-BRAND]`; top-cited domain `[PEEC-D]` |
| 21 | 17 | Useful community posts (Reddit, Show HN, dev.to, Hashnode) with affiliation disclosed | G3, G11 | M / M | Account | Not started | Kept; Reddit share is volatile, Show HN advantage unproven **[unverified]** `[CASES]` |
| 22 | 20 | Research distribution: arXiv cross-links, Semantic Scholar, Hugging Face paper page; ask the DREAM lab to link livegeobench.com and the skills repo | G4, G12 | M / L | Account | Not started | Kept |
| 23 | new | Co-publish LIVE-GEO or study data with an independent researcher or publication | G1, G12 | M / M | Account | Not started | **New.** Third-party validation in data (Scrunch+Bain, Profound+Indig, Semrush+Adobe) `[COMP]` |
| 24 | new | One customer case study with a hard number and permission | G1, G4 | M / M | Account | Not started | **New.** Peec/SIXT +320% (index only) `[COMP]`; vendor self-report, so state method |
| 25 | 19 | Product Hunt launch of the skills repo or free tools | G9, G11 | L / M | Account | Not started | **Down.** No Product Hunt data for any rival could be fetched `[COMP]` |

### P3: the skills repo

| # | Old | Action | Groups | Impact / effort | Owner | Status | Δ and evidence |
|---|---|---|---|---|---|---|---|
| 26 | 21 | README: problem phrasing, one-line install, example output | G3, G11 | M / L | This repo | **Done in PR #11** | Kept `[SKILLREPOS]` |
| 27 | 22 | Skill descriptions use the phrases people type | G3, G11 | M / L | This repo | **Done in PR #11** | Kept |
| 28 | new | Evidence-calibrated skill: `references/evidence.md`, caveats on schema/llms.txt, audit messages say "no measured citation lift" | G3 | M / L | This repo | **Done in PR #11** | **New.** `[AHR-SCHEMA][AHR-LLMS][SER-LLMS][GOOG]` |
| 29 | new | More committed example outputs (our own properties) and a before/after example on an improvement PR | G3, G11 | M / L | This repo | Not started | **New.** SE Ranking ships 25 examples and requires before/after `[SKILLREPOS]` |
| 30 | 23 | Tag v0.2.0 after merge; GitHub topics (`claude-code-skill`, `ai-seo`, `llm-seo`, `mcp`, `codex`, `cursor`, `llms-txt`); org description and website | G11 | M / L | Account (repo admin) | Not started | Kept `[SKILLREPOS]` |
| 31 | 24 | Drive real installs: `npx skills add TopCited/topcited-skills` linked from /developers, docs, blog | G3, G11 | H / M | Account + code | Not started | Kept. Installs populate skills.sh `[SKILLS-FAQ]` |
| 32 | 25 | Registry/list submissions: Anthropic directory, Cursor marketplace, MCP Registry, claudemarketplaces.com, awesome-claude-skills (PR), awesome-claude-code (issue/collaborators), VoltAgent, Composio, mcp.so, Glama, ClawHub | G11 | M / M | Account (approval each) | Not started | Kept; contribution routes updated `[SKILLREPOS]` |
| 33 | 26 | /features/mcp page and MCP Registry entry (needs OAuth for claude.ai/ChatGPT) | G11 | M / M | Code + account | Not started | Kept |
| 34 | new | Skills repo "works with / extensions" list linking complementary tools | G11 | L / L | This repo | Not started | **New, weak.** claude-seo does this; backlink effect unverified `[COMP]` |

Order of work: weeks 1-2: 1-8, 26-30 (cheap, unblock the rest, fix accuracy first); weeks 2-6: 9-17, 29, 31;
ongoing and approval-gated: 18-25, 32; measure from the first week.

## 9. Measurement

1. **Baseline now (done for 2 engines, free):** [geo-baseline/](geo-baseline/). Repeat the same 15 queries monthly;
   run [geo-manual-check.md](geo-manual-check.md) for ChatGPT app, Perplexity, Gemini, Copilot, AI Overviews and Claude.ai.
2. **Method:** fixed prompt panel, 3 runs per query per engine, report mention rate (runs with a mention / runs),
   not rank; lists rarely repeat `[SPARK]`; test engines separately since they differ widely `[AUTH][LIVE]`.
3. **TopCited tracking (spends T-coins; not run):** one brand for TopCited with competitors (Profound, Peec AI,
   Otterly.AI, AthenaHQ, Semrush AI Visibility, Ahrefs Brand Radar), one query set per group from
   [geo-queries.csv](geo-queries.csv), created with `--manual` (auto sets run and spend daily). Cost: 1 T-coin per
   query per engine per run; 77 queries x 3 engines is about 231 per run; the 40 non-definition queries in
   G1-G4 and G11 is 120. `topcited monitor run <set> --dry-run` prints the exact estimate first. Platforms per
   the CLI guide: `chatgpt`, `gemini`, `grok`, `deepseek`, `google`, `bing`, `brave`, `baidu_search`.
4. **Metrics:** mention rate, citation rate (our URLs among cited sources), share of voice vs competitors, per
   group and engine; plus AI-referral traffic in analytics and skills.sh installs.
5. **Review:** judge trends over at least 3 monthly checks; no outcome is promised.

## 10. Follow-ups outside this repo (not made)

topcited.ai site/backend: items 1-8, 10, 11, 15-17, 33, plus MCP OAuth. Update `SKILLS_PLUGIN_COMMANDS` on
/developers to `topcited@topcited`. Review the "validated on four models" and "peer-reviewed" wording on
/methodology against `[LIVE][CORE]`.

## 11. Caveats

- Round-2 reports were produced by research agents reading public pages; where a page failed to load
  (G2, Product Hunt, Capterra, Search Engine Land, several GitHub READMEs) claims are marked or omitted.
- Competitor star counts, funding and vendor study numbers are secondary; none are used as claims in the repo.
- The real-AI baseline used coding-agent CLIs, one run per query; it is directional only.
- The AuthorityTech ledger is from a competitor; treat as indicative.
- LIVE-GEO and CORE share authors and CORE was tuned with live ChatGPT feedback, so the CORE-vs-rest margin is not independent `[LIVE]`.

## Sources

Search and fetch results consulted 2026-11-05.

- `[BASE]` this repo, [geo-baseline/](geo-baseline/) (Claude Code 2.1.318; Codex 0.165.0).
- `[R1-BASE]` round-1 web-search baseline by research agent (33 queries); `[AUDIT]` round-1 audit of topcited.ai, livegeobench.com, GitHub, arXiv, third-party mentions.
- `[COMP]` competitor playbook research: tryprofound.com/blog (e.g. /where-do-ai-citations-come-from), peec.ai/blog, otterly.ai/blog, semrush.com/blog/most-cited-domains-ai/ and semrush.com/news/463141-..., ahrefs.com/blog/ai-overview-brand-correlation/, scrunch.com/blog, athenahq.ai/blog, seranking.com/blog/profound-alternatives/.
- `[SKILLREPOS]` github.com/AgriciDaniel/claude-seo, github.com/coreyhaines31/marketingskills, github.com/zubair-trabzada/geo-seo-claude, github.com/seranking/seo-skills, github.com/aaron-he-zhu/aaron-marketing-skills, github.com/travisvn/awesome-claude-skills, github.com/hesreallyhim/awesome-claude-code, star-history.com.
- `[SKILLS-FAQ]` skills.sh/docs/faq.
- `[PEEC-L]` peec.ai/blog/self-promotional-listicles-analysis-from-232k-citations; `[PEEC-D]` docs.peec.ai/research/most-cited-domains-in-ai-search.md.
- `[AHR-LISTS]` ahrefs.com/blog/best-lists-research/ (2025-12-04); `[AHR-BRAND]` ahrefs.com/blog/ai-brand-visibility-correlations (2025-12-12) and ahrefs.com/blog/ai-overview-brand-correlation/ (2025-05-26); `[AHR-SCHEMA]` ahrefs.com/blog/schema-ai-citations/ (2026-05-11); `[AHR-LLMS]` ahrefs.com/blog/llmstxt-study/ (2026-06-15); `[AHR-FRESH]` ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/ (snippet).
- `[SER-LLMS]` searchenginejournal.com/llms-txt-shows-no-clear-effect-on-ai-citations-based-on-300k-domains/ and seranking.com/blog/llms-txt/.
- `[GOOG]` developers.google.com/search/docs/fundamentals/ai-optimization-guide.
- `[SPARK]` searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242; `[SEER]` seerinteractive.com/insights/what-drives-brand-mentions-in-ai-answers.
- `[AMP]` amplifying.ai/research/claude-code-picks/report; `[VERCEL]` vercel.com/blog/how-were-adapting-seo-for-llms-and-ai-search; `[CASES]` case-study research (Ramp/Profound at casestudies.com, Gumlet/DerivateX at derivatex.agency, a16z.com/announcement/investing-in-resend/, firecrawl.dev/blog/firecrawl-v2-series-a-announcement, vercel.com/blog/introducing-skills, devclass.com tailwind report, others in the PR notes).
- `[AUTH]` authoritytech.io/blog/profound-review-alternatives-2026 (competitor; related-party).
- Papers: `[GEO24]` arxiv.org/abs/2311.09735; `[CORE]` arxiv.org/abs/2602.03608; `[LIVE]` arxiv.org/abs/2611.01126; `[SPRK]` arxiv.org/abs/2605.25517 (SIGIR'26); `[MD]` arxiv.org/abs/2609.35077; `[ZHG]` arxiv.org/abs/2604.25707; `[CHEN]` arxiv.org/abs/2509.08919; `[EGEO]` arxiv.org/abs/2511.20867; `[AGEO]` arxiv.org/abs/2603.20213; `[AUTOGEO]` arxiv.org/abs/2510.11438; `[AGENTSMD]` arxiv.org/abs/2602.11988; `[LIBPOP]` arxiv.org/abs/2507.10818.
