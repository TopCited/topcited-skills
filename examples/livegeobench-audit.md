# Example output: audit.py on a real site

Raw output of `python3 skills/optimize-website/scripts/audit.py https://livegeobench.com --pages 4`, run 2026-11-05. The agent turns this into the ranked report and rewrites described in [SKILL.md](../skills/optimize-website/SKILL.md). Findings are facts from the fetched HTML, not judgments.

```text
# Audit: https://livegeobench.com

## Site level
- no site-level problems found
- AI crawler access: GPTBot=allowed; OAI-SearchBot=allowed; ChatGPT-User=allowed; ClaudeBot=allowed; Claude-SearchBot=allowed; Claude-User=allowed (via *); PerplexityBot=allowed; Perplexity-User=allowed; Google-Extended=allowed; Applebot-Extended=allowed; CCBot=allowed (via *); Bytespider=allowed (via *)
- llms.txt: HTTP 200
- sitemap https://livegeobench.com/sitemap.xml: HTTP 200, 1070 URLs

## https://livegeobench.com
- title (47): 'LIVE-GEO benchmark: GEO in real-world AI search'
- meta description: 'An open benchmark that measures how generative-engine optimisation methods change which products live AI search engines cite.'
- h1: ['A benchmark for evaluating Generative Engine Optimization in real-world search environments.']  |  h2 count: 1  |  words: 354
- structured data: ['Organization', 'WebSite']
- ISSUE: 3/3 images lack alt text

## https://livegeobench.com/s/live-geo-20261015-r4/
- title (116): 'LIVE-GEO — evaluating Generative Engine Optimization in real-world searchAgenticGEOCOREC-SEOE-GEOStatistics Addition'
- meta description: 'LIVE-GEO publishes fictitious products and their GEO rewrites on the public web so that any AI search tool can rank them.'
- h1: ['A benchmark for evaluating Generative Engine Optimization in real-world search environments.']  |  h2 count: 2  |  words: 1101
- structured data: none
- ISSUE: title length 116 (aim ~30-60)
- ISSUE: no JSON-LD structured data
- ISSUE: 75/75 images lack alt text
- ISSUE: no Open Graph tags

## https://livegeobench.com/s/live-geo-20261015-r4/about.html
- title (20): 'About LIVE Benchmark'
- meta description: 'What this catalogue is, and what it is not.'
- h1: ['Clear information, without a checkout']  |  h2 count: 4  |  words: 278
- structured data: none
- ISSUE: meta description length 43 (aim ~110-160)
- ISSUE: no JSON-LD structured data
- ISSUE: no Open Graph tags

## https://livegeobench.com/s/live-geo-20261015-r4/family-acoustic-spaces.html
- title (36): 'Acoustic spaces · LIVE-GEO catalogue'
- meta description: 'An ambient-floor audition vault is a site listed in this catalogue under Acoustic spaces. Listings in this category are described on the same six attributes: floor_area_m2, noise_floor_dba, occupancy, session_length_hours, session_fee_usd, isolation_method.'
- h1: ['Acoustic spaces']  |  h2 count: 1  |  words: 206
- structured data: none
- ISSUE: meta description length 257 (aim ~110-160)
- ISSUE: no JSON-LD structured data
- ISSUE: no Open Graph tags
```
