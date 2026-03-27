# Changelog — Sleep & Dreams Project

## Session 1 — 2026-03-25

**What happened:**
- Created complete paper-drive project structure for sleep science and dream research
- Literature collection: 50+ sources across 6 dimensions
- Overview deep-dive (6 sections) with SVG diagrams: sleep architecture cycles, brain region map, circadian rhythm chart, dream theory comparison, sleep deprivation timeline
- 6 section deep-dives (s1 through s6) following canonical template with 6-8 subsections each, SVGs, detail panels
- Project index page with section listing, status badges, and cross-cutting tensions
- Notes: synthesis file + 6 per-section markdown notes

**Source discipline:**
- Literature collection built before deep-dives
- Source adequacy assessed per section before writing
- All sections met minimum source threshold (6+ sources per section)

**Decisions made:**
- Placed in `cog-sci/sleep-and-dreams/` — interdisciplinary sleep science survey
- Walker's "Why We Sleep" treated as influential popularization with known criticisms (Guzey)
- Polyvagal-adjacent claims about glymphatic system presented with both discovery evidence and ongoing controversy
- Lucid dreaming section balances scientific rigor with genuine therapeutic promise
- Sleep industry ($585B) figure contextualized as both validation of sleep's importance and commercialization concern

**Project files created:**
- `.project/methodology.md` — research question, scope, source strategy
- `.project/changelog.md` — this file
- `.project/todo.md` — deliverables plan with source adequacy table
- `literature-collection.md` — 50+ sources organized by dimension
- `overview.dd.html` — overview deep-dive
- `s1-why-we-sleep.dd.html` through `s6-disorders.dd.html` — section deep-dives
- `index.html` — project index
- `notes/00-synthesis.md` — cross-section synthesis
- `notes/01-why-we-sleep.md` through `notes/06-disorders.md` — section notes

## Session — March 25, 2026

### Deliverables
- **survey-paper.html**: Standalone survey paper synthesizing all 6 dimensions. 47 hyperlinks (sources linked inline first mention per section), 3 SVG diagrams, 6 tension cards, section source footers. Zero `dd.html` references. Follows `anthro/religion-today/survey-paper.html` template (sidebar nav, theme toggle, paper-hero layout).
- **survey-slides.html**: 13-slide deck covering all 6 dimensions + synthesis. 10 SVG diagrams, section dividers, key ideas, tension summary. Read-aid slide-deck template (arrow keys, click/swipe, auto-hiding nav, dark/light/system theme toggle).
- **index.html update**: Added Key Deliverables card grid at top (matching religion-today pattern). Survey paper status = done, slides linked from same card.

### Verification
- `grep -c '<a href' survey-paper.html` → 47 (requirement: 20+)
- `grep -c 'dd.html' survey-paper.html` → 0 (standalone check passed)
- All commits pushed to main branch

## Session — March 25, 2026 (Peer Review Response)

### Integrity Fixes
- **Slide count**: Corrected changelog from 21 to 13 slides (actual HTML slide count)
- **Citations CSS**: Added `sup.fn` hover-tooltip citation styles to `dd-shared.css` and `overview.dd.html` inline styles

### Wikipedia-Style Citations Retrofit
- Added inline citations with hover tooltips to all 7 deep-dive files:
  - `overview.dd.html` — 17 citations across 6 overview sections
  - `s1-why-we-sleep.dd.html` — 10 citations (Walker, Borbely, PMC evolutionary papers, Nature Drosophila)
  - `s2-sleeping-brain.dd.html` — 9 citations (glymphatic, SHY, Cell 2024, controversy)
  - `s3-dream-theories.dd.html` — 6 citations (Freud, Hobson, Revonsuo, predictive processing, ARRM, continuity)
  - `s4-lucid-dreaming.dd.html` — 6 citations (LaBerge, Dresler, PMC neuroscience, PTSD RCTs, meta-analysis)
  - `s5-deprivation.dd.html` — 10 citations (Gardner, blue light, caffeine, shift work, sleep economy)
  - `s6-disorders.dd.html` — 7 citations (AASM, apnea, narcolepsy, FFI, parasomnias, dream engineering)

### New Deliverable
- **tensions-paper.html**: Standalone tensions paper analyzing 6 unresolved contradictions in sleep science. Sidebar nav, theme toggle, SVG tension map, tension-block components with vs-grids, 12 numbered citations, references section. Follows `anthro/religion-today/tensions-paper.html` template.

### Index Update
- Added tensions paper card to Key Deliverables grid on `index.html`
- Updated `todo.md` with completed items and corrected slide count
