# Peer Review: physics/the-cosmos

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25

## Overall Assessment

This is a well-structured paper-drive project at the midpoint of execution. Three of seven planned section deep-dives are complete (S1: Scales, S2: Big Bang, S3: Dark Matter), plus a comprehensive overview deep-dive that covers all seven dimensions at summary level. A literature collection of 55 sources across all 7 sections is fully compiled, with notes written for every section (including the four not yet built as deep-dives). The synthesis notes provide a strong cross-cutting narrative. The project has a clear continuation plan and consistent template system.

The completed deep-dives are substantial: S2 (90KB, 9 SVGs, 8 sections) and S3 (82KB, 7 SVGs, 8 sections) demonstrate serious depth, with detail panels running 5-10K characters each. The overview deep-dive (71KB, 3 SVGs, 9 sections covering all planned topics) functions as a complete survey at reduced resolution. Content quality is high throughout -- claims cite specific numbers, named researchers, and concrete experimental results. The project treats tensions and open questions as first-class content rather than afterthoughts.

The primary weaknesses are incomplete execution (4 of 7 sections unbuilt), missing hero images for S2 and S3, no synthesis paper or slide deck yet, no inline citations or reference lists, and no cross-referencing links between sections. These are largely a consequence of being mid-project rather than quality deficiencies.

**Content Quality: A-**
**Paper-Drive Compliance: B** (incomplete; all completed components are high quality)

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | Done | 55 sources across 7 sections. Well-structured table with IDs, source names, key data points, and dates. Source adequacy assessment included. All sections marked adequate. |
| Source adequacy checks | Done | Each section's notes file begins with source count and explicit adequacy judgment. Ranges from 6 (Multiverse) to 10 (Frontiers). All assessed as adequate. |
| Deep-dives (3/7 built + overview) | Partial | S1 (8 sections, 2 SVGs, 48KB), S2 (8 sections, 9 SVGs, 90KB), S3 (8 sections, 7 SVGs, 82KB), Overview (9 sections, 3 SVGs, 71KB). S4-S7 not yet built. |
| Notes for all sections | Done | 8 markdown files: 00-synthesis.md plus 01 through 07. All contain synthesized content organized by sub-topic with source attribution. |
| Papers | Not started | No synthesis paper, tensions paper, or other standalone papers exist. Planned for after all sections are complete. |
| Slides | Not started | No slide deck exists. Planned for after papers. |
| Index page | Done | Clean design with badge, title, subtitle, section list with status indicators, key tensions list, and footer. Links to literature collection. 3 of 7 marked done, 4 planned. |
| Hero images | Partial | Overview hero (hero.png) and S1 hero (s01-scales.png, s1-hero.png) exist. S2 and S3 hero images not yet generated. Continuation prompt documents this gap with generation instructions. |
| .project/ management | Minimal | Only continuation-prompt.md exists. No changelog, no TODO file, no methodology document in the project directory. The continuation prompt is well-written but the project management artifact set is thin. |
| Citations (Wikipedia-style) | Missing | No inline citations in any deep-dive or notes file. Source attribution is present narratively (e.g., "Vera Rubin and Kent Ford") but no superscript footnotes, no reference anchors, no bibliography sections. |
| External source links | Minimal | The deep-dives do not contain hyperlinks to external sources. The literature collection has source names but not URLs. The overview has no outbound links. |
| Cross-referencing between sections | Missing | No deep-dive links to another deep-dive. Continuation prompt identifies this as a planned future pass. |

## Content Quality

**Intellectual depth:** The completed deep-dives demonstrate genuine engagement with the material. The Dark Matter deep-dive (S3) is particularly strong: it walks through five independent lines of evidence, gives specific experimental results (LZ: 280 days, no signal, 5x sensitivity improvement), addresses the contrarian MOND view fairly before explaining why Gaia data disfavors it, and treats the "detection crisis" as a serious intellectual challenge rather than a temporary inconvenience. The Big Bang deep-dive (S2) handles the inflation debate with appropriate nuance -- presenting both the strong circumstantial evidence and the legitimate criticism that an unfalsifiable eternal inflation may not qualify as science.

**Synthesis quality:** The synthesis notes (00-synthesis.md) successfully compress seven topics into a coherent narrative organized around the "95% ignorance problem." The six cross-cutting tensions are well-chosen and specific. The meta-observation that "all six tensions share a common structure" -- our best theories are extraordinarily successful yet leave fundamental questions unanswered -- is the project's most original contribution.

**Data usage:** Consistently strong. Claims are backed by specific values: "2.725 K," "r < 0.036," "n_s = 0.9649 +/- 0.0042," "280 days of data," "2.8-4.2 sigma." Named sources and dates appear throughout. The stat boxes in summaries effectively anchor key numbers.

**Diagram quality:** The SVG diagrams are informative and well-integrated. S2's "Three Pillars of Big Bang Evidence" diagram and S3's "Five Lines of Dark Matter Evidence" diagram provide clear visual structure. The overview's cosmic composition bar chart effectively communicates the 5%/27%/68% split. All diagrams use the project's CSS variable system for theme compatibility.

