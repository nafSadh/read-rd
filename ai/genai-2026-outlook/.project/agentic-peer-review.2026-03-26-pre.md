# Peer Review: ai/genai-2026-outlook

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25

## Overall Assessment

This is a remarkably complete paper-drive project. Eight section deep-dives, three synthesis papers, a slide deck, and a well-maintained literature collection of 53+ sources were produced in what appears to be a single extended session. The central framing -- mapping tensions rather than asserting consensus -- gives the project genuine intellectual value beyond a typical survey. The methodology is well-documented, the source adequacy discipline was followed (with evidence of gap-filling searches for S2 and S3), and the deliverable set is comprehensive.

The main weaknesses are the absence of Wikipedia-style inline citations in the markdown papers (though the HTML papers do have footnoted citations with tooltips), somewhat thin source coverage in S6 (5 sources) and S8 (5 sources), and papers that lack formal reference lists at the bottom. The deep-dives have strong SVG diagram coverage (54 total across 9 files) and substantial external source linking (222 links across deep-dives). Content quality is high: data-backed claims, named sources, specific numbers, and genuine engagement with contradictions rather than false synthesis.

**Content Quality: A-**
**Paper-Drive Compliance: A-**

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | ✅ | 53+ sources across 8 sections + forward-looking + tensions. Well-structured with IDs, key data points, dates. |
| Source adequacy checks | ✅ | Documented in changelog: S2 assessed as insufficient (3 sources), searched and expanded to 10. S3 similarly expanded. All sections met 5+ minimum. |
| Deep-dives (9/8 built) | ✅ | All 8 planned sections complete plus an overview deep-dive. 54 SVG diagrams total. 222 external source links across deep-dives. |
| Papers (3/3) | ✅ | Survey paper (~4K words), tensions paper (~3.5K words), scenarios paper (~3.5K words). All have HTML renderings with sidebar nav. |
| Slides | ✅ | 17-slide deck with 5 SVG diagrams, arrow-key navigation, light/dark theme. ~30 slide elements. |
| Index deliverable cards | ✅ | Clean index page with overview, 8 section cards, 4 paper/slide cards, 6 tension summaries. All status badges show "done". Links to methodology, lit collection, changelog, TODO. |
| .project/ management | ✅ | changelog.md (detailed session-by-session), todo.md (all items checked), paper-drive-methodology.md (comprehensive 7-phase workflow), continuation-prompt.md. |
| Citations (Wikipedia-style) | ⚠️ | HTML papers have superscript footnotes with tooltip previews (`<sup class="fn">`) and `id="ref-N"` anchors (19 in survey paper). Markdown papers have no inline citations. Deep-dives use inline source links rather than numbered citations. |
| External source links (20+) | ✅ | Survey paper HTML: 48 external links. Tensions paper: 32. Scenarios paper: 28. Total across papers: 108. Deep-dives: 222 additional. |

## Content Quality

**Intellectual depth:** The project goes well beyond summary. The six-tensions framework is the project's most original contribution -- identifying where credible sources contradict each other and treating those contradictions as the primary finding rather than noise to be resolved. The Dallas Fed career-ladder analysis in S5, the NVIDIA efficiency counter-narrative in S1, and the production-vs-demo gap in S3 all represent genuine analytical insight.

**Synthesis quality:** The survey paper successfully compresses 8 deep-dives into a coherent 12-section narrative without losing the tensions. The scenarios paper is particularly strong -- the argument that the "middle scenario" may be least likely because installation-phase economics tend toward binary outcomes is well-reasoned and non-obvious.

**Data usage:** Claims are consistently backed by specific numbers with source attribution (e.g., "SWE-bench 4% to 72%", "48,000 people across 47 countries", "$500B+ capex"). The project avoids vague claims and consistently names its sources.

**Tensions and disagreements:** Exceptionally well-handled. Every section ends with explicit "consensus" and "where sources disagree" framing. The tensions paper devotes full sections to each contradiction with "why both sides are right" and "what would resolve it" sub-sections.

## Strengths

- Source adequacy discipline was genuinely followed, not just documented. The changelog shows S2 was assessed as insufficient, gaps were identified, 7 additional sources were found, and only then was the deep-dive built.
- Tensions-first framing elevates the project from survey to analysis. The six tensions are specific, data-grounded, and actionable.
- Comprehensive SVG diagram coverage in deep-dives (54 diagrams) provides visual anchoring for quantitative claims.
- The scenarios paper's signal dashboard provides a practical monitoring framework that transforms academic analysis into decision-support.
- Breaking news integration (Sora shutdown on March 24) demonstrates real-time source responsiveness.
- Strong cross-referencing: 145 cross-reference links documented in changelog, linking sections to each other and to source materials.
- The methodology document is itself a valuable artifact -- it codifies the paper-drive workflow clearly enough to be reused.

## Weaknesses

- S6 (Trust) has only 5 sources and S8 (Economics) has only 5 sources. While both meet the stated minimum, they are thinner than S1-S4 (8-10 sources each). S6 in particular leans heavily on the KPMG study as anchor, with limited triangulation from other large-scale trust studies.
- The markdown versions of all three papers lack inline citations entirely. The HTML versions have footnoted citations, but a reader of the .md files gets no citation apparatus. For a paper-drive project, the markdown should be citation-complete since it is described as "where the thinking happens."
- Papers lack formal reference/bibliography sections. The HTML papers end without a numbered reference list. The `id="ref-N"` anchors exist but there is no consolidated references section at the bottom of any paper.
- The overview deep-dive (genai-2026-overview.dd.html) has only 3 external source links and 4 SVG diagrams, significantly less than the section deep-dives. As a 9-section overview, it could benefit from more visual and citation density.
- S2 panel depth is flagged in the TODO as "currently OK (~3K), could reach DEEP (~7K)" and remains unresolved. This is the only section with a known quality gap explicitly acknowledged but not addressed.
- The slide deck has 5 SVG diagrams across 17 slides. The methodology document states "every content slide has an SVG diagram" as a target. With ~12 content slides (excluding title, TOC, dividers, closing), this falls short of the stated standard.
- No audio narration for the slide deck (the overview deep-dive has an .mp3, but slides do not).

## Recommendations

1. **Add a references section to each paper HTML.** The `id="ref-N"` anchors are already in place. A consolidated bibliography at the bottom of each paper would complete the citation apparatus and bring the papers closer to publication-ready format.

2. **Backfill citations into the markdown papers.** Even a simple `[source name, date]` inline format would make the .md files self-contained research documents rather than citation-free drafts.

3. **Strengthen S6 (Trust) sourcing.** Consider adding Edelman Trust Barometer AI data, Eurobarometer AI surveys, or the AI Policy Observatory trust metrics. Five sources for a section on public perception across 47 countries leaves room for geographic and methodological triangulation.

4. **Complete S2 panel depth.** The TODO explicitly flags this as unfinished (~3K vs target ~7K). Since the sources are already collected (10 sources), this is a deepening task, not a research task.

5. **Add SVG diagrams to remaining content slides.** The methodology document sets the standard at one diagram per content slide. Adding 5-7 more diagrams would meet the project's own stated criteria.

6. **Consider a fourth paper.** The project's source base and analytical depth could support a position paper on the career-ladder thesis (Dallas Fed + Goldman + Brookings data). The employment analysis in S5 is among the project's strongest original synthesis and deserves standalone treatment.
