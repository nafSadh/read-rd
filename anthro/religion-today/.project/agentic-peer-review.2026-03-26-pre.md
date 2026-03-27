# Peer Review: anthro/religion-today

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25

## Overall Assessment

This is an ambitious and well-scoped anthropological survey of religion in the contemporary world, organized around six thematic dimensions and culminating in a compelling "unbundling thesis." The literature collection is strong (52 sources across credible survey data, academic sociology, market research, and journalism), and the two synthesis papers -- the survey paper and the tensions paper -- are substantive deliverables with inline SVG diagrams, Wikipedia-style footnote citations, and 22 external reference links in the survey paper alone. The project demonstrates genuine analytical insight, particularly in its identification of six tensions where sources contradict each other, and in its meta-thesis that religion is being unbundled rather than simply declining or resurging.

However, the project is materially incomplete: 4 of 6 section deep-dives (S3 through S6) exist only as markdown notes -- the HTML deep-dive files are not built, yet the index page links to them as if they are done (all marked with a "done" status badge and linking to nonexistent `.dd.html` files). There is no slide deck. The deep-dive files that do exist (overview, S1, S2) lack Wikipedia-style inline citations, which are present only in the papers. These gaps prevent a top grade.

**Content Quality: B+** -- The intellectual substance is strong, but the incomplete deliverables and inconsistent citation practices across file types hold it back.
**Paper-Drive Compliance: C+** -- Key deliverables are missing (4 deep-dives, slides), the index misrepresents completion status, and citation style is inconsistent.

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | ✅ | 52 sources across 6 sections, well-organized with IDs, key data points, and dates. Source diversity is good: Pew, Gallup, PRRI, academic monographs, Nature Communications, market research. |
| Source adequacy checks | ✅ | Explicit adequacy table in todo.md confirms 8-10 sources per section, all marked adequate. Methodology states minimum 5-6 threshold. |
| Deep-dives (2/7 built) | ❌ | Only overview.dd.html, s1-global-landscape.dd.html, and s2-rise-of-nones.dd.html exist as HTML. S3, S4, S5, S6 .dd.html files do not exist on disk despite being linked from index.html with "done" badges. Markdown notes for all 6 sections are complete. |
| Papers | ✅ | survey-paper.html (55KB) and tensions-paper.html (39KB) are both substantial. Survey paper has 8 sections with SVG diagrams, sidebar nav, theme toggle, and a 22-item reference list with external links. Tensions paper has 6 tension blocks with vs-comparison grids and a meta-tension synthesis. |
| Slides | ❌ | No slide deck exists. Marked "Optional" in todo.md. |
| Index deliverable cards | ⚠️ | index.html has deliverable cards for both papers and section deep-dives with links and status badges. However, S3-S6 deep-dive links point to nonexistent files (8 broken href references). All 6 sections are marked "done" which is inaccurate. |
| .project/ management | ✅ | changelog.md, methodology.md, todo.md, and continuation-prompt.md are all present and well-maintained. The todo correctly identifies S3-S6 as incomplete. Continuation prompt provides clear next-step instructions. |
| Citations (Wikipedia-style) | ⚠️ | Survey paper has 12 Wikipedia-style superscript footnotes with hover tooltips (sup.fn class). Tensions paper has 5. Deep-dive HTML files (overview, S1, S2) have zero inline citations -- they rely on implicit source attribution in prose. Inconsistent citation practice across deliverable types. |
| External source links (20+) | ✅ | Survey paper references section contains 22 externally-linked sources. Tensions paper has approximately 18 href links. Literature collection provides full source details. Combined across all files, the project substantially exceeds 20 external links. |

## Content Quality

The analytical substance of this project is its greatest asset. The six-tension framework is not merely a list of contradictions but a genuine analytical lens: each tension (growth vs. decline, belief vs. belonging, nationalism vs. pluralism, science vs. faith framing, secular wellness vs. religious practice, digital expansion vs. institutional decline) is grounded in specific data points from opposing sources. The "unbundling thesis" -- that religion is being decomposed into separable components (belief, ritual, community, identity, morality) that are recombined in new configurations -- is a strong synthetic claim that emerges naturally from the evidence.

