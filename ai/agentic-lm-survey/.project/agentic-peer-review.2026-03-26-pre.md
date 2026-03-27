# Peer Review: ai/agentic-lm-survey

**Reviewer:** Claude (agentic peer review)
**Date:** 2026-03-25

## Overall Assessment

This is an impressively complete paper-drive project that has progressed from literature collection through deep-dives, a synthesis paper, and a slide deck — all within a compressed timeline. The core intellectual contribution — extending Plaat et al.'s three-axis taxonomy with a fourth "Operate" axis and identifying the cross-cutting Skills layer — is well-argued and backed by quantitative evidence from 28 papers read from primary sources. The project demonstrates unusual methodological honesty: per-paper reading depth statistics, explicit acknowledgment of the 28/85 reading gap, and transparent documentation of what was extracted versus merely cataloged. The writing quality is high throughout, with claims consistently grounded in specific data points rather than vague assertions.

The main weaknesses are structural rather than intellectual: the survey paper HTML uses numbered-bracket citations rather than Wikipedia-style inline citations, the deep-dives are synthesis-heavy but sourced from a relatively narrow evidence base per section (3-7 papers each), and several paper-drive compliance items (deliverable cards with status badges on the index page, consistent citation format) could be tightened. The .project/ management is exemplary.

**Content Quality: A-**
**Paper-Drive Compliance: B+**

## Completeness Scorecard

| Criterion | Status | Notes |
|-----------|--------|-------|
| Literature collection | ✅ | 85 entries across 7 sections with 14 subsections. Well-organized with ID codes, key contributions, and dates. Includes a "Papers Still To Locate" section showing awareness of gaps. Strong. |
| Source adequacy checks | ✅ | Methodology doc explicitly describes selection criteria, exclusion rationale, and honest accounting of 28/85 reading depth. Forward citation sweep via Semantic Scholar API added 6 papers. |
| Deep-dives (5/5 built) | ✅ | All 5 planned sections built as both interactive HTML (three-panel layout with sidebar nav) and companion markdown. Each 54K-70K HTML. Forward citation update boxes and web research update boxes added iteratively. |
| Papers | ✅ | Survey paper exists in both markdown (~6,300 words) and HTML with sidebar navigation. 35 references. 11 sections including synthesis and research agenda. Argument-paper structure rather than catalog. |
| Slides | ✅ | 20-slide deck with light/dark theme, arrow-key/click/swipe navigation. 4-5 content SVG diagrams (taxonomy evolution, section-specific figures). Proper slide template with chapter headers and numbering. |
| Index deliverable cards | ⚠️ | Index page has section items with status badges ("done" for all 5 deep-dives and survey paper). However, it uses a custom minimal layout rather than the full deliverable-card pattern. No thumbnail previews or word/page counts per card. Links are functional and well-organized into three groups (Deep-Dives, Papers & Presentations, Resources). |
| .project/ management | ✅ | Exemplary. changelog.md (detailed per-phase narrative with reading depth table), todo.md (5 priority levels, specific per-section items), methodology.md (10 sections covering research question through reproducibility). All three are substantive documents, not stubs. |
| Citations (Wikipedia-style) | ⚠️ | The survey paper HTML uses numbered-bracket citations with hover tooltips (e.g., `[1]` with tooltip showing paper title and arXiv link) — a hybrid between academic and Wikipedia styles. External links are embedded inline in the text. This is functional and well-executed but not the Wikipedia-style `<sup>` inline citation pattern used in other read-rd papers. The deep-dive HTMLs do not have formal citation systems (they reference papers by name inline). |
| External source links (20+) | ✅ | The survey paper HTML contains 50+ external href links (arXiv papers, tool documentation, organization websites). The markdown paper has 35 numbered references with arXiv IDs. Well above the 20+ threshold. |

## Content Quality

**Intellectual depth.** The project's strongest quality is its argument-driven structure. Rather than cataloging papers source-by-source, each section advances a specific claim backed by quantitative evidence. The POMDP formalization in Section 3, the benchmark-reality gap analysis in Section 4, the protocol-stack layering in Section 5, and the defense-failure evidence in Section 6 are all substantive analytical contributions, not summaries.

**Synthesis quality.** Cross-source synthesis is strong within sections: the Section 4 analysis weaves together 5 SWE-bench variants to build a composite picture of benchmark inflation; Section 6 triangulates three independent security analyses (Breaking the Protocol, SMCP, Prompt Injection SoK) to establish architectural rather than implementation-level vulnerability. The five findings in Section 8 successfully synthesize across all four axes. The weakest synthesis is in Section 5 (Interact), which relies heavily on protocol descriptions and the single Drammeh orchestration study for empirical evidence.

**Tensions and disagreements.** The paper identifies several genuine tensions:
- The security-capability tradeoff (Claude Code's safety via restriction vs. Cursor's vulnerability via permissiveness)
- The mechanistic debate (does RL amplify or create capabilities?)
- The self-improvement threshold (works for capable models, degrades small ones)
- The 60/20 paradox (high usage, low full delegation)
- Benchmark inflation vs. real-world performance

These are not manufactured disagreements but actual unresolved questions in the field.

**Data-backed claims.** Nearly every substantive claim cites a specific number: 23-41% attack amplification, 77.4% SWE-bench solve rate, 57.07% data over-exposure, 26.1% skill vulnerability rate, 97M monthly SDK downloads, $2.5B/$2B ARR figures. The project avoids vague qualitative assertions.

**Reading depth honesty.** The per-paper coverage statistics (3 full reads, 9 at 40-80%, 16 at 11-26%) and the explicit methodology section documenting three reading tiers are unusually transparent for this kind of work. The project states what it doesn't know, which strengthens credibility for what it does claim.

