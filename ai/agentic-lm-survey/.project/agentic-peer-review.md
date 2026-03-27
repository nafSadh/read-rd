# Peer Review: ai/agentic-lm-survey

**Reviewer:** Claude (agentic peer review, round 2)
**Date:** 2026-03-26

## Overall Assessment

This project represents a mature, argument-driven research workflow that has executed the full paper-drive pipeline: literature collection (85 entries) through source assessment, five deep-dive sections, a synthesis paper, and a slide deck -- all within a compressed but well-documented timeline. The core contribution -- extending Plaat et al.'s three-axis taxonomy (Reason/Act/Interact) with a fourth "Operate" axis and identifying a cross-cutting Skills layer -- is substantive, well-argued, and grounded in 28 papers read from primary sources (~460pp). The project's distinguishing quality is its intellectual honesty: per-paper reading depth statistics, explicit acknowledgment of the 28/85 reading gap, a transparent methodology document, and a limitations section that does not hedge. Since the round-1 review, the project has added web research update boxes across all deep-dives, updated the survey paper with current figures ($2.5B/$2B ARR, 80.9% SWE-bench Verified), and improved index design consistency.

The main remaining gaps are format-level rather than intellectual: deep-dive HTMLs have Wikipedia-style inline citations in their detail panels but not consistently across all sections, the survey paper HTML uses a hybrid citation system (numbered brackets in body text plus a separate `<sup class="fn">` overlay system for hyperlinks), and no taxonomy diagram appears in the paper itself despite excellent SVGs in the slides.

**Content Quality: A-**
**Paper-Drive Compliance: B+**

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | ✅ | 85 entries across 7 sections + 14 subsections in `literature-collection.md`. Well-organized with ID codes, authors, venue/date, key contributions. Includes a "Papers Still To Locate" section (Section 7) showing gap awareness. Recommended next steps document future work paths. |
| Source adequacy checks | ✅ | `methodology.md` Section 3 documents selection criteria (5 inclusion, 4 exclusion rules), forward citation sweep via Semantic Scholar API on 8 key papers, and honest accounting of 28/85 reading coverage. Phase 9 in changelog narrates the forward citation process and its yield (6 new papers). |
| Deep-dives (5/5 built) | ✅ | All 5 planned sections built as both interactive three-panel HTML (54K-68K each) and companion markdown (12K-24K each). Each has sidebar navigation, light/dark theme toggle, detail panels, forward citation update boxes, and web research update boxes added in Phase 11. |
| Wikipedia-style citations in deep-dives | ⚠️ | Partial. S4 (Operate) and S5 (Cross-Cutting) have proper `<sup class="fn">` citations with hover tooltips in their detail panels (6 citations in S4, 3 in S5). S1 (Reason) has 16 `<sup class="fn">` instances -- the most thorough. S2 (Act) has 10, S3 (Interact) has 9. However, citations appear primarily in detail panels, not in the summary center column. Total of 44 inline citations across all 5 deep-dives. Coverage is uneven. |
| Papers | ✅ | Survey paper exists in both markdown (`survey-paper.md`, ~6,300 words) and HTML (`survey-paper.html`) with sidebar navigation. 11 sections. Argument-paper structure: each section advances a specific claim rather than cataloging sources. |
| Paper reference list | ✅ | 35 numbered references in the markdown. HTML has both a full reference list (35 entries with arXiv IDs and venue data) and a secondary `<ol class="ref-list-num">` with 11 hyperlinked entries for the `<sup class="fn">` overlay system. |
| Paper external source links (20+) | ✅ | Well above threshold. The HTML contains 50+ external href links (arXiv papers, tool docs, organization sites). The markdown has 35 numbered references with arXiv IDs. |
| Slides | ✅ | 20-slide deck (`survey.slides.html`) with light/dark theme, arrow-key/click/swipe navigation. 10 substantive SVG diagrams on content slides (taxonomy evolution, four structural shifts, POMDP formalization, benchmark landscape, protocol stack, security surface, skills layer, synthesis, research agenda, closing). Chapter divider slides for each section. |
| Index deliverable cards | ⚠️ | Index page has section items with status badges ("done" for all 5 deep-dives and survey paper), organized into three groups (Deep-Dives, Papers & Presentations, Resources). Links are functional. However, it uses a minimal list layout without thumbnail previews, word/page counts, or last-updated timestamps per card. The `.meta` section at top provides aggregate stats (85 sources, 28 papers, ~460pp). |
| Index status badges accurate | ✅ | All 5 deep-dives marked "done" -- confirmed, all `.dd.html` files exist on disk. Survey paper marked "done" -- confirmed, both `survey-paper.html` and `survey-paper.md` exist. Slides linked and present. Literature collection and project management links all resolve. |
| .project/ management | ✅ | Exemplary. `changelog.md` (162 lines, per-phase narrative with reading depth table covering Phases 0-11), `todo.md` (5 priority levels with specific per-section items, 57 unread papers tracked), `methodology.md` (289 lines, 10 sections from research question through reproducibility and limitations). Previous peer review preserved as `agentic-peer-review.2026-03-26-pre.md`. |

