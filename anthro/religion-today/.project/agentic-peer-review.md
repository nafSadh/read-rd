# Peer Review: anthro/religion-today

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-26
**Round:** 2

## Overall Assessment

Since the round-1 review (2026-03-25), the most critical gap has been closed: all six section deep-dives (S1 through S6) now exist as fully built HTML files with substantial content, SVG diagrams, Wikipedia-style superscript citations with hover tooltips, and the read-aid template (sidebar, detail panels, theme toggle). The previously broken links from index.html are now functional and the "done" badges are accurate. The project now delivers 7 deep-dive HTML files, 2 synthesis papers, 6 section markdown notes, a literature collection, and a well-maintained .project/ directory.

The remaining gaps are secondary: deep-dive files contain no external hyperlinks in their citation tooltips (tooltips show source text but do not link out), the todo.md has not been updated to reflect the completed S3-S6 builds, no slide deck exists, and the papers' reference entries could be fuller. The intellectual substance remains strong and the project reads as a coherent, well-sourced survey.

**Content Quality: A-** -- Strong analytical substance across all deliverables, consistent design system, Wikipedia-style citations now present in all deep-dives, and the unbundling thesis is well-argued. The remaining gaps (no outbound links in deep-dive citations, terse reference entries in the tensions paper) prevent a full A.

**Paper-Drive Compliance: B+** -- All core deliverables are built and linked. The literature collection, source adequacy tracking, deep-dives, and papers are complete. Deductions for: no slide deck, stale todo.md, deep-dive citations lacking outbound URLs, and tensions paper having only 9 reference entries versus the survey paper's 22.

## Completeness Scorecard

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | Literature collection | Pass | 52 sources across 6 sections. IDs, key data points, dates. Source diversity: Pew, Gallup, PRRI, Inglehart, Ecklund, Berger, Nature Communications, GWI, McKinsey, ACT Alliance, Johns Hopkins, and journalism. |
| 2 | Source adequacy checks | Pass | Explicit adequacy table in todo.md: 8-10 sources per section, all adequate. Methodology states 5-6 minimum threshold. Every section exceeds it. |
| 3 | Deep-dives completeness | Pass | All 7 deep-dives built (overview + S1-S6). Each uses the read-aid template with sidebar navigation, detail panels, theme toggle. S3: 265 lines, 8 subsections. S4: 245 lines, 7 subsections. S5: 247 lines, 7 subsections. S6: 243 lines, 7 subsections. SVG diagrams present in all files (14-21 svg/viewBox occurrences per file). |
| 4 | Wikipedia-style citations | Pass | All deep-dives now have sup.fn citations with hover tooltips: overview (16), S1 (17), S2 (12), S3 (16), S4 (12), S5 (11), S6 (14). Total: 98 data-cite occurrences across deep-dives. However, tooltip text is plain-text source attribution without outbound hyperlinks (unlike the papers, where citation tooltips contain clickable links). |
| 5 | Papers with 20+ links + reference lists | Pass | Survey paper: 22-item numbered reference list, each with external href. 39 total external links. Tensions paper: 9-item reference list with external links, 18 total external links. Both have sidebar nav, theme toggle, SVG diagrams, stat rows, and callout blocks. |
| 6 | Slides | Fail | No slide deck exists. Marked "Optional" in todo.md but expected in paper-drive compliance. |
| 7 | Index deliverable cards + accurate badges | Pass | Both paper cards marked "done" with working links. All 6 section deep-dive cards marked "done" with working links. Overview card marked "done" with working link. No broken links remain. |
| 8 | Content quality | Pass | Six-tension framework with data-grounded analysis. Unbundling meta-thesis. Specific data points traced to named sources throughout. "What We Cannot Know" section in survey paper shows intellectual honesty. Verdict/pro-con grids in deep-dives present balanced evidence. |
| 9 | .project/ management | Partial | changelog.md, methodology.md, todo.md, continuation-prompt.md, image-banana-claude.md all present. Changelog records all phases. However, todo.md is stale: it lists S3-S6 deep-dives as "NOT built" and shows them under "Remaining" despite all four being complete. The changelog also does not record the S3-S6 build or the citation retrofit. |
| 10 | Design system consistency | Pass | All HTML deliverables share: EB Garamond + Jost + IBM Plex Mono type stack, light/dark theme toggle with localStorage persistence, CSS custom properties, grain texture overlay, consistent component patterns (callouts, stat rows, diagram wraps, sidebar nav). Deep-dives use the read-aid template with detail panels. Papers use scroll-based sidebar with IntersectionObserver. |

## Content Quality

The analytical substance is the project's strongest asset. The six-tension framework provides genuine intellectual value: each tension is grounded in specific data from opposing sources rather than constructed as a rhetorical device. The unbundling thesis -- that religion is being disaggregated into separable components (belief, ritual, community, identity, morality) redistributed across new containers -- is a strong synthetic claim that emerges naturally from the evidence across all six dimensions.

