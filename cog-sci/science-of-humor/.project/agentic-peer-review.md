# Peer Review: cog-sci/science-of-humor

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-26
**Round:** 2

## Overall Assessment

This project has reached full maturity since the round 1 review. All seven section deep-dives are now built and live, with Wikipedia-style superscript citations across every deep-dive and both papers. The deliverable set is unusually rich for a paper-drive project: two standalone papers (survey + position), two slide decks, an overview deep-dive, seven section deep-dives, eight research notes, and a 55-source literature collection. The writing quality remains the project's standout feature -- clear, intellectually substantive, and appropriately wry without forcing humor. The three weaknesses flagged in round 1 (missing deep-dives, missing citations, stale todo.md) have all been addressed. The remaining issues are minor: the overview deep-dive still uses inline CSS rather than dd-shared.css, and overview.mp3 remains undocumented.

**Content Quality: A**
**Paper-Drive Compliance: A**

## Completeness Scorecard

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | Literature collection | PASS | 55 sources across 7 sections with structured tables (IDs, key data points, dates). Source adequacy summary with per-section ratings. |
| 2 | Source adequacy checks | PASS | Explicit adequacy table at bottom of literature-collection.md. All 7 sections rated ADEQUATE or STRONG. S6 (Health) rated STRONG with 10 sources including multiple meta-analyses. |
| 3 | Deep-dives (7/7 built) | PASS | All 7 section deep-dives built as dd.html files using dd-shared.css/js. Each has 7-8 subsections with summaries plus expandable detail panels. Overview deep-dive also present. |
| 4 | Papers | PASS | Survey paper (58 external links, 13 sup.fn citations, SVG diagram, 9 sections with source footers). Position paper (30 external links, 11 sup.fn citations, SVG diagram, 10 sections). Both standalone, high quality. |
| 5 | Slides | PASS | survey-slides.html and position-slides.html. JS-generated decks with arrow-key/touch navigation, progress bars, theme toggles, responsive layout. |
| 6 | Wikipedia-style citations | PASS | 76 sup.fn citations across 10 HTML files. All deep-dives (S1-S7), the overview, and both papers have superscript footnotes with hover tooltips linking to external sources. |
| 7 | External source links (20+) | PASS | 162 external href links across all HTML files. Survey paper alone has 58. Deep-dives S1-S7 have 6-10 each. Well above the 20-link threshold. |
| 8 | Index page with deliverable cards | PASS | index.html has Key Deliverables grid (survey + position papers with links to papers and slides), overview card, all 7 section items with "done" status badges. Theme toggle, Key Tensions list. |
| 9 | .project/ management files | PASS | methodology.md (research question, scope, 7 dimensions, source strategy, tone note). changelog.md (2 sessions documented). todo.md (accurate hand-off status, all items checked). |
| 10 | Research notes | PASS | 8 markdown notes (00-synthesis through 07-ai-humor). Synthesis note identifies cross-cutting themes. Each section note provides structured raw material with key sources referenced. |

## Content Quality

