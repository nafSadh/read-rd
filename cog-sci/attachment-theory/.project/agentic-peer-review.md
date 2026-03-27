# Peer Review: cog-sci/attachment-theory

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-26
**Round:** 2

## Overall Assessment

This project has matured significantly since the round 1 review. The two most critical gaps identified previously -- the missing S7 deep-dive and the absence of Wikipedia-style citations in the deep-dives -- have both been addressed. S7 (Personal Application) is now built with 8 subsections and marked "done" on the index. The deep-dive files now carry 69 superscript footnote citations with hover tooltips across S1-S6 (S1: 13, S2: 7, S3: 9, S4: 8, S5: 10, S6: 7), plus 4 in the overview. The survey paper retains its 36 numbered references. The project now delivers 9 interactive HTML pages (overview + 7 section deep-dives + survey paper), a 16-slide deck, a 40-source literature collection, and a well-maintained project index with accurate status badges.

The remaining gaps are secondary: stale metadata files (methodology.md, continuation-prompt.md), S5's inline CSS/JS, unfilled source gaps from the literature collection, and the still-unwritten standalone synthesis paper. None of these undermine the project's core intellectual achievement, which is a genuinely critical, multi-dimensional survey that treats attachment theory as contested rather than settled.

**Content Quality: A**
**Paper-Drive Compliance: A-**

## Completeness Scorecard

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | Literature collection | PASS | 40 sources across 6 sections with IDs, links, dates, key data points, and identified gaps. Tensions table included. Collection statistics summary at bottom. |
| 2 | Source adequacy checks | PASS | Explicit adequacy table in todo.md. All 6 research sections marked ADEQUATE. Gaps acknowledged per section (Fraley & Spieker taxometric, Gottman/Johnson, Mesman/Keller primary papers). |
| 3 | Deep-dives (8/8 built) | PASS | All 8 planned deep-dives built (overview + S1-S7). Each has 8 subsections with summary cards and detail panels. S7 was the last to be completed, resolving the round 1 gap. |
| 4 | Deep-dive citations | PASS | 73 Wikipedia-style superscript citations (`sup.fn`) with hover tooltips across 7 files (S1-S6 + overview). S7 has 0 citations, appropriate for a reflective/applied section. This resolves the primary round 1 complaint. |
| 5 | Papers (20+ links) | PASS | survey-paper.html: 8 sections (abstract, 6 dimensions, synthesis, methods) + references. 36 numbered refs with superscript citations and hover tooltips. 2 SVG diagrams. 6 tension cards. Well above the 20-link threshold. |
| 6 | Slides | PASS | survey-slides.html: 16 slides with 5 SVGs. Title, TOC, per-dimension slides, synthesis, tensions, conclusion. Navigation, progress bar, dark mode. |
| 7 | Index deliverable cards + badges | PASS | index.html has deliverable card grid (survey paper + slides), overview entry, 7 section deep-dive entries with source counts, status badges (all "done"), and 6 key tensions. All badges are accurate. |
| 8 | .project/ management | PARTIAL | 5 files (methodology, todo, changelog, continuation-prompt, image-banana-claude). Changelog is detailed. Todo has source adequacy table. However: methodology.md deliverables checklist still stale (literature collection unchecked). continuation-prompt.md still reports 31 sources (actual: 40) and lists S7 as future work despite completion. |
| 9 | Content quality + analytical depth | PASS | Each deep-dive has 8 substantive subsections. Writing engages with tensions rather than summarizing. The "science-to-folk pipeline" thesis is original. SVG diagrams, stat bars, verdict panels, and cross-references create a cohesive research web. |
| 10 | Design + technical consistency | PARTIAL | 7 of 8 deep-dives use dd-shared.css/js. S5 remains self-contained with inline CSS/JS (~250 lines of CSS variables + layout rules duplicated from the shared file). This is a maintenance liability but not a content issue. |

## Content Quality

The analytical writing remains the project's strongest asset. The depth of engagement with sources is above what most paper-drive projects achieve:

