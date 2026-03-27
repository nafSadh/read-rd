# Literature Collection: Agentic LLMs Survey Update
## Compiled March 23, 2026

---

## 0. Baseline & Related Surveys

| ID | Paper | Authors | Venue/Date | Role |
|----|-------|---------|------------|------|
| S-01 | Agentic Large Language Models, a survey | Plaat, van Duijn, van Stein, Preuss, van der Putten, Batenburg | JAIR 2025 (arXiv:2503.23037, v3 Nov 2025) | **Primary baseline** — Reason/Act/Interact taxonomy |
| S-02 | Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native Agentic AI | ADaM-BJTU group | 2025 (GitHub: ADaM-BJTU/model-native-agentic-ai) | Key framing: model-native vs. scaffold-based; RL as unifying mechanism |
| S-03 | The Landscape of Agentic Reinforcement Learning for LLMs: A Survey | Zhang, Geng, Yu et al. (25 authors) | arXiv:2509.02547, v4 Jan 2026 | Comprehensive ARL taxonomy — POMDPs, capabilities, applications |
| S-04 | A Survey of Reinforcement Learning for Large Reasoning Models | Zhang et al. | arXiv:2509.08827, v3 Oct 2025 | RL for LRMs — scaling, algorithms, DeepSeek-R1 context |
| S-05 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Tran et al. | arXiv:2501.06322, Jan 2025 | MAS collaboration taxonomy: types, structures, strategies, coordination |
| S-06 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers | Chen, Liu, Han, Zhang, Liu | arXiv:2412.17481, late 2024 | MAS applications: complex tasks, simulation, evaluation |
| S-07 | A Review of Prominent Paradigms for LLM-Based Agents: Tool Use, Planning, and Feedback Learning | Li | CoLing 2025 | Tool use + RAG, planning, feedback learning paradigms |
| S-08 | A Survey on the Optimization of Large Language Model-based Agents | Du et al. | ACM Computing Surveys 2025 | Parameter-driven + parameter-free optimization methods |
| S-09 | Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents | (multiple) | arXiv:2601.12560, Jan 2026 | Systems architecture focus: perception, memory, brain, action; MCP/orchestration |
| S-10 | Large Language Model Agents: A Comprehensive Survey on Architectures, Capabilities, and Applications | (multiple) | Preprints.org, Dec 2025 | Formal taxonomy: reasoning-enhanced, tool-augmented, multi-agent, memory-augmented |
| S-11 | A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, ANP | (multiple) | arXiv:2505.02279, 2025 | Protocol comparison — architecture, security, phased adoption roadmap |
| S-12 | From prompt injections to protocol exploits: Threats in LLM-powered AI agents workflows | (multiple) | ScienceDirect, pub. 2026 | 150+ sources, 30+ attack techniques taxonomy, MCP/ACP/A2A vulnerabilities |

---

## 1. REASON — Model-Native Reasoning & RL

### 1.1 Foundational Reasoning Models

| ID | Paper | Key Contribution | Date |
|----|-------|-----------------|------|
| R-01 | DeepSeek-R1 (Guo et al.) | GRPO RL training → emergent self-reflection; the paper that catalyzed model-native reasoning | Jan 2025 |
| R-02 | Kimi k1.5 (Du et al.) | RL-trained reasoning; reinforces generalizability of the DeepSeek approach | 2025 |
| R-03 | Scaling Behaviors of LLM Reinforcement Learning Post-Training | Empirical scaling laws for RL post-training on Qwen2.5 (0.5B–72B); 63 models, power-law fits | arXiv:2509.25300, v3 Dec 2025 |
| R-04 | Recursive Language Models: the paradigm of 2026 | Prime Intellect — RLM for context management; model manages its own context via code delegation | arXiv:2512.24601, blog 2026 |

### 1.2 Agentic RL Training

