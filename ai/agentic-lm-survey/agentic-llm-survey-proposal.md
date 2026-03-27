# Agentic LLMs in the Wild: A Survey of Reasoning, Acting, Interacting, and Operating

**Proposal v2** — Updated March 24, 2026 after completing first-pass deep-dives.
See [v1 proposal](agentic-llm-survey-proposal.v1.md) for the original scope.

---

## Status: First Pass Complete, Full Survey In Progress

### What's Done
- **Taxonomy established:** Reason, Act, Interact, Operate + Cross-Cutting (Skills/Config)
- **Literature collected:** 85 entries across 7 sections, 14 subsections
- **22 papers read from PDFs** (~280 pages of actual text extraction)
- **5 interactive deep-dives** (~314K HTML, ~95K markdown) published at [nafsadh.github.io/read-rd/ai/agentic-lm-survey/](https://nafsadh.github.io/read-rd/ai/agentic-lm-survey/)
- **Industry sources** analyzed: Anthropic 2026 Trends Report, AAIF governance, tool landscape, OpenClaw incidents, protocol adoption data

### What's Not Done
- **63 of 85 cataloged entries unread** — reading list, not survey
- **Full reads:** Most papers read at ~25–50% (abstract + intro + key results), not cover-to-cover
- **Missing subsections:** GUI agents, embodied agents, scientific discovery agents, agent economics/FinOps, observability
- **No formal synthesis section** linking all five categories
- **No quantitative analysis** (citation network, keyword trends, publication timeline)

---

## 1. Taxonomy (Finalized)

| Axis | Plaat et al. (2025) | This Survey (2026) | Key Addition |
|------|--------------------|--------------------|-------------|
| **Reason** | Reasoning, reflection, retrieval | Model-native reasoning via RL; POMDP formalization; scaling laws; efficiency as training objective | Scaffold → weights migration |
| **Act** | Action models, robots, tools | Agentic coding (SWE-bench family), self-improving agents, production tools | The coding explosion |
| **Interact** | Multi-agent systems, social simulation | Protocol standards (MCP/A2A/ACP/ANP), AAIF governance, flow engineering, difficulty-aware routing | Infrastructure, not research |
| **Operate** | *(not covered)* | MCP security (23–41% amplification), prompt injection (78%+ bypass), skill supply chain | The central engineering challenge |
| **Cross-Cut** | *(not covered)* | SKILL.md portability, CLAUDE.md/AGENTS.md, progressive disclosure, five configuration layers | The portable agent layer |

---

## 2. Papers Read (Honest Accounting)

### Section 1: REASON — 7 papers, ~120pp read
| Paper | Pages | Read | Coverage |
|-------|-------|------|----------|
| Zhang et al. "Landscape of Agentic RL" (TMLR 2026) | 95 | pp1-20, 43-46 | 26% |
| Cheng et al. "Agent-R1" | 13 | pp1-3 | 23% |
| Tan et al. "Scaling Behaviors" | 27 | pp1-3 | 11% |
| Ning et al. "Agent-Omit" | 20 | pp1-3 | 15% |
| Yu et al. "Demystifying RL" | 24 | pp1-3 | 13% |
| Wang et al. "OpenClaw-RL" | 24 | pp1-3 | 13% |
| Zhang et al. "RL for LRMs" | 120 | pp1-2 (TOC only) | 2% |

### Section 2: ACT — 7 papers, ~55pp read
| Paper | Pages | Read | Coverage |
|-------|-------|------|----------|
| Deng et al. "SWE-Bench Pro" | 20 | pp1-4, 7-12 | 50% |
| Thai et al. "SWE-EVO" | 27 | pp1-4, 9-15 | 41% |
| Zhang et al. "SWE-bench Live" | 24 | pp1-4 | 17% |
| Garg et al. "Saving SWE-Bench" | 11 | pp1-4 | 36% |
| Yu et al. "UTBoost" | 13 | pp1-4 | 31% |
| Xia et al. "Live-SWE-agent" | 20 | pp1-4, 6-10 | 45% |
| Zhang et al. "One Tool Is Enough" | 25 | pp1-4 | 16% |

### Section 3: INTERACT — 5 papers, ~45pp read
| Paper | Pages | Read | Coverage |
|-------|-------|------|----------|
| Ehtesham et al. "Agent Interoperability Protocols" | 21 | pp1-5, 8-9, 15 | 38% |
| Tran et al. "Multi-Agent Collaboration" | 35 | pp1-5 | 14% |
| Drammeh "Multi-Agent Orchestration" | 10 | Full | 100% |
| Su et al. "DAAO" (WWW '26) | 12 | pp1-5 | 42% |
| Arunkumar et al. "Agentic Architectures" | 28 | pp1-5, 12-13, 17-18 | 36% |

### Section 4: OPERATE — 3 papers, ~30pp read
| Paper | Pages | Read | Coverage |
|-------|-------|------|----------|
| Maloyan et al. "Breaking the Protocol" | 7 | Full | 100% |
| Hou et al. "SMCP" | 23 | pp1-6 | 26% |
| Maloyan et al. "Prompt Injection SoK" | 10 | Full | 100% |

### Section 5: Cross-Cutting — 0 papers (web research only)

---

## 3. Key Findings (Preliminary)

**REASON:** Scaffold → weights migration via RL is the defining shift. Agentic RL = POMDP, not RLHF's degenerate MDP. Efficiency (accuracy/token) is becoming a training objective.

**ACT:** Real capabilities below headlines (<45% enterprise, 65%→21% evolution). Self-improving agents (77.4%) beat hand-crafted scaffolds at zero offline cost. Engineers use AI in 60% of work, delegate only 0–20%.

**INTERACT:** MCP/A2A compose like TCP/IP. Multi-agent decomposition → deterministic quality (100% vs 1.7%). AAIF: six competitors co-governing standards.

**OPERATE:** MCP amplifies attacks 23–41%. All defenses bypassed at 78%+. Skill ecosystems face supply chain attacks worse than npm (direct system access).

**CROSS-CUT:** SKILL.md = first cross-vendor standard (1,300+ skills, 8 tools). Five configuration layers emerging organically.

---

## 4. Next Steps

See [TODO](.project/todo.md) for detailed breakdown. Priorities:

1. Close the 63-paper reading gap (especially GUI, embodied, MCPSecBench, DGM/HGM)
2. Full reads of top papers (ARL Survey, SWE-EVO, SMCP, Multi-Agent Collaboration)
3. Write synthesis/conclusion linking all five axes
4. Decide format: blog series vs. workshop paper vs. full survey
5. If full paper: related work, quantitative analysis, practitioner survey

---

## 5. Differentiation from Plaat et al.

| Dimension | Plaat et al. | This Survey |
|-----------|-------------|-------------|
| Taxonomy | Reason / Act / Interact | + **Operate** + Cross-Cutting |
| Act focus | Robotics, hypothetical | **Agentic coding** (benchmarks + tools + production) |
| Interact focus | Social simulation | **Protocol infrastructure** (MCP/A2A/AAIF) |
| Operate | "Future work" | **Dedicated section** (security, supply chain) |
| Paradigm | Scaffold-based | + **model-native** (RL-internalized) |
| Evidence | Papers only | + **production data** + industry reports |
| Config | Not covered | **SKILL.md / CLAUDE.md / AGENTS.md** layer |
