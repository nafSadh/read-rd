# Changelog — History & Evolution of Flags

All changes to the vexillology paper-drive project.

---

## Session: March 25, 2026

### Phase 0: Initial Deep-Dive (prior session)
- Built single monolithic deep-dive (`flag-history.dd.html`) covering all 7 sections
- Created project index page (`index.html`)
- All section links pointed to anchors in the single file
- Known issues: oversized flag SVGs, some HTML rendering problems

### Phase 1: Paper-Drive Restructure (this session)
- Converted from single deep-dive to full paper-drive project structure
- Created `.project/` directory (changelog, todo, methodology)
- Created `notes/` directory with synthesis notes
- Renamed `flag-history.dd.html` to `overview.dd.html` (kept as overview)
- Split into 7 per-section deep-dives:
  - `s1-origins.dd.html` — Ancient Origins (~2400 BCE to 651 CE)
  - `s2-heraldic.dd.html` — The Heraldic Age (12th--15th centuries)
  - `s3-empire.dd.html` — Empire & Conquest (Ottoman, colonial, Mughal)
  - `s4-revolution.dd.html` — Revolution & the Tricolor (1572--1848)
  - `s5-decolonization.dd.html` — Decolonization & Pan-Movements
  - `s6-design.dd.html` — Design Patterns & Symbolism
  - `s7-collection.dd.html` — The flags.fyi Collection
- Each section expanded to 6--8 subsections with detail panels
- Built `literature-collection.md` with 35+ vexillological sources
- Created `notes/00-synthesis.md` with cross-section synthesis
- Updated `index.html` to link individual section files + overview
- Fixed all flag SVG sizing: inline flags max-width 120px, diagrams in `.diagram-wrap`
- Added source citation links (flags.fyi, Wikipedia, scholarly references)
- Added cross-references between sections

## Session: March 25, 2026 (peer review remediation)

### Phase 1: Integrity Fixes
- Fixed index.html links: changed all 7 section links from `flag-history.dd.html#section-N` anchors to individual section files (`s1-origins.dd.html` through `s7-collection.dd.html`)
- Section 7 link now points to `s7-collection.dd.html` (newly created)

### Phase 2: Wikipedia-Style Citations
- Added `.cite` CSS class with hover tooltips to all 6 existing deep-dives (s1--s6)
- Added inline `<span class="cite">[N]<span class="cite-tip">...</span></span>` citations to summaries and detail panels
- Citations reference literature-collection.md entries (A-01 through P-06)
- Each deep-dive now has 4--8 inline citations with source tooltips

### Phase 3: Missing Deep-Dive
- Built `s7-collection.dd.html` — The flags.fyi Collection (8 subsections)
- Covers: dataset overview, category breakdown, evolution chains, Egypt/Afghanistan/Germany case studies, statistical patterns
- Includes Wikipedia-style citations referencing C-01 through C-05
- Follows exact dd.html template pattern (sidebar, detail panels, theme toggle)

### Phase 4: Synthesis Paper
- Wrote `flags-compressed-histories.html` — "Flags as Compressed Histories" synthesis paper
- 40 references (20+ with URLs), Wikipedia-style inline citations with hover tooltips
- Follows survey-paper.html template (sidebar nav, abstract, numbered sections, reference list)
- Covers: material evolution, three color families, tricolor revolution, crescent lineage, flags as first acts, evolution chains, three tensions

### Phase 5: Index Update
- Added deliverable cards to index.html: synthesis paper, overview deep-dive, slide deck (TODO)
- All section and deliverable links now point to correct files
