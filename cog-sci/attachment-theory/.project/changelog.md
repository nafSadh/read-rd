# Changelog — Attachment Theory Project

## Session 2 — 2026-03-25

**What happened:**
- Gap-filled literature collection: added 9 new sources (total now 40 across 6 sections)
  - S1: Vicedo (SSP critique), Simply Psychology (Bowlby overview), BPS (historical context)
  - S2: Attachment Project AAI overview
  - S6: EMDR meta-analysis 2023, ICEEFT EFT research, Brom SE RCT, AAI earned-secure, de Jongh EMDR review 2024
- Built 6 section deep-dives with full interactive HTML (sidebar nav, detail panels, theme toggle):
  - S5: The Critique (8 subsections, 8 sources) — temperament confound, stability problem, WEIRD bias, mother-blame, pop psychology distortion, era of exhaustion, MBTI parallel, honest assessment
  - S3: Adult Attachment (8 subsections) — Hazan-Shaver bridge, ECR vs AAI, pursue-withdraw cycle, stability & change, attachment under stress, EFT, dimensional reality
  - S1: Historical Origins (8 subsections) — Bowlby's revolution, ethological roots, Ainsworth & SSP, Main's extensions, political context, Harlow's monkeys, timeline, legacy
  - S4: Neuroscience & Polyvagal (8 subsections) — PVT explained, three-tier hierarchy, neuroception, PVT scientific problems, somatic storage, oxytocin, neural correlates
  - S2: Taxonomy & Measurement (8 subsections) — four styles overview, secure/avoidant/anxious/disorganized detail, categories vs dimensions, instrument comparison
  - S6: Earned Security & Healing (8 subsections) — earned-secure concept, narrative pathway, somatic pathway, relational pathway, EFT evidence, EMDR & trauma, three-layer model
- Created shared CSS (`dd-shared.css`) and JS scaffold (`dd-shared.js`) to reduce duplication across deep-dives
- Built project index page (`index.html`) with links to all deep-dives, source counts, and key tensions
- Updated literature-collection.md with new sources and corrected source counts
- Updated todo.md with completion status

**Architecture decisions:**
- S5 was built first (self-contained, inline CSS/JS) as the strongest section
- S1-S4, S2, S6 use shared CSS/JS files for maintainability
- Each deep-dive has 8 subsections with summary cards (left panel) and detailed analytical essays (right panel, 6-10K chars each)
- Detail panels include: SVG diagrams, stat bars, feature grids, verdict pro/con, timelines, callouts, security boxes, chip tags
- Cross-references between sections via relative links (e.g., s5-critique.dd.html links to s2-taxonomy.dd.html)

**What was skipped:**
- S7 (Personal Application) — reflective section, not source-dependent, deferred
- Synthesis paper — deferred until all sections complete
- S5 could be refactored to use shared CSS/JS (currently self-contained with inline styles)

**Build order followed:** S5 → S3 → S1 → S4 → S2 → S6 (as recommended by todo)

## Session 1 — 2026-03-25

**What happened:**
- Created overview deep-dive (8 sections, 677 lines) covering all 7 dimensions
- Built directly from web search + Claude conversation history synthesis
- Sections: Origins, Four Styles, Adult Love, Nervous System, The Critique, Earned Security, Personal Lens, Sources
- 5 SVG diagrams: style taxonomy, pursue-withdraw cycle, polyvagal hierarchy, rigor spectrum, earned security pathways
- Initial framing: "useful rather than true" — attachment between Big Five and MBTI on evidence spectrum

**What was skipped (acknowledged):**
- Literature collection was not done before building (violated paper-drive source-first discipline)
- Source adequacy assessment happened retroactively, not prospectively
- No per-section deep-dives yet — overview covers all dimensions at summary level

**Decisions made:**
- Placed in `cog-sci/attachment-theory/` (not `self/`) — this is a research project, not a personal reflection
- Critical lens is a first-class section (S5), not an afterthought
- Polyvagal theory included with its own scientific controversies noted
- Jerome Kagan's temperament critique given prominent placement

**Project files created:**
- `overview.dd.html` — overview deep-dive
- `.project/methodology.md` — research question, scope, source strategy
- `.project/todo.md` — deliverables plan with source adequacy table
- `.project/changelog.md` — this file
- `literature-collection.md` — initial source catalog

## Session — March 25, 2026

### Deliverables
- **survey-paper.html**: "Useful Rather Than True" — 38 links, 6 sections + synthesis + methods, 2 SVG diagrams, 6 tension cards. Science-to-folk pipeline thesis. Zero dd.html references.
- **survey-slides.html**: 16 slides, 5 SVGs. Title → TOC → Origins → Taxonomy → Adult → Polyvagal → Critique → Healing → Synthesis → Tensions → Conclusion.
- **index.html**: Added Key Deliverables card grid at top.
