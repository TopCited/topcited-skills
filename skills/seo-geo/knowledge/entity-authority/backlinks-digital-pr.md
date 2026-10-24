---
topic: What makes backlinks valuable now, and why brand mentions outcorrelate them for AI citation
stage-relevance: [5, 7]
last-verified: 2026-10-24
sources:
  - https://developers.google.com/search/docs/essentials/spam-policies#link-spam (updated 2026-08-28; the old link-schemes URL redirects here)
  - https://colabdxb.ae/backlinks-in-2026-advanced-strategy-real-data-and-what-actually-works/ (heuristic, no traceable primary study)
  - https://ahrefs.com/blog/ai-overview-brand-correlation/ (Ahrefs 75,000-brand study, 2025-05-26)
  - https://ahrefs.com/blog/ai-brand-visibility-correlations/ (Ahrefs follow-up across ChatGPT, AI Mode, AI Overviews, 2025-12-12)
  - https://markets.financialcontent.com/wss/article/gnwcq-2025-12-2-earned-media-still-drives-generative-ai-citations-as-press-release-visibility-grows (Muck Rack "What is AI reading?", 2025-12-02, press-release mirror)
  - https://www.globenewswire.com/news-release/2026/05/07/3290268/0/en/generative-pulse-earned-media-consistently-drives-ai-citations-holding-at-84.html (Muck Rack Generative Pulse, 2026-05-07)
  - https://arxiv.org/abs/2311.09735 (Aggarwal et al., "GEO: Generative Engine Optimization," KDD 2024)
  - https://cracklepr.com/insights/ai-optimized-pr-playbook (heuristic, agency marketing claim)
  - https://www.loopexdigital.com/digital-pr/digital-pr-for-ai-visibility (heuristic, agency marketing claim)
---

# Backlinks and digital PR

## In plain words
A backlink still helps, but in 2026 the bigger story is that just being
*talked about* by name — mentioned in an article, a review, a YouTube video,
even without a link — correlates more strongly with showing up in AI answers
than having a link does. That shifts the smart move from chasing links for
their own sake toward earning genuine, independent mentions: real coverage,
reviews, and PR placements in outlets an AI assistant would treat as
trustworthy.

## What practitioners need to know

### Backlinks: the documented rule, and the industry numbers around it
- Google's link-spam policy is the primary source here: "Link spam is the
  practice of creating links to or from a site primarily for the purpose of
  manipulating search rankings" — buying/selling links, excessive link
  exchanges, automated link programs, and paid guest posts/advertorials
  without `rel="sponsored"`/`nofollow` are its named examples. The
  practical reading — a link counts when it's an editorial choice, not
  something paid for, traded, or automated — is an industry paraphrase of
  that policy, not Google's wording. Since 2026 the spam policy also covers
  "attempting to manipulate generative AI responses in Google Search," so
  manufactured mentions aimed at AI Overviews/AI Mode are in scope too.
- Widely repeated industry figures — "the #1 ranking result has ~3.8x more
  backlinks than positions 2–10," and "links on topically-matched DR50+
  domains produce ~2.8x greater ranking improvement than lower-relevance
  domains of comparable authority" — were **not traced to a named study or
  sample size** in the sources surfaced for this track. Treat both as
  *(heuristic)*, repeated as if factual across 2026 SEO-tool blogs but not
  independently verified here.

### The core shift: brand mentions now outcorrelate backlinks for AI citation
- **Ahrefs' 75,000-brand study** (first-party, disclosed methodology;
  original 2025-05-26 on AI Overviews, 2025-12-12 follow-up expanding to
  ChatGPT + AI Mode + AI Overviews) reports: branded web mentions correlate
  with AI Overview presence at **0.664**, versus backlinks at **0.218** —
  brand mentions roughly 3x more predictive than backlinks. Other
  correlations in the original: branded anchors 0.527, branded search
  volume 0.392, Domain Rating 0.326, referring domains 0.295. The December
  follow-up found branded web mentions at 0.664 (ChatGPT), 0.709 (AI Mode),
  and 0.656 (AI Overviews), and **YouTube mentions ~0.737** — the single
  strongest factor. Note the 0.664 and 0.737 figures come from two
  different posts. *(I)*
  - **Caveat, stated explicitly by the study's own framing and worth
    repeating every time this stat is used**: this is correlation, not
    causation. A brand that's already well-known will naturally accumulate
    both mentions and AI citations regardless of which one "causes" the
    other — the study doesn't isolate mention-causes-citation from
    popularity-causes-both.
