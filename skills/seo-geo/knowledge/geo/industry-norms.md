---
topic: How the AI-visibility monitoring industry collects data — cadence, surfaces, vendor norms
stage-relevance: [2, 8]
last-verified: 2026-08-20
sources:
  - internal TopCited research (LLM-monitoring industry study, 2026-08-01), §2, §4, §4b, §4c
  - https://www.surmado.com/blog/best-ai-visibility-tools-2026 (accessed 2026-08-20)
  - heuristic
---

# Industry norms for AI-visibility monitoring

## In plain words
Every serious vendor that tracks "is my brand mentioned by ChatGPT/Perplexity/etc."
runs the same basic playbook: query each assistant once per day, per prompt, per
platform, while logged out (or as a "neutral" user), and treat any single day's
result as noisy. This isn't a TopCited-specific choice — it's the converged
industry standard as of mid-2026, and nothing found in this research pass
contradicts it.

## What practitioners need to know

This file validates, and does not re-derive, the internal design doc's monitoring
findings (internal TopCited research (LLM-monitoring industry study, 2026-08-01), §2/§4/§4b) —
that document remains the authoritative source. This pass specifically searched
for reversals and found none as of 2026-08-20 (19 days after the design doc's own
research date):

- **Cadence remains 1 run/prompt/platform/geo/day** across the named vendors
  (Peec, Otterly, Profound) — no vendor found this pass has moved off that
  cadence. One 2026 comparison piece describes Otterly's collection as "neutral,
  non-personalized querying... designed to avoid personalization bias rather than
  reflect a logged-in user state" (heuristic, weak corroboration — no single
  source strong enough to cite individually) — consistent with, though not an
  independent confirmation of, the design doc's "logged-out" characterization.
  Defer to the design doc's own citations (docs.peec.ai) over this source.
- **Claude coverage is still sold as a paid API add-on**, not UI-monitored —
  confirmed unchanged, matches design doc §4b exactly.
- **No new legal development** was found on the account-pool question beyond the
  design doc's §4c coverage (OpenAI/Anthropic/Google ToS bans on automated access,
  the account-pool-is-not-viable finding). Note: Amazon v. Perplexity and Web Bot
  Auth were not specifically re-searched this pass, since they're a
  playbooks/legal question rather than a "geo" one per the research brief's
  per-track split — flagging the gap rather than silently treating it as checked.
- **No assistant was found to have opened or closed a guest-access path** since
  the design doc's 2026-08-01 research date. One specific line is flagged as
  possibly stale and unverified either way: **Copilot's guest-access status** —
  the design doc says "tightening... through 2025-26," and no fresher
  confirmation (in either direction) was found this pass. Treat that line as
  needing a targeted re-check before treating it as current.

**New since the design doc (market positioning, not collection methodology):**
vendor-comparison content as of 2026-08 positions **Profound as the enterprise
leader, Peec AI as the fastest-growing mid-market challenger, and Otterly as the
most accessible/lightweight entry tier** (heuristic — vendor-comparison marketing
content, treat market-share claims skeptically; source:
https://www.surmado.com/blog/best-ai-visibility-tools-2026 and similar). This is
tangential to GEO proper and belongs more to a competitive-landscape note for the
playbooks/measurement tracks than to monitoring-methodology guidance here.

**What this means in practice:** TopCited's own 1×/day, per-platform, logged-out
(where possible) collection design is aligned with converged industry practice,
not an outlier or a corner cut. Where TopCited diverges from a vendor (e.g., no
Claude UI coverage, since Claude has no guest mode — see
`assistant-sourcing-behavior.md`), that divergence matches the rest of the
industry's own workaround (API add-on), not a gap unique to TopCited.

## How this shows up in the workflow
Not currently referenced by any stage file in `visibility-workflow/stages/` (grep
run 2026-08-20 found no hits). It's most relevant in practice to **baseline
monitoring (stage 02)** and **review/monitoring (stage 08)** — setting client
expectations about why a single day's result is noisy and why cadence is fixed at
once/day rather than more frequent. Flag to the workflow maintainer as a candidate
knowledge-ref addition rather than adding an unrequested stage link here.
