# Phase 2 Continuation — Write Papers for Completed Projects

## Repo
- URL: https://github.com/nafSadh/read-rd
- PAT: (provide at runtime)

## What This Is
Phase 2 of the paper-drive skill audit. Phase 1 (adding source links to all 6 existing papers) is done. Phase 2: write survey papers + slides for the 6 projects that have all deep-dives complete but no papers.

## Use paper-drive skill

## Priority Order (all have 6-7 completed deep-dives, notes, lit collections)

1. **cog-sci/religion-psychology** — 6/6 DDs, 7 notes, lit collection ✅ DONE (survey paper + slides)
2. **cog-sci/sleep-and-dreams** — 6/6 DDs, 7 notes, lit collection ✅ DONE (survey paper + slides)
3. **cog-sci/stoicism-in-practice** — 6/6 DDs, 7 notes, lit collection
4. **neuro/brain-energy** — 6/6 DDs, 7 notes, lit collection
5. **sci-fi-te/time-travel-fiction** — 6/6 DDs, 6 sections, lit collection
6. **sci-fi-te/retrocausal-emotion** — 7/7 DDs, has slides already but no paper ✅ DONE (survey paper added)

### Additional projects (not in original list, picked up during audit)
7. **cog-sci/attachment-theory** — ✅ DONE (survey paper + slides)
8. **cog-sci/science-of-humor** — ✅ DONE (survey paper + slides; note: S4–S7 deep-dives still pending)

## For Each Project, Do:
1. Read `notes/00-synthesis.md` and all section notes to understand the material
2. Read `literature-collection.md` for source URLs (NOTE: lit collections have NO URLs yet — search for each source and build a URL map, same as Phase 1)
3. Write `survey-paper.html` — standalone, no dd.html references, source names hyperlinked, section-sources footers
4. Write `survey-slides.html` — accompanying slide deck
5. Update `index.html` — add Key Deliverables cards at top, flip status badges
6. Commit and push after each deliverable
7. One project per session is realistic

## Key Rules From Updated Skill
- Papers are STANDALONE — no references to deep-dives
- Source names must be hyperlinked (first mention per section)
- Each paper must have accompanying slides (same deliverable card)
- Index gets Key Deliverables cards at top
- Check sibling project indexes for style conformity
- `grep -c '<a href' paper.html` should return 20+ for multi-section papers
- Papers use scrollable layout (not three-panel deep-dive template)

## Template Reference
See `anthro/religion-today/survey-paper.html` for the paper layout pattern (sidebar nav, paper-section classes, paper-stat-row, diagram-wrap, etc.)

## Start With
`cog-sci/religion-psychology` — read its notes, search for source URLs, write survey paper + slides, update index.
