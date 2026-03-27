# Agentic Peer Review -- Brain Energy & Metabolic Psychiatry

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25
**Project:** `neuro/brain-energy/`

---

## Overall Assessment

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Completeness** | B | All 6 section deep-dives built; literature collection solid. Missing overview.dd.html (referenced but absent), no synthesis paper, no slide deck. |
| **Source Quality** | B+ | 50 sources across 6 dimensions. Mix of meta-analyses, RCTs, reviews, and critical perspectives. Some citations lack full bibliographic detail. |
| **Analytical Depth** | B+ | Strong mechanistic coverage. Good tension identification. Detail panels are substantive with callouts, diagrams, and verdict grids. |
| **Critical Balance** | A- | Critiques treated as first-class content in S1 and S6. Unfalsifiability, evidence quality, and premature adoption risks explicitly addressed. |
| **Technical Execution** | B+ | Consistent dd.html template usage. SVG diagrams in 5/6 deep-dives. Callout boxes throughout. S3 has 7 sections (not 8), minor inconsistency. |
| **Workflow Discipline** | B- | Source adequacy table present. Changelog documents decisions. But project completed in a single session with no iterative source assessment. No paper or slides produced. |

**Overall Grade: B+**

The project delivers a well-structured literature survey with strong mechanistic coverage and honest critical assessment. It stops at Phase 3 of the paper-drive workflow (deep-dive build) without advancing to synthesis papers (Phase 5) or slides (Phase 6). For the scope completed, quality is high.

---

## Completeness Scorecard

| Deliverable | Status | Quality |
|-------------|--------|---------|
| Project directory structure | Complete | Correct layout |
| `.project/methodology.md` | Complete | Clear scope, exclusions, source strategy |
| `.project/todo.md` | Complete | Source adequacy table present |
| `.project/changelog.md` | Complete | Single session documented with decisions |
| `literature-collection.md` | Complete | 50 sources, well-organized by section |
| `notes/00-synthesis.md` | Complete | Concise; identifies 4 tensions and evidence hierarchy |
| `notes/01-06` (per-section) | Complete | Vary in depth; some are telegraphic shorthand |
| `index.html` | Complete | Clean design, theme toggle, tension list |
| `overview.dd.html` | **Missing** | Referenced in index.html and changelog but file does not exist |
| `s1-metabolic-theory.dd.html` | Complete | 8 sections, diagram, timeline, verdict grid |
| `s2-mitochondria.dd.html` | Complete | 8 sections, diagrams, detailed ETC coverage |
| `s3-psychiatric-applications.dd.html` | Complete | 7 sections (not 8), diagrams, disorder-specific |
| `s4-neuroinflammation.dd.html` | Complete | 8 sections, diagrams, NLRP3 pathway detail |
| `s5-interventions.dd.html` | Complete | 8 sections, diagrams, safety coverage |
| `s6-clinical-evidence.dd.html` | Complete | 8 sections, verdict grid, no SVG diagrams |
| Synthesis paper(s) | **Not started** | Expected per paper-drive Phase 5 |
| Slide deck | **Not started** | Expected per paper-drive Phase 6 |

---

## Content Quality

### Literature Collection
- **Strengths:** Balanced source types (meta-analyses, RCTs, reviews, critical commentary, institutional). Includes both landmark papers (Shimazu 2013/Science BHB/HDAC) and recent evidence (JAMA Psychiatry 2025 RCT). Critical perspectives (Psychiatric Times) included alongside advocacy sources.
- **Weaknesses:** Some citations are imprecise -- "PMC" or "Frontiers Psychiatry" without full author/title for several entries (e.g., sources 11, 12, 14, 17, 18, 21-30). This makes verification and cross-referencing difficult. No DOIs or URLs provided for most sources. The JAMA Psychiatry 2025 RCT (source 32) is the project's most important clinical citation but lacks full author attribution.

