# Agentic LLMs in the Wild: Reasoning, Acting, Interacting, and Operating

**A Survey Update for 2026**

nafSadh · March 2026

---

## Abstract

Plaat et al.'s "Agentic Large Language Models" (JAIR 2025) organized the field around three capabilities: reason, act, and interact. We revisit this taxonomy thirteen months later and find four structural shifts that demand a reframing rather than an update. First, agentic capabilities are migrating from external scaffolds into model weights via reinforcement learning — the distinction between the LLM and the scaffolding around it is dissolving. Second, software development has become the dominant action domain, with production tools generating over $4.5B in combined annual revenue and benchmarks revealing that real capabilities remain far below headline numbers. Third, agent interaction has transformed from a research topic into an infrastructure and governance problem, with standardized protocols (MCP, A2A) now governed by a consortium of six competing AI companies. Fourth, safety and security have grown from a paragraph of future work into the field's central engineering challenge, with evidence that the protocol layer itself amplifies attacks by 23–41% and that all tested defenses can be bypassed at 78%+ rates.

We introduce a fourth taxonomy axis — **Operate** — covering security, reliability, and the economics of running agents in production. We also identify a cross-cutting **Skills** layer: a portable configuration standard (SKILL.md) that works across eight competing vendor tools, representing the first genuine cross-vendor standard in agentic AI. Our analysis is based on 28 papers read from PDFs (~460 pages), six identified through forward citation sweeps, supplemented by industry reports and protocol documentation. We provide honest per-paper coverage statistics and distinguish between what we read, what we extracted, and what we merely cataloged. The paper is accompanied by interactive deep-dives for each section, published at read.sadh.app/ai/agentic-lm-survey/.

---

## 1. Introduction

In March 2025, Plaat, van Duijn, van Stein, Preuss, van der Putten, and Batenburg published "Agentic Large Language Models, a survey" — an elegant organization of the emerging field around three capabilities: reason, act, and interact. The taxonomy captured a virtuous cycle: reasoning feeds better actions, actions generate training data, interactions produce emergent behaviors that loop back into improved reasoning. The paper was published in JAIR and became a reference point for the field.

Thirteen months later, the landscape has shifted in ways the paper either couldn't anticipate or only gestured at. The shifts are not incremental — they require a reframing of what agentic AI is, what it does, and what problems it creates.

### 1.1 Four Structural Shifts

**Shift 1: Scaffold to Weights.** Plaat et al. treated agentic capabilities as largely external to the model: Chain-of-Thought as prompting, tool use as API scaffolding, memory as retrieval pipelines. The biggest conceptual change since their paper is that planning, tool use, memory, and reflection are being internalized into model weights via reinforcement learning. DeepSeek-R1 (January 2025) demonstrated that self-reflection behavior could emerge from GRPO training without being explicitly programmed. By early 2026, the Agentic RL Landscape survey synthesizes over 500 works documenting this migration across every capability category. The formal distinction — traditional RLHF as a degenerate single-step MDP versus agentic RL as a temporally extended POMDP — is not a gradual evolution. It is a categorical change in the mathematical structure of the learning problem.

**Shift 2: Coding as the Dominant Action Domain.** Plaat et al.'s "Act" category focused on robotics, hypothetical assistants, and tool-use demonstrations. By March 2026, the dominant manifestation of agentic AI is software development. Claude Code reached $2.5B ARR by March 2026 (up from $1B in November 2025). Cursor surpassed $2B ARR — among the fastest-scaling SaaS products in history. Google launched Antigravity, an agent-first IDE. The SWE-Bench benchmark family fragmented usefully into five variants testing different failure modes. Self-improving agents (Live-SWE-agent at 77.4% on SWE-bench Verified, with zero offline training cost) outperform all hand-crafted scaffolds. Yet the most striking finding is the gap between benchmarks and reality: GPT-5 drops from 65% on single-issue tasks to 21% on software evolution tasks, and engineers report using AI in 60% of their work but fully delegating only 0–20%.

**Shift 3: Interaction as Infrastructure.** Plaat et al.'s "Interact" category treated multi-agent systems as a research topic — Generative Agents, social simulations, game-playing. What actually happened: the Model Context Protocol (MCP), launched by Anthropic in November 2024, crossed 97 million monthly SDK downloads by February 2026. Google's Agent-to-Agent protocol (A2A) became the de facto standard for agent-to-agent communication. The Linux Foundation's Agentic AI Foundation (AAIF) — co-founded by OpenAI, Anthropic, Google, Microsoft, AWS, and Block in December 2025 — now governs both. The questions that matter are no longer "can agents collaborate?" but "what protocols do agents speak, who governs the standards, and what happens when a malicious agent enters the network?"

**Shift 4: Operate as the Central Challenge.** Plaat et al. mentioned safety as future work. By March 2026, it is the defining engineering challenge. The first formal security analysis of MCP demonstrates that the protocol's architectural choices amplify attack success rates by 23–41% compared to non-MCP integrations. A meta-analysis of 78 studies shows that all tested defense mechanisms can be bypassed at 78%+ rates when adaptive attack strategies are employed. Real-world incidents — 21,000+ exposed agent gateways, 14 malicious skills uploaded to a marketplace within 72 hours, an agent autonomously creating a dating profile without user consent — demonstrate the gap between capability and safety. This gap is not a detail to be addressed later. It is the central problem.

### 1.2 Why a Reframing, Not an Update

