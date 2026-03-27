# Peer Review: cog-sci/attachment-theory

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25

## Overall Assessment

This is a strong research project that demonstrates genuine intellectual engagement with a complex, contested topic. The project surveys attachment theory across 6 dimensions with 40 cataloged sources, produces 7 deep-dive HTML pages (overview + 6 section deep-dives), a survey paper with 36 numbered references and Wikipedia-style superscript citations, a 16-slide deck with 5 SVGs, and a well-maintained project index. The critical framing ("useful rather than true") is intellectually honest, and the project treats the critique literature as structurally equal to the theory itself -- a notable strength. The writing is substantive and analytical, not merely summarizing sources but engaging with tensions and contradictions. The project management artifacts (.project/ files) are thorough and self-aware, explicitly noting where the paper-drive methodology was violated (overview built before literature collection).

The main gaps: S7 (Personal Application) remains unplanned, the deep-dive `.dd.html` files lack Wikipedia-style inline citations (though the survey paper has them), and S5's CSS/JS is self-contained rather than using the shared system. The methodology.md deliverables checklist is stale (shows literature collection as unchecked despite being done). The continuation-prompt.md reports 31 sources when the collection has 40.

**Content Quality: A-**
**Paper-Drive Compliance: B+**

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | ✅ | 40 sources across 6 sections, well-structured with IDs, links, dates, key data points, and identified gaps. Tensions table included. |
| Source adequacy checks | ✅ | Explicit adequacy table in todo.md with per-section assessment. All 6 active sections marked ADEQUATE. Gaps acknowledged (e.g., Fraley & Spieker taxometric, Gottman/Johnson, Mesman primary). |
| Deep-dives (7/8 built) | ⚠️ | 7 of 8 planned deep-dives built (overview + S1-S6). S7 (Personal Application) is planned but not built. Each has 8 subsections with summary + detail panels. |
| Papers | ✅ | survey-paper.html: 6 sections + synthesis + methods + abstract + references. 36 numbered refs with superscript Wikipedia-style citations and hover tooltips. 2 SVG diagrams. 6 tension cards. |
| Slides | ✅ | survey-slides.html: 16 slides with 5 SVGs. Title, TOC, one slide per dimension, synthesis, tensions, conclusion. Navigation, progress bar, dark mode. |
| Index deliverable cards | ✅ | index.html has deliverable card grid (survey paper + slides), overview section, 6 section deep-dive links with status badges and source counts, 6 key tensions listed. |
| .project/ management | ⚠️ | 4 files (methodology, todo, changelog, continuation-prompt). Changelog is detailed with architecture decisions. Todo has source adequacy table. However: methodology.md deliverables checklist is stale; continuation-prompt.md has outdated source count (31 vs 40). |
| Citations (Wikipedia-style) | ⚠️ | Survey paper has full Wikipedia-style citations (36 refs, superscript numbers, hover tooltips with links). Deep-dive dd.html files do NOT have Wikipedia-style citations -- they reference sources by name in prose but lack numbered superscript footnotes with links. |
| External source links (20+) | ✅ | Survey paper has 36 unique external source links in its references section. Literature-collection.md has 40 linked sources. The deep-dives themselves have cross-references (46 internal links) but few external source links. |

## Content Quality

The analytical depth is genuinely impressive across the deep-dives. Each section has 8 subsections with both summary cards and detailed essays (estimated 6-10K characters per detail panel). The content engages seriously with primary and secondary literature:

- S5 (Critique) is the strongest section, with systematic treatment of the temperament confound, stability problem, WEIRD bias, mother-blame, pop psychology distortion, and the "era of exhaustion" framing from Thompson et al.
- S4 (Neuroscience) handles polyvagal theory with appropriate nuance, presenting both the clinical utility and the scientific criticism (Neuhuber & Berthoud).
- The survey paper's abstract is a model of concise, well-supported synthesis.
- The "science-to-folk pipeline" thesis (synthesis notes) provides an original organizing framework.
- SVG diagrams are informative: attachment style taxonomy, pursue-withdraw cycle, polyvagal hierarchy, pathways to earned security, three-layer model, rigor spectrum.

## Strengths

1. **Intellectual honesty.** The project does not take sides; it treats attachment theory as a contested framework and gives the critique equal structural weight to the theory. The "useful rather than true" framing is earned through evidence, not assumed.

