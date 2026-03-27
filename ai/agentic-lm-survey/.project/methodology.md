# Methodology — Agentic LLMs in the Wild Survey

**Document version:** March 24, 2026  
**Scope:** Complete methodology for the literature survey, from inception to deliverables, executed in a single extended session between a human researcher and Claude (Anthropic).

---

## 1. Research Question

**Starting point:** User identified Plaat et al.'s "Agentic Large Language Models, a survey" (JAIR 2025, arXiv:2503.23037) as interesting but stale. The paper's last revision was November 2025. The question: how would you redo this research with current (March 2026) knowledge?

**Framing decision:** Rather than a comprehensive re-survey (Plaat et al.'s approach: 85 pages, 300+ references), we chose an *argument paper* — a thesis-driven update that uses primary sources as evidence for specific structural claims. The thesis: four shifts between January 2025 and March 2026 require extending Plaat et al.'s three-axis taxonomy (Reason / Act / Interact) with a fourth axis (Operate).

---

## 2. Taxonomy Design

### 2.1 Extending the Baseline

We preserved Plaat et al.'s core taxonomy (Reason, Act, Interact) as still valid, then identified what it couldn't cover:

- **Reason** was reframed from "external scaffolding" to "model-native capabilities via RL" — the same category, but the dominant paradigm shifted
- **Act** was narrowed from "robots + hypothetical assistants" to "agentic coding" — the domain where production deployment actually happened
- **Interact** was reframed from "research topic (social simulation)" to "infrastructure and governance problem (protocols)"
- **Operate** was added as an entirely new axis — safety, security, reliability, economics — which Plaat et al. explicitly deferred as "future work"
- **Cross-Cutting** was identified as a layer that spans all four axes — portable skills, configuration standards, the five-layer stack

### 2.2 Validation

The taxonomy was validated iteratively: as papers were read, we checked whether each paper fit cleanly into one axis or required cross-axis placement. Papers that spanned multiple axes (e.g., Self-Play SWE-RL spanning Reason + Act) were noted as evidence for cross-cutting themes rather than taxonomy failures.

---

## 3. Literature Collection

### 3.1 Initial Sweep

**Method:** Web search across arXiv, Semantic Scholar, Google Scholar, industry blogs, and tool documentation. Searches used domain-specific terms rather than broad queries:

- "agentic RL LLM POMDP" (not "agentic AI")
- "SWE-bench" + specific variant names
- "MCP security" / "A2A protocol"
- "SKILL.md" / "agent skills" / "CLAUDE.md"
- Tool-specific: "Claude Code," "Antigravity," "OpenClaw," etc.

**Result:** 85 entries organized across 7 sections with 14 subsections in `literature-collection.md`. Each entry recorded: paper title, authors, venue/date, key contribution, and relevance to taxonomy section.

### 3.2 Selection Criteria

Papers were prioritized if they:
1. Introduced new formalizations or frameworks (e.g., ARL Landscape Survey's POMDP tuple)
2. Provided quantitative results on established benchmarks (e.g., SWE-bench family)
3. Addressed topics absent from Plaat et al. (e.g., MCP security, SKILL.md portability)
4. Documented production deployment data (e.g., Anthropic 2026 Trends Report)
5. Were cited by or cited other papers in our collection (network density)

Papers were deprioritized if they:
- Covered domains Plaat et al. already handled well and that hadn't structurally changed (embodied agents, GUI navigation)
- Were application papers in narrow domains (agent for X) without generalizable findings
- Were concurrent surveys without novel framing

### 3.3 What Was Excluded and Why

- GUI agents (OSWorld, WebArena): Acknowledged but not re-reviewed — Plaat et al. covered these, and the structural story hasn't changed
- Embodied agents / VLAs: Same — important but not where the paradigm shifted
- Scientific discovery agents: Insufficient primary sources in our timeframe
- Agent economics / FinOps: Mentioned in industry sources but no rigorous primary papers found

---

## 4. Paper Reading Process

### 4.1 PDF Acquisition

Papers were downloaded as PDFs from arXiv using `curl -sL -o paper.pdf "https://arxiv.org/pdf/XXXX.XXXXX"`. All PDFs were stored in a working directory and text-extracted using PyMuPDF (`fitz`).

**Verification:** After download, the first page of each PDF was text-extracted and checked against the expected title/authors. This caught 4 arXiv ID collisions where the wrong paper was downloaded (e.g., arXiv:2602.15498 returned a cosmology paper instead of the SoK on Agentic Skills). Wrong papers were identified and re-downloaded with correct IDs found via web search.

### 4.2 Reading Strategy

Three tiers of reading depth:

**Full read (100%):** Reserved for short, high-impact papers. 3 papers: Drammeh multi-agent orchestration (10pp), Breaking the Protocol MCP security (7pp), Prompt Injection SoK (10pp).

**Deep read (40–70%):** Abstract, introduction, methodology, key results tables/figures, discussion/conclusion. Skipped related work, detailed proofs, and appendices unless directly relevant. 9 papers including Self-Play SWE-RL, SoK Agentic Skills, Agent Skills Survey.

**Extraction read (11–25%):** Abstract, introduction, key results tables. Used for large survey papers where the contribution is the framework rather than specific results. 16 papers including the 95-page ARL Landscape Survey (read pp1-20 + taxonomy tables) and the 120-page RL for LRMs survey (read TOC only).

### 4.3 What Was Extracted Per Paper

For each paper, we recorded:
- **Formal definitions** (if any): e.g., POMDP tuple, skill four-tuple S=(C,π,T,R)
- **Key quantitative results**: e.g., 77.4% solve rate, 23–41% amplification, 57.07% leak rate
- **Architectural/design contributions**: e.g., progressive disclosure, self-play training loop
- **Claims that support or challenge our thesis**
- **Connections to other papers in the collection**

### 4.4 Honest Accounting

We were explicit about reading depth throughout. The literature deep-dives document (`notes/00-literature-deep-dives.md`) records per-paper page ranges and percentage coverage. This transparency is itself a methodological contribution — the field moves too fast for any individual to read comprehensively, and pretending otherwise is dishonest.

---

## 5. Forward Citation Sweep

### 5.1 Rationale

After reading 22 papers, we assessed whether additional reading from the existing literature collection (63 unread entries) would change conclusions. The answer was no — the structure was solid. But *unknown unknowns* — recent papers citing our sources — could introduce findings that challenge or extend the thesis.

### 5.2 Method

Used the **Semantic Scholar API** to pull forward citations for 8 key papers:

```
GET https://api.semanticscholar.org/graph/v1/paper/ArXiv:{ID}/citations
    ?fields=title,year,publicationDate&limit=50
```

Papers queried:
- ARL Landscape Survey (arXiv:2509.02547) — 50+ citations in 3 months
- Breaking the Protocol (arXiv:2601.17549) — 0 citations (too recent)
- Live-SWE-agent (arXiv:2511.13646) — 27 citations
- SWE-EVO (arXiv:2512.18470) — 4 citations
- Agent-Omit (arXiv:2602.04284) — 0 citations
- Prompt Injection SoK (arXiv:2601.17548) — 2 citations
- SMCP (arXiv:2602.01129) — 0 citations
- OpenClaw-RL (arXiv:2603.10165) — 1 citation

### 5.3 Supplementary arXiv Keyword Sweep

Additionally searched arXiv for Feb–Mar 2026 papers using domain-specific queries:
- "agentic RL LLM 2026 training stability self-improving"
- "SWE-bench agent 2026 new benchmark self-play"

### 5.4 Selection from Forward Citations

From ~80 forward citations across all queries, identified 8 candidate papers based on:
- Direct relevance to our taxonomy axes
- Novel findings that would change or strengthen conclusions
- Recency (Feb–Mar 2026 — papers published after our initial reading)

Downloaded and read 6 papers (2 had arXiv ID collisions that couldn't be resolved):

| Paper | Why Selected | What It Changed |
|-------|-------------|----------------|
| Self-Play SWE-RL | Missing link between REASON and ACT | Added to Section 2 |
| Self-Evolving Agents Survey | Formal framework for entire self-improvement paradigm | Context for Section 2 |
| Agentic Critical Training | RL → general reasoning transfer (surprising finding) | Strengthened Section 1 |
| SoK: Agentic Skills | Formal definition + seven design patterns | Major upgrade to Section 5 |
| Agent Skills Survey | SKILL.md spec + security stats (26.1%) | Upgraded Sections 4 + 5 |
| AgentRaft | New risk class (DOE, 57% data leaks) | New content for Section 4 |

### 5.5 What Forward Citations Revealed

- The ARL Survey's high citation count (50+ in 3 months) confirmed it as the canonical reference for Section 1
- Zero citations for Breaking the Protocol and SMCP confirmed we were covering frontier security work
- Live-SWE-agent's 27 citations were mostly SWE-bench variants, confirming benchmark saturation but not introducing new paradigms
- The surprise finds were AgentRaft (entirely new risk class) and ACT (agentic RL → reasoning transfer)

---

## 6. Writing Process

### 6.1 Deep-Dives (Per-Section Literature Reviews)

Each of the five taxonomy sections was written in two formats:

**Markdown** (`notes/{NN}-{name}.md`): Structured as paper-by-paper analysis with extracted findings, key results tables, and cross-paper synthesis paragraphs. Designed for machine consumption (searchable, parseable) and as raw material for the paper draft.

**Interactive HTML** (`s{N}-{name}.dd.html`): Three-panel layout (sidebar nav, summary center, expandable detail right) using a custom template extracted from the reading-assist skill. Built via Python scripts that injected content arrays (sections[], summaries[], details[]) into template CSS/JS. Designed for human reading with progressive disclosure.

### 6.2 HTML Build System

Template CSS (26K) and JS (7.7K) were extracted once from the reading-assist skill's deep-dive reference file and reused across all five sections. Python build scripts:
1. Read template CSS/JS from cache files
2. Defined JavaScript arrays for sections, summaries, and details
3. Patched hero text (title, subtitle, stats badge)
4. Output single standalone HTML file

### 6.3 Forward Citation Updates

After the forward citation sweep, existing markdowns and HTMLs were updated:
- Markdowns: Appended new paper writeups with "(Forward Citation)" labels
- HTMLs: Inserted "Forward Citation Updates (Mar 2026)" callout boxes into the last detail section of each affected HTML

### 6.4 Survey Paper Draft

Written as a single markdown file (`survey-paper-draft.md`), structured as an argument paper:
- Sections 1–2 (Introduction, Method) written from scratch — framing the argument
- Sections 3–7 condensed from existing deep-dives — each section leads with its strongest quantitative result
- Section 8 (Synthesis) written from scratch — five findings + research agenda
- Abstract written last, distilling the thesis to 250 words

**Key constraint:** The paper is an argument (thesis + evidence), not a catalog (paper-by-paper review). Each section advances a specific claim rather than summarizing every source.

### 6.5 Slide Deck

Built using the reading-assist skill's slide-deck template (Crimson Pro/IBM Plex Mono/Source Sans 3 typography, light/dark theme toggle, arrow-key/click/swipe navigation). 20 slides with hand-crafted SVG diagrams, one idea per slide. Structure mirrors the paper: title → TOC → one section divider + 1–2 content slides per axis → synthesis → research agenda → closing.

---

## 7. Tooling

### 7.1 Infrastructure

- **Repository:** github.com/nafSadh/read-rd, subfolder `ai/agentic-lm-survey/`
- **Deployment:** GitHub Pages at nafsadh.github.io/read-rd/ai/agentic-lm-survey/
- **PDF extraction:** PyMuPDF (`fitz`) for text extraction from downloaded arXiv PDFs
- **Citation API:** Semantic Scholar Graph API for forward citation sweep
- **Build system:** Python scripts generating standalone HTML from template CSS/JS + content arrays
- **Version control:** Git with descriptive commit messages documenting each phase

### 7.2 Claude's Role

This entire project — literature collection, paper reading, deep-dive writing, forward citation sweep, paper drafting, HTML building, slide creation — was executed by Claude in a single extended conversation with human direction. The human provided:
- The initial research question and paper reference
- Strategic direction at each phase transition ("read more?" "write the paper" "make slides")
- Quality feedback ("S1 doesn't load" "the index is blank" "flatten the survey entry")
- Scope decisions ("keep as is for now" "8 papers to read")

Claude provided:
- Web research and literature discovery
- PDF download, extraction, and reading
- Content writing (markdown deep-dives, HTML builds, paper draft, slides)
- Semantic Scholar API queries for forward citations
- Git operations (commits, pushes)
- Debugging (finding missing JS arrays, corrupted UTF-8, broken comments)

### 7.3 What Broke and How We Fixed It

| Issue | Root Cause | Fix |
|-------|-----------|-----|
| S1 deep-dive HTML blank | Missing `const sections[]` array — built before template was standardized | Added array manually, commit `de42d99` |
| Root index.html blank | S4 entry had corrupted em dash from bad `sed` command | Fixed in commit `3d446c7` |
| 4 of 8 forward-citation PDFs wrong | arXiv ID collisions (e.g., `2602.15498` was a cosmology paper) | Web-searched correct IDs, re-downloaded |
| Slide deck JS broken | Template had single `/` instead of `//` for comments | `sed` fix on 4 comment lines |

---

## 8. Deliverables

| Deliverable | Format | Location | Size |
|------------|--------|----------|------|
| Literature collection | Markdown | `literature-collection.md` | 85 entries |
| Section 1: REASON deep-dive | HTML + MD | `s1-reason.dd.html` + `notes/01-reason.md` | 68K + 24K |
| Section 2: ACT deep-dive | HTML + MD | `s2-act.dd.html` + `notes/02-act.md` | 67K + 22K |
| Section 3: INTERACT deep-dive | HTML + MD | `s3-interact.dd.html` + `notes/03-interact.md` | 63K + 18K |
| Section 4: OPERATE deep-dive | HTML + MD | `s4-operate.dd.html` + `notes/04-operate.md` | 63K + 18K |
| Section 5: Cross-Cutting deep-dive | HTML + MD | `s5-cross-cutting.dd.html` + `notes/05-cross-cutting.md` | 55K + 15K |
| Literature deep-dives index | Markdown | `notes/00-literature-deep-dives.md` | 28 papers |
| Survey paper draft | Markdown | `survey-paper-draft.md` | ~5,000 words |
| Slide deck | HTML | `ai/agentic-llm-survey.slides.html` | 75K, 20 slides |
| Survey index | HTML | `ai/agentic-lm-survey/index.html` | Landing page |
| Proposal v1 + v2 | Markdown | `agentic-llm-survey-proposal.v1.md` / `.md` | Original + updated |
| Changelog | Markdown | `.project/changelog.md` | Full timeline |
| TODO | Markdown | `.project/todo.md` | Prioritized remaining work |

---

## 9. Limitations of This Methodology

1. **Single-session bias:** The entire project was executed in one extended conversation. A multi-session approach with reflection periods between phases might have caught gaps earlier.

2. **Reading depth:** Most papers read at 25–50%. Critical details in methodology sections, appendices, or late-paper discussions may have been missed. The efficiency tradeoff was deliberate but has real costs.

3. **Forward citation lag:** Semantic Scholar indexes papers with a delay. Papers submitted in February–March 2026 but not yet indexed were necessarily missed.

4. **Industry sources via web research only:** The Anthropic 2026 Trends Report, AAIF governance documents, and tool documentation were analyzed via web search results and page fetches, not as downloaded primary documents. Specific claims may lack the precision of PDF-extracted content.

5. **No practitioner survey component:** The original proposal included a practitioner survey. This was dropped due to scope — the session focused on literature rather than primary data collection.

6. **arXiv bias:** The literature collection skews heavily toward arXiv preprints. Peer-reviewed publications at ICML, NeurIPS, ACL, USENIX Security, and other venues may contain relevant work not captured by our search methodology.

7. **Sole researcher:** Claude operated as both literature reviewer and author. Human oversight provided strategic direction and quality checks but not independent verification of extracted claims. All quantitative figures cited in the paper should be verified against original sources before publication.

---

## 10. Reproducibility

The entire project is version-controlled at github.com/nafSadh/read-rd with descriptive commit messages for each phase. The commit history (`git log --oneline`) serves as an execution trace. The `.project/changelog.md` file provides a narrative timeline. Any future researcher can:

1. Start from `literature-collection.md` (85 entries) as a reading list
2. Download the same PDFs from arXiv
3. Run the same Semantic Scholar API queries for forward citations
4. Compare their findings against our deep-dives and paper draft
5. Extend the work by reading the 57 unread entries or conducting new literature searches

The methodology is designed to be transparent about its limitations so that future work can address them directly rather than discovering gaps through replication failure.
