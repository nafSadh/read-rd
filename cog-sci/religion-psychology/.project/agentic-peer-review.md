# Peer Review: cog-sci/religion-psychology

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-26
**Round:** 2

## Overall Assessment

This is a comprehensive, intellectually rigorous paper-drive project surveying religion from six empirical dimensions: cognitive science, belief psychology, mental health, moral psychology, developmental psychology, and neuroscience. Since the round 1 review (2026-03-25), the primary weakness -- the absence of Wikipedia-style inline citations in deep-dive pages -- has been fully resolved. All 7 `.dd.html` files now contain `<sup class="fn">` inline citations with tooltip hovers and linked source references, matching the pattern in the survey paper. The project is now citation-complete across all deliverables except the slide deck (where citations are conventionally omitted).

The "Six Tensions" framework remains the project's standout intellectual contribution, providing genuine analytical structure that elevates this beyond aggregation. The synthesis notes demonstrate internalization of the material. The writing is consistently empirical rather than polemical, with appropriate hedging, reported effect sizes, and prominent treatment of null and negative findings.

**Content Quality: A**
**Paper-Drive Compliance: A** (round 1 citation gap resolved)

## Completeness Scorecard

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | Literature collection | PASS | 52 sources across 6 sections + 2 cross-cutting, each with linked URLs, key data points, and dates. All sections assessed as ADEQUATE. |
| 2 | Source adequacy checks | PASS | Each section in `literature-collection.md` has an explicit ADEQUATE assessment. Balanced coverage: foundational texts, meta-analyses, critical/null findings, 2024-2026 recent work. |
| 3 | Deep-dives (7/7 built) | PASS | Overview + S1-S6 all present as `.dd.html` files. Each has 6-8 subsections, stat bars, SVG diagrams, callout boxes, sidebar navigation, theme toggle, and audio player (overview). |
| 4 | Citations (Wikipedia-style) | PASS | All 7 deep-dives now have inline `<sup class="fn">` citations with tooltip hovers linking to external sources (58 citation markers across deep-dives). Survey paper has 25+ inline citations with numbered references. Round 1 gap resolved. |
| 5 | External source links (20+) | PASS | 67 external `href` links across deep-dives alone. Survey paper has 89 external links. Literature collection has 52 linked sources. Total far exceeds threshold. |
| 6 | Papers | PASS | `survey-paper.html` is a substantial standalone paper: abstract, 6 content sections, methods & limitations, sidebar navigation, 4 SVG diagrams, stat rows, tension cards, numbered references. |
| 7 | Slides | PASS | `survey-slides.html` is an 18-slide deck with arrow-key/touch navigation, progress bar, theme toggle, stat rows, grid cards, tension cards, and quote blocks. |
| 8 | Index with deliverable cards | PASS | `index.html` has a Key Deliverables card (paper + slides), overview listing, 6 section deep-dive cards with links, Six Tensions summary, and project metadata links. |
| 9 | Research notes | PASS | `notes/00-synthesis.md` through `notes/06-neuroscience.md` all present. Synthesis note (00) is substantive with Six Tensions framework and methodological caveat. Section notes (01-06) are structured summaries with key findings, critical problems, and source counts. |
| 10 | .project/ management | PASS | `methodology.md`, `changelog.md`, and `todo.md` all present. Changelog documents decisions, source distribution, and rationale. Todo accurately reflects completion status. |

## Content Quality

The intellectual substance remains the project's greatest strength. Key qualities:

- **Epistemic honesty.** Effect sizes are reported throughout (r = .13 overall prosociality, r = .06 behavioral; 18.7% CRT advantage; 0.4-3.1% TLE ictal religious experiences). Methodological limitations are discussed explicitly -- WEIRD sampling, publication bias, operationalization challenges -- rather than footnoted.

- **Balanced treatment of contested questions.** Barrett (devout Christian) and Dennett (committed atheist) are presented as drawing opposite conclusions from the same CSR evidence. Positive and negative religious coping receive equal analytical weight. The project neither defends nor attacks religion.

- **Null findings given prominence.** HADD's lack of empirical support after 30 years, the 2025 Bayesian null result on religious priming, the self-report vs. behavioral gap in prosociality (r = .15 vs. r = .06), and the God Helmet's failed replication are all presented as substantive findings rather than caveats.

- **Recency.** 15+ sources from 2024-2025, plus a 2026 MDPI paper on TLE. The literature collection is not stale.