| ID | Paper | Key Contribution | Date |
|----|-------|-----------------|------|
| R-05 | Agent-R1: Training Powerful LLM Agents with End-to-End RL | Extends MDP framework for multi-turn agents; modular training framework | arXiv:2511.14460, Nov 2025 |
| R-06 | ARLArena / SAMPO (OpenClaw-RL) | Training stability analysis framework; decomposes policy gradient into 4 dimensions; SAMPO for stable agentic policy optimization | arXiv:2603.10165, Mar 2026 |
| R-07 | Enhancing Agentic RL with Progressive Reward Shaping and VSPO | PRS (curriculum reward) + VSPO (value-based sampling) for tool-integrated reasoning | arXiv:2512.07478, v2 Jan 2026 |
| R-08 | Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission | Trains agents to skip redundant reasoning steps; dual sampling + omission reward | arXiv:2602.04284, Feb 2026 |
| R-09 | Demystifying Reinforcement Learning in Agentic Reasoning | Systematic investigation of GRPO variants for agentic settings; loss granularity, reward shaping, clipping | arXiv:2510.11701, Oct 2025 |
| R-10 | OpenClaw-RL: Train Any Agent Simply by Talking | Fully async RL from natural conversation feedback; Binary RL + OPD; tracks for terminal/GUI/SWE/tool-call | arXiv:2603.10165, Mar 2026 |

### 1.3 Inference-Time Compute

| ID | Paper | Key Contribution | Date |
|----|-------|-----------------|------|
| R-11 | PETS: Principled and Efficient Test-Time Self-Consistency | Optimization framework for trajectory allocation; self-consistency rate metric | 2026 (cited in LLM papers survey) |
| R-12 | A Survey on LLM Test-Time Compute via Search | Li (TMLR 2025) — tasks, LLM profiling, search algorithms, frameworks | TMLR 2025 |

---

## 2. ACT — Agentic Coding & Tool Use

### 2.1 Agentic Coding Benchmarks

| ID | Paper | Key Contribution | Date |
|----|-------|-----------------|------|
| A-01 | SWE-bench (Jimenez et al.) | Original issue-resolution benchmark — de facto standard | 2024 (foundational) |
| A-02 | SWE-Bench Pro: Can AI Agents Solve Long-Horizon SE Tasks? | 1,865 problems, 41 repos, 123 languages; enterprise-grade; <45% Pass@1 | arXiv:2509.16941, v2 Nov 2025 |
| A-03 | SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution | 48 evolution tasks, avg 21 files changed; GPT-5 achieves only 21% (vs 65% on SWE-Bench Verified) | arXiv:2512.18470, v4 Jan 2026 |
| A-04 | SWE-bench Goes Live! | Automated pipeline for continuous benchmark updates; contamination-resistant | arXiv:2505.23419, May 2025 |
| A-05 | Saving SWE-Bench: Benchmark Mutation for Realistic Agent Evaluation | Transforms formal benchmarks into realistic user queries; reveals >50% overestimation | arXiv:2510.08996, v4 Jan 2026 |
| A-06 | UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench | Test case augmentation; found 345 erroneous patches, 40.9% of SWE-Bench Lite affected | arXiv:2506.09289, Jun 2025 |

### 2.2 Self-Improving & RL-Trained Coding Agents

| ID | Paper | Key Contribution | Date |
|----|-------|-----------------|------|
| A-07 | Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly? | Self-evolving agent starting from basic scaffold; 77.4% on SWE-bench Verified, 45.8% on Pro | arXiv:2511.13646, v3 |
| A-08 | One Tool Is Enough: RL of LLM Agents for Repository-Level Code Navigation | Single "jump" tool + RL training; code localization via RL rather than hand-designed multi-tool agents | arXiv:2512.20957, Jan 2026 |
| A-09 | Darwin-Gödel Machine (Zhang et al.) | Open-ended evolution of self-improving agents through iterative refinement | 2025 |
| A-10 | Huxley-Gödel Machine (Wang et al.) | Approximating optimal self-improving machines for human-level coding | 2025 |

### 2.3 Agentic Coding Tools (Non-Academic — Industry Sources)