The intellectual substance is exceptional for a survey project. The project genuinely synthesizes across seven disciplines rather than merely listing findings side by side. Three cross-cutting themes recur with increasing sophistication: the ha-ha/a-ha connection (humor as cognitive debugging reward), the social primacy of laughter (Provine's 30x finding, Dunbar's grooming theory), and psychological distance as the master variable (McGraw's BVT distance mechanism). These themes bind the sections together and elevate the project beyond a catalog of humor research.

The survey paper synthesizes 2,400 years of humor theory into a coherent narrative arc. The position paper ("Humor Is Irreducibly Social") takes a genuine argumentative stance, marshaling 9 lines of evidence and addressing counterarguments. The deep-dives achieve strong depth: S1 covers 7 subsections from Plato through BVT to a meta-synthesis with SVG diagrams; S4 treats dark humor with the Willinger intelligence study and BVT distance framework; S7 honestly assesses AI humor's failures as diagnostic of what current systems lack. The newly built S4-S7 deep-dives match the quality of S1-S3, with Wikipedia-style citations, stat rows, feature grids, callout boxes, and detail panels.

The literature collection is well-organized with consistent ID schemes (TH-01, NS-01, CC-01, etc.) and covers the full range from primary philosophical texts (Kant, Freud, Hobbes) through landmark empirical studies (Mobbs 2003, Wattendorf 2023, Willinger 2017) to recent AI benchmarks (HumorBench 2025).

## Strengths

1. **Complete deliverable set**: All planned deliverables are built and functional -- 7/7 deep-dives, overview, 2 papers, 2 slide decks, index page, 8 research notes, literature collection. This is one of the most complete paper-drive projects in the collection.

2. **Genuine interdisciplinary synthesis**: The project integrates philosophy, neuroscience, evolutionary psychology, comedy craft, cultural anthropology, clinical research, and computational approaches. The synthesis note and survey paper identify cross-cutting themes that emerge only from this integration (the ha-ha/a-ha connection, social primacy, distance as master variable).

3. **Two complementary papers with distinct purposes**: The survey paper maps the territory comprehensively. The position paper takes a stance (cognitive theories have the emphasis backwards; humor is primarily social technology). Neither is redundant with the other.

4. **Consistent citation infrastructure**: All deep-dives now use the sup.fn pattern with hover tooltips linking to external sources. 76 footnote citations across 10 files, plus 162 external links. Claims are traceable to sources throughout.

5. **Writing quality and tone**: The prose achieves the methodology's stated goal -- dry, knowing wit without forced punchlines. Technical content is accessible without being simplified. The project is genuinely enjoyable to read, which is appropriate given the subject matter.

6. **Visual design consistency**: All dd.html deep-dives use dd-shared.css/js with a consistent design language (EB Garamond / Jost / IBM Plex Mono, light/dark toggle, accent colors, stat rows, callout boxes, SVG diagrams). Papers share a consistent but distinct paper-specific styling.

7. **Honest treatment of evidence quality**: The health section (S6) explicitly flags the evidence quality problem (small samples, short interventions, publication bias). The AI section (S7) treats computational humor honestly rather than hyping LLM capabilities. The synthesis note acknowledges that the failure to find a unified theory may itself be the finding.

## Weaknesses

1. **Overview deep-dive uses inline CSS**: overview.dd.html embeds its full CSS (~200 lines of theme variables and layout rules) rather than linking dd-shared.css. All other deep-dives (S1-S7) correctly use the shared stylesheet. This creates a maintenance divergence -- any CSS changes to dd-shared.css would not propagate to the overview.

2. **Audio file undocumented**: overview.mp3 exists in the project directory but is not referenced from any HTML page, not documented in the changelog, and not listed in todo.md. Its purpose and content are unclear.

3. **Papers duplicate CSS inline**: Both survey-paper.html and position-paper.html embed their full CSS (~80+ lines each) rather than sharing a paper-specific stylesheet. The CSS is nearly identical between the two files. Extracting a shared paper.css would reduce duplication.

4. **Some citation URLs are generic**: A few sup.fn citations in S4-S7 link to domain homepages (e.g., pmc.ncbi.nlm.nih.gov, academia.edu, pdxscholar.library.pdx.edu) rather than specific article URLs. These are functional but less useful for source verification than direct article links.

5. **No images**: The image-banana-claude.md file documents planned hero images for the overview and S1 deep-dives, but no images have been generated. The deep-dives work well without them, but images would enhance the visual experience.

## Recommendations

1. **Normalize overview.dd.html CSS**: Refactor overview.dd.html to use dd-shared.css instead of inline styles. This is a straightforward migration since the variable naming is identical.

2. **Fix generic citation URLs**: Replace the handful of domain-level URLs in S4-S7 citations with direct links to the specific articles referenced. The literature collection has the article titles needed for lookup.

3. **Document or remove overview.mp3**: Either link the audio from the overview page (as a podcast-style narration option) or note its purpose in the changelog. If it is a leftover artifact, remove it.

4. **Extract shared paper CSS**: Create a paper-shared.css for the survey and position papers to eliminate the duplicated CSS block.

5. **Generate planned images**: The image-banana-claude.md has well-defined prompts for overview and S1 hero images. Generating these would add visual polish to the two most-visited pages.