## Content Quality

**Intellectual depth.** The project's strongest quality is its argument-driven structure. The survey paper is not a catalog of 28 papers -- it is a thesis (four structural shifts require a fourth taxonomy axis) with evidence marshaled from primary sources. Each section leads with its strongest quantitative result: the POMDP formalization for Reason, the 65%-to-21% SWE-EVO drop for Act, the 100%-vs-1.7% orchestration result for Interact, and the 23-41% attack amplification for Operate. The cross-cutting Skills section offers genuine novelty: no existing survey maps the five-layer configuration stack or the SKILL.md portability phenomenon.

**Synthesis quality.** Cross-source synthesis is strong within and across sections. Section 4 (Act) weaves 5 SWE-bench variants into a composite picture of benchmark inflation, then pivots to self-improving agents as the counternarrative. Section 6 (Operate) triangulates three independent security analyses to establish architectural (not implementation-level) vulnerability. The five findings in Section 8 successfully synthesize across all four axes. The weakest synthesis remains Section 5 (Interact), which relies heavily on protocol descriptions and a single empirical orchestration study (Drammeh, n=348). This was noted in round 1 and has not changed.

**Tensions and disagreements identified.** The paper surfaces several genuine unresolved tensions:
- The mechanistic debate: does RL amplify existing capabilities or create new ones?
- Self-improvement threshold: works for capable models (Claude 4.5 Sonnet +22.6%), degrades small ones (GPT-5-Nano -68.2%)
- The 60/20 paradox: 60% of work uses AI, only 0-20% fully delegated
- Security-capability tradeoff: Claude Code achieves Low vulnerability via restriction, Cursor rates Critical via permissiveness
- Benchmark inflation vs real-world performance (SWE-EVO 65% to 21%)

These are not manufactured; they reflect actual field-level disagreements.

**Data-backed claims.** Nearly every substantive claim cites a specific number: 23-41% attack amplification, 77.4% solve rate, 57.07% data over-exposure, 26.1% skill vulnerability rate, 97M monthly SDK downloads, $2.5B/$2B ARR. The project avoids vague qualitative assertions. Updated figures from Phase 11 web research (80.9% SWE-bench Verified, MCPSecBench 85%+ compromise rate, 30+ CVEs in 60 days) keep the data current through March 2026.

## Strengths

- **Complete pipeline execution.** Every deliverable from literature collection through slides is built, linked, and functional. The index page provides clean navigation. All status badges match actual files on disk.
- **Argument-driven paper structure.** The survey paper advances a specific thesis rather than cataloging papers. This makes it more readable and more citable than a comprehensive literature review. The "what this survey is not" section (2.3) is refreshingly honest.
- **Quantitative grounding throughout.** Specific numbers anchor every major claim. The benchmark-reality gap analysis (Section 4) and defense-failure evidence (Section 6) are particularly well-supported with tables and cross-study comparisons.
- **Forward citation methodology.** Using Semantic Scholar API for forward citation sweeps on 8 key papers, then reading 6 newly identified papers, demonstrates genuine iterative research. The surprise finds (AgentRaft, Agentic Critical Training) meaningfully strengthened the paper.
- **Exceptional .project/ documentation.** The `methodology.md` is a standalone contribution. Its sections on three-tiered reading strategy, forward citation sweep rationale, tooling, and "what broke and how we fixed it" could serve as a template for future paper-drive projects.
- **Dual-format deep-dives.** Each section exists as both interactive HTML (with sidebar nav, detail panels, theme toggle) and structured markdown. The HTML template is consistent across all 5 sections.
- **Iterative improvement.** Forward citation boxes (Phase 9) and web research update boxes (Phase 11) show the project was refined over multiple passes, not built once and abandoned.
- **Slide deck quality.** 10 hand-crafted SVG diagrams on content slides, including the taxonomy evolution diagram, four-shifts visualization, and protocol stack figure. These are the project's best visual arguments.
- **Honest limitations.** The paper states it is a first-pass survey, documents per-paper reading percentages, and explicitly names what was excluded and why.

## Weaknesses

