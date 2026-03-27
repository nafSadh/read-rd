# Peer Review: ai/genai-2026-outlook

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-26
**Round:** 2

## Overall Assessment

This is a comprehensive and well-executed paper-drive project that has matured significantly since the round 1 review. The project delivers 9 deep-dives (8 sections + overview), 3 synthesis papers, a 17-slide deck, and a 53+ source literature collection -- all built around a tension-mapping framework that gives the project genuine analytical value. The round 1 recommendation to add formal reference lists to all three papers has been addressed: each paper HTML now ends with a numbered `<ol class="ref-list-num">` section with `id="ref-N"` anchors (survey: 19 refs, tensions: 16 refs, scenarios: 10 refs). Wikipedia-style inline citations (`sup.fn` with tooltip previews) have been added across all 8 section deep-dives (63 total citations) and all 3 paper HTMLs (51 total citations). The central paradox framing -- extraordinary capability coexisting with modest enterprise value -- is sustained coherently across every deliverable.

The remaining weaknesses are concentrated in three areas: the markdown paper files still lack any citation apparatus, the slide deck has 5 SVGs across 17 slides (falling short of the methodology's "every content slide" target), and source coverage in S6 (5 sources) and S8 (5 sources) remains thinner than other sections. These are genuine but bounded gaps in an otherwise thorough project.

**Content Quality: A**
**Paper-Drive Compliance: A-**

## Completeness Scorecard

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | Literature collection | PASS | 53+ sources across 9 categories (8 sections + forward-looking). Each entry has ID, source name, key data points, and date. Tension synthesis table at bottom. Collection statistics accurate. |
| 2 | Source adequacy | PASS | Documented in changelog: S2 expanded from 3 to 10 sources, S3 from 7 to 10. All 8 sections meet the 5+ minimum. Assessments recorded before building. S6 and S8 at the minimum (5 each). |
| 3 | Deep-dives (9/8) | PASS | All 8 planned sections built plus an overview deep-dive. Panel counts: S1(10), S2(10), S3(9), S4(9), S5(8), S6(6), S7(7), S8(7), overview(9) = 75 total panels. 54 SVG diagrams across deep-dives. |
| 4 | Citations in deep-dives | PASS | All 8 section deep-dives contain `sup.fn` Wikipedia-style citations with tooltip previews. S1 leads with 26 citations; S2-S8 have 4-6 each. 63 total across deep-dives. |
| 5 | Papers (3/3) | PASS | Survey (~4K words, 12 sections), tensions (~3.5K words, 6 contradictions), scenarios (~3.5K words, 3 scenarios + signal dashboard). All have HTML renderings with sidebar nav, theme toggle, and `sup.fn` citations (17 each in survey and tensions, 17 in scenarios). |
| 6 | Paper reference lists | PASS | All 3 paper HTMLs now have formal reference sections (`<section id="references">`) with numbered `<ol>` lists. Survey: 19 refs, tensions: 16 refs, scenarios: 10 refs. Each ref links to an external URL. Addresses round 1 weakness. |
| 7 | Slides | PARTIAL | 17-slide deck with arrow-key nav, light/dark theme, progress bar. 5 SVG diagrams. Methodology target states "every content slide has an SVG diagram"; with ~10 content slides (excluding title, TOC, 5 section dividers, closing), coverage is 5/10. |
| 8 | Index deliverable cards | PASS | 13 deliverable cards: 1 overview, 8 section deep-dives, 3 papers, 1 slide deck. Each has descriptive text, source count, and link(s). 6 tension summaries with section cross-references. Meta links to methodology, lit collection, changelog, TODO. |
| 9 | Index badges accurate | PASS | All 13 cards show `<span class="status done">done</span>`. Verified: all linked files exist, all deep-dives render (template JS builds DOM from `sections[]`, `summaries[]`, `details[]` arrays), all papers have content. No stale "wip" or "planned" badges. |
| 10 | .project/ management | PASS | 6 files: changelog.md (detailed 8-phase session log), todo.md (all items checked, one remaining item flagged), paper-drive-methodology.md (7-phase workflow), continuation-prompt.md, agentic-peer-review.md, image-banana-claude.md. Changelog documents source adequacy decisions and bug fixes. |

## Content Quality

**Analytical framework:** The six-tensions framework remains the project's most distinctive contribution. Each tension is grounded in specific, named, quantified sources on both sides (e.g., Yale "no discernible disruption" vs Goldman "+3pp young tech workers"). The tensions paper goes further with "why both sides are right" and "what would resolve it" sub-sections for each -- a structure that elevates the work from summary to analysis.

**Data rigor:** Claims throughout the project are backed by specific numbers with source attribution. The literature collection provides traceable IDs (T-01 through T-08, M-01 through M-10, etc.) that can be cross-referenced to deep-dive content. External link density is strong: 334 external links across all HTML files, with the three papers alone containing 108.

**Citation quality improvement:** The addition of `sup.fn` citations with tooltip previews across all deep-dives and papers is a significant improvement from round 1. The citation apparatus in the HTML papers is now complete: inline superscript numbers link to `id="ref-N"` anchors in a formal references section at the bottom of each paper. The tooltips provide source URLs on hover, enabling verification without scrolling.

**Synthesis quality:** The survey paper compresses 8 deep-dives into a coherent narrative without losing the tension structure. The scenarios paper is particularly well-constructed: the argument that the "middle scenario" may be least likely (because installation-phase economics tend toward binary outcomes) is non-obvious and well-supported. The signal dashboard transforms academic analysis into a practical monitoring framework.

**SVG diagrams:** 54 SVGs across 9 deep-dives provide visual anchoring for quantitative claims. Distribution is uneven: S1 has 11, S3 has 9, S4 and S5 have 7 each, while S6 has 4, S7 and S8 have 3 each. The overview has 4.

## Strengths

1. **Round 1 remediation.** The two most significant round 1 weaknesses -- missing paper reference lists and limited citation apparatus -- have been addressed. All 3 papers now have formal reference sections, and all 8 section deep-dives have Wikipedia-style `sup.fn` citations.

2. **Source adequacy discipline.** The changelog provides auditable evidence that S2 was assessed as insufficient (3 sources), 7 additional sources were found (including breaking news of the Sora shutdown), and only then was the deep-dive built. This discipline is the project's methodological backbone.

3. **Tension-first framing.** Treating contradictions between credible sources as the primary finding rather than noise to resolve gives every section an analytical edge. The six tensions are specific, data-grounded, and each suggests a concrete resolution signal.

4. **Comprehensive deliverable set.** 9 deep-dives (75 panels), 3 papers with reference lists, 17-slide deck with 5 SVGs, literature collection, synthesis notes, methodology document, and a clean index page linking everything. The dual-format approach (markdown + HTML for deep-dives and papers) serves both machine and human readers.

5. **Real-time source integration.** The Sora shutdown (March 24, 2026) was captured in S2 the day it happened, with multiple source citations (CNBC, Bloomberg, Variety, Deadline). This demonstrates the project's capacity for live updating.

6. **Methodological documentation.** The paper-drive-methodology.md is itself a reusable artifact, codifying the 7-phase workflow clearly enough that a different agent or human could follow it for a new project.

7. **Cross-referencing.** The index page's tension summaries link directly to relevant deep-dives (e.g., T1 links to S4, T2 to S5). The 145 cross-reference links documented in the changelog create a navigable web between sections.

## Weaknesses

1. **Markdown papers lack citations.** The .md files for all three papers (survey-paper.md, tensions-paper.md, scenarios-paper.md) contain no inline citations of any kind -- no `[source, date]`, no footnotes, no numbered references. The methodology document describes markdown as "where the thinking happens," but these files are not self-contained research documents without citations. A reader of the markdown files has no way to verify any claim.

2. **Slide SVG coverage gap.** The methodology document states "every content slide has an SVG diagram." The deck has 17 slides with 5 SVGs. Excluding 1 title slide, 1 TOC slide, 5 section dividers, and 1 closing slide, there are approximately 9 content slides -- meaning roughly 4 content slides lack SVG diagrams.

3. **Uneven citation density in deep-dives.** S1 has 26 `sup.fn` citations; the other 7 sections have 4-6 each. This suggests S1 received a thorough citation pass while S2-S8 may have received a lighter treatment. The discrepancy does not affect readability but undermines consistency.

4. **Thin sourcing in S6 and S8.** Both sections have exactly 5 sources -- the stated minimum. S6 (Public Perception & Trust) relies heavily on the KPMG 48K study as anchor, with limited triangulation from other large-scale trust studies. S8 (Economics & Infrastructure) covers a $500B+ market with only 5 sources, leaving room for additional perspectives (e.g., Morgan Stanley, Bank of America, or Sequoia's AI market analyses).

5. **S2 panel depth still flagged.** The TODO explicitly notes: "S2 panel depth: currently OK (~3K), could reach DEEP (~7K)" -- the only item not checked off. The sources are collected (10 sources), making this a deepening task rather than a research task, but it remains unresolved.

6. **Overview deep-dive under-developed.** The overview has only 3 external source links and 4 SVGs, significantly less than section deep-dives (which average 25+ external links and 6+ SVGs each). As a 9-section overview serving as the project's top-level entry point, it would benefit from denser citation and visual coverage.

7. **Literature collection agent source count discrepancy.** The collection statistics table lists AI Agents at 7 sources, but the actual agent section in the collection contains 10 entries (A-01 through A-10). The table appears not to have been updated after the gap-filling search.

## Recommendations

1. **Backfill citations into markdown papers.** Even a lightweight format like `(McKinsey 2025)` or `[ref 1]` inline would make the .md files self-contained. Given that the HTML papers already have numbered references, a mechanical pass to insert matching inline citations into the markdown would be relatively low-effort.

2. **Add SVG diagrams to remaining content slides.** 4-5 additional SVGs would bring the slide deck into compliance with the methodology's stated standard and strengthen the visual communication of quantitative claims.

3. **Equalize citation density across deep-dives.** S1's 26 citations demonstrate the target quality. A focused pass on S2-S8 to bring each to 10-15 citations would strengthen verifiability without requiring new research.

4. **Fix the literature collection statistics table.** Update the AI Agents row from 7 to 10, and verify other rows against actual entry counts. The table is a reader's first checkpoint for coverage assessment.

5. **Strengthen S6 sourcing.** Consider Edelman Trust Barometer AI findings, Eurobarometer AI surveys, or the OECD AI Policy Observatory trust data. These would provide geographic and methodological triangulation beyond the KPMG anchor.

6. **Complete S2 panel depth.** The TODO flags this explicitly. Deepening the 10 panels from ~3K to ~7K average would resolve the only unchecked deliverable item.

7. **Enrich the overview deep-dive.** Add external source links and 2-3 additional SVGs to match the density of section-level deep-dives. As the top-level entry point, the overview sets expectations for the project's depth.