- **Muck Rack's "What is AI reading?" / Generative Pulse reports** (1M+
  links from ChatGPT, Gemini, Claude, and Perplexity in Dec 2025; 25M+ links
  across 17 industries in May 2026) consistently find citations dominated
  by **earned media**: Dec 2025 — 94% of cited links non-paid, 82% earned;
  May 2026 — ~84% earned, paid/advertorial ~0.3%, journalism ~27%. The
  apparent inconsistency in earlier write-ups was two different metrics
  (non-paid share vs earned share), not conflicting results. Caveat:
  Muck Rack's "earned" bucket also includes academic, government,
  encyclopedic, and third-party corporate sites — not just press coverage.
  *(I)*

### Digital PR: the evidenced-adjacent case, and where the evidence stops
- The case for digital PR over generic link-building rests on combining the
  two findings above: since brand *mentions* (linked or not) outcorrelate
  backlinks, and since the large majority of citations trace to earned or
  independent media rather than brand-owned or paid content, PR placements
  that generate mentions in authoritative independent outlets are the
  better-evidenced play. **This is our own synthesis of two separate
  studies, not a claim either source makes end-to-end** — present it that
  way rather than attributing the full chain to one source.
- No controlled experiment was found that isolates a digital-PR placement as
  an independent variable and measures before/after AI-citation lift for a
  specific brand. PR-agency claims (e.g. "we track client mentions across
  ChatGPT/Gemini/Claude/Perplexity weekly") are agency self-promotion without
  published before/after numbers — rank these **below** typical industry-blog
  heuristics, as marketing claims rather than disclosed research
  *(heuristic, low-confidence tier)*.

### The one controlled experiment in this space
- **"GEO: Generative Engine Optimization"** (Aggarwal, Murahari, Rajpurohit,
  Kalyan, Narasimhan, Deshpande — KDD 2024, arXiv:2311.09735) is the field's
  only peer-reviewed controlled experiment touching this area. Confirmed
  directly from the abstract: it introduces GEO-bench, "a large-scale
  benchmark of diverse user queries... along with relevant web sources," and
  finds GEO methods "can boost visibility by up to 40% in generative engine
  responses," with efficacy varying by domain.
  - Per-tactic numbers (quotations, statistics, cite-sources) have now been
    checked against the full paper — see
    `../content-strategy/ai-citation-signals.md`, which owns this paper in
    depth. Agency blogs that round them to "each boosts visibility 30–40%"
    overstate it: effects are metric-, engine-, and domain-specific.
  - Relevance here specifically: the paper's authoritative-sourcing tactics
    are content-layer, not backlink/directory-layer — they support the
    inference that being cited alongside authoritative sources correlates
    with GE visibility, which is adjacent to but distinct from this file's
    backlink/PR questions.

### What to actually do
1. Don't chase link volume for its own sake — a link from a topically
   relevant, editorially-earned placement is worth more than many generic
   ones, per Google's own policy framing.
2. Weight PR and outreach effort toward placements that generate a genuine
   brand *mention* (named, in context) even when a link isn't guaranteed —
   the correlational evidence favors mentions over links specifically.
3. Track mentions, not just backlinks, when measuring digital-PR effect —
   a mentions-only placement in an authoritative outlet may matter more than
   a low-relevance backlink.
4. Present the Ahrefs correlation numbers and Muck Rack's earned-media share
   with their caveats intact (correlational; Muck Rack's "earned" is a broad
   bucket) rather than as settled statistics.
5. Treat agency PR-firm claims about AI-citation tracking as marketing
   framing, not evidence, when deciding how much weight to give a pitch.

## How this shows up in the workflow
Stage 5 (technical & entity fixes) uses this file when explaining to the
user why entity/mention consistency and earned coverage matter more than raw
link count. Stage 7 (distribution) uses it when prioritizing outreach and PR
targets — favoring placements likely to generate a named brand mention in an
independent, authoritative outlet over pure link-building.