- **Citation format inconsistency across deliverables.** The survey paper HTML uses a hybrid system: `[N]` numbered bracket references in body text (referencing the 35-item reference list), plus a separate `<sup class="fn">` overlay system with 6 hover-tooltip citations linking to a secondary 11-item reference list. These are two parallel citation systems in the same document. The deep-dive HTMLs use `<sup class="fn">` citations with hover tooltips, but only in detail panels -- the summary center column references papers by name inline without formal citations. Neither matches the Wikipedia-style convention used elsewhere in the read-rd repository.
- **No taxonomy diagram in the survey paper.** The paper's central visual argument -- the evolution from Plaat et al.'s 3-axis taxonomy to the 4-axis + cross-cutting framing -- exists only in the slide deck (Slide 1 SVG). The paper HTML has a small decorative color-bar SVG at the top but no substantive diagram. For a paper proposing a new taxonomy, this is a significant omission.
- **Section 5 (Interact) empirical thinness.** This was noted in round 1 and persists. The section's empirical evidence rests on a single study (Drammeh, 348 trials) for orchestration claims and protocol descriptions for the infrastructure narrative. The Multi-Agent Collaboration survey (S-05, Tran et al.) was read at only 14% (pp1-5 of 35pp). The DroidSpeak paper (I-10) remains unread. Adding empirical orchestration studies would strengthen the weakest axis.
- **Concentration risk in Section 6 (Operate).** Two of three core security papers (Breaking the Protocol and Prompt Injection SoK) share authors (Maloyan and Namiot). A single research group providing the bulk of evidence for the new taxonomy axis is a methodological concern. MCPSecBench (O-03) and the ScienceDirect comprehensive review (S-12, 150+ sources) are in the literature collection but unread.
- **Cross-cutting section (S5) built primarily from web research.** While the two SoK papers found via forward citation sweep (Jiang et al., Xu & Yan) added academic grounding, the section's original construction relied entirely on blog posts, GitHub repos, and tool documentation. The deep-dive markdown for this section is the thinnest (12K vs 18K-24K for others).
- **Industry source verification gap.** Revenue figures ($2.5B ARR for Claude Code, $2B+ for Cursor, 80.9% SWE-bench Verified), adoption statistics (97M monthly SDK downloads), and market projections (Gartner 1,445% surge) are cited from web research without primary links to official company disclosures or SEC filings. These figures are plausible but not independently verifiable from the materials provided.
- **Index page lacks per-section metadata.** Word counts, source counts, reading depth indicators, and last-updated timestamps per deliverable card would help readers assess coverage depth without clicking through. The aggregate stats in the `.meta` section partially address this but are project-level, not section-level.
- **Limited engagement with counter-arguments to the taxonomy.** The paper does not address the strongest objection: that "Operate" could be treated as a cross-cutting concern (like Skills) rather than a dedicated axis. Is safety-of-reasoning fundamentally different from safety-as-its-own-axis? The paper assumes the answer is yes but does not argue it explicitly.
- **Survey paper HTML has two parallel reference lists.** The main body `<section class="references">` contains 35 entries with full bibliographic data. A separate `<section class="paper-section" id="references">` contains an `<ol class="ref-list-num">` with only 11 entries (hyperlinks for the `<sup class="fn">` system). This duplication is confusing -- it appears to be an artifact of the HTML build process.

## Recommendations

1. **Unify the survey paper's citation system.** Remove the secondary 11-item reference list and consolidate on either (a) Wikipedia-style `<sup class="fn">` inline citations throughout, pointing to the existing 35-item reference list, or (b) the current `[N]` bracket system consistently. The hybrid creates confusion.

2. **Add the taxonomy evolution SVG to the survey paper HTML.** The Slide 1 diagram (Plaat et al. 2025 three-axis vs. this survey's four-axis + cross-cutting) is the paper's visual thesis statement. Embedding it between Sections 1.1 and 1.2 would significantly improve comprehension.

3. **Strengthen Section 5 (Interact) with additional empirical evidence.** Read the Multi-Agent Collaboration survey (S-05, Tran et al.) beyond pp1-5, or add MCPSecBench orchestration data from Phase 11 web research. A second empirical orchestration study would eliminate the single-study dependency.

4. **Diversify Section 6 (Operate) evidence base.** Read MCPSecBench (O-03, already in literature collection) and/or the ScienceDirect comprehensive review (S-12, 150+ sources). Adding a third independent author group beyond Maloyan/Namiot would address the concentration concern.

5. **Add a "counter-arguments" subsection to Section 8 (Synthesis).** Explicitly engage with objections: Could Operate be a cross-cutting concern like Skills? Does adding it to the taxonomy create a false separation between safety and the axes it protects? Addressing these would strengthen argumentative rigor.

6. **Add per-section metadata to the index page.** Source counts, reading depth indicators (e.g., "7 papers, ~120pp read"), and last-updated dates per deliverable card would improve navigability.

7. **Propagate Wikipedia-style citations into deep-dive summary columns.** Currently, `<sup class="fn">` citations appear primarily in detail panels. Adding them to the summary center column (where most readers will spend their time) would improve source traceability.

8. **Read the top-3 highest-impact unread papers.** DeepSeek-R1 (R-01, currently covered only via secondary sources and foundational to the Reason section), the Multi-Agent Collaboration survey (S-05, for Interact evidence depth), and MCPSecBench (O-03, for Operate evidence diversity) would close the most visible gaps between the literature collection and synthesized content.