| ID | Tool/Source | Key Data Points | Date |
|----|------------|----------------|------|
| A-11 | Claude Code (Anthropic) | Agent Teams (parallel sub-agents), MCP-native, CLAUDE.md config; $1B ARR by Nov 2025; leads VS Code Marketplace | Ongoing; Opus 4.6 Feb 2026 |
| A-12 | Google Antigravity | Agent-first IDE (VS Code fork); Manager View for multi-agent orchestration; Artifacts for verification; Gemini 3 Pro | Launched Nov 2025 |
| A-13 | OpenAI Codex CLI | Rust-based, local-first sandbox; IDE + CLI; GPT-5-Codex | Mar 2025 launch |
| A-14 | Gemini CLI (Google, open source) | 1M token context, free tier (1000 req/day), Google Search grounding; 96.6K+ GitHub stars | 2025, open source |
| A-15 | Cursor (Anysphere) | VS Code fork; cloud agents with computer use; sub-agents; $1.2B ARR in 2025 | Ongoing |
| A-16 | OpenClaw (Steinberger → OpenAI → open-source foundation) | Messaging-platform agent; 100K+ GitHub stars; self-extending skills; ClawHub; major security incidents | Nov 2025 – present |
| A-17 | Antigravity Awesome Skills (v5.4.0) | 868+ skills portable across Claude Code, Gemini CLI, Codex, Cursor; SKILL.md standard; official skills from Anthropic, Vercel, OpenAI, Microsoft, Google DeepMind | Feb 2026 |
| A-18 | Anthropic 2026 Agentic Coding Trends Report | 8 trends; case studies: Fountain, Rakuten (7h autonomous, 12.5M LOC), CRED, TELUS (500K hours saved); 60% AI usage, 67% more PRs/day | 2026 |
| A-19 | 2026 Guide to Coding CLI Tools: 15 AI Agents Compared (Tembo) | Comprehensive comparison across 15 tools — philosophy, pricing, model support | Feb 2026 |

### 2.4 Tool Use — MCP Ecosystem

| ID | Paper/Source | Key Contribution | Date |
|----|-------------|-----------------|------|
| A-20 | MCP Specification v1.0 (Anthropic → AAIF) | JSON-RPC client-server for tool invocation; 97M+ monthly SDK downloads by Feb 2026 | Nov 2024 spec; Dec 2025 AAIF transfer |
| A-21 | MCP-Bench: Benchmarking tool-using LLM agents with complex real-world tasks via MCP servers | Wang et al. | arXiv:2508.20453, Aug 2025 |
| A-22 | LiveMCP-101: Stress Testing MCP-enabled Agents on Challenging Queries | 101 real-world queries; ground-truth execution plans | 2025 |

---

## 3. INTERACT — Protocols & Multi-Agent Systems

### 3.1 Protocol Architecture

| ID | Paper/Source | Key Contribution | Date |
|----|-------------|-----------------|------|
| I-01 | A2A (Agent-to-Agent Protocol) specification | Google → Linux Foundation; Agent Cards, task lifecycle, SSE streaming | Apr 2025 launch; Jun 2025 LF transfer |
| I-02 | ACP (Agent Communication Protocol) — IBM → merged into A2A | REST-native messaging, multimodal agent responses | Merged Aug 2025 |
| I-03 | ANP (Agent Network Protocol) | Peer-to-peer agent communications; decentralized identity (DID) | 2025 |
| I-04 | AAIF (Agentic AI Foundation) — Linux Foundation | Co-founded by OpenAI, Anthropic, Google, Microsoft, AWS, Block; governs MCP + A2A + Goose + Agents.md | Dec 2025 |
| I-05 | The Agent Protocol Stack (Subhadip Mitra) | TCP/IP analogy: A2A as network layer, MCP as resource layer; security gaps; LangGraph v0.2 A2A+MCP support | Blog, Jan 2026 |
| I-06 | MCP and A2A: A Network Engineer's Mental Model (Cisco) | MCP for tool-level, A2A for agent-level routing; compose rather than compete | Cisco Blog, Jan 2026 |
| I-07 | UCP (Universal Commerce Protocol) + AP2 (Agent Payments Protocol) | Google; agent-to-business payments and commerce | Mar 2026 |

### 3.2 Multi-Agent Orchestration

| ID | Paper | Key Contribution | Date |
|----|-------|-----------------|------|
| I-08 | Multi-Agent LLM Orchestration for Incident Response (MyAntFarm.ai) | 348 trials; multi-agent: 100% actionable vs 1.7% single-agent; 80x specificity, 140x correctness | arXiv:2511.15755, v2 Jan 2026 |
| I-09 | Difficulty-Aware Agent Orchestration in LLM-Powered Workflows | Heterogeneous LLM routing by query difficulty; up to 11.21% accuracy gain at 64% cost | arXiv:2509.11079, Sep 2025 |
| I-10 | DroidSpeak: Enhancing Cross-LLM Communication (Liu et al.) | Direct model-to-model communication without serialization | arXiv:2411.02820, 2024 |

---

## 4. OPERATE — Safety, Security, Reliability, Economics

### 4.1 MCP & Protocol Security