The survey paper's structure (6 dimensions plus synthesis plus methodology) is well-organized, and the inclusion of a "What We Cannot Know" section shows intellectual honesty. Data points are specific and traceable (e.g., "29% of US adults unaffiliated," "Islam +347M," "$6.8T wellness economy").

The tensions paper's vs-comparison grids are an effective visual device for presenting contradictory evidence side by side.

## Strengths

1. **Literature collection breadth and rigor.** 52 sources spanning survey data (Pew, Gallup, PRRI), academic monographs (Inglehart, Ecklund, Berger), a Nature Communications study, market research (GWI, McKinsey, Grand View), and journalism. Source adequacy is explicitly tracked per section.

2. **Analytical framework.** The six tensions and the unbundling meta-thesis elevate this beyond a descriptive survey into genuine synthesis. The project identifies where credible sources disagree rather than cherry-picking a single narrative.

3. **Design system consistency.** All HTML deliverables share a coherent visual language: EB Garamond + Jost + IBM Plex Mono type stack, light/dark theme toggle, accent color palette, grain texture overlay, and consistent component patterns (callouts, stat rows, diagram wraps).

4. **Paper quality.** Both papers are substantial (55KB and 39KB respectively), include inline SVG data visualizations, sidebar navigation, and a proper reference list with external links.

5. **Project management.** The .project/ directory is well-maintained with accurate todo tracking, clear continuation prompts, and a detailed changelog that records the phases of work.

## Weaknesses

1. **Four missing deep-dives with false "done" status.** S3-S6 deep-dive HTML files do not exist, but the index.html marks all six sections as "done" and provides links to the nonexistent files. This creates 8 broken links on the project's landing page. The todo.md correctly identifies these as incomplete, but the index misrepresents the project's state to readers.

2. **No slide deck.** The paper-drive workflow expects slides as a deliverable. The todo marks this as "Optional," but the absence still represents incomplete pipeline coverage.

3. **Inconsistent citation practice.** The papers use Wikipedia-style superscript footnotes with hover tooltips, but the deep-dive HTML files (overview, S1, S2) have no inline citations at all. Sources are mentioned by name in prose but not linked with a formal citation apparatus. This creates a two-tier quality standard within the same project.

4. **Reference list brevity in papers.** While the survey paper has 22 references with external links, several entries are terse (e.g., just "Pew Research Center" or "Ecklund" with a link). Full bibliographic entries (author, title, date, publication) would strengthen the academic framing.

5. **No cover image.** The changelog notes a failed attempt with Gemini Imagen (403 error). While minor, this leaves the project without a visual identity element.

## Recommendations

1. **Build S3-S6 deep-dives or remove "done" badges.** The highest-priority fix is either building the four remaining deep-dive HTML files from the existing markdown notes (which are complete and adequate) or updating index.html to mark S3-S6 as "planned" / "wip" and removing the broken links. Shipping broken links undermines reader trust.

2. **Add Wikipedia-style citations to existing deep-dives.** Retrofit inline superscript citations into overview.dd.html, s1-global-landscape.dd.html, and s2-rise-of-nones.dd.html to match the citation standard set by the papers.

3. **Expand reference entries.** Convert the terse reference list items in survey-paper.html into fuller bibliographic citations (e.g., "Inglehart, Ronald F. *Religion's Sudden Decline*. Oxford University Press, 2021.").

4. **Build a slide deck.** Even a minimal 10-15 slide deck covering the six tensions with SVG diagrams would complete the paper-drive pipeline and provide a shareable summary artifact.

5. **Add a Limitations section to methodology.md.** The survey paper includes a brief limitations paragraph, but the standalone methodology.md in .project/ does not address limitations. The todo notes this as optional but recommended.
