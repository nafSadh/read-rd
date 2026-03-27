# Changelog — Agentic LLMs in the Wild Survey

All changes to the survey literature collection and deep-dive project.

---

## Session: March 23–24, 2026

### Phase 0: Inception
- **User prompt:** "arXiv:2503.23037 is interesting. But it's stale. How'd you redo a similar but updated research?"
- Analyzed Plaat et al.'s survey strengths (Reason/Act/Interact taxonomy, virtuous cycle, research agenda) and gaps (no protocol layer, no production data, no model-native shift, no specialist model economics)
- Proposed four-axis taxonomy: **Reason, Act, Interact, Operate** (adding "Operate" as new category)
- User requested scoping as a survey paper

### Phase 1: Literature Collection & Proposal
- Conducted extensive web research across agentic RL, coding benchmarks, protocols, security
- Built `literature-collection.md` with **85 entries** organized across 7 sections + 14 subsections
- Wrote `agentic-llm-survey-proposal.md` (21K) covering taxonomy, structure, methodology, venue options, execution plan
- **Commit `35b95be`:** Initial push to `nafSadh/read-rd` repo under `ai/agentic-lm-survey/`

### Phase 2: Section 1 — REASON (Model-Native Reasoning & Agentic RL)
- Downloaded 7 PDFs (~300pp total): ARL Landscape Survey (95pp), Agent-R1, Scaling Laws, Agent-Omit, Demystifying RL, OpenClaw-RL, RL for LRMs (120pp)
- Read abstracts + intros + key sections from each (actual reading ~120pp, ~26% average coverage)
- Wrote `notes/01-reason.md` (24K markdown deep-dive)
- Built `s1-reason.dd.html` (67K interactive three-panel HTML with sidebar nav, 8 subsections)
- Extracted CSS/JS templates from reading-assist skill for reuse across sections
- Created `index.html` survey landing page
- **Commit `e7340a6`:** Section 1 complete

### Phase 3: Root Index Update
- Updated `read-rd/index.html` root tree to include Agentic LLM Survey subfolder with S1–S5 entries
- **Commit `f321cf8`:** Root index updated

### Phase 4: Section 2 — ACT (Agentic Coding & Tool Use)
- Downloaded 7 PDFs (~140pp): SWE-Bench Pro, SWE-EVO, SWE-bench Live, Saving SWE-Bench, UTBoost, Live-SWE-agent, One Tool Is Enough (RepoNavigator)
- Read abstracts + intros + results sections (~55pp, ~40% average coverage)
- Web-searched Anthropic 2026 Agentic Coding Trends Report (8 trends), tool landscape (Claude Code, Antigravity, Codex, Gemini CLI, Cursor, OpenClaw), skills portability
- Wrote `notes/02-act.md` (22K) and `s2-act.dd.html` (65K)
- **Commit `81c2d75`:** Section 2 complete