| ID | Paper | Key Contribution | Date |
|----|-------|-----------------|------|
| O-01 | Breaking the Protocol: Security Analysis of MCP (Maloyan et al.) | First formal MCP security analysis; 3 architectural vulnerabilities; MCPBench framework; 23–41% amplified attack rates; MCPSec mitigation (52.8% → 12.4%) | arXiv:2601.17549, Jan 2026 |
| O-02 | SMCP: Secure Model Context Protocol | Backward-compatible security extension: capability attestation, policy validation, audit logging, tenant isolation | arXiv:2602.01129, Feb 2026 |
| O-03 | MCPSecBench (Yang, Wu, Chen) | Systematic security benchmark and playground for MCP | arXiv:2508.13220, Aug 2025 |
| O-04 | Log-To-Leak: Prompt Injection via MCP Tool Invocation | Covert privacy attacks forcing malicious tool invocation; tested on GPT-4o, GPT-5, Claude-Sonnet-4 | OpenReview (under review) |
| O-05 | Prompt Injection on Agentic Coding Assistants (SoK) | 78 studies synthesized; 3D taxonomy (vectors, modalities, propagation); 85%+ attack success with adaptive strategies | arXiv:2601.17548, Jan 2026 |
| O-06 | Prompt Injection Attacks in LLMs and AI Agent Systems (comprehensive review) | 45 key sources; MCP tool poisoning, A2A expansion of attack surface; OWASP LLM Top 10 mapping | Information (MDPI), Jan 2026 |

### 4.2 OpenClaw Security Case Study

| ID | Source | Key Data Points | Date |
|----|--------|----------------|------|
| O-07 | OpenClaw — Wikipedia | Full history: Clawdbot → Moltbot → OpenClaw; Anthropic trademark complaint; MoltMatch dating incident; creator joined OpenAI; Chinese govt restrictions | Ongoing |
| O-08 | OpenClaw: Agentic AI in the wild (Acronis) | Gateway architecture analysis; 21K+ exposed instances (Censys); skill supply chain attacks; 14 malicious skills on ClawHub Jan 27–29 | 2026 |
| O-09 | Cisco AI security research on OpenClaw skill | Found data exfiltration + prompt injection in third-party skill; skill repo lacked vetting | 2026 |
| O-10 | NanoClaw (The New Stack mention) | Docker containerization approach for OpenClaw security | Mar 2026 |

### 4.3 Agent Observability & Evaluation

| ID | Paper/Source | Key Contribution | Date |
|----|-------------|-----------------|------|
| O-11 | LangChain State of AI Agents Report | 1,300+ respondents; 57% agents in production; 32% cite quality as top barrier; 89% have observability; multi-model norm | Survey Nov–Dec 2025, published 2026 |
| O-12 | OWASP Top 10 for LLM Applications (2025 edition) | LLM01=Prompt Injection; 600+ experts, 18 countries; expanded for agentic AI | 2025 |
| O-13 | Anthropic AI Fluency Index | 9,830 conversations analyzed; iteration multiplies fluency behaviors 2x; Artifact Paradox (polished outputs reduce critical evaluation) | Feb 2026 |

### 4.4 Economics & Model Routing

| ID | Source | Key Contribution | Date |
|----|--------|-----------------|------|
| O-14 | Gartner agentic AI projections | 1,445% surge in multi-agent inquiries Q1 2024→Q2 2025; 80% customer-facing processes by multi-agent AI by 2028; 40% enterprise apps with embedded agents by 2026 | Various 2025–2026 |
| O-15 | Deloitte 2026 Tech Trends | Agentic AI as one of three transformative forces | 2026 |
| O-16 | Context rot research | Models claiming 1M+ token windows experience >50% performance degradation at 100K tokens | Various 2025–2026 |

---

## 5. Cross-Cutting: Skills & Configuration Standards

| ID | Source | Key Contribution | Date |
|----|--------|-----------------|------|
| X-01 | SKILL.md format | Universal skill definition format used across Claude Code, Gemini CLI, Codex, Cursor, Antigravity | Emerging 2025–2026 |
| X-02 | CLAUDE.md | Claude Code project configuration; coding standards, workflow rules | 2025 |
| X-03 | AGENTS.md | Adopted by Cursor, OpenAI Codex, OpenCode; defines agent behavior, tool access, project instructions | 2025–2026 |
| X-04 | Antigravity Awesome Skills v5.4.0 | 868+ skills, 40+ contributors, official skills from 6 companies; universal installer with per-tool paths | Feb 2026 |
| X-05 | Pi: The Minimal Agent Within OpenClaw (Armin Ronacher / lucumr.pocoo.org) | Philosophy: agent extends itself via code; no MCP by design; skills as self-written extensions | Blog, Jan 2026 |