2. **Source diversity.** The 40 sources span peer-reviewed meta-analyses (Fraley 2002, EMDR meta-analysis 2023), foundational texts (Bretherton 1992), critical journalism (UnHerd, Fatherly Kagan interview), institutional overviews (Wikipedia, Polyvagal Institute), and clinical evidence bases (ICEEFT, Brom SE RCT). This provides genuine multi-perspective coverage.

3. **Survey paper quality.** Wikipedia-style superscript citations with hover tooltips, proper reference numbering, sidebar navigation, responsive design, dark mode. The paper reads as a genuine survey rather than a summary of summaries.

4. **Cross-referencing.** The deep-dives have 46 internal cross-references linking between sections (e.g., S1 links to S5 for the critique context, S2 links to S3 for measurement schism). This creates a coherent research web.

5. **Self-aware methodology.** The changelog explicitly notes that Session 1 violated paper-drive discipline by building the overview before the literature collection. This kind of procedural honesty is rare.

6. **Design consistency.** Shared CSS/JS (dd-shared.css, dd-shared.js) across 6 of 7 deep-dives. Consistent visual language: stat bars, feature grids, verdict panels, timelines, callouts, chip tags.

## Weaknesses

1. **Deep-dives lack Wikipedia-style citations.** The survey paper has proper superscript footnote citations, but the 7 deep-dive `.dd.html` files reference sources by name in prose only (e.g., "Kagan argued..." or "Fraley's (2002) meta-analysis found...") without numbered superscript links to the actual source URLs. This is a significant paper-drive compliance gap -- the deep-dives are the project's primary research artifacts and should have inline citations linking to the literature collection.

2. **S7 (Personal Application) not built.** The index lists it as "planned" and the todo marks it incomplete. While the section is described as "not source-dependent," it represents a gap in the 7-dimension scope the project defined.

3. **S5 uses inline CSS/JS.** S5 (The Critique) was built first with self-contained styles (573 lines, the longest file), creating a maintenance inconsistency with the other 5 deep-dives that use dd-shared.css/js. The changelog acknowledges this but it remains unaddressed.

4. **Stale project files.** methodology.md shows "Literature collection" as unchecked despite being complete. continuation-prompt.md reports "31 sources" when there are 40. These inconsistencies suggest the metadata was not updated after Session 2's gap-filling work.

5. **Some sources are secondary or low-rigor.** Several sources (Reachlink, Calm Blog, Kindman & Co, Good EMDR Therapy) are practitioner/commercial sites rather than peer-reviewed literature. While they serve a role (presenting how the theory is communicated to consumers), they inflate the source count without adding proportional scholarly depth. The literature collection's gaps section identifies missing primary papers (Fraley & Spieker 2003 taxometric, Roisman 2007 AAI-ECR correlation, Mesman 2021, Keller 2021, Grossmann German SSP) that would strengthen the evidence base.

6. **No synthesis paper yet.** The todo lists "Synthesis paper" as a future deliverable distinct from the survey paper. The survey paper partially fills this role but the planned "Between Science and Folklore" synthesis remains unwritten.

## Recommendations

1. **Add Wikipedia-style citations to all deep-dives.** Each dd.html should have superscript numbered footnotes linking to the corresponding source in literature-collection.md or directly to external URLs, matching the survey paper's citation style. This is the single highest-impact improvement for paper-drive compliance.

2. **Update stale project metadata.** Fix methodology.md deliverables checklist (mark literature collection as done). Update continuation-prompt.md source count from 31 to 40. These are quick fixes that improve project hygiene.

3. **Fill identified source gaps.** Prioritize adding the missing primary papers: Fraley & Spieker (2003) taxometric analysis, Roisman et al. (2007) AAI-ECR convergence study, and Hazan & Shaver (1987) original paper. These are among the most-cited works in the field and their absence is notable.

4. **Refactor S5 to shared CSS/JS.** Migrate S5's inline styles to dd-shared.css for consistency and maintainability. This was already identified as a next step in the changelog.

5. **Build S7 or remove from scope.** Either build the Personal Application deep-dive or formally remove it from the project scope with a note in the methodology explaining the decision.

6. **Consider replacing low-rigor sources.** The commercial/practitioner sources (Calm, Reachlink, Kindman) could be supplemented or replaced with peer-reviewed or institutional sources that cover the same concepts with more rigor.