- S5 (Critique) remains the standout, with systematic treatment of 6 distinct lines of criticism, each backed by named researchers and specific findings. The "era of exhaustion" framing from Thompson et al. (2022) anchors the section in the field's own self-assessment.
- S1 (Origins) now has 13 inline citations -- the densest of any deep-dive -- linking claims to Bretherton, Simply Psychology, Attachment Project, Flaherty & Sadler, Wikipedia, BPS, and Vicedo. The political context subsection (Bowlby's WHO report, Vicedo's SSP critique) shows genuine historiographic engagement.
- S6 (Healing) provides evidence-based assessments of three therapeutic modalities (EMDR, SE, EFT) with specific effect sizes (Cohen's d values) and RCT counts, avoiding the therapeutic cheerleading common in pop psychology treatments.
- S7 (Personal Application) successfully walks the line between practical and reflective. The "three traps" framework (identity, diagnosis, insight) is a useful contribution. The verdict panel ("Use This" vs. "Resist This") distills the project's central argument into actionable guidance.
- The survey paper's abstract is notably strong -- it states the central finding, names specific evidence (r=.30, 52% avoidant in Germany, 0% in Japan), and arrives at a conclusion ("useful rather than true") that is earned rather than assumed.

## Strengths

1. **Critical round 1 gaps resolved.** The two highest-priority recommendations from round 1 -- build S7 and add Wikipedia-style citations to deep-dives -- have been implemented. This demonstrates responsive project management.

2. **Citation density is now substantial.** 73 inline citations across the deep-dives, each with a hover tooltip linking to the source URL and identified by the literature collection's ID system (O1, T1, A1, etc.). This creates traceability from claims to sources throughout the project.

3. **Intellectual integrity of the framing.** The project consistently holds attachment theory at arm's length -- taking the patterns seriously while questioning the framework. This is harder to sustain across 9 HTML pages than it sounds. The critical sections are not afterthoughts; they are structurally integrated.

4. **Survey paper as standalone deliverable.** The paper works independently of the deep-dives: it has its own abstract, 8 sections covering all dimensions, 36 references with full citation apparatus, 2 SVGs, and 6 tension cards. It could be shared without the rest of the project and would still communicate the findings.

5. **Source diversity across the evidence spectrum.** The 40 sources span meta-analyses (Fraley 2002, EMDR RCT meta-analysis 2023), foundational texts (Bretherton 1992), named critics (Kagan via Fatherly, Thompson et al. 2022), archival critique (Vicedo 2022), neuroscience proponents and critics (Porges 2009/2022/2025, Wikipedia PVT with Neuhuber & Berthoud), and clinical evidence bases (ICEEFT, Brom SE RCT 2017, de Jongh 2024).

6. **Synthesis notes and cross-referencing.** The "science-to-folk pipeline" (notes/00-synthesis.md) provides an original analytical framework that the survey paper operationalizes. Cross-references between deep-dives create navigable knowledge architecture.

## Weaknesses

1. **Stale project metadata.** methodology.md still shows the literature collection deliverable as unchecked (`[ ]`). continuation-prompt.md still reports 31 sources and lists tasks (gap-fill S6, build S5, build index) that were completed in session 2. These files are now significantly out of date across two review rounds. The todo.md is mostly current but still lists S7 as incomplete (`[ ] S7: Personal application deep-dive`).

2. **S5 inline CSS/JS.** S5 (The Critique) was the first deep-dive built and retains self-contained inline CSS variables and layout rules rather than linking to dd-shared.css. This means visual changes to the shared system (theme colors, spacing, typography) would not propagate to S5. The issue has been noted since session 2 but remains unaddressed.

3. **Identified source gaps remain unfilled.** The literature collection explicitly identifies missing primary papers: Fraley & Spieker (2003) taxometric analysis, Roisman et al. (2007) AAI-ECR convergence, Hazan & Shaver (1987), Mesman (2021), Keller (2021), Grossmann German SSP study, Miyake Japanese SSP study. These are repeatedly cited in the deep-dives by name but are not in the collection with their own IDs and links.

4. **Uneven citation density across deep-dives.** S1 has 13 citations; S6 and S2 have 7 each; the overview has only 4. S7 has 0 (defensible for a reflective section). The overview, as the project's entry point, would benefit from more inline citations connecting its summary claims to specific sources.

5. **Some commercial/practitioner sources.** Reachlink (T4), Calm Blog (H3), Kindman & Co (H4), and Good EMDR Therapy (H2) are practitioner or wellness-brand sites rather than peer-reviewed or institutional sources. They serve a documentary role (showing how the theory reaches consumers) but their inclusion alongside PMC meta-analyses can give a misleading impression of uniform rigor.

6. **No standalone synthesis paper.** The todo and methodology both reference a planned "Between Science and Folklore" synthesis paper distinct from the survey paper. The survey paper substantially fills this role, but the planned deliverable remains unbuilt. This should either be completed or formally removed from scope.

## Recommendations

1. **Update stale metadata (quick fix).** Mark literature collection as done in methodology.md. Update continuation-prompt.md to reflect current state (40 sources, all deep-dives built, survey paper and slides complete). Update todo.md to mark S7 as complete. This is 15 minutes of work that improves project hygiene significantly.

2. **Refactor S5 to shared CSS/JS.** Migrate S5's inline theme variables and layout rules to dd-shared.css. This was the round 1 recommendation that remains the easiest technical improvement.

3. **Add 2-3 citations to the overview deep-dive.** The overview has only 4 inline citations across 8 subsections. Adding citations to the critique, stability, and healing subsections would bring it in line with the other deep-dives and strengthen the entry point.

4. **Formally close or fill source gaps.** Either add the missing primary papers (Fraley & Spieker 2003, Roisman 2007, Hazan & Shaver 1987 at minimum) to the literature collection, or add a note explaining that these are cited via secondary sources and the gap is acceptable for the project's scope.

5. **Resolve the synthesis paper question.** If the survey paper is the synthesis paper, say so in the methodology and todo. If a separate paper is still planned, note it as a future deliverable. The ambiguity makes the project's completion status unclear.

6. **Consider adding an audio overview link to the index.** There is an overview.mp3 file in the project directory that is not linked from the index page. If this is a recorded overview, it should be discoverable.
