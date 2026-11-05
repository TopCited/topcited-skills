# GEO tracking queries

77 queries derived from what TopCited actually does, grouped by feature. Machine-readable copy: [geo-queries.csv](geo-queries.csv) (use it as the tracking set, see [geo-plan.md](geo-plan.md#measurement)).

Intent: **problem-first** (names no tool), **tool-seeking**, **agent-skill**, **research / definition**. *Should win* = which property ought to be the answer: topcited.ai (product), topcited-skills (this repo), livegeobench.com / papers (research), or both.

## G1. AI visibility tracking

Product basis: Monitoring runs across AI engines (ChatGPT, Gemini, Grok, search engines), visibility summary.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q01 | problem-first | why doesn't ChatGPT mention my brand | founder | topcited.ai |
| Q02 | problem-first | how to track my brand in AI answers | marketer | topcited.ai |
| Q03 | problem-first | how to check if ChatGPT recommends my product | founder | topcited.ai |
| Q04 | problem-first | how often does Perplexity cite my website | SEO | topcited.ai |
| Q05 | problem-first | how to monitor brand mentions in ChatGPT Gemini and Claude | brand manager | topcited.ai |
| Q06 | tool-seeking | best AI visibility tracker | marketer | topcited.ai |
| Q07 | tool-seeking | best tool to track brand mentions in LLM answers | brand manager | topcited.ai |
| Q08 | tool-seeking | AI search visibility tool for small business | founder | topcited.ai |
| Q09 | tool-seeking | cheap alternative to Profound for AI visibility | founder | topcited.ai |
| Q10 | tool-seeking | Otterly AI alternative | SEO | topcited.ai |
| Q11 | tool-seeking | Peec AI alternative | agency | topcited.ai |
| Q12 | tool-seeking | TopCited vs Profound | SEO | topcited.ai |
| Q13 | agent-skill | MCP server to track brand visibility in AI search | developer | both |

## G2. Competitors and share of voice

Product basis: Competitor tracking, gaps, share of voice.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q14 | problem-first | how to measure share of voice in AI search | marketer | topcited.ai |
| Q15 | problem-first | why does ChatGPT recommend my competitor instead of me | founder | topcited.ai |
| Q16 | problem-first | how to see which competitors AI engines cite for my keywords | SEO | topcited.ai |
| Q17 | tool-seeking | AI competitor benchmarking tool | brand manager | topcited.ai |
| Q18 | research / definition | what is LLM share of voice | marketer | both |

## G3. Site audit and AI crawler access

Product basis: Site audit incl. AI-crawler checks; this repo's optimize-website skill.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q19 | problem-first | how to optimize my website for AI search | founder | both |
| Q20 | problem-first | how to make my site visible to ChatGPT crawlers | developer | both |
| Q21 | problem-first | does robots.txt block GPTBot and ClaudeBot | developer | topcited-skills |
| Q22 | problem-first | how to add llms.txt to my website | developer | topcited-skills |
| Q23 | problem-first | what schema markup helps AI search citations | SEO | both |
| Q24 | tool-seeking | free GEO audit tool | founder | both |
| Q25 | tool-seeking | free AI SEO checker for my website | founder | both |
| Q26 | agent-skill | SEO audit skill for Claude Code | developer | topcited-skills |
| Q27 | agent-skill | optimize my website with Claude Code | developer | topcited-skills |

## G4. Content Optimizer (GEO + CORE)

Product basis: CORE / GEO rewrite-simulate-score loop, product-content optimization.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q28 | problem-first | how to rewrite content so AI cites it | content marketer | both |
| Q29 | problem-first | how to get cited by ChatGPT and Perplexity | marketer | both |
| Q30 | problem-first | how to rank product pages in ChatGPT shopping recommendations | ecommerce | topcited.ai |
| Q31 | problem-first | what content format do LLMs cite most | SEO | both |
| Q32 | tool-seeking | best tool to optimize content for generative engines | marketer | topcited.ai |
| Q33 | tool-seeking | AI tool to rewrite product descriptions for ChatGPT recommendations | ecommerce | topcited.ai |
| Q34 | research / definition | what is the CORE method for generative engine optimization | researcher | livegeobench.com / papers |
| Q35 | research / definition | GEO optimization methods compared (E-GEO AgenticGEO CORE) | researcher | livegeobench.com / papers |

## G5. GEO education / definitions

Product basis: Blog + methodology; seo-geo knowledge base.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q36 | research / definition | what is generative engine optimization | marketer | both |
| Q37 | research / definition | GEO vs SEO difference | marketer | both |
| Q38 | research / definition | what is answer engine optimization | marketer | both |
| Q39 | research / definition | GEO ranking factors | SEO | both |
| Q40 | research / definition | does schema markup help ChatGPT cite you | SEO | both |
| Q41 | research / definition | how long does GEO take to work | founder | both |

## G6. Keywords, prompts, pillar-cluster, trending

Product basis: Keyword & prompt recommendation, competitor keywords, pillar-cluster content, trending topics.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q42 | problem-first | how to find which prompts customers ask AI about my category | marketer | topcited.ai |
| Q43 | problem-first | how to build a pillar cluster content strategy for AI search | content marketer | both |
| Q44 | tool-seeking | AI keyword research tool for GEO | SEO | topcited.ai |
| Q45 | problem-first | how to find trending topics for my niche | content marketer | topcited.ai |
| Q46 | problem-first | how to find keyword gaps vs competitors | SEO | topcited.ai |

## G7. Reports and agencies

Product basis: Report generation (client reports).

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q47 | problem-first | how to report AI visibility to clients | agency | topcited.ai |
| Q48 | tool-seeking | white label AI visibility report for agencies | agency | topcited.ai |
| Q49 | tool-seeking | GEO platform for SEO agencies | agency | topcited.ai |

## G8. Marketing channels and posting

Product basis: Channel recommendations from cited-source data; posting automation.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q50 | problem-first | where should I post to get cited by AI engines | marketer | topcited.ai |
| Q51 | problem-first | which Reddit and Medium communities do AI engines cite for my industry | marketer | topcited.ai |
| Q52 | tool-seeking | tool to automate posting to Reddit LinkedIn Medium for brand visibility | marketer | topcited.ai |

## G9. AI Usage Detection (SCI-Defense)

Product basis: Free page scan for content engineered to game AI rankings.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q53 | problem-first | is a competitor manipulating AI search results with hidden text | SEO | topcited.ai |
| Q54 | problem-first | how to detect keyword stuffing aimed at LLM rankings | SEO | topcited.ai |
| Q55 | tool-seeking | free tool to detect AI-manipulated web pages | researcher | topcited.ai |
| Q56 | research / definition | what is generative engine manipulation or prompt injection in web content | researcher | livegeobench.com / papers |

## G10. Influencer Distortion System

Product basis: Distortion Index across YouTube, X, Weibo, Bluesky, Reddit.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q57 | problem-first | is this influencer post misleading | consumer | topcited.ai |
| Q58 | problem-first | how to measure emotional manipulation in influencer content | researcher | topcited.ai |
| Q59 | tool-seeking | influencer distortion index tool | researcher | topcited.ai |
| Q60 | research / definition | rhetorical distortion in influencer content multi-platform study | researcher | livegeobench.com / papers |

## G11. Agent skills, CLI, MCP

Product basis: topcited-skills, topcited CLI, hosted MCP, OpenAPI.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q61 | agent-skill | SEO skill for Claude Code | developer | topcited-skills |
| Q62 | agent-skill | GEO plugin for Cursor | developer | topcited-skills |
| Q63 | agent-skill | best agent skills for SEO | developer | topcited-skills |
| Q64 | agent-skill | Codex skill for SEO and AI search optimization | developer | topcited-skills |
| Q65 | agent-skill | claude code plugin marketplace SEO | developer | topcited-skills |
| Q66 | agent-skill | npx skills add SEO GEO | developer | topcited-skills |
| Q67 | agent-skill | open source GEO skills for AI coding agents | developer | topcited-skills |
| Q68 | agent-skill | CLI to check brand AI visibility from terminal | developer | both |

## G12. Research: LIVE-GEO, CORE, ProductBench

Product basis: livegeobench.com, arXiv papers.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q69 | research / definition | LIVE-GEO benchmark | researcher | livegeobench.com / papers |
| Q70 | research / definition | benchmark for evaluating generative engine optimization in real-world search | researcher | livegeobench.com / papers |
| Q71 | research / definition | do GEO methods actually work in live AI search | researcher | livegeobench.com / papers |
| Q72 | research / definition | ProductBench LLM product ranking benchmark | researcher | livegeobench.com / papers |

## G13. Agent Chat / end-to-end

Product basis: In-app agent that runs the workflow.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q73 | problem-first | AI agent that does SEO and GEO for me end to end | founder | topcited.ai |
| Q74 | tool-seeking | agentic growth platform for AI search | founder | topcited.ai |

## G14. Brand / navigational

Product basis: Name queries.

| # | Intent | Query | Persona | Should win |
|---|---|---|---|---|
| Q75 | research / definition | TopCited | any | both |
| Q76 | research / definition | what is TopCited.ai | any | both |
| Q77 | research / definition | TopCited review | any | topcited.ai |