- **The Six Tensions framework** (HADD vs. evidence, religion helps vs. hurts, moral self-report vs. behavior, born believers vs. Gen Z exodus, neural correlates vs. meaning, byproduct vs. adaptation) provides genuine analytical structure that surfaces contradictions rather than smoothing them over.

## Strengths

1. **Citation infrastructure now complete.** The round 1 primary weakness has been fully addressed. All 7 deep-dive pages now have Wikipedia-style inline citations with `<sup class="fn">` markers, tooltip hovers showing source details, and external links to source papers. A reader of any deep-dive can now click through to the actual source material.

2. **Statistical specificity throughout.** The project grounds claims in data rather than impressions: 811,663 participants in the 2024 prosociality meta-analysis; 701 effects across 237 samples; 74% of Gen Z exiters left before age 17; 67% of psilocybin subjects rated the experience among their top-5 life events. These numbers appear consistently across deep-dives, notes, and the survey paper.

3. **Complete deliverable set.** The project includes all paper-drive deliverables: literature collection with adequacy checks, 7 deep-dives with citations, survey paper with numbered references, slide deck, index page with deliverable cards, research notes, and project metadata. Audio narration (overview.mp3) is a bonus deliverable.

4. **Visual and structural polish.** 4 SVG diagrams in the survey paper, sidebar navigation with scroll tracking, section source footers, stat rows, callout boxes, tension cards, dark/light theme toggling across all pages, and audio bar integration in the overview deep-dive. The slide deck supports arrow-key and touch navigation with a progress bar.

5. **Synthesis note is substantive.** The `00-synthesis.md` file is not a summary but a genuine analytical synthesis, with the Six Tensions framework, a "What the Evidence Actually Shows" section organized by dimension, and an honest methodological caveat.

6. **Source balance.** Each section includes both supporting and critical/null sources. S1 includes HADD critique alongside HADD proponents. S3 includes religious trauma alongside positive coping. S4 includes the 2025 null priming result alongside the 2016 positive meta-analysis. This is methodologically sound.

## Weaknesses

1. **Methodology deliverables checklist remains outdated.** `methodology.md` still shows 4 unchecked boxes (overview deep-dive, per-section deep-dives, section notes, project index page) despite all being complete. This was flagged in round 1 and has not been fixed. The `todo.md` is accurate, but the methodology file is inconsistent.

2. **Missing shared CSS/JS.** No `dd-shared.css` or `dd-shared.js` files exist. Each deep-dive contains its own complete copy of the full CSS theme definitions. This was flagged in round 1. The duplication creates a maintenance burden -- a theme change requires editing 7+ files.

3. **No hero images.** The `image-banana-claude.md` file documents planned hero images for 4 pages with specific prompts, but no `img/` directory exists and no images have been generated. This is a visual gap, though not a paper-drive compliance requirement.

4. **Section notes are outline-weight.** Notes 01-06 are structured summaries (20-35 lines each) with key findings, critical problems, and researcher lists. They function well as section outlines but lack detailed reading notes, key quotes with page references, or cross-section analytical connections. The synthesis note (00) is substantially more developed than the section notes.

5. **Slide deck has no source references.** The 18-slide deck mentions researchers by name but includes only 2 external links and no citation markers. For a presentation context this is conventionally acceptable, but it limits standalone reference value.

6. **Cross-project links are minimal.** The index footer links to `attachment-theory` but no substantive cross-referencing exists in the body content of deep-dives or the survey paper. The `anthro/religion-today` cross-link suggested in the todo has not been implemented.

## Recommendations

1. **Update methodology.md checklist.** Mark the 4 remaining deliverables as complete (`[x]`). This is a 30-second fix that resolves an internal consistency issue flagged in both review rounds.

2. **Extract shared CSS/JS.** Create `dd-shared.css` and `dd-shared.js` to centralize the duplicated theme and layout code. This reduces maintenance burden and ensures theme consistency across all 7+ pages.

3. **Generate hero images.** The prompts in `image-banana-claude.md` are well-crafted and ready for execution. Adding 4 hero images would significantly enhance the visual experience of the deep-dive pages.

4. **Deepen section notes.** Add cross-section connections (e.g., how the dual-process finding in S2 relates to the meditation exception in S3), specific methodological observations per source, and unresolved questions that emerged during reading. The synthesis note (00) demonstrates what substantive notes look like.

5. **Consider adding a few slide citations.** Even 1-2 source links per slide (in small footer text) would increase the deck's standalone value without cluttering the presentation format.
