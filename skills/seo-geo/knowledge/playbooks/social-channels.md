---
topic: Social channels (LinkedIn, X) — post patterns and cadence for visibility-driving content
stage-relevance: [7]
last-verified: 2026-10-24
sources:
  - internal TopCited content-distribution playbook (2026-06-14, generalized)
  - internal TopCited generated LinkedIn/X drafts (2026-06-14, generalized as pattern examples)
  - [industry] LinkedIn personal-vs-company reach analyses (tryordinal.com, digitalapplied.com, refinelabs.com, accessed 2026-08-20) — third-party analyses, no LinkedIn primary source publishes exact reach percentages
  - [industry] Metricool 2026 LinkedIn study (673,658 posts) and Algorithm InSights 2025 (1.8M posts), via search summaries, accessed 2026-10-24
  - [industry] LinkedIn feed-ranking rebuild, Mar 2026 (searchengineland.com/linkedin-updates-feed-algorithm-llm-ranking-retrieval-471708, accessed via search summary)
  - heuristic
---

# Social channels playbook (LinkedIn, X)

## In plain words
LinkedIn and X won't get a page indexed the way a directory listing does, but
they do two other things well: they drive traffic and engagement back to
specific content pages (which itself is a freshness/relevance signal), and
they're part of the "talked about consistently across many sources" pattern
that both search and AI answers use to gauge whether a brand is real and
current. The posts that work share a small set of repeatable patterns rather
than being one-off creative writing.

## What practitioners need to know

### Repeatable post patterns
- **Data hook**: open with a specific, surprising number or finding, then
  connect it to a broader claim, then link to the piece with the full
  detail. The hook has to work as a standalone claim — "we found X" — before
  it explains why that matters.
- **Contrarian / POV**: state a common piece of advice, then explain
  specifically why it's incomplete or dangerous now, then link to the
  framework/reasoning. This works because it invites disagreement, which
  drives engagement, but only holds up if the counter-argument is genuinely
  substantive rather than a strawman.
- **How-to / listicle**: a short numbered list of concrete, specific
  actions (not vague principles) with a link to the full breakdown. This
  pattern is the one most likely to be saved/bookmarked, which platforms
  weight as an engagement signal.
- **Result / proof**: lead with a concrete before/after number, briefly
  explain what produced it, then a clear call to action. Only use this
  pattern with a number that's actually verifiable and sourced — an
  unverifiable stat undermines the entity-consistency and credibility signals
  this whole channel is supposed to build.
- **Tool/comparison angle**: useful specifically for category-defining
  "best X tools" style content, because it targets the exact query pattern
  both searchers and assistants use when comparing options in a category.
  Being genuinely evenhanded (naming where the product doesn't fit) reads as
  more credible than a one-sided comparison, and is more likely to be the
  kind of source an assistant is willing to cite.

### Platform-specific notes
- **LinkedIn**: post from both a personal profile (usually a founder/team
  member) and the company page — personal-profile reach is much higher on
  LinkedIn's algorithm than company-page reach, so treat the personal post as
  primary and the company reshare as reinforcement, not the other way
  around. The better-sourced numbers: Metricool's 2026 study (673,658
  posts) found personal-profile posts get **~63% higher engagement** than
  company-page posts (2.60% vs 1.74%), and a 2025 analysis of 1.8M posts
  found company posts reach only **~1.6% of followers** *(industry,
  disclosed sample sizes)*. Widely repeated bigger figures — "company pages
  get 5% of feed allocation vs 65% for people," "personal reach is 561%
  higher" — have no traceable study behind them; don't cite them.
  LinkedIn also rebuilt feed ranking in Mar 2026 around LLM-based
  retrieval and topical relevance, favoring expert posts that travel beyond
  the poster's connections and demoting engagement bait *(industry, per
  LinkedIn Engineering coverage)* — substance on a topic the poster is
  known for matters more than engagement tricks.
- **X**: longer-form findings work better as a numbered thread than as a
  single post — each tweet in the thread should be able to stand alone as a
  small, complete claim, with the payoff/link placed in the final tweet
  rather than the first.
- **Always end with a specific link, not a generic homepage link where a
  more specific page exists.** Linking to the exact blog post or page the
  post is about (rather than just the homepage) is what drives the
  freshness/traffic signal to the page that actually needs it, and gives the
  reader something concrete to act on.
- **Broken preview cards silently kill this whole channel.** If the site's
  Open Graph image or metadata is broken, every social post's link preview
  renders blank or broken, which suppresses click-through — verify OG tags
  render correctly (e.g. with LinkedIn's Post Inspector, or by pasting the URL
  into a draft post) before investing in a social cadence. *(heuristic)*

### Cadence
Two to three posts per week is a sustainable default that keeps the account
active without diluting each post's audience. Mix patterns rather than
repeating the same one — a run of five straight "result/proof" posts reads
as promotional in a way that a mix of data/POV/how-to/result does not.

## How this shows up in the workflow
Stage 7 (distribution) uses this file to pick a post pattern per planned
post and to check that each post links to a specific, relevant page rather
than a generic one — and to flag if OG/preview rendering hasn't been
verified before a social push begins.
