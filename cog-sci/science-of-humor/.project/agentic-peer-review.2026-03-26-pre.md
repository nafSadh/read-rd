# Peer Review: cog-sci/science-of-humor

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25

## Overall Assessment

This is a strong, ambitious project that surveys the science of humor across seven interdisciplinary dimensions. The completed deliverables — a survey paper (55 sources, Wikipedia-style footnotes, SVG diagrams), a position paper arguing humor is irreducibly social (39 source links, 9 lines of evidence), two slide decks, an overview deep-dive, and three section deep-dives — are well-written, intellectually substantive, and visually polished. The literature collection is thorough at 55 sources with explicit adequacy assessments. The writing achieves the stated tone goal: dry, knowing wit without forced humor. The project's main weakness is incompleteness: 4 of 7 section deep-dives remain unbuilt (S4–S7), despite notes existing for all of them. The papers compensate significantly by synthesizing all 7 dimensions, so the research coverage is complete even where the deep-dive HTML is not.

**Content Quality: A-**
**Paper-Drive Compliance: B+**

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | ✅ | 55 sources across 7 sections, structured tables with IDs, key data points, and dates. Source adequacy summary included. |
| Source adequacy checks | ✅ | Explicit adequacy table at bottom of literature-collection.md; all 7 sections rated ADEQUATE or STRONG. |
| Deep-dives (3/7 built) | ⚠️ | S1 (Theories), S2 (Neuroscience), S3 (Comedy Craft) are complete HTML deep-dives with 7-8 subsections each and detail panels. S4-S7 have notes but no HTML builds. |
| Papers | ✅ | Survey paper (55 sources, 9 sections, SVG, footnotes) and position paper (39 links, 10 sections, SVG, footnotes) — both standalone, high quality. |
| Slides | ✅ | survey-slides.html and position-slides.html — JS-generated decks with arrow-key/touch nav, progress bars, theme toggles. |
| Index deliverable cards | ✅ | index.html has Key Deliverables grid (survey + position papers), overview card, all 7 section items with status badges (done/planned). |
| .project/ management | ✅ | methodology.md (research question, scope, source strategy, tone note), changelog.md (2 sessions documented), todo.md (accurate hand-off status). |
| Citations (Wikipedia-style) | ⚠️ | Papers have Wikipedia-style superscript footnotes with hover tooltips (survey: 13 sup.fn, position: 11 sup.fn). Deep-dives S1-S3 and overview lack footnote citations — they use inline references and cross-reference links but not the sup.fn pattern. |
| External source links (20+) | ✅ | Survey paper: ~58 external links. Position paper: ~30 external links. Overview deep-dive: ~12 links. S2 deep-dive: 4 inline links. Total well above 20. |

## Content Quality

The intellectual substance is the project's greatest asset. The survey paper successfully synthesizes 2,400 years of humor theory into a coherent narrative, moving from classical philosophy through cognitive neuroscience to computational humor. The position paper ("Humor Is Irreducibly Social") is a genuine argument, not a summary — it marshals 9 lines of evidence, addresses counterarguments, and reaches a defensible conclusion that the cognitive theories have the emphasis backwards. The deep-dives achieve strong depth: S1 covers 7 subsections from Plato through BVT to a synthesis; S2 maps 8 neuroscience topics including the Mobbs study, Duchenne/non-Duchenne distinction, and neurochemistry; S3 treats 8 comedy craft topics with practitioner knowledge grounded in cognitive science.

The overview deep-dive provides an effective 7-section aerial view. The research notes (notes/00-07) provide solid raw material for all 7 dimensions. The literature collection is well-organized with consistent ID schemes (TH-01, NS-01, CC-01, etc.).

## Strengths

1. **Interdisciplinary synthesis**: The project genuinely integrates philosophy, neuroscience, practitioner knowledge, cultural anthropology, clinical research, and AI/NLP — not just listing them side by side but finding cross-cutting themes (the ha-ha/a-ha connection, the social primacy of laughter, the distance mechanism).