These four shifts could theoretically be accommodated within Plaat et al.'s original three-axis taxonomy. One could expand "Reason" to include RL internalization, expand "Act" to include coding, expand "Interact" to include protocols. But this would miss the most important development: the emergence of a fourth axis that Plaat et al. explicitly deferred.

The safety, security, reliability, and economics of running agents in production constitute a coherent category with its own literature, its own benchmarks, its own engineering challenges, and its own failure modes. We call this **Operate**. It is not a subcategory of any of the original three axes. Prompt injection is not a reasoning failure. MCP security vulnerabilities are not an interaction design pattern. Supply chain attacks on skill marketplaces are not an action model limitation. These problems require dedicated architectural solutions — protocol-level changes, defense-in-depth frameworks, trust-tiered execution models — that do not fit naturally within reason, act, or interact.

We therefore propose a four-axis taxonomy: **Reason, Act, Interact, Operate**, plus a cross-cutting Skills layer. The first three axes extend Plaat et al.'s categories with the 2025–2026 evidence. The fourth is new. The cross-cutting layer — SKILL.md, CLAUDE.md, AGENTS.md — represents the quiet emergence of vendor-neutral agent configuration standards that may matter more for practical adoption than any protocol or model improvement.

---

## 2. Taxonomy, Scope, and Method

### 2.1 The Four Axes

| Axis | Plaat et al. (2025) | This Survey (2026) |
|------|--------------------|--------------------|
| **Reason** | Reasoning, reflection, retrieval | Model-native reasoning via RL; POMDP formalization; scaling laws; efficiency as training objective |
| **Act** | Action models, robots, tools | Agentic coding (benchmarks, self-improving agents, production tools); the 60/20 paradox |
| **Interact** | Multi-agent systems, social simulation | Protocol standards (MCP/A2A); AAIF governance; flow engineering; difficulty-aware routing |
| **Operate** | *(future work)* | MCP security; prompt injection; data over-exposure; skill supply chain; platform vulnerability |
| **Cross-Cut** | *(not covered)* | SKILL.md portability; configuration convergence; five-layer stack; self-extension vs pre-configuration |

### 2.2 Paper Selection

We began with Plaat et al.'s survey (arXiv:2503.23037, v3 November 2025) as our baseline and collected 85 candidate sources through keyword search across arXiv, Semantic Scholar, and industry reports. From these, we downloaded and text-extracted 22 papers as PDFs. We then conducted a forward citation sweep via the Semantic Scholar API on our six most-cited papers, identifying 6 additional papers published between December 2025 and March 2026 that our initial collection had missed. Total: 28 papers read from PDFs, approximately 460 pages of text.

