# TODO — Agentic LLMs in the Wild Survey

## Status: First Pass Complete + Forward Citations + Web Research Update (Mar 25, 2026)

### Recently Completed (Phase 11)
- [x] Fix index.html design consistency (section headers, meta styling, duplicate entries)
- [x] Add prev/next navigation to all 5 deep-dive HTMLs
- [x] Web research: S2 (SWE-bench 80.9%, revenue $2.5B/$2B)
- [x] Web research: S3 (AAIF governance, A2A v0.3.0, MCP 10K+ servers)
- [x] Web research: S4 (MCPSecBench 17 attacks, MCPGuard 78% vuln, 30+ CVEs)
- [x] Web research: S5 (500K+ skills marketplace, 19 agents, Spring AI)
- [x] Update survey-paper.md with latest data
- [x] Update all 4 deep-dive HTMLs with Web Research Update boxes

---

---

## Priority 1: Close the Reading Gap (57 unread papers)

### Section 1 — REASON (5 unread)
- [ ] R-04: Prime Intellect RLM (Recursive Language Models) — context management via code delegation
- [ ] R-07: PRS + VSPO (Progressive Reward Shaping) — curriculum reward for tool-integrated reasoning  
- [ ] R-11: PETS (Principled Test-Time Self-Consistency) — trajectory allocation optimization
- [ ] R-12: Li "Survey on LLM Test-Time Compute via Search" (TMLR 2025)
- [ ] R-01/R-02: DeepSeek-R1 and Kimi k1.5 original papers (currently covered via secondary sources)

### Section 2 — ACT (12 unread)
- [ ] A-01: Original SWE-bench (Jimenez et al.) — foundational benchmark
- [ ] A-09: Darwin-Gödel Machine — open-ended agent evolution
- [ ] A-10: Huxley-Gödel Machine — optimal self-improving machines
- [ ] A-21: MCP-Bench — benchmarking tool-using agents via MCP
- [ ] A-22: LiveMCP-101 — stress testing MCP-enabled agents
- [ ] Remaining industry sources: detailed analysis of Cursor architecture, Codex CLI internals, Gemini CLI architecture, OpenClaw Pi engine design

### Section 3 — INTERACT (3 unread)
- [ ] S-06: Chen et al. "LLM-based Multi-Agent System: Advances and Frontiers"
- [ ] Additional protocol sources: A2A v0.2 spec, ANP reference implementation
- [ ] LangGraph v0.2 architecture documentation

### Section 4 — OPERATE (9 unread)
- [ ] MCPSecBench — attack taxonomy benchmark for MCP
- [ ] MCPGuard — runtime scanning for MCP
- [ ] MindGuard — detection tools for agent manipulation
- [ ] AgentArmor — agent behavior tracking
- [ ] AgentSpec — contract-based rules for agents
- [ ] SAGA — privilege control framework
- [ ] DRIFT — input/output isolation
- [ ] Log-To-Leak (original paper) — covert privacy attacks via logging tools
- [ ] From prompt injections to protocol exploits (ScienceDirect) — 150+ sources

### Sections 6–7 — Industry & TBD (14 unread)
- [ ] LangChain State of AI Agents 2026 survey (1,300+ respondents)
- [ ] Gartner predictions on agentic AI
- [ ] Deloitte 2026 report on agentic AI
- [ ] RE-Bench (Economic Efficiency Factors in Agent Evaluation)
- [ ] Various industry blog posts and analysis pieces

---

## Priority 2: Deepen Existing Sections

### Per-Paper Full Reads (top candidates)
- [ ] ARL Landscape Survey (Zhang et al.) — currently ~26% read. Priority: §4 Applications, §5 Challenges
- [ ] SWE-EVO — currently ~41% read. Priority: failure mode appendix, per-model analysis
- [ ] SWE-Bench Pro — currently ~50% read. Priority: per-repo analysis, language-specific findings
- [ ] SMCP — currently ~26% read. Priority: full SMCP architecture details, implementation examples
- [ ] Multi-Agent Collaboration — currently ~14% read. Priority: §4 detailed mechanisms, §5 applications

### Missing Subsection Deep-Dives
- [ ] GUI agents (OSWorld, WebArena) — not covered in any section
- [ ] Embodied agents (VLAs, robotics) — not covered
- [ ] Scientific discovery agents — not covered
- [ ] Agent observability & evaluation (beyond CLASSic) — thin coverage
- [ ] Agent economics / FinOps — mentioned but not deep-dived

---

## Priority 3: Structural Improvements

### Survey Index
- [ ] Add reading depth indicators per section (e.g., "22/85 papers read")
- [ ] Add "last updated" timestamps per section
- [ ] Add per-section paper list with read/unread status

### Cross-Section Integration
- [ ] Write a synthesis/conclusion section linking all 5 sections
- [ ] Create a "key findings" summary document (1-pager)
- [ ] Map which lit-collection entries were used in which deep-dive sections

### HTML Improvements
- [ ] Add navigation links between sections (prev/next)
- [ ] Add a "reading depth" disclaimer to each deep-dive
- [ ] Fix any broken rendering in dark mode (untested)
- [ ] Add search/filter functionality to survey index

---

## Priority 4: Proposal v2 Refinements

- [ ] Update methodology section to reflect actual reading process (first-pass extraction vs full reads)
- [ ] Revise scope: explicitly state what's covered and what's deferred
- [ ] Add "honest limitations" section documenting the 22/85 gap
- [ ] Consider venue: blog post series vs. workshop paper vs. full survey
- [ ] Add collaboration invitation for co-authors who can cover missing subsections

---

## Priority 5: If Writing a Full Paper

- [ ] Formal related work section comparing to Plaat et al. and other 2025–2026 surveys
- [ ] Quantitative analysis: citation network, publication timeline, keyword trends
- [ ] Practitioner survey component (as proposed in original proposal)
- [ ] Figures: timeline visualization, taxonomy diagram, protocol stack diagram
- [ ] Camera-ready formatting for target venue (JAIR, ACM Computing Surveys, or NeurIPS workshop)