## Strengths

- **Complete pipeline execution.** All deliverables from literature collection through slides are built and linked. The index page provides clean navigation across the full project.
- **Argument-driven paper structure.** The survey paper is not a catalog but a thesis: four structural shifts require a fourth taxonomy axis. This makes it more readable and more citable than a comprehensive literature review.
- **Quantitative grounding.** Specific numbers anchor every major claim. The benchmark-reality gap analysis (Section 4) and defense-failure evidence (Section 6) are particularly well-supported.
- **Forward citation methodology.** Using Semantic Scholar API for forward citation sweeps on 8 key papers, then reading 6 newly identified papers, demonstrates genuine iterative research rather than a single-pass collection.
- **Exceptional .project/ documentation.** The methodology.md is a standalone contribution — its sections on reading strategy, tooling, limitations, and reproducibility could serve as a template for future paper-drive projects.
- **Dual-format deep-dives.** Each section exists as both interactive HTML (for human browsing) and structured markdown (for machine consumption / downstream use). The HTML files feature three-panel layouts with sidebar navigation, light/dark themes, and progressive disclosure.
- **Honest limitations.** The paper explicitly states it is a first-pass survey, not a systematic literature review, and documents exactly what percentage of each paper was read.
- **Self-updating design.** Forward citation boxes and web research update boxes show the project was iteratively improved, not just built once.

## Weaknesses

- **Citation format inconsistency.** The survey paper HTML uses a numbered-bracket citation style with hover tooltips rather than the Wikipedia-style inline citations used elsewhere in the read-rd repository. The deep-dive HTMLs have no formal citation system at all — papers are referenced by name inline. This creates a format gap across the project.
- **Narrow per-section evidence base.** While 28 papers total is respectable, individual sections rest on thin foundations: Section 5 (Interact) relies on ~5 papers with only one empirical orchestration study (Drammeh, n=348); Section 6 (Operate) is dominated by two authors (Maloyan and Namiot, who authored both the MCP security paper and the Prompt Injection SoK). A single research group providing the bulk of evidence for a new taxonomy axis is a concentration risk.
- **Cross-cutting section (S5) has no primary academic sources.** It is built entirely from web research, blog posts, and GitHub repositories. While the SKILL.md ecosystem is genuinely novel, the section would be strengthened by the two SoK papers that were later found via forward citation sweep. The HTML deep-dive may not fully reflect this update.
- **No figures or diagrams in the survey paper itself.** The paper markdown and HTML are entirely text and tables — no taxonomy diagram, no timeline visualization, no protocol stack figure. The slides have SVG diagrams, but the paper does not. For a paper proposing a new taxonomy, a visual representation would significantly aid comprehension.
- **Industry source verification gap.** Revenue figures ($2.5B ARR for Claude Code, $2B+ for Cursor), adoption statistics (97M monthly SDK downloads), and market projections (Gartner) are cited from web research without primary source links to official company disclosures. These numbers are plausible but unverifiable from the materials provided.
- **Index page lacks deliverable metadata.** The index shows status badges (all "done") and descriptions, but does not include word counts, page counts, source counts per section, or last-updated dates — metadata that would help a reader quickly assess coverage depth without clicking through.
- **Limited coverage of disagreements with the proposed taxonomy.** The paper acknowledges what Plaat et al. got right and wrong but does not engage with potential criticisms of the four-axis framing — e.g., whether "Operate" could be a cross-cutting concern rather than a separate axis, or whether the Skills layer belongs inside "Act" rather than as a cross-cutting layer.

## Recommendations

1. **Retrofit Wikipedia-style citations into the survey paper HTML** to match the citation pattern used in other read-rd papers. The current hover-tooltip approach is functional but inconsistent with the repository's established convention.

2. **Add a taxonomy diagram to the survey paper HTML.** The SVG from Slide 1 (taxonomy evolution comparing Plaat et al. 2025 to the four-axis 2026 framing) could be adapted directly into the paper. This is the project's core visual argument and deserves to appear in the main deliverable.

3. **Strengthen Section 5 (Interact) with additional empirical evidence.** The Drammeh orchestration study is compelling but isolated. Consider reading the Multi-Agent Collaboration survey (S-05, Tran et al.) or the DroidSpeak paper (I-10) to add empirical depth beyond protocol descriptions.

4. **Address concentration risk in Section 6.** Two of the three core security papers share authors (Maloyan and Namiot). Adding MCPSecBench (O-03, already in literature collection) or the ScienceDirect comprehensive review (S-12, 150+ sources) would diversify the evidence base for the Operate axis.

5. **Add a "counter-arguments" subsection to Section 8.** Explicitly engage with the strongest objections to the four-axis taxonomy: Could Operate be treated as a cross-cutting concern like Skills? Does separating it from the original three axes create a false distinction between safety-of-reasoning and safety-as-its-own-axis? Addressing these would strengthen the paper's argumentative rigor.

6. **Add deliverable metadata to index.html.** Word counts, source counts per section, and last-updated dates would help readers navigate the project without opening each file.

7. **Consider formalizing the methodology.md as a standalone reproducibility guide.** Its sections on reading strategy, forward citation methodology, and honest accounting of limitations are valuable beyond this specific project and could serve as a template for the paper-drive workflow.

8. **Read the 5 highest-priority unread papers from the TODO list** — particularly DeepSeek-R1 (R-01, currently covered only via secondary sources), the Multi-Agent Collaboration survey (S-05), and MCPSecBench (O-03) — to close the most visible gaps between the literature collection and the synthesized content.