**Tensions treatment:** Each completed deep-dive ends with a "What We Know" consensus section (pro-list format), and the overview's dedicated "Six Tensions" section with its "Meta-Tension" callout is the structural heart of the project. The tensions are genuinely open questions, not straw positions to be demolished.

## Strengths

- Literature collection is comprehensive and complete for all 7 sections before any deep-dive was built. This is proper paper-drive discipline -- sources first, then assessment, then writing.
- The template system (shared CSS, shared JS DOM-builder, section-specific data arrays) ensures visual and structural consistency across deep-dives. The dark/light theme system works across all files.
- Detail panel depth in S2 and S3 is substantial (multi-paragraph treatments with embedded diagrams, timelines, feature grids, and callouts). These are not surface-level summaries.
- The overview deep-dive functions as a complete standalone survey. A reader who only reads overview.dd.html gets a coherent picture of all seven dimensions at meaningful depth.
- Notes files for all 7 sections (including the 4 unbuilt ones) contain synthesized, structured content ready for deep-dive construction. This front-loading of research work de-risks the remaining build phases.
- The continuation prompt is well-written with clear instructions for the next builder, including template mechanics, image generation references, and a sequenced task list.
- Source recency is strong: DESI 2025, LIGO O4 2025, JWST 2025-2026, Vera Rubin 2025-2026, Gaia wide binary 2024. The project reflects the state of cosmology as of early 2026.

## Weaknesses

- Four of seven section deep-dives (S4: Dark Energy, S5: Fermi Paradox, S6: Multiverse, S7: Frontiers) are not yet built. The project is at the ~43% mark for deep-dive execution despite having 100% of the research completed. This is the largest gap.
- No synthesis paper, no slide deck, and no standalone papers exist. The paper-drive pipeline stops at deep-dives. The continuation prompt acknowledges these as post-section deliverables.
- No inline citations anywhere. The deep-dives mention researchers and experiments by name but do not link to sources, provide footnotes, or include reference lists. For a research project with 55 collected sources, the citation apparatus is entirely absent from all HTML output.
- No external hyperlinks in the deep-dives. The literature collection lists source names but not URLs. A reader cannot click through to any primary source from any deep-dive page.
- The .project/ directory contains only a continuation prompt. No changelog tracking session history, no TODO checklist, no methodology document. The index.html links to a TODO file that does not exist. Compared to mature paper-drive projects in this repository, the project management layer is underdeveloped.
- Hero images are missing for S2 and S3. The continuation prompt documents this with generation instructions, but the HTML files reference images that do not exist on disk.
- S1 deep-dive (48KB, 2 SVGs) is noticeably lighter than S2 (90KB, 9 SVGs) and S3 (82KB, 7 SVGs). The S1 detail panels are shorter and contain fewer diagrams, suggesting it was built at an earlier stage of the template's maturity.
- The overview deep-dive has only 3 SVGs across 9 sections. Given that each section covers a major cosmological topic, the visual density is lower than in the section-specific deep-dives.

## Recommendations

1. **Complete S4-S7 deep-dives.** All notes and sources are ready. Follow the established S2/S3 pattern: 8 sections, 7-9 SVG diagrams, 5-10K character detail panels, consensus section at the end. Prioritize S4 (Dark Energy) and S7 (Frontiers) as these contain the most time-sensitive content (DESI results, Vera Rubin first light).

2. **Add inline citations and reference lists.** Implement the Wikipedia-style superscript footnote system visible in other read-rd projects (e.g., the genai-2026-outlook HTML papers use `<sup class="fn">` with tooltip previews). Each deep-dive should cite its sources from the literature collection using the existing IDs (SC-01, BB-02, DM-05, etc.).

3. **Add external source links.** Convert source names in the literature collection to clickable URLs. Add first-mention hyperlinks in each detail panel, linking to the source when it is first cited.

4. **Generate missing hero images.** S2 and S3 hero images are documented in the image generation instructions. Generate and save to `img/s2-hero.png` and `img/s3-hero.png`.

5. **Backfill S1 to match S2/S3 depth.** Expand S1 detail panels from their current ~2-3K characters to the 5-10K target. Add 3-5 more SVG diagrams (distance ladder schematic, Gaia precision diagram, cosmic web simulation comparison). The notes file has ample material.

6. **Create .project/ management files.** Add a changelog.md tracking session history, a todo.md with the deliverable checklist from the continuation prompt, and a methodology.md documenting the paper-drive approach. Fix the broken TODO link in index.html.

7. **Build cross-reference links.** Once S4-S7 are complete, add inter-section links (e.g., the dark matter section's MOND discussion should link to S1's Gaia discussion; S4's DESI results should link to S7's frontiers treatment). The continuation prompt already identifies this as a planned pass.

8. **Plan the synthesis paper.** The synthesis notes (00-synthesis.md) and the six cross-cutting tensions provide a strong outline. The "meta-tension" insight -- that our best theories are simultaneously triumphant and incomplete -- is a thesis worth developing into a standalone paper.
