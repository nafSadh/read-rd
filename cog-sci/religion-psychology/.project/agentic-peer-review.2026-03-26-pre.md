# Peer Review: cog-sci/religion-psychology

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25

## Overall Assessment

This is a strong, well-organized research project that surveys religion from six empirical dimensions (cognitive science, belief psychology, mental health, moral psychology, developmental psychology, and neuroscience). The writing is consistently rigorous, epistemically honest, and careful to distinguish what evidence shows from what it does not. The project includes a complete literature collection (52 sources across 6 sections + 2 cross-cutting), 7 deep-dive pages (overview + S1-S6), a full survey paper with 54 numbered references and inline Wikipedia-style citations, an 18-slide deck, research notes for every section, and well-maintained project metadata. The "Six Tensions" framework is a genuine intellectual contribution that elevates this beyond a standard literature review.

**Content Quality: A**
**Paper-Drive Compliance: A-** (minor gaps in deep-dive citation infrastructure)

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | ✅ | 52 sources across 6 sections + 2 cross-cutting, each with linked URLs, key data points, and dates. All sections assessed as ADEQUATE. |
| Source adequacy checks | ✅ | Each section in `literature-collection.md` has an explicit ADEQUATE assessment. Balanced: includes foundational texts, meta-analyses, critical/null findings, and 2024-2025 recent work. |
| Deep-dives (7/7 built) | ✅ | Overview + S1-S6 all present as `.dd.html` files. Each has 6-8 subsections, stat bars, SVG diagrams, callout boxes, sidebar navigation, and theme toggle. |
| Papers | ✅ | `survey-paper.html` is a substantial standalone paper with abstract, 6 content sections, methods & limitations section, sidebar navigation, 4 SVG diagrams, stat rows, tension cards, and 54 numbered references. |
| Slides | ✅ | `survey-slides.html` is an 18-slide deck with arrow-key/touch navigation, progress bar, theme toggle, stat rows, grid cards, tension cards, and quote blocks. |
| Index deliverable cards | ✅ | `index.html` has a Key Deliverables card (paper + slides), overview listing, 6 section deep-dive cards with links, and a Six Tensions summary. |
| .project/ management | ✅ | `methodology.md`, `changelog.md`, and `todo.md` all present and well-maintained. Changelog documents decisions and source distribution. Todo reflects completion status accurately. |
| Citations (Wikipedia-style) | ⚠️ | Survey paper has full Wikipedia-style inline citations (`<sup class="fn">` with tooltip hover and `#ref-N` anchors). Deep-dive `.dd.html` files reference researchers by name but lack inline clickable citation markers linking to sources. |
| External source links (20+) | ✅ | Survey paper alone has 89 external `href` links (54 unique source references). Literature collection has 52 linked sources. Total across project far exceeds 20. |

## Content Quality

The intellectual substance is the project's greatest strength. The framing is consistently empirical rather than polemical. Key findings are presented with appropriate hedging: effect sizes are reported (r = .13 overall prosociality, r = .06 behavioral), methodological limitations are explicitly discussed (WEIRD sampling, publication bias, operationalization problems), and null results are given equal prominence (HADD's lack of empirical support, 2025 priming null result). The Six Tensions framework (HADD vs. evidence, religion helps vs. hurts, moral self-report vs. behavior, born believers vs. Gen Z exodus, neural correlates vs. meaning, byproduct vs. adaptation) provides genuine analytical structure rather than mere summarization.

The survey paper's methods section is unusually self-aware, noting that "we know less than textbooks suggest but more than skeptics admit." The synthesis notes (`00-synthesis.md`) demonstrate that the author has internalized the material rather than just aggregated it.

## Strengths

1. **Epistemic balance.** The project resists taking sides. Barrett (devout Christian) and Dennett (committed atheist) are presented as drawing opposite conclusions from the same evidence, with the science declared compatible with both interpretations. This is intellectually honest and rare.

2. **Recency of sources.** 15+ sources from 2024-2025, including a 2026 MDPI paper on TLE. The literature collection is not stale.

3. **Statistical specificity.** The project reports actual effect sizes, sample counts, and confidence-relevant details (811,663 participants in the 2024 meta-analysis; 18.7% CRT advantage; 74% of Gen Z exiters left before 17). This grounds claims in data rather than impressions.

4. **Critical inclusion of null and negative findings.** HADD's empirical failure, the 2025 priming null result, the self-report vs. behavioral gap in prosociality, and the enactivist critique of CSR's theoretical foundations are all prominently featured rather than footnoted.

5. **Visual and structural polish.** The survey paper includes 4 SVG diagrams, sidebar navigation with scroll tracking, section source footers, stat rows, callout boxes, and tension cards. The slide deck is fully navigable with keyboard/touch. All pages support dark/light theme toggling.

6. **Complete project infrastructure.** Methodology, changelog, todo, and literature collection are all maintained. The changelog documents not just what was built but why decisions were made.

## Weaknesses

1. **Deep-dive citation gap.** The 7 `.dd.html` files mention researchers by name (Boyer, Barrett, Kelemen, Pargament, etc.) but do not include Wikipedia-style inline citations with clickable links to sources. The survey paper has this (`<sup class="fn">` with hover tooltips), but the deep-dives do not. A reader of `s1-csr.dd.html` cannot click through to the actual Barrett or Lisdorf papers from the text.

2. **Missing shared CSS/JS.** The todo notes that `dd-shared.css` and `dd-shared.js` are absent. Each `.dd.html` file contains its own complete copy of the full CSS (~30 lines of dense theme definitions). This is a maintenance burden. A change to the theme requires editing 7+ files.

3. **Notes are thin.** The section notes (`notes/01-csr.md` through `notes/06-neuroscience.md`) are brief summaries (15-25 lines) rather than detailed reading notes. They read more like section outlines than the kind of working notes that would help a future researcher reconstruct the reasoning process.

4. **No cross-links to related projects.** The index footer mentions `anthro/religion-today` but the todo suggests cross-linking has not been implemented. The `attachment-theory` link in the footer is present but no substantive cross-referencing exists in the body content.

5. **Slide deck lacks source references.** The 18-slide deck mentions researchers by name but includes no source links or citation markers. For a presentation context this is acceptable, but it limits the slides' value as a standalone reference.

6. **Methodology deliverables checklist is outdated.** `methodology.md` still shows unchecked boxes for overview deep-dive, per-section deep-dives, notes, and index page, even though all are complete. The todo file is accurate, but the methodology file has not been updated.

## Recommendations

1. **Retrofit Wikipedia-style citations into deep-dives.** Add `<sup>` inline citation markers with source links to each `.dd.html` file, matching the pattern used in `survey-paper.html`. This is the single highest-impact improvement for research credibility.

2. **Extract shared CSS/JS.** Create `dd-shared.css` and `dd-shared.js` to eliminate the duplicated theme and layout code across 7 deep-dive files.

3. **Update methodology.md checklist.** Mark all completed deliverables as done to maintain consistency with `todo.md`.

4. **Expand section notes.** Add key quotes, specific page references, methodological observations, and cross-section connections. The current notes are too thin to serve as working research documentation.

5. **Consider a consolidated bibliography page.** The survey paper has a numbered reference list, but a standalone bibliography page (or section in `literature-collection.md`) with full APA-style citations would strengthen the project's academic credibility.