---

## 6. Industry Reports & Non-Academic Sources

| ID | Source | Key Data | Date |
|----|--------|----------|------|
| N-01 | 5 Key Trends Shaping Agentic Development in 2026 (The New Stack) | MCP server management, parallel agent execution, CLI vs desktop convergence | Dec 2025 |
| N-02 | 7 Agentic AI Trends to Watch in 2026 (Machine Learning Mastery) | Multi-agent orchestration, MCP/A2A, FinOps, governance maturity | Jan 2026 |
| N-03 | Top Agentic LLM Models & Frameworks for 2026 (Adaline) | Framework battle: native SDK vs. LangChain; context rot; model comparison | Jan 2026 |
| N-04 | Deciphering the alphabet soup of agentic AI protocols (The Register) | MCP, A2A, ACP, ANP, UCP/AP2 landscape overview | Jan 2026 |
| N-05 | OpenClaw vs Claude Code (DataCamp) | Feature comparison; security analysis; use-case recommendations | Feb 2026 |
| N-06 | Claude Code vs Codex vs Gemini Code Assist (Educative) | Hands-on comparison on real projects | 2026 |
| N-07 | 9 Best AI Coding Agents in 2026, Ranked (MightyBot) | Rankings, market data, multi-agent architectures, MCP adoption | Mar 2026 |
| N-08 | Major AI coding tools comparison 2026 (Terry Cho, Medium) | GitHub commit data showing Claude Code dominance; Gemini for planning, Claude for coding pattern | Feb 2026 |

---

## 7. Papers Still To Locate (Known to Exist)

These are referenced in the collected literature but I haven't retrieved full details yet:

| Topic | What to find |
|-------|-------------|
| VLA progress | π0 (Physical Intelligence), RT-2 (Google), Octo — latest results on vision-language-action models |
| GUI agents | OSWorld benchmark, WebArena, VisualWebArena — browser/GUI agent evaluations |
| Generative Agents updates | Park et al. updates beyond the 2023 paper; agent behavior at scale |
| RLVR beyond math/code | Mitra's Part 2 on RLVR (Reinforcement Learning with Verifiable Rewards) in non-math domains |
| Mechanistic interpretability for agents | Circuit tracing, attention patterns in tool-calling decisions |
| Agent memory systems | MemWeaver, MEM-Agent, persistent memory architectures for long-running agents |
| DeepSeek-V3.2 agentic capabilities | Latest DeepSeek with agentic features |
| Kimi-K2 | Moonshot's latest agentic model |
| Computer use (Anthropic) | Claude computer use — academic analysis of browser/desktop agent capabilities |
| AgentRxiv | Framework for LLM agent labs to share research collaboratively |
| MultiAgentBench | Evaluation framework for LLM multi-agent collaboration and competition |

---

## 8. Collection Statistics

- **Total entries collected:** ~85
- **Academic papers (arXiv, conferences, journals):** ~45
- **Industry reports & technical blogs:** ~25
- **Tool/product documentation & analysis:** ~15
- **Date range:** Nov 2024 (MCP spec) – Mar 2026
- **Coverage by taxonomy section:**
  - Reason: 12 entries
  - Act: 19 entries (+ 9 tool entries)
  - Interact: 10 entries
  - Operate: 16 entries
  - Cross-cutting: 5 entries
  - Surveys/baselines: 12 entries

---

## 9. Recommended Next Steps

1. **Semantic Scholar API sweep:** Query for "agentic LLM" OR "agent reinforcement learning" OR "model context protocol" OR "AI coding agent" with date filter Nov 2025+. Will likely surface 50–100 additional papers I haven't found via web search.

2. **Forward citation tracking from Plaat et al.:** Who has cited arXiv:2503.23037? These are the papers most directly extending the baseline work.

3. **GitHub repo analysis:** Stars/forks/activity for Claude Code, Gemini CLI, OpenClaw, OpenCode, Aider — quantitative adoption data.

4. **Conference accepted paper lists:** Check NeurIPS 2025 proceedings, ICLR 2026 accepted papers, ICML 2026 accepted papers for agent-related work.

5. **Fill gaps in Section 7:** Especially VLAs, GUI agents, memory systems, and mechanistic interpretability — these are thinner in my collection.

6. **Interview/survey planning:** If you want practitioner data, design the survey instrument now while the literature collection crystallizes the questions.