We are explicit about reading depth. Three papers were read cover-to-cover (Drammeh's orchestration study, Maloyan's MCP security analysis, and Maloyan's prompt injection SoK — all short papers where the full text was essential). Nine papers were read at 40–80% (typically abstract, introduction, method, and results). The remaining sixteen were read at 11–26% (abstract, introduction, and key figures/tables). This is a first-pass survey, not a systematic literature review. We compensate for depth with honesty: every claim in this paper can be traced to a specific page range in a specific PDF, documented in our per-paper coverage tables.

Industry sources — the Anthropic 2026 Agentic Coding Trends Report, AAIF governance documentation, Cisco and Mitra protocol analyses, Acronis and Censys security reports, the OWASP Top 10 for LLM Applications — are treated as first-class evidence alongside academic papers. The field is moving too fast for a purely academic literature review to capture what is actually happening in production.

### 2.3 What We Do Not Cover

We do not cover GUI agents (OSWorld, WebArena), embodied agents (VLAs, robotics), or scientific discovery agents — all areas where Plaat et al. and the Self-Evolving Agents Survey (TMLR 2026) provide recent coverage. We focus on the gaps their surveys leave: the coding explosion, the protocol stack, and the security crisis.

---

## 3. REASON — Model-Native Reasoning and Agentic RL

The most consequential shift in agentic AI between early 2025 and early 2026 is not any single model release. It is a change in where agent capabilities live. In 2024, an agent's ability to plan, use tools, manage memory, and reflect was implemented as external code — prompt templates, retrieval pipelines, orchestration logic. By early 2026, these capabilities are increasingly being internalized into model weights via reinforcement learning.

### 3.1 The POMDP Formalization

Zhang et al.'s Agentic RL Landscape survey (TMLR, January 2026; 25 authors, 14 institutions, 95 pages synthesizing 500+ works) provides the definitive formalization. The core distinction: traditional RLHF is a degenerate single-step MDP (horizon T=1, deterministic transitions, single scalar reward). Agentic RL is a temporally extended POMDP (horizon T>1, stochastic transitions via tool use, step-wise rewards, partial observability).

The action space decomposes into text actions (reasoning steps — deterministic) and structured actions (tool calls — stochastic). The RL algorithm must handle both within a single trajectory. This is not a gradual extension of RLHF. It is a categorically different mathematical problem.

Agent-R1 (USTC, November 2025) makes this concrete with a clean three-level architecture taxonomy: Workflows (human-designed routing) → Agentic Workflows (ReAct-style loops, still prompt-engineered) → Fully Autonomous Agents (no predefined workflow, end-to-end RL, proactive environment interaction). The field is moving from the second level to the third.

### 3.2 Scaling Laws and Their Limits

Tan et al. (December 2025) provide the first systematic scaling laws for RL post-training, studying 63 models across the full Qwen2.5 series (0.5B to 72B). The core formula — log L(N,X) = -k(N)·log X + E(N) — reveals that learning efficiency k(N) saturates as model size increases. Larger models are more efficient but with diminishing returns. A hypothetical 720B model wouldn't be proportionally better than 72B for RL training.

The practically important finding: data reuse is surprisingly effective. Performance is governed by total optimization steps, not unique data volume. Teams don't need massive unique RL datasets — a well-curated small set trained longer can match.

### 3.3 Efficiency as a Training Objective

Agent-Omit (HKUST/DiDi, February 2026) addresses a practical problem: 97.3% of agent token cost comes from thoughts (45.1%) and observations (52.2%), not actions (2.7%). The framework trains agents to adaptively skip unnecessary reasoning via omission-aware RL. Agent-Omit-8B matches seven frontier LLM agents while achieving the best efficiency trade-off.

This represents a conceptual shift from "maximize accuracy" to "maximize accuracy per token" — signaling production maturity.

### 3.4 Practitioner Recipes

Yu et al.'s "Demystifying RL" (NUS/Princeton/UIUC, October 2025) provides the practitioner's guide. Three key findings that defy conventional wisdom: real end-to-end trajectories dramatically outperform synthetic data for SFT initialization; exploration-friendly RL techniques (clip higher, entropy management) matter most; and a deliberative strategy with fewer tool calls outperforms both frequent tool calling and verbose self-reasoning. With proper recipes, 4B models achieve competitive results.

### 3.5 Emergent Training Paradigms

Two forward-citation papers extend the REASON section. Agentic Critical Training (UMD, March 2026) trains agents to judge which action is better under the current state via RL — producing genuine self-reflection rather than imitating pre-constructed reflections. The striking result: despite being trained purely on action-level supervision, ACT also improves MATH-500 and GPQA-Diamond without any reasoning-specific training data, suggesting that learning to evaluate actions serves as a general mechanism for enhancing reasoning.

OpenClaw-RL (Princeton/NUS, March 2026) observes that every deployed AI agent already discards the training signal it needs to improve. Next-state signals carry both evaluative (how well the agent performed) and directive (how it should change) information. The framework is fully asynchronous: policy serving, judging, and training run concurrently with zero coordination overhead.

### 3.6 Section Synthesis

Four themes emerge. First, the scaffold-to-weights migration is real and comprehensive — planning, tool use, memory, self-improvement, and context management are all moving from prompt engineering to RL-trained capabilities. Second, training stability (entropy collapse, reward hacking, mode collapse) is the field's central engineering challenge, with ARLArena/SAMPO and algorithmic recipes emerging as responses. Third, real trajectories beat synthetic data for SFT, and data reuse is effective for RL — invest in quality cold-start data, then RL with reuse. Fourth, efficiency is becoming a first-class training objective, not just an operational concern.

---

## 4. ACT — Agentic Coding and Tool Use

This is the most dramatically transformed axis since Plaat et al. In their survey, acting meant robotics, hypothetical assistants, and tool-use demos. By March 2026, the dominant action domain is software development — agents writing, testing, debugging, and deploying code at production scale.

### 4.1 The Benchmark Reality Check

The SWE-Bench benchmark family has fragmented into five variants, each addressing a different failure mode of the original.

SWE-Bench Verified has seen remarkable progress: Claude Opus 4.5 leads at 80.9% (March 2026), up from ~65% a year ago, with Gemini 3.1 Pro at 80.6% and MiniMax M2.5 (open-weight) at 80.2%. Agent frameworks add 10-20 points over raw model scores. However, these headline numbers mask deeper challenges.

SWE-Bench Pro (Scale AI, November 2025) scales to enterprise: 1,865 problems from 41 repositories spanning Python, JavaScript, TypeScript, and Go. Three-tier contamination resistance (public, commercial from purchased startup codebases, held-out). Average reference solution: 107.4 lines across 4.1 files. GPT-5.3-Codex leads at 56.8%; Claude Opus 4.5 scores 45.9% on the SEAL leaderboard with standardized scaffolding. The Verified-to-Pro gap (80.9% vs 45.9%) is the clearest evidence of the benchmark-to-reality gulf. Without human augmentations (requirements and interface specifications), GPT-5 drops from 25.9% to 8.4% — evidence that agents fail not because they can't code, but because they can't infer intended behavior from ambiguous descriptions.

SWE-EVO (FPT/Melbourne, January 2026) tests what SWE-Bench can't: continuous software evolution. 48 tasks requiring agents to interpret release notes and evolve codebases across versions. GPT-5 drops from 65% on SWE-Bench Verified to 21% on SWE-EVO — a 44 percentage-point gap that reveals the frontier problem. Fix Rate, a new metric for partial progress, shows agents make meaningful headway (27.64% of failing tests fixed) even when they don't fully solve the task.

Three complementary papers address SWE-Bench's structural problems. SWE-bench Live (Microsoft) automates benchmark construction for continuous updates from 93 repositories, revealing a performance gap suggesting overfitting to the static benchmark. Saving SWE-Bench (Microsoft, CAIN '26) transforms formal GitHub issues into realistic user queries via telemetry analysis, revealing 20–50% overestimation on public benchmarks. UTBoost (CUHK-SZ/UIUC) augments test suites and finds 345 erroneous patches incorrectly labeled as passing, affecting 40.9% of SWE-Bench Lite leaderboard entries.

The collective message: reported capabilities on SWE-Bench are inflated by data contamination, over-specified task descriptions, insufficient test cases, and saturation on isolated tasks. The real state of the art is considerably below the headline numbers.

### 4.2 Self-Improving Agents