The deep-dives demonstrate substantive engagement with sources. S3 (Fundamentalism) handles the three-theater comparison (US Christian nationalism, Indian Hindu nationalism, political Islam) with appropriate nuance, including the critical distinction between fundamentalism and orthodoxy drawn from ACT Alliance. S4 (Religion & Science) correctly identifies the gap between the public's "warfare thesis" and the scholarly "complexity thesis." S5 (New Movements) connects the wellness economy data to the unbundling framework. S6 (Interfaith) distinguishes secularism from pluralism as competing frameworks for managing religious diversity.

The survey paper's structure (6 dimensions, synthesis, methodology, references) is well-organized and the data density is high without sacrificing readability. The tensions paper's vs-comparison grids are an effective visual device.

## Strengths

1. **All deep-dives now complete with citations.** The most critical round-1 finding (4 missing deep-dives with false "done" badges) has been fully resolved. All 7 deep-dives are built with the read-aid template, include SVG diagrams, and have Wikipedia-style superscript citations with hover tooltips. The citation counts are substantial (11-17 per file, 98 total across deep-dives).

2. **Literature collection breadth and rigor.** 52 sources spanning survey data (Pew, Gallup, PRRI), academic monographs (Inglehart, Ecklund, Berger), Nature Communications, market research (GWI, McKinsey, Grand View), and journalism. Source adequacy is explicitly tracked per section with a threshold and a table.

3. **Analytical framework.** The six tensions and the unbundling meta-thesis elevate this beyond a descriptive survey into genuine synthesis. The project identifies where credible sources disagree rather than cherry-picking a single narrative. The verdict grids in deep-dives (pro/con columns) demonstrate balanced presentation.

4. **Design system consistency.** Every HTML file shares a coherent visual language. The deep-dives use the same read-aid template with identical CSS custom property names, theme toggle behavior, and component patterns. The papers use a scroll-based layout with sidebar tracking. Both systems are polished and functional.

5. **Survey paper reference quality.** 22 numbered references with full bibliographic information and external links to source URLs. Sources include Pew, Gallup, PRRI, Oxford UP, Nature Communications, PNAS, Johns Hopkins, McKinsey, and others.

## Weaknesses

1. **Deep-dive citations lack outbound links.** While all deep-dives now have sup.fn citations with hover tooltips, the tooltips contain only plain-text source attributions (e.g., "Pew Research, 'Religious Nationalism Around the World,' Jan 2025"). The paper citations, by contrast, include clickable links in their tooltips that open the source URL. Zero external hrefs appear in any deep-dive file beyond Google Fonts. This means readers cannot click through to verify sources from the deep-dives.

2. **Stale project management files.** todo.md lists S3-S6 as "NOT built" under "Remaining" and shows the status line as "Papers complete. S3-S6 deep-dives pending." The changelog does not record the S3-S6 build session or the Wikipedia-style citation retrofit. The continuation-prompt.md still lists "Build S3 HTML deep-dive" as the first next step. These files no longer reflect the actual project state.

3. **No slide deck.** The paper-drive workflow expects slides as a deliverable. The todo marks this as "Optional," but its absence still represents incomplete pipeline coverage.

4. **Tensions paper reference list is thin.** Only 9 reference entries compared to the survey paper's 22. Several key sources cited in the body (e.g., Pew Religious Nationalism, PRRI, Gallup, GWI, Subsplash) are missing from the reference list.

5. **No cover image or visual identity.** The changelog notes a failed Gemini Imagen attempt. While minor, the project index has no hero image or visual branding element.

## Recommendations

1. **Add outbound links to deep-dive citation tooltips.** Retrofit the sup.fn tooltip spans in all 7 deep-dive files to include clickable anchor tags pointing to source URLs, matching the pattern used in survey-paper.html. This is the highest-impact improvement remaining.

2. **Update project management files.** Update todo.md to mark S3-S6 as complete, add a changelog entry for the deep-dive build session and citation retrofit, and update continuation-prompt.md to reflect current state. Accurate project tracking is a core paper-drive requirement.

3. **Expand the tensions paper reference list.** Add the missing sources (Pew Religious Nationalism, PRRI CN, Gallup, GWI, Subsplash, Barna, etc.) to bring the reference list closer to the survey paper's 22-entry standard.

4. **Build a minimal slide deck.** A 10-12 slide deck covering the six tensions with key data points and SVG diagrams would complete the paper-drive pipeline and provide a shareable summary.

5. **Add a Limitations section to methodology.md.** The survey paper includes a brief limitations paragraph, but the standalone methodology document does not address limitations, data gaps, or methodological caveats.