2. **Two complementary papers**: Having both a survey paper (comprehensive mapping) and a position paper (argumentative thesis) gives the project intellectual range. The position paper is not redundant with the survey — it takes a stance the survey identifies but does not commit to.

3. **Writing quality and tone**: The prose is clear, engaging, and appropriately wry. The methodology note ("the subject should infect the style, just a little") is well-executed. Technical content is accessible without being dumbed down.

4. **Visual design consistency**: All HTML deliverables share a consistent design language (EB Garamond / Jost / IBM Plex Mono, light/dark toggle, accent colors, stat rows, callout boxes, SVG diagrams). The dd-shared.css/js pattern for deep-dives is well-structured.

5. **Source depth**: 55 sources is substantial for a 7-dimension survey. The mix of primary texts (Kant, Freud, Hobbes), landmark empirical studies (Mobbs 2003, Wattendorf 2023), meta-analyses (laughter interventions), practitioner resources, and recent AI benchmarks provides genuine breadth.

6. **SVG diagrams in papers**: The four-stage humor processing model (survey) and Dunbar's scaling model (position) add visual clarity to complex arguments.

## Weaknesses

1. **4 of 7 deep-dives unbuilt**: S4 (Dark Humor), S5 (Cultural Comedy), S6 (Health & Bonding), S7 (AI & Computational Humor) exist only as markdown notes. This is the most significant gap. The notes are complete and the papers cover all 7 dimensions, but the deep-dive HTML format offers a richer reading experience (interactive sidebar, detail panels, diagrams) that the notes cannot replicate.

2. **No Wikipedia-style citations in deep-dives**: The three built deep-dives (S1-S3) and the overview lack the superscript footnote (sup.fn) citation pattern used in the papers. S2 has a few inline hyperlinks to PubMed/Springer, but S1 and S3 have only 1 external link each (Google Fonts). The deep-dives contain substantial claims that would benefit from inline source attribution.

3. **Overview deep-dive uses inline CSS**: The overview.dd.html embeds its full CSS (~200 lines of theme variables and layout) rather than using dd-shared.css. S1-S3 correctly use `<link rel="stylesheet" href="dd-shared.css">`. This creates a maintenance divergence.

4. **No position-paper slides reference count**: The position-slides.html exists but it is unclear from the index page how many slides it contains or what it covers (no description beyond "Slides" link).

5. **Audio file unexplained**: overview.mp3 exists in the project directory but is not referenced from any HTML page or documented in the changelog. Its purpose is unclear.

6. **Todo.md inconsistency**: The todo.md still lists "Project index page (index.html) — NOT present" even though index.html exists and is complete. The todo was apparently written before the index was built but not updated afterward.

## Recommendations

1. **Build remaining deep-dives (S4-S7)**: The notes are complete and the literature is collected. Converting these to dd.html format using dd-shared.css/js would bring the project to full completion. Prioritize S4 (Dark Humor) and S7 (AI & Computational Humor) as the most intellectually distinctive sections.

2. **Add inline citations to deep-dives**: Retrofit S1-S3 and the overview with sup.fn footnote citations matching the pattern used in the papers. Each deep-dive draws on 7-8 sources from the literature collection; linking claims to those sources would strengthen credibility.

3. **Normalize overview.dd.html CSS**: Refactor overview.dd.html to use dd-shared.css instead of inline styles, matching the pattern of S1-S3.

4. **Update todo.md**: The hand-off document has stale entries (index.html listed as missing). Align it with current project state.

5. **Document or remove overview.mp3**: Either link the audio from the overview page (as a podcast-style narration) or remove it if it is a leftover artifact.

6. **Consider a third paper**: The project's seven dimensions and two existing papers leave room for a focused paper on one of the unbuilt sections — e.g., "Why Machines Cannot Be Funny (Yet)" synthesizing S7 with the AI benchmark literature. This would add a third distinct intellectual contribution.