The most compelling direction in agentic coding is agents that improve themselves.

Live-SWE-agent (UIUC, November 2025) starts with the most basic scaffold — bash tools only — and creates custom tools on the fly as it solves problems. The reflection step is critical: without explicit prompting to consider tool creation, agents don't do it. With it, they generate 3.28 tools per problem on average, achieving 77.4% on SWE-bench Verified — state-of-the-art with zero offline training cost. Critically, there is a model capability threshold: Claude 4.5 Sonnet gains +22.6% relative improvement, but GPT-5-Nano actually degrades by 68.2%.

Self-Play SWE-RL (Meta FAIR/UIUC, December 2025) — identified through our forward citation sweep — is the missing link between Section 3's RL training and this section's coding agents. A single LLM plays dual roles: bug injector (introduces bugs into real codebases, weakens tests to hide them) and bug solver (finds and fixes bugs given only the buggy codebase). No human-curated issues, no human test suites. SSR achieves +10.4 points on SWE-bench Verified and +7.8 on SWE-Bench Pro, outperforming the human-data RL baseline throughout the entire training trajectory.

RepoNavigator (PKU/Baidu, January 2026) demonstrates that a single execution-aware tool — "jump" to a symbol's definition — plus RL training outperforms multi-tool agents with much larger models. The 7B model beats 14B baselines; 14B surpasses 32B competitors; 32B exceeds GPT-5 on most metrics. This is perhaps the strongest evidence that the right tool design plus RL can overcome raw model scale.

### 4.3 The Production Landscape

The agentic coding tool market has exploded: Claude Code ($2.5B ARR by March 2026, up from $1B in November 2025), Cursor ($2B+ ARR, valued at $50B), Antigravity (Google, agent-first IDE), Codex CLI (OpenAI, local-first sandbox), Gemini CLI (1M token context, free tier, 96K+ GitHub stars), OpenClaw (100K+ stars, general-purpose agent). 84% of developers report using multiple AI coding tools simultaneously. Each makes different bets about the future of development. The axes of differentiation: CLI vs IDE, model lock-in vs flexibility, single-agent vs multi-agent, specialized coding vs general-purpose.

Anthropic's 2026 Agentic Coding Trends Report identifies eight trends. The central finding: engineers use AI in approximately 60% of their work but fully delegate only 0–20%. This is not a failure — it reflects the nature of effective collaboration. Approximately 27% of AI-assisted work consists of tasks that wouldn't have been done otherwise. AI isn't just replacing work — it's creating new categories of work.

### 4.4 Section Synthesis

The benchmark family paints a more honest picture than any single number: enterprises remain below 45%, evolution tasks below 21%, and test adequacy problems inflate all reported results by 20–50%. Self-improving agents (Live-SWE-agent, SSR, RepoNavigator) consistently outperform hand-crafted scaffolds — the trend is clear: let agents learn and create their own tools rather than engineering them. And the 60/20 paradox (60% AI usage, 0–20% full delegation) defines the actual human-AI collaboration pattern for years to come.

---

## 5. INTERACT — Protocols and Multi-Agent Systems

Plaat et al.'s "Interact" category treated multi-agent systems as a research topic. By March 2026, interaction has become primarily an engineering and governance problem.

### 5.1 The Protocol Stack

Four protocols address agent interoperability at different layers. MCP (Anthropic, November 2024) standardizes agent-to-tool communication via JSON-RPC with four primitives: Tools, Resources, Prompts, and Sampling. A2A (Google, April 2025) enables agent-to-agent discovery and task delegation via Agent Cards — high-level capability descriptors that expose what an agent can do without revealing implementation. ACP (IBM, merged into A2A August 2025) added REST-native multimodal messaging. ANP enables decentralized peer-to-peer agent networking via W3C Decentralized Identifiers.

The emerging consensus, articulated by Cisco and others, is that these protocols compose rather than compete. MCP operates at the tool/resource layer (like HTTP for content). A2A operates at the agent discovery and routing layer (like TCP for reliable delivery). An agent uses A2A to discover and delegate to a specialist, which then uses MCP to invoke specific tools. Neither replaces the other.

LangGraph v0.2 (January 2026) added both as first-class protocol targets. MCP has crossed 97 million monthly SDK downloads, with the server ecosystem growing from 1,000 servers in early 2025 to over 10,000 active servers by March 2026. A2A reached v0.3.0 with extension support for vendor-specific features and concrete protocol bindings (JSON-RPC, gRPC, HTTP/REST).

### 5.2 Governance