### Phase 5: Section 3 — INTERACT (Protocols & Multi-Agent Systems)
- Downloaded 5 PDFs (~106pp): Agent Interoperability Protocols (MCP/A2A/ACP/ANP), Multi-Agent Collaboration Mechanisms, Multi-Agent Orchestration (incident response), DAAO (WWW '26), Agentic Architectures
- Read abstracts + intros + protocol/results sections (~45pp, ~42% average coverage)
- Full read of Drammeh (10pp) orchestration paper
- Web-searched AAIF governance, Cisco blog, Mitra protocol stack analysis
- Wrote `notes/03-interact.md` (18K) and `s3-interact.dd.html` (63K)
- Fixed survey index links for S2/S3 (had broken pending→done update earlier)
- **Commit `f54e56f`:** Section 3 complete
- **Commit `14b8ef4`:** Fix survey index links

### Phase 6: Section 4 — OPERATE (Safety, Security, Reliability)
- Downloaded 3 PDFs (~40pp): Breaking the Protocol (MCP security), SMCP (Secure MCP), Prompt Injection SoK
- Full read of Breaking the Protocol (7pp) and Prompt Injection SoK (10pp)
- Read SMCP intro + threat catalog + architecture (~6pp of 23pp)
- Web-searched OpenClaw security incidents (Acronis, Censys, Cisco), OWASP, Simon Willison
- Wrote `notes/04-operate.md` (18K) and `s4-operate.dd.html` (63K)
- **Commit `85e185e`:** Section 4 complete

### Phase 7: Section 5 — Cross-Cutting (Skills & Configuration Standards)
- No new PDFs — synthesis from web research across all sections
- Web-searched SKILL.md format (Google Codelab, Antigravity Awesome Skills v8.6.0, agentskills.io)
- Researched CLAUDE.md, AGENTS.md, .cursorrules convergence
- Pi's self-extension philosophy (Armin Ronacher/OpenClaw)
- Wrote `notes/05-cross-cutting.md` (12K) and `s5-cross-cutting.dd.html` (54K)
- Updated both indexes to show all 5 sections done
- **Commit `75ea612`:** ALL SECTIONS COMPLETE

### Phase 8: Honest Assessment & Project Cleanup (this commit)
- User asked about reading depth — provided honest per-paper coverage table
- User noted gap between literature-collection (85 entries) and actual coverage (22 papers read)
- Updated survey index to show coverage stats
- Backed up original proposal as v1, wrote updated v2 proposal
- Created `.project/changelog.md` and `.project/todo.md`

---

## Reading Depth Summary

| Section | Papers in Lit Collection | Papers Read from PDFs | Pages Read (est.) | Coverage |
|---------|------------------------|-----------------------|-------------------|----------|
| 0. Surveys | 12 | 3 (ARL, RL for LRMs, Agentic Arch) | ~30pp | Selective |
| 1. REASON | 12 | 7 | ~120pp | Good |
| 2. ACT | 22 | 7 | ~55pp | Good (papers) + industry |
| 3. INTERACT | 8 | 5 | ~45pp | Good |
| 4. OPERATE | 12 | 3 | ~30pp | Good (security core) |
| 5. Cross-Cut | 5 | 0 (web research) | N/A | Industry only |
| 6–7. Industry/TBD | 14 | 0 | N/A | Not started |
| **Total** | **85** | **22** | **~280pp** | **26% of entries** |

### Phase 9: Forward Citation Sweep & Literature Deep-Dives

- Forward citation sweep via Semantic Scholar API on 6 key papers (ARL Survey, Breaking the Protocol, Live-SWE-agent, SWE-EVO, Agent-Omit, Prompt Injection SoK, SMCP, OpenClaw-RL)
- ARL Survey: 50+ citations in 3 months; Live-SWE-agent: 27 citations
- Identified 8 candidate papers, downloaded 6 correctly (2 arXiv ID collisions)
- Read 6 new papers (~180pp): Self-Play SWE-RL, Self-Evolving Agents Survey, Agentic Critical Training, SoK Agentic Skills, Agent Skills Survey, AgentRaft

**Updated markdowns:**
- `notes/02-act.md`: Added Self-Play SWE-RL (SSR) and Self-Evolving Survey
- `notes/04-operate.md`: Added AgentRaft (DOE, 57.07% tool chain leaks) and skills vulnerability data (26.1%)
- `notes/05-cross-cutting.md`: Added SoK Agentic Skills (S=(C,π,T,R), 7 patterns) and Agent Skills Survey (progressive disclosure, governance)

**Updated HTMLs:**
- `s2-act.dd.html`: Forward citation box added (SSR, Self-Evolving Survey, ACT)
- `s4-operate.dd.html`: Forward citation box added (AgentRaft DOE, skills vulnerabilities)
- `s5-cross-cutting.dd.html`: Forward citation box added (SoK Skills, Agent Skills Survey)

**New file:**
- `notes/00-literature-deep-dives.md`: Unified index of all 28 papers read, with per-paper coverage stats, key extractions, dates, links

**Updated survey index:** 28 papers / ~460pp stats, link to literature deep-dives page

### Phase 10: Survey Paper Draft

- Wrote full survey essay `survey-paper.md` (~6,300 words, 383 lines, 11 sections)
- Execution order: (1) framing (intro + taxonomy), (2) synthesis + research agenda, (3) condensed sections 3–7 from existing deep-dives, (4) abstract + conclusion
- 35 references (29 primary papers + 6 industry sources)
- Five main findings articulated in synthesis
- Research agenda: 5 open problems (architectural security, long-horizon gap, skill governance, mechanistic debate, agent economics)
- Added to survey index

### Phase 11: Web Research Update & Design Consistency (Mar 25, 2026)

**Design Improvements:**
- Fixed `index.html` design consistency with reference style (`genai-2026-outlook/index.html`): added `.meta strong`, `.meta a` styling, `h2` section headers
- Added section headers ("Section Deep-Dives", "Papers & Presentations", "Resources") matching reference layout
- Consolidated duplicate Survey Paper entries into single entry with all links
- Added footer cross-link to GenAI 2026 Outlook project
- Added prev/next navigation links to all 5 deep-dive HTMLs (S1-S5)

**Web Research Updates (all 4 focused sections):**

*S2 — ACT:*
- SWE-Bench Verified: Claude Opus 4.5 at 80.9% (up from ~65% a year ago), Gemini 3.1 Pro at 80.6%
- SWE-Bench Pro: GPT-5.3-Codex leads at 56.8%; Verified-to-Pro gap (80.9% vs 45.9%) confirms benchmark-to-reality gulf
- Revenue: Claude Code $2.5B ARR (up from $1B Nov 2025), Cursor $2B+ ARR, 84% of devs use multiple tools

*S3 — INTERACT:*
- AAIF governance: neutral oversight with open RFC process, six co-founders plus Cisco
- A2A at v0.3.0 with extension support and concrete protocol bindings (JSON-RPC, gRPC, HTTP/REST)
- MCP ecosystem: 10,000+ active servers (up from 1,000 in early 2025)

*S4 — OPERATE:*
- MCPSecBench (AIS2Lab, Feb 2026): 17 attack types across 4 surfaces, 85%+ compromise rate, <30% defense success
- MCPGuard: 78% of 700+ open-source MCP servers have critical vulnerabilities
- 30+ CVEs in 60 days (Jan-Feb 2026), including CVSS 9.6 RCE
- AgentArmor: 8-layer defense addressing OWASP ASI Top 10

*S5 — CROSS-CUTTING:*
- SkillsMP marketplace: 500,000+ agent skills
- agentskill.sh: 44K+ skills with two-layer security scanning
- SKILL.md format now works across 19 supported agents
- Spring AI (Jan 2026) brought Agent Skills to Java ecosystem

**Updated files:**
- `s2-act.dd.html`: Web Research Update box with SWE-bench and revenue data
- `s3-interact.dd.html`: Web Research Update box with AAIF, A2A, MCP data
- `s4-operate.dd.html`: Web Research Update box with MCPSecBench, MCPGuard, CVE data
- `s5-cross-cutting.dd.html`: Web Research Update box with ecosystem growth data
- `survey-paper.md`: Updated abstract ($4.5B revenue), Shift 2 ($2.5B/$2B ARR), S4.1 (MCPSecBench), S5.1 (MCP 10K+ servers), S4.3 (production tools), S7.2 (500K+ skills), Findings 4 & 5
- `survey-paper.html`: Updated revenue figures
- `index.html`: Design consistency fixes, section headers, navigation