### Section Deep-Dives (dd.html)
- **S1 (Metabolic Theory):** Strong. 8 sections covering thesis, Palmer, paradigm shift, history, field status, critiques, implications, sources. The SVG diagram (Palmer's Metabolic Model) effectively visualizes the causal chain. The verdict grid (Supported vs. Unproven) in S1-06 is a standout element. Detail panels offer genuine analytical depth beyond the summaries.
- **S2 (Mitochondria):** Most technically dense. 8 sections with ETC detail, Complex I/IV meta-analysis coverage, acquired vs. genetic distinction. Good use of stat boxes (ATP yield numbers, meta-analysis figures). Two diagrams present.
- **S3 (Psychiatric Applications):** Solid disorder-by-disorder coverage. Only 7 sections (missing a Sources section at position 08?). Depression, bipolar, schizophrenia, anxiety each get dedicated treatment with disorder-specific metabolic evidence.
- **S4 (Neuroinflammation):** Well-structured NLRP3 -> cytokines -> microglia -> ROS cycle narrative. Gut-brain axis integration is logical. 8 sections with diagrams.
- **S5 (Interventions):** Broadest coverage -- keto, BHB signaling, fasting, exercise, sleep, supplements, safety. Good practical detail (protocol specifics, safety monitoring). 8 sections, 2 diagrams, highest callout count (9).
- **S6 (Clinical Evidence):** Critical assessment backbone. Evidence hierarchy, study limitations, theoretical critiques, implementation challenges all covered. Only deep-dive without SVG diagrams -- a gap given this section would benefit from an evidence-hierarchy visualization.

### Markdown Notes
- Synthesis notes (00) are well-structured with tensions, cross-section findings, and evidence hierarchy.
- Per-section notes (01-06) are quite telegraphic -- bullet-point shorthand rather than the narrative synthesis described in the paper-drive methodology. They read as extraction notes rather than working analytical documents. The methodology calls for notes to be "where the thinking happens" with sub-topics synthesized across sources; these notes mostly list claims without cross-source synthesis.

### Index Page
- Clean, professional design. Theme toggle works. Badge, subtitle, and meta description set context well.
- Key Tensions section (T1-T4) is a strong element -- these are genuine analytical insights, not just summaries.
- Links to methodology, literature collection, changelog, and TODO are present.
- Cross-links to other projects in footer (GenAI 2026 Outlook).

---

## Strengths

1. **Critical balance is the standout quality.** The project does not advocate for metabolic psychiatry; it assesses it. Critiques about unfalsifiability, evidence quality, researcher-advocate overlap, and premature adoption are prominent in S1 and S6. The verdict grids (Supported vs. Unproven) enforce this discipline visually.

2. **Tension identification.** The four tensions (mechanism vs. clinical evidence, paradigm shift vs. incremental addition, diet as medicine vs. distraction, emerging field vs. hype cycle) are genuinely insightful and well-supported by the source material. These would form the backbone of a tensions paper.

3. **Source breadth.** 50 sources across meta-analyses, RCTs, landmark mechanistic studies, clinical commentary, and institutional perspectives. The inclusion of the Moncrieff 2022 umbrella review (serotonin hypothesis challenge) and the Shimazu 2013 Science paper (BHB/HDAC) shows attention to foundational evidence.

4. **Consistent template execution.** All 6 deep-dives use the same three-panel template with sidebar navigation, summary center, and detail right panel. Stat boxes, callout boxes, feat grids, and timelines are used appropriately.

5. **Scope discipline.** The methodology explicitly excludes epilepsy treatment, weight loss, pharmacology detail, and non-psychiatric neurology. These are defensible exclusions that keep the project focused.

---

## Weaknesses

1. **Missing overview.dd.html.** The index page links to `overview.dd.html` and the changelog says it was "moved from `neuro/brain-energy.dd.html`" -- but the file does not exist in the project directory. This is a broken link on the main landing page.

2. **No synthesis papers or slides.** The paper-drive workflow defines 7 phases. This project completed through Phase 3 (deep-dive build) but did not attempt Phase 5 (synthesis/paper) or Phase 6 (slides). The four identified tensions are strong enough to support at least a tensions paper.

3. **Thin markdown notes.** The per-section notes (01-06) are shorthand extraction lists, not analytical working documents. The methodology prescribes these as "where the thinking happens" with cross-source synthesis. Instead, notes like S2 are 8 lines of telegraphic bullets. This suggests the HTML deep-dives were built from sources directly rather than through the notes-first discipline.

4. **Incomplete citations.** Many sources in literature-collection.md use vague attributions: "PMC," "Frontiers Psychiatry," "ScienceDirect" without full titles or authors. At least 15 of 50 sources have incomplete bibliographic data. This undermines verifiability.

5. **Single-session execution.** The entire project -- from restructuring through all 6 deep-dives, notes, and index -- was completed in one session. The paper-drive methodology emphasizes iterative source assessment with human checkpoints. Single-session execution risks insufficient reflection and source adequacy assessment.

6. **S6 lacks diagrams.** The clinical evidence section is the only deep-dive without SVG diagrams. An evidence-hierarchy pyramid or a timeline of trial milestones would strengthen this critical section.

7. **S3 section count inconsistency.** S3 has 7 sections while all others have 8. The missing section appears to be a standalone Sources/References section (S3-07 is titled "References & Resources" equivalent content but counted differently from the others' S-08).

---

## Recommendations

### High Priority
1. **Create or restore overview.dd.html.** Either build the overview deep-dive or remove the broken link from index.html. The changelog indicates this file existed previously -- check if it remains at the old path (`neuro/brain-energy.dd.html`).

2. **Complete citation data.** Add full author lists, titles, journal names, DOIs/URLs for the ~15 sources currently attributed only to "PMC" or publisher names. This is essential for a project that aspires to publishable quality.

3. **Write a synthesis paper.** The four tensions identified in the index page and synthesis notes provide a natural paper structure. A tensions-style paper ("Metabolic Psychiatry: Promise, Evidence, and Open Questions") would be a high-value deliverable.

### Medium Priority
4. **Expand markdown notes.** Rewrite notes 01-06 to include cross-source synthesis, disagreements between sources, and analytical observations. These should be genuine working documents, not just extraction shorthand.

5. **Add SVG diagrams to S6.** An evidence hierarchy pyramid (meta-analyses > RCTs > pilots > case reports) and/or a trial landscape timeline would strengthen the clinical evidence section.

6. **Build a slide deck.** The material is well-organized enough to support a 20-25 slide presentation. The tensions and evidence hierarchy provide natural slide structure.

### Low Priority
7. **Normalize S3 to 8 sections.** Either add a dedicated Sources section or restructure to match the 8-section pattern of other deep-dives.

8. **Add a second session of source assessment.** Revisit the literature collection after a break. Identify any gaps that only become visible with fresh perspective -- particularly around negative trials or failed interventions.

9. **Cross-link between deep-dives.** The dd.html files are self-contained but don't link to each other. Adding cross-references (e.g., S2 linking to S4 for the ROS-inflammation bridge) would improve navigation.