The Linux Foundation's Agentic AI Foundation (AAIF), launched December 2025, represents an unprecedented act of co-governance. Six directly competing companies — OpenAI, Anthropic, Google, Microsoft, AWS, and Block — agreed to jointly steward the interoperability standards their agents use. MCP, Goose (Block's open-source agent), and Agents.md (OpenAI's agent configuration standard) were donated. This compressed the kind of standards process that took the early web years into months.

### 5.3 Multi-Agent Orchestration

Drammeh's orchestration study (January 2026) provides the cleanest empirical evidence for multi-agent systems. 348 controlled trials comparing single-agent versus multi-agent on an identical incident scenario with TinyLlama (1B parameters). Multi-agent achieves 100% actionable recommendations versus 1.7% for single-agent, with 80× specificity improvement and zero quality variance. Both systems take approximately 40 seconds. The value is deterministic quality, not speed. The reframing: multi-agent orchestration isn't a performance optimization — it's a production-readiness requirement.

DAAO (WWW '26) introduces difficulty-aware routing: a VAE estimates query difficulty without manual labels, an operator allocator selects which reasoning tools to activate, and an LLM router pairs each operator with the optimal model from a heterogeneous candidate set. Result: +3.2–10.2% accuracy at 41% of inference cost. The future isn't one big model doing everything — it's orchestrated fleets of specialized models, dynamically routed by difficulty.

### 5.4 The Flow Engineering Shift

The industry has moved from open-ended multi-agent chat loops toward explicit workflow graphs. LangGraph exemplifies this: agent execution as graph traversal with explicit state, typed transitions, and developer-defined guardrails. The motivation is practical: developers specify state transitions and guardrails; models fill in local decisions. This trades theoretical capability for debuggability, checkpointing, and human approval gates.

### 5.5 Section Synthesis

Interaction is now an infrastructure problem (protocols, governance, adoption metrics), not a research question (can agents collaborate?). The compose-not-compete pattern (MCP + A2A at different layers) mirrors early internet protocol development. Flow engineering prioritizes reliability over autonomy. And heterogeneous routing (DAAO) demonstrates that matching different LLMs to different subtasks by difficulty produces better results at lower cost.

---

## 6. OPERATE — Safety, Security, Reliability

This is the entirely new axis. Plaat et al. deferred safety as future work. By March 2026, the evidence base demands dedicated treatment.

### 6.1 MCP Amplifies Attacks

Maloyan and Namiot's "Breaking the Protocol" (January 2026) is the first study to isolate MCP-specific security effects by comparing MCP-integrated agents against non-MCP baselines with identical tool semantics. Three architectural vulnerabilities: absence of capability attestation (servers self-declare permissions without cryptographic proof), bidirectional sampling without origin authentication (servers inject prompts indistinguishable from user input), and implicit trust propagation in multi-server configurations (no isolation between servers sharing a context window).

Across 847 attack scenarios on five MCP servers with three LLM backends: MCP amplifies attack success by 23–41% depending on attack type. Cross-server propagation — impossible without MCP — achieves 61.3% attack success. Sampling-based injection reaches 67.2%.

The proposed defense, AttestMCP, adds capability attestation, message authentication, origin tagging, and isolation enforcement as backward-compatible protocol extensions. It reduces overall attack success from 52.8% to 12.4% with 8.3ms median latency overhead. The residual 12.4% reflects fundamental LLM limitations that cannot be solved at the protocol layer.

SMCP (HUST, February 2026) independently identifies the same architectural gaps and proposes complementary solutions: unified identity management, mutual authentication, security context propagation, fine-grained policy enforcement, and comprehensive audit logging. A production system would likely need both — AttestMCP for trust establishment, SMCP for runtime governance.

MCPSecBench (AIS2Lab, February 2026) provides the first systematic benchmark: 17 attack types across 4 attack surfaces, tested across Claude Desktop, OpenAI GPT-4.1, and Cursor with 15 trials per attack per model. Over 85% of identified attacks successfully compromise at least one platform. Current protection mechanisms achieve less than 30% success rate. Meanwhile, MCPGuard's analysis of 700+ open-source MCP servers found critical vulnerabilities in 78% of implementations, and security researchers filed 30+ CVEs targeting MCP infrastructure in January-February 2026 alone.

### 6.2 All Defenses Fail

The Prompt Injection SoK (Maloyan and Namiot, January 2026) synthesizes 78 studies and catalogs 42 distinct attack techniques across a three-dimensional taxonomy: delivery vectors (direct, indirect, protocol-level), attack modalities (syntactic, semantic, multimodal), and propagation behaviors (contained, persistent, viral).

The most consequential finding: every tested defense mechanism — Protect AI, PromptGuard, PIGuard, Model Armor, TaskTracker, instruction detection — shows less than 12% attack success in reported evaluations but 78–93% when adaptive optimization (gradient descent, RL, random search) is applied. The gap is devastating. The security community must treat prompt injection as a first-class vulnerability requiring architectural mitigation, not ad-hoc filtering.

Platform comparison: Claude Code achieves the lowest vulnerability rating (Low) through aggressive sandboxing and permission constraints. Cursor is rated Critical — high across all three attack vectors. Copilot and Codex CLI are High. Gemini CLI is Medium. The ranking inversely correlates with capability permissiveness.

### 6.3 Data Over-Exposure

AgentRaft (Sun Yat-sen, March 2026) — identified through our forward citation sweep — defines a novel risk class: Data Over-Exposure (DOE). Unlike prompt injection (adversarial), DOE is systemic: broad tool design combined with LLMs' lack of contextual privacy awareness causes agents to transmit sensitive data beyond what users intend or tasks require.

Testing 6,675 real-world MCP tools: 57.07% of potential tool call chains exhibit unauthorized sensitive data exposure. 65.42% of transmitted data fields are identified as over-exposed. This is the baseline condition — no adversarial attack needed. More than half of all tool interaction paths leak data by default.

### 6.4 The Skill Supply Chain

Two concurrent studies (October 2025 – February 2026) characterize skill ecosystem security at scale. Liu et al. analyzed 42,447 skills from two major marketplaces: 26.1% contain at least one vulnerability across 14 distinct patterns. A behavioral verification of 98,380 skills confirmed 157 malicious skills with 632 vulnerabilities, falling into two archetypes: "Data Thieves" (credential exfiltration) and "Agent Hijackers" (instruction manipulation). Skills bundling executable scripts are 2.12× more likely to contain vulnerabilities.

The OpenClaw case study grounds this: 14 malicious skills uploaded to ClawHub within 72 hours of launch. One reached the front page before removal. 21,000+ OpenClaw gateways exposed to the public internet. Chinese authorities restricted it on government computers. The skill ecosystem faces npm-style supply chain risks but worse — skills have direct system access via the agent.

### 6.5 Section Synthesis

Both MCP security papers independently conclude that the protocol's weaknesses are architectural, not implementation-specific. Patching individual CVEs won't fix the fundamental issues. The skill supply chain lacks the security tooling that took package managers years to develop. And the security-capability tradeoff is the central design challenge: Claude Code's safety comes from restricting what agents can do; Cursor's vulnerability comes from enabling maximum autonomy. The winning approach will find an asymmetric advantage — high capability with architectural security, not capability restriction.

---

## 7. Cross-Cutting — Skills, Configuration, and the Portable Agent Layer

The most surprising development in the agentic AI ecosystem isn't any single model, benchmark, or protocol. It's the quiet emergence of a portable configuration layer that works across competing vendor tools.

### 7.1 The SKILL.md Format

A SKILL.md file is a Markdown document with YAML frontmatter that teaches an AI agent how to perform a specific workflow. The same file works in `.claude/skills/`, `.gemini/skills/`, `.cursor/skills/`, and `.codex/skills/` without modification. The format decouples skill content from tool-specific invocation conventions.

The SoK on Agentic Skills (UTS/CSIRO, February 2026) provides the formal definition: S = (C, π, T, R) — applicability condition, executable policy, termination condition, reusable interface. This four-tuple distinguishes skills from tools (atomic, stateless), plans (one-time, session-scoped), and prompt templates (static text, no termination logic).

The Agent Skills Survey (Zhejiang, February 2026) documents the progressive disclosure architecture: Level 1 metadata (~30 tokens/skill) always loaded as a menu; Level 2 instructions (200–2K tokens) loaded on trigger; Level 3 resources (scripts, references) loaded on demand. This prevents context bloat while maintaining access to deep procedural knowledge.

### 7.2 The Skills Ecosystem

Antigravity Awesome Skills (v8.6.0, March 2026) ships 1,300+ curated skills across eight tools. 22,000+ GitHub stars. Official contributions from Anthropic, Vercel Labs, OpenAI, Supabase, Microsoft, Google DeepMind, Sentry, Trail of Bits, Expo, and Hugging Face. Universal installation: `npx antigravity-awesome-skills --claude` (or `--gemini`, `--cursor`, `--codex`). The broader ecosystem has grown dramatically: SkillsMP marketplace hosts 500,000+ agent skills, agentskill.sh indexes 44,000+ with two-layer security scanning, and the format now works across 19 supported agents. Spring AI (January 2026) brought Agent Skills to the Java ecosystem, signaling enterprise maturation beyond the original developer-tool niche.

The SoK identifies seven design patterns: metadata-driven progressive disclosure, code-as-skill, workflow enforcement, self-evolving libraries, hybrid NL+code macros, meta-skills (skills that create skills), and plugin/marketplace distribution. Each carries distinct risks — from metadata poisoning (Pattern 1) to recursive error amplification (Pattern 6) to malicious packages (Pattern 7, the ClawHavoc campaign).

### 7.3 The Configuration Convergence

Per-project agent configuration is converging under different filenames: CLAUDE.md (Anthropic), AGENTS.md (OpenAI/AAIF), `.cursorrules` (Cursor), `.github/copilot-instructions.md` (GitHub). All define coding standards, workflow constraints, tool permissions, and project context. The skill layer (SKILL.md) achieved format unification. The config layer hasn't — yet.

Pi's self-extension philosophy (Armin Ronacher, OpenClaw engine) takes the opposite approach: no MCP, no skill marketplace — the agent extends itself through code. This parallels Live-SWE-agent's approach from Section 4 and is validated empirically (77.4% vs hand-crafted scaffolds). But the OpenClaw security incidents from Section 6 demonstrate what happens when self-extension meets adversarial conditions.

### 7.4 The Five Configuration Layers

Across the full survey, five distinct layers have emerged for agentic AI:

1. **Model Config** (system prompt): Provider-defined, always loaded, highest trust
2. **Project Config** (CLAUDE.md / AGENTS.md): Team-defined, per-repo, version-controlled
3. **Skills** (SKILL.md): Community-contributed, cross-project, on-demand loading
4. **Tools** (MCP servers): Developer-configured, per-integration, OAuth + attestation
5. **Agent-to-Agent** (A2A Agent Cards): Cross-organizational discovery, capability-based routing

Trust decreases as you move down the stack. Security requirements increase accordingly. The stack emerged organically — no one designed it as a unified architecture — but the layering is now clear enough to be formalized.

---

## 8. Synthesis and Research Agenda

### 8.1 Five Findings

**Finding 1: The scaffold-to-weights migration is the defining paradigm shift.** Across every capability category — planning, tool use, memory, self-improvement, context management — the trend is identical: from external prompt engineering to RL-trained model capabilities. This is not aspirational. It is documented across 500+ works synthesized in the ARL Landscape survey, validated empirically in Agent-R1, scaling law studies, and training recipe papers. The POMDP formalization provides the mathematical foundation. The question is no longer whether this migration will happen but how far it will go — the mechanistic debate (does RL amplify existing capabilities or create genuinely new ones?) remains unresolved and fundamental.

**Finding 2: Self-improvement outperforms hand-crafted engineering.** Live-SWE-agent (self-evolving scaffolds, 77.4%), Self-Play SWE-RL (self-play training data, +10.4 points), RepoNavigator (single tool + RL beats multi-tool with larger models) — each demonstrates independently that letting agents learn, create, or discover their own capabilities produces better results than pre-configuring them. The cost advantage is equally striking: Live-SWE-agent has zero offline training cost versus $22,000 for DGM. But there is a minimum capability threshold: small models (GPT-5-Nano) actively degrade with self-improvement — the ability to self-improve is itself an emergent capability.

**Finding 3: Real capabilities are far below headline numbers.** The SWE-Bench family reveals systematic overestimation: 20–50% from benchmark mutation (Saving SWE-Bench), 40.9% of leaderboard entries affected by test inadequacy (UTBoost), 65%→21% when moving from single issues to evolution tasks (SWE-EVO), and <45% on enterprise-grade problems (SWE-Bench Pro). Engineers' 60/20 paradox (60% AI usage, 0–20% full delegation) confirms this: the technology is deeply useful but not autonomously reliable.

**Finding 4: Safety is an architectural problem, not a filtering problem.** MCP amplifies attacks by 23–41%. MCPSecBench finds 85%+ of identified attacks compromise at least one platform, with current protections achieving less than 30% success. All tested defenses fail at 78%+ against adaptive attacks. 57.07% of MCP tool chains leak data by default. 26.1% of community skills contain vulnerabilities. 78% of open-source MCP servers have critical vulnerabilities. These are not edge cases or theoretical risks — they are the baseline condition of deployed systems. The analogy is SQL injection: the solution was not better input filtering but architectural change (parameterized queries). Prompt injection likely requires an equivalent paradigm shift.

**Finding 5: Portability is happening bottom-up, not top-down.** The SKILL.md format, CLAUDE.md/AGENTS.md convergence, and the five-layer configuration stack emerged from community adoption, not standards bodies. 1,300+ curated skills work across eight competing vendor tools, while the broader ecosystem exceeds 500,000 skills across marketplaces and registries. The format now works across 19 supported agents. Official contributions come from companies that compete on models and IDE features but cooperate on skill definitions. Spring AI's adoption brought the pattern to the Java enterprise ecosystem. This mirrors how JSON became a standard — through adoption, not committee.

### 8.2 What Plaat et al. Got Right

The Reason/Act/Interact taxonomy remains the correct conceptual backbone. The virtuous cycle they identified — reasoning feeds better actions, actions generate training data, interactions produce emergent behaviors — is exactly what we observe in Self-Play SWE-RL (where agents generate their own training data through action), in multi-agent orchestration (where interaction produces deterministic quality that single agents cannot achieve), and in the scaffold-to-weights migration (where reasoning capabilities bootstrapped from prompting become RL-trained model features).

Their research agenda was prescient: they flagged hallucination accumulation in multi-step reasoning, emergent behavior stability, knowledge distillation, and the open question of internal self-reflection. All four are active research areas with significant 2025–2026 progress.

### 8.3 What Plaat et al. Missed

The protocol layer barely existed when they wrote. The production tool ecosystem was nascent. The security evidence base was thin. Most critically, they treated safety as a closing paragraph rather than a central axis. The evidence now demands that safety, security, reliability, and economics receive dedicated architectural treatment — hence our fourth axis.

They also missed the skills/configuration layer entirely. This is understandable — SKILL.md, CLAUDE.md, and Antigravity Awesome Skills emerged after their last revision. But this portable agent layer may ultimately matter more for adoption than any protocol or model improvement, because it is the layer that individual developers and teams actually touch daily.

### 8.4 Research Agenda

**Open Problem 1: Architectural Security for Agent Protocols.** AttestMCP and SMCP propose complementary protocol-level defenses, but neither has been adopted into the MCP specification. The AAIF governance structure exists to make such changes. The research question: can we design agent protocol security that is as effective and transparent as TLS for web traffic?

**Open Problem 2: The Long-Horizon Gap.** SWE-EVO's 65%→21% drop is the clearest evidence that sustained multi-file reasoning remains unsolved. 80% of software engineering effort is maintenance and evolution, not greenfield development. Closing this gap requires agents that maintain coherent plans across dozens of files and hundreds of changes — a capability no current model demonstrates reliably.

**Open Problem 3: Skill Ecosystem Governance.** With 26.1% of community skills containing vulnerabilities, the skill layer needs supply chain security at the level of package managers — signing, sandboxing, behavioral verification, permission scoping. But the tooling is nascent and the adoption pressure is intense.

**Open Problem 4: The Mechanistic Debate.** Does RL merely amplify capabilities that exist in pretrained weights (the "sharpening" view), or does it create genuinely new reasoning patterns (the "discovery" view)? The answer determines the ceiling of RL-based agent training and has implications for every other finding in this survey.

**Open Problem 5: Agent Economics.** The 60/20 paradox suggests that agent value comes from collaboration, not replacement. But the economic models (FinOps for agents, cost allocation across heterogeneous model fleets, the pricing of agent-generated code versus human-written code) are entirely undeveloped. DAAO's difficulty-aware routing hints at the approach: match model cost to task difficulty. Formalizing this is critical for enterprise adoption.

---

## 9. Conclusion

Between January 2025 and March 2026, agentic LLMs moved from research demonstrations to production systems generating billions in revenue. This transition exposed both capabilities and limitations that Plaat et al.'s three-axis taxonomy anticipated in structure but not in specifics.

The scaffold-to-weights migration via RL is real and comprehensive. Software development has become the primary arena where agentic capabilities are measured, deployed, and monetized. Interaction has become an infrastructure problem governed by standardized protocols under neutral governance. And safety — the axis Plaat et al. deferred — has become the central challenge: not because agents can't act, but because we can't yet make them act safely.

We add Operate as a fourth axis not because safety was previously unknown, but because the 2025–2026 evidence base is now large enough, specific enough, and alarming enough to demand dedicated architectural treatment. The protocol amplification effect, the comprehensive defense failure, the systemic data over-exposure, and the skill supply chain crisis are not subcategories of reasoning, acting, or interacting. They are a coherent engineering domain with its own problems, its own solutions, and its own research frontier.

The quiet emergence of a portable agent configuration layer — SKILL.md files that work across eight competing tools, per-project configs converging under different names, five configuration layers stacking organically — may be the most practically significant development of all. Standards emerge from adoption, not committee. The agentic AI ecosystem is standardizing from the bottom up, one markdown file at a time.

---

## References

*Primary sources (read from PDFs):*

[1] Plaat, van Duijn, van Stein, Preuss, van der Putten, Batenburg. "Agentic Large Language Models, a survey." JAIR 2025. arXiv:2503.23037.

[2] Zhang et al. "The Landscape of Agentic Reinforcement Learning for LLMs." TMLR Jan 2026. arXiv:2509.02547.

[3] Cheng et al. "Agent-R1: Training Powerful LLM Agents with End-to-End RL." arXiv:2511.14460, Nov 2025.

[4] Tan et al. "Scaling Behaviors of LLM Reinforcement Learning Post-Training." arXiv:2509.25300, Dec 2025.

[5] Ning et al. "Agent-Omit: Adaptive Thought and Observation Omission via Agentic RL." arXiv:2602.04284, Feb 2026.

[6] Yu et al. "Demystifying Reinforcement Learning in Agentic Reasoning." arXiv:2510.11701, Oct 2025.

[7] Wang et al. "OpenClaw-RL: Train Any Agent Simply by Talking." arXiv:2603.10165, Mar 2026.

[8] Zhang et al. "A Survey of Reinforcement Learning for Large Reasoning Models." arXiv:2509.08827, Oct 2025.

[9] Deng, Da et al. "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?" arXiv:2509.16941, Nov 2025.

[10] Thai et al. "SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution." arXiv:2512.18470, Jan 2026.

[11] Zhang et al. "SWE-bench Goes Live!" arXiv:2505.23419, Jun 2025.

[12] Garg et al. "Saving SWE-Bench: Benchmark Mutation for Realistic Agent Evaluation." CAIN '26. arXiv:2510.08996.

[13] Yu et al. "UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench." arXiv:2506.09289, Jun 2025.

[14] Xia et al. "Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?" arXiv:2511.13646, Nov 2025.

[15] Zhang et al. "One Tool Is Enough: RL of LLM Agents for Repository-Level Code Navigation." arXiv:2512.20957, Jan 2026.

[16] Wei et al. "Toward Training Superintelligent Software Agents through Self-Play SWE-RL." arXiv:2512.18552, Dec 2025.

[17] Gao et al. "A Survey of Self-Evolving Agents." TMLR Jan 2026. arXiv:2507.21046.

[18] Ehtesham et al. "A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, ANP." arXiv:2505.02279, May 2025.

[19] Tran et al. "Multi-Agent Collaboration Mechanisms: A Survey of LLMs." arXiv:2501.06322, Jan 2025.

[20] Drammeh. "Multi-Agent LLM Orchestration Achieves Deterministic, High-Quality Decision Support." arXiv:2511.15755, Jan 2026.

[21] Su et al. "Difficulty-Aware Agentic Orchestration for Query-Specific Multi-Agent Workflows." WWW '26. arXiv:2509.11079.

[22] Arunkumar et al. "Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents." arXiv:2601.12560, Jan 2026.

[23] Maloyan, Namiot. "Breaking the Protocol: Security Analysis of the Model Context Protocol." arXiv:2601.17549, Jan 2026.

[24] Hou et al. "SMCP: Secure Model Context Protocol." arXiv:2602.01129, Feb 2026.

[25] Maloyan, Namiot. "Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis." arXiv:2601.17548, Jan 2026.

[26] Lin et al. "AgentRaft: Automated Detection of Data Over-Exposure in LLM Agents." arXiv:2603.07557, Mar 2026.

[27] Jiang et al. "SoK: Agentic Skills — Beyond Tool Use in LLM Agents." arXiv:2602.20867, Feb 2026.

[28] Xu, Yan. "Agent Skills for Large Language Models: Architecture, Acquisition, Security." arXiv:2602.12430, Feb 2026.

[29] Liu et al. "Agentic Critical Training." arXiv:2603.08706, Mar 2026.

*Web research sources (Mar 25, 2026):*

[30a] Yang, Wu et al. "MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols." arXiv:2508.13220, Feb 2026.

*Industry sources:*

[30] Anthropic. "2026 Agentic Coding Trends Report." Jan 2026.

[31] Linux Foundation. "Agentic AI Foundation (AAIF) Launch." Dec 2025.

[32] OWASP. "Top 10 for LLM Applications." 2025 edition.

[33] Willison, S. "The Lethal Trifecta." Jun 2025.

[34] Acronis. "OpenClaw: Agentic AI in the Wild — Security Analysis." Jan 2026.

[35] sickn33/antigravity-awesome-skills. GitHub, v8.6.0, Mar 2026.
