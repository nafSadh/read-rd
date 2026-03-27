# Agentic LLMs in the Wild: Reasoning, Acting, Interacting, and Operating

**Draft v1 — March 24, 2026**

---

## Abstract

Between January 2025 and March 2026, the field of agentic large language models underwent four structural shifts that collectively outpace the framing of existing surveys. Capabilities previously implemented as external prompt scaffolding — Chain-of-Thought, ReAct, Reflexion — are being internalized into model weights via reinforcement learning, transforming the learning problem from a degenerate single-step MDP to a temporally extended POMDP. Software development has become the dominant action domain, with self-improving agents achieving 77.4% on SWE-bench Verified while self-play training on raw codebases eliminates the need for human-curated data entirely. Agent interaction has shifted from a research topic to an infrastructure and governance challenge, with standardized protocols (MCP, A2A) governed by six competing companies under the Linux Foundation's Agentic AI Foundation. Most critically, production deployment has exposed a security surface that the prior survey literature deferred as future work: MCP's architectural choices amplify attack success by 23–41%, all tested defenses are bypassed at 78%+ rates under adaptive attacks, and 57% of MCP tool interaction paths leak sensitive data by default.

This survey updates and extends Plaat et al.'s taxonomy (JAIR 2025) with a fourth axis — **Operate** — covering safety, security, reliability, and the economics of agentic deployment. We synthesize 28 papers read from primary sources across the four categories, identify five cross-cutting themes including the emergence of a portable skills layer, and propose a research agenda grounded in the gap between benchmark performance and production reality.

---

## 1. Introduction

Plaat, van Duijn, van Stein, Preuss, van der Putten, and Batenburg published "Agentic Large Language Models, a survey" in JAIR in 2025, organizing the field around three capabilities: **(1) Reason, (2) Act, (3) Interact** [1]. Their taxonomy was elegant and correct for early 2025. The virtuous cycle they identified — reasoning feeds better actions, actions generate training data, interactions produce emergent behaviors that improve reasoning — remains the conceptual backbone of the field.

But by March 2026, several structural shifts make a pure update insufficient. The paper needs a reframing.

### 1.1 Four Shifts

**The model-native shift.** Plaat et al. treated agentic capabilities as largely external to the model: Chain-of-Thought as prompting, tool use as API scaffolding, memory as retrieval pipelines. The biggest conceptual change since their paper is that planning, tool use, memory, and reflection are being internalized into model weights via reinforcement learning [2, 3]. DeepSeek-R1 (January 2025) demonstrated that self-reflection behavior could emerge from GRPO training without being explicitly taught [4]. By early 2026, a full ecosystem has formed: formal POMDP extensions [5], scaling laws for RL post-training [6], efficiency as a training objective [7], and practitioner recipes [8]. The mathematical distinction is precise: RLHF is a degenerate single-step MDP (horizon T=1, deterministic transitions, single scalar reward); agentic RL is a temporally extended POMDP (horizon T>1, stochastic transitions via tool use, step-wise rewards, partial observability) [2].

**The coding explosion.** Plaat et al.'s "Act" category focused on robotics, hypothetical assistants, and tool-use demonstrations. By March 2026, the dominant action domain is software development. The SWE-Bench benchmark family has fragmented usefully: enterprise-scale [9], long-horizon evolution [10], continuous updates [11], realistic user queries [12], and test adequacy [13]. Self-improving agents achieve 77.4% on SWE-bench Verified with zero offline training cost [14]. Self-play RL on raw codebases eliminates the need for human-curated training data entirely [15]. The tools landscape has exploded: Claude Code ($1B ARR), Antigravity, Cursor ($1.2B ARR), Codex CLI, Gemini CLI (96K+ GitHub stars), OpenClaw (100K+ stars) — each making different bets about developer workflow.

**The protocol infrastructure.** Plaat et al.'s "Interact" category treated multi-agent systems as a research topic — Generative Agents, social simulations, game-playing. What actually happened: standardized protocols (MCP, A2A) now govern how agents communicate with tools and with each other. The Linux Foundation's Agentic AI Foundation (AAIF), co-founded by OpenAI, Anthropic, Google, Microsoft, AWS, and Block in December 2025, provides neutral governance. MCP has crossed 97 million monthly SDK downloads. Multi-agent orchestration has moved from academic design patterns to production architectures, with empirical evidence that decomposition produces deterministic quality impossible with single agents [16].

**The safety imperative.** Plaat et al. mentioned safety as "future work." By March 2026, it is the central engineering challenge. MCP's architectural choices amplify attack success rates by 23–41% compared to equivalent non-MCP integrations [17]. A meta-analysis of 78 studies finds that all tested defenses are bypassed at 78%+ rates under adaptive attacks [18]. 57% of MCP tool interaction paths leak sensitive data by default through unintentional over-exposure [19]. 26.1% of community-contributed agent skills contain security vulnerabilities [20]. The field has moved from "can agents act?" to "can we make them act safely?"

### 1.2 Why a Fourth Axis

These shifts motivate extending the taxonomy from three axes to four:

| Axis | Plaat et al. (2025) | This Survey (2026) |
|------|--------------------|--------------------|
| **Reason** | Reasoning, reflection, retrieval | Model-native reasoning via RL; POMDP formalization; scaling laws; efficiency as training objective |
| **Act** | Action models, robots, tools | Agentic coding (benchmarks, self-improving agents, production tools); the 60/20 paradox |
| **Interact** | Multi-agent systems, social simulation | Protocol infrastructure (MCP/A2A/AAIF); flow engineering; difficulty-aware routing |
| **Operate** | *(deferred as future work)* | MCP security; prompt injection; skill supply chain; data over-exposure; the security-capability tradeoff |

We additionally identify a **cross-cutting** layer: the emergence of portable configuration standards (SKILL.md, CLAUDE.md, AGENTS.md) that work across competing vendor tools and represent the first genuine cross-vendor standard in agentic AI.

---

## 2. Method and Scope

### 2.1 Paper Selection

We began with Plaat et al.'s bibliography and conducted a structured literature search across arXiv, Semantic Scholar, and web sources for publications from November 2025 through March 2026. We prioritized papers that: (a) introduced new formalizations or frameworks, (b) provided quantitative results on established benchmarks, (c) addressed topics absent from Plaat et al., or (d) documented production deployment data.

We then conducted a forward citation sweep on our six most-cited primary sources using the Semantic Scholar API, identifying 6 additional papers published in February–March 2026 that either extended or challenged our initial findings.

### 2.2 Reading Depth

We read 28 papers from downloaded PDFs at varying depth. Three papers were read in full (7–10 pages each). Nine papers were read at 50%+ (abstract, introduction, method, key results, discussion). The remainder were read at 15–40% (abstract, introduction, key results tables). Industry sources (Anthropic 2026 Trends Report, AAIF governance documents, tool documentation, security incident reports) were analyzed via web research. We are explicit about this because the field is moving faster than any individual can read comprehensively, and intellectual honesty about coverage depth is itself a contribution.

### 2.3 What This Survey Is Not

This is not a comprehensive survey in the style of Plaat et al. (85 pages) or the ARL Landscape Survey (95 pages, 500+ works) [2]. It is an *argument paper* that uses 28 primary sources as evidence for a specific thesis: that the field has undergone four structural shifts requiring a fourth taxonomy axis. We sacrifice breadth for depth of argument. Sections that Plaat et al. covered well and that have not structurally changed — embodied agents, GUI navigation, scientific discovery agents — are acknowledged but not re-reviewed.

---

## 3. REASON: From Scaffolds to Weights

The defining paradigm shift between early 2025 and early 2026 is the migration of agent capabilities from external scaffolding into model weights via reinforcement learning.

### 3.1 The POMDP Formalization

The Agentic RL Landscape survey [2] — 25 authors across 14 institutions, published in TMLR January 2026, synthesizing 500+ works — provides the canonical formalization. Traditional RLHF operates as a degenerate single-step MDP: the model sees a prompt, generates a response, and receives a scalar reward. Agentic RL operates as a temporally extended POMDP with the seven-element tuple ⟨S, O, A, P, R, T, γ⟩.

The critical distinction: the action space decomposes into A_text (reasoning steps — deterministic transitions) and A_action (tool calls — stochastic transitions). The RL training loop must handle both types within a single policy. Agent-R1 [5] makes this concrete with a three-level architecture: Workflows (human-designed routing) → Agentic Workflows (ReAct-style iterative loops) → Fully Autonomous Agents (no predefined workflow, end-to-end RL).

### 3.2 Scaling Laws and Saturation

The first systematic scaling law study for RL post-training [6] trained 63 models across the Qwen2.5 series (0.5B to 72B) and discovered a predictive power-law: `log L(N,X) = -k(N)·log X + E(N)`. The critical finding: learning efficiency k(N) saturates as model size increases. Larger models are more efficient but with diminishing returns. Data reuse is surprisingly effective — total optimization steps matter more than unique data volume. This has immediate practical implications: teams don't need massive unique RL datasets.

### 3.3 Efficiency as Training Objective

Agent-Omit [7] quantified the waste: 45.1% of agent token cost comes from thoughts, 52.2% from observations, and only 2.7% from actions. Not all reasoning contributes equally — early planning is critical, but later reasoning becomes redundant once execution is clear. The framework trains agents to adaptively skip unnecessary reasoning via omission-aware RL, achieving frontier-matching performance at a fraction of the token cost with an 8B model.

### 3.4 Practitioner Recipes

"Demystifying RL in Agentic Reasoning" [8] systematically investigated three dimensions: data curation (real end-to-end trajectories dramatically outperform synthetic stitched data), algorithm design (exploration-friendly techniques like "clip higher" and entropy management improve training), and reasoning mode (a deliberative strategy with fewer tool calls outperforms both frequent calling and verbose self-reasoning). With proper recipes, 4B models achieve competitive results on AIME2024, GPQA-Diamond, and LiveCodeBench-v6.

### 3.5 The Training Signal Question

OpenClaw-RL [21] observed that every deployed agent already discards the training signal it needs: next-state signals carry both evaluative information (did it work?) and directive information (how to fix it), yet systems ignore both. Their asynchronous architecture decouples policy serving, reward judging, and training into concurrent processes.

Agentic Critical Training [22] demonstrated that training agents to *judge* which action is better (via RL) produces genuine self-reflection rather than imitated reflection (via SFT). The surprising finding: action-judgment training in agentic environments improves general reasoning benchmarks (MATH-500, GPQA-Diamond) *without any reasoning-specific training data* — suggesting that agentic RL may be a general mechanism for reasoning improvement.

---

## 4. ACT: The Agentic Coding Explosion

### 4.1 The Benchmark Reality Check

The SWE-Bench family has fragmented into five complementary benchmarks, each addressing a different failure mode of the original:

**SWE-Bench Pro** [9]: 1,865 problems across 41 repositories spanning Python, JavaScript, TypeScript, and Go. Three-tier contamination resistance (public/commercial/held-out). Best model performance remains below 45% Pass@1. Without human augmentations specifying requirements and interfaces, GPT-5 drops from 25.9% to 8.4%.

**SWE-EVO** [10]: Tests what SWE-Bench can't — continuous software evolution. 48 tasks from release notes of mature projects, averaging 21 files edited and 874 tests per instance. GPT-5 achieves only 21% on SWE-EVO versus 65% on SWE-Bench Verified — a 44 percentage-point drop that reveals the fundamental gap between single-issue resolution and long-horizon evolution.

**SWE-bench Live** [11]: Automated pipeline (REPOLAUNCH) for continuous benchmark updates from 93 repositories. Agents show "substantial performance gap compared to static benchmarks," suggesting overfitting to fixed test sets.

**Saving SWE-Bench** [12]: Transforms formal GitHub issues into realistic user queries based on telemetry analysis. Reveals 20–50% overestimation on public benchmarks. Users write 10–30 word queries with error stacks; GitHub issues contain 100+ words with reproduction code.

**UTBoost** [13]: LLM-generated test augmentation finds 345 erroneous patches incorrectly labeled as passing, impacting 40.9% of SWE-Bench Lite leaderboard entries.

The collective implication: reported capabilities are inflated by contamination, over-specified descriptions, insufficient tests, and benchmark saturation. The real state of the art is considerably below headline numbers.

### 4.2 Self-Improving Agents

**Live-SWE-agent** [14] achieves 77.4% on SWE-bench Verified — state-of-the-art with zero offline training cost. Starting from a minimal bash-only scaffold, the agent creates custom tools on-the-fly as it solves problems. The reflection loop is critical: without explicit prompting to consider tool creation, agents don't spontaneously create tools. Model capability matters: Claude 4.5 Sonnet shows +22.6% improvement, but GPT-5-Nano actually degrades (-68.2%) — there is a minimum model capability threshold for self-improvement to work.

**Self-Play SWE-RL** [15] trains a single LLM in a self-play setting as both bug-injector and bug-solver, requiring only sandboxed repositories with source code — no human issues, no human tests. On SWE-bench Verified: +10.4 points over the pre-RL checkpoint, consistently outperforming human-data RL baselines throughout training. This demonstrates that agents can generate their own training curriculum from raw codebases.

**RepoNavigator** [23] demonstrates that a single execution-aware tool ("jump" to a symbol's definition via language server) combined with RL training outperforms multi-tool agents with much larger models: the 7B model beats 14B baselines, the 14B surpasses 32B competitors.

Together, these results paint a clear picture: self-generated tools (Live-SWE-agent), self-generated training data (SSR), and minimal tool design with RL (RepoNavigator) each independently outperform hand-crafted alternatives. The trend toward learned rather than engineered agent capabilities, identified in Section 3, extends directly to the coding domain.

### 4.3 The 60/20 Paradox

Anthropic's 2026 Agentic Coding Trends Report documents that engineers use AI in approximately 60% of their work but fully delegate only 0–20%. This is not a failure — it reflects the nature of effective human-AI collaboration. Engineers develop "intuitions for AI delegation" over time, delegating easily verifiable or low-stakes tasks while retaining conceptually difficult or design-dependent work. Approximately 27% of AI-assisted work consists of tasks that wouldn't have been done otherwise — AI isn't just replacing work, it's creating new categories of work.

---

## 5. INTERACT: Protocol Infrastructure

### 5.1 The Protocol Stack

Before standardized protocols, connecting N AI models to M external tools required N×M custom integrations. Four protocols now address this at different layers [24]:

**MCP** (Model Context Protocol, Anthropic, November 2024): JSON-RPC 2.0 client-server interface for tool invocation. Four primitives: Tools (model-controlled), Resources (application-controlled), Prompts (user-controlled), Sampling (server-initiated). 97M+ monthly SDK downloads by February 2026.

**A2A** (Agent-to-Agent Protocol, Google, April 2025): Agent Cards for capability-based discovery. Peer-to-peer task delegation via HTTPS + SSE. Donated to Linux Foundation June 2025; merged with IBM's ACP August 2025.

The emerging consensus: MCP and A2A compose at different layers, like TCP/IP. MCP for precise tool-level execution, A2A for scalable agent-level routing. LangGraph v0.2 (January 2026) added both as first-class protocol targets.

### 5.2 Governance

The Agentic AI Foundation (AAIF), launched December 2025 under the Linux Foundation, represents an unprecedented act of co-governance. Six competing companies — OpenAI, Anthropic, Google, Microsoft, AWS, and Block — agreed to jointly steward interoperability standards. This provides the neutral governance that enterprises require before committing to protocol adoption.

### 5.3 Orchestration Evidence

In 348 controlled trials comparing single-agent versus multi-agent orchestration on incident response [16], multi-agent systems achieved 100% actionable recommendations versus 1.7% for single agents, with 80× specificity improvement and 140× correctness improvement. Both systems achieve ~40 second latency — the value is quality and determinism, not speed. Multi-agent quality variance is σ ≈ 0, making it production-ready, while single-agent outputs remain inconsistent.

### 5.4 Difficulty-Aware Routing

DAAO [25] dynamically generates query-specific multi-agent workflows guided by predicted query difficulty using a VAE-based estimator. A heterogeneous LLM router pairs each subtask with the optimal model. Result: +3.2–10.2% accuracy at 41% of the inference cost, generalizing to unseen model backbones.

### 5.5 Flow Engineering

The production shift is toward controllable orchestration — explicit workflow graphs (LangGraph-style state machines) rather than open-ended chat loops [26]. Developers define state transitions and guardrails; models fill in local decisions. This trades theoretical autonomy for practical reliability, prioritizing debuggability and human approvals.

---

## 6. OPERATE: The Security Surface

This section represents the entirely new contribution that Plaat et al. deferred as future work. By March 2026, the evidence base warrants dedicated treatment.

### 6.1 Protocol-Level Vulnerabilities

The first formal MCP security analysis [17] identified three architectural vulnerabilities: (1) absence of capability attestation allowing servers to self-declare arbitrary permissions, (2) bidirectional sampling without origin authentication enabling server-side prompt injection, and (3) implicit trust propagation in multi-server configurations where tool responses from Server A influence invocations on Server B.

Through 847 attack scenarios across five MCP servers and three LLM backends, MCP's architecture was shown to amplify attack success by 23–41% compared to equivalent non-MCP integrations. Cross-server propagation (61.3% ASR) and sampling-based injection (67.2% ASR) represent entirely new attack classes that don't exist without the protocol.

The proposed AttestMCP defense — capability attestation, message authentication, origin tagging, isolation enforcement — reduces overall attack success from 52.8% to 12.4% with 8.3ms median latency overhead. The residual 12.4% reflects indirect injection through legitimately-retrieved content — a fundamental LLM limitation unsolvable at the protocol layer.

SMCP [27] complements this with the most detailed threat-per-workflow-step mapping: 19 distinct threats across 6 MCP workflow steps, with five protocol-level security enhancements (unified identity, mutual authentication, security context propagation, fine-grained policy enforcement, comprehensive audit logging).

### 6.2 Defense Failure

A systematization of 78 studies [18] catalogs 42 distinct attack techniques and reveals that all tested defense mechanisms fail under adaptive attacks:

| Defense | Reported ASR | Adaptive ASR |
|---------|-------------|-------------|
| Protect AI | <5% | 93% |
| PromptGuard | <3% | 91% |
| PIGuard | <5% | 89% |
| Model Armor | <10% | 78% |

This establishes that prompt injection requires architectural mitigation, not ad-hoc filtering. The analogy to SQL injection is apt: that vulnerability was solved by parameterized queries (an architectural change), not by input filtering.

### 6.3 Data Over-Exposure

AgentRaft [19] defines a distinct risk class: Data Over-Exposure (DOE), where agents inadvertently transmit sensitive data beyond user intent. Unlike prompt injection (adversarial), DOE is systemic — caused by overly broad tool data provision and LLMs' lack of contextual privacy awareness. Testing on 6,675 real-world MCP tools found that 57.07% of tool call chains exhibit unauthorized sensitive data exposure and 65.42% of transmitted data fields are over-exposed.

### 6.4 The Skill Supply Chain

Three concurrent studies provide the first empirical characterization of skill security [20]. Analysis of 42,447 skills from two major marketplaces found 26.1% contain at least one vulnerability across 14 distinct patterns. Behavioral verification of 98,380 skills from community registries identified 157 confirmed malicious skills with 632 vulnerabilities. Skills bundling executable scripts are 2.12× more likely to contain vulnerabilities. The speed of the ClawHub incident — 14 malicious skills within 72 hours of marketplace launch — demonstrates that skill ecosystem security requires the same rigor as package management, but the tooling doesn't exist yet.

### 6.5 The Security-Capability Tradeoff

Platform vulnerability assessment [18] reveals an inverse correlation between security and capability permissiveness: Claude Code achieves the lowest vulnerability rating (Low) through aggressive sandboxing, while Cursor rates Critical due to extensive extension trust. The market will not accept either extreme. The winning approach must find an asymmetric advantage — high capability with architectural security, not capability restriction.

---

## 7. Cross-Cutting: The Portable Agent Layer

### 7.1 SKILL.md as Emerging Standard

The most surprising development is the emergence of a portable configuration layer across competing vendor tools. SKILL.md files — Markdown documents with YAML frontmatter — define reusable agent capabilities that work across Claude Code, Gemini CLI, Cursor, Codex CLI, and four other tools without modification [28, 29].

The SoK on Agentic Skills [28] formalizes this: a skill is a four-tuple S = (C, π, T, R) — applicability condition, executable policy, termination condition, and reusable callable interface — distinguishing skills from tools (atomic, no decision-making), plans (one-time, session-scoped), and prompt templates (static text, no termination logic). Seven design patterns capture how skills are packaged and executed in practice, from metadata-driven progressive disclosure to self-evolving libraries and marketplace distribution.

The Agent Skills Survey [29] documents the progressive disclosure architecture: Level 1 metadata (~30 tokens/skill, always loaded) acts as a "menu" for intent matching; Level 2 instructions (200–2K tokens) are loaded on trigger; Level 3 resources (scripts, references) are loaded on demand. This prevents context bloat — the agentic equivalent of lazy loading.

Antigravity Awesome Skills (v8.6.0, March 2026) bundles 1,300+ skills with official contributions from Anthropic, Vercel Labs, OpenAI, Supabase, Microsoft, Google DeepMind, Sentry, Trail of Bits, Expo, and Hugging Face. The universal SKILL.md format decouples skill content from tool-specific invocation, creating the first genuine cross-vendor standard.

### 7.2 Configuration Convergence

Per-project agent configuration is converging under different filenames: CLAUDE.md (Anthropic), AGENTS.md (OpenAI/AAIF), .cursorrules (Cursor), .github/copilot-instructions.md (GitHub). All define coding standards, workflow constraints, tool permissions, and project-specific context. The semantic convergence is clear even if format unification hasn't happened yet.

### 7.3 Five Configuration Layers

Five distinct layers are emerging:

1. **Model Config** (system prompt): Provider-defined, always loaded, highest trust
2. **Project Config** (CLAUDE.md / AGENTS.md): Team-defined, per-repo, version-controlled
3. **Skills** (SKILL.md): Community-contributed, cross-project, on-demand loading
4. **Tools** (MCP servers): Developer-configured, per-integration, OAuth-scoped
5. **Agent-to-Agent** (A2A Agent Cards): Cross-organizational discovery, capability-based

Trust decreases as you move down the stack. Security requirements increase accordingly. No existing survey maps this full stack.

---

## 8. Synthesis: Five Findings and a Research Agenda

### 8.1 Finding 1: The Scaffold-to-Weights Migration Is Real and Accelerating

Every paper in Section 3 documents the same trajectory: capabilities that were prompt-engineered in 2024 are RL-trained in 2026. Planning, tool use, memory, self-improvement, and context management are all moving inside the model boundary. The mechanistic question — does RL amplify existing capabilities or create new ones? — remains unresolved [2], but the practical shift is undeniable. Agentic Critical Training [22] provides the strongest evidence that RL in agentic environments produces capabilities that transfer beyond the training domain.

### 8.2 Finding 2: Self-Improvement Outperforms Hand-Crafting

Three independent results converge: Live-SWE-agent (self-generated tools, 77.4%) beats all manually designed scaffolds. Self-Play SWE-RL (self-generated training data, +10.4) beats human-data RL throughout training. RepoNavigator (one tool + RL, 7B beats 14B) beats multi-tool agents with larger models. The consistent lesson: let agents learn their own capabilities rather than engineering them. But this requires sufficiently capable base models — below a threshold (approximately GPT-5-Mini), self-improvement degrades rather than helps.

### 8.3 Finding 3: Benchmarks Overestimate and Production Underdelivers

The SWE-Bench family collectively demonstrates that headline numbers are inflated by contamination [11], over-specified descriptions [12], insufficient tests [13], and saturation on isolated tasks [9, 10]. SWE-EVO's 65%→21% drop is the clearest evidence that current agents lack sustained multi-file reasoning. Meanwhile, the 60/20 paradox (60% of work uses AI, 0–20% is fully delegated) shows that production adoption is real but bounded by the need for human judgment.

### 8.4 Finding 4: Interaction Became Infrastructure

Plaat et al. asked whether agents can collaborate and what emergent behaviors arise. The 2026 answer: interaction is an infrastructure, governance, and security problem. Six competing companies co-govern the protocol stack. The compose-not-compete pattern (MCP for tools, A2A for agents) mirrors TCP/IP. Flow engineering (explicit state machines with guardrails) has won over fully autonomous loops in production.

### 8.5 Finding 5: Security Is Architectural, Not Patchable

Both MCP security analyses [17, 27] independently conclude that the protocol's security weaknesses are architectural — patching individual CVEs won't fix fundamental issues like absent capability attestation and implicit trust propagation. The SoK [18] finds every tested defense bypassed at 78%+ rates. AgentRaft [19] identifies a risk class (Data Over-Exposure) that exists independently of adversarial attacks. The skill supply chain [20] faces npm-style threats but worse, since skills have direct system access. The security community must treat prompt injection as a first-class vulnerability requiring architectural mitigation, not ad-hoc filtering.

### 8.6 Research Agenda

**Closing the long-horizon gap.** SWE-EVO's 65%→21% drop is the clearest open problem. Agents that can sustain multi-file reasoning across hours of work, maintain coherence across interdependent changes, and recover from errors mid-execution would transform software engineering productivity. This likely requires advances in both model capability (longer effective context) and training methodology (RL on evolution tasks, not just issue resolution).

**Agentic scaling laws.** Existing scaling laws [6] were measured for pure reasoning RL. When agents use tools, "offloading deterministic computations to tools and focusing learning on high-level decision making" should shift the scaling curve upward. Measuring agentic scaling laws across tool-augmented settings is critical for compute-optimal training allocation.

**Protocol-level security.** AttestMCP [17] and SMCP [27] propose complementary protocol extensions. Incorporating these into the MCP specification itself — rather than leaving them as optional add-ons — would address the architectural vulnerabilities at the right layer. The identity gap across MCP/A2A/A2UI (no unified identity flowing across protocol layers) is a specific unsolved problem.

**Data Over-Exposure mitigation.** AgentRaft [19] quantifies the problem (57% of tool chains leak data) but doesn't solve it. Architectures that enforce data minimization at the protocol layer — where tools return only the data requested, not their full schema — would address the root cause rather than filtering symptoms.

**Skill governance at scale.** The 26.1% vulnerability rate [20] across 42K skills demands the same supply chain security rigor as package managers (npm, pip). Signed skill manifests, sandboxed execution, behavioral verification before marketplace listing, and trust-tiered deployment permissions are all needed. The SoK's proposed governance framework [28] provides the conceptual architecture; the implementation is the engineering challenge.

**Bridging benchmarks and production.** The gap between SWE-bench scores and production deployment experience (the 60/20 paradox) suggests that current benchmarks measure the wrong thing. Benchmarks that evaluate sustained, multi-session, human-collaborative coding workflows — rather than isolated issue resolution — would better predict production value.

---

## 9. Limitations

We read 28 papers at varying depth (11–100%), not the comprehensive coverage of Plaat et al.'s 300+ references. Embodied agents, GUI agents, and scientific discovery agents — categories Plaat et al. covered well — are acknowledged but not re-reviewed. Our industry source analysis relies on public reports and web research rather than proprietary deployment data. The forward citation sweep (6 papers) covers only papers indexed by Semantic Scholar by March 23, 2026; concurrent work submitted but not yet indexed is necessarily missing.

Our security analysis of coding platforms [18] relies on the SoK authors' methodology and may not capture defenses deployed after January 2026. The Data Over-Exposure statistics [19] come from a single study on MCP.so-listed tools and may not represent the full MCP ecosystem.

---

## 10. Conclusion

Between January 2025 and March 2026, agentic LLM capabilities underwent four structural shifts that require extending Plaat et al.'s three-axis taxonomy with a fourth axis: **Operate**. Reasoning capabilities migrated from external scaffolds to model weights via RL. Software development became the dominant action domain, with self-improving agents outperforming all hand-crafted alternatives. Interaction shifted from a research topic to an infrastructure and governance challenge, with standardized protocols governed by competing companies under neutral stewardship. And the safety surface that prior surveys deferred as future work became the central engineering challenge, with architectural vulnerabilities amplifying attacks, comprehensive defense failures, and systemic data leakage.

The field is no longer asking "can agents reason, act, and interact?" It is asking "can we make them do so safely, reliably, and economically at production scale?" — and the evidence suggests we cannot yet answer yes.

---

## References

[1] Plaat, van Duijn, van Stein, Preuss, van der Putten, Batenburg. "Agentic Large Language Models, a survey." JAIR 2025. arXiv:2503.23037.

[2] Zhang et al. (25 authors). "The Landscape of Agentic Reinforcement Learning for LLMs." TMLR, Jan 2026. arXiv:2509.02547.

[3] Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native Agentic AI. ADaM-BJTU, 2025.

[4] Guo et al. "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning." Jan 2025. arXiv:2501.12948.

[5] Cheng et al. "Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning." Nov 2025. arXiv:2511.14460.

[6] Tan et al. "Scaling Behaviors of LLM Reinforcement Learning Post-Training." Dec 2025. arXiv:2509.25300.

[7] Ning et al. "Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL." Feb 2026. arXiv:2602.04284.

[8] Yu et al. "Demystifying Reinforcement Learning in Agentic Reasoning." Oct 2025. arXiv:2510.11701.

[9] Deng, Da et al. "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?" Scale AI. Nov 2025. arXiv:2509.16941.

[10] Thai et al. "SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios." FPT/Melbourne. Jan 2026. arXiv:2512.18470.

[11] Zhang et al. "SWE-bench Goes Live!" Microsoft. Jun 2025. arXiv:2505.23419.

[12] Garg et al. "Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation." Microsoft. CAIN '26. arXiv:2510.08996.

[13] Yu et al. "UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench." CUHK-SZ/UIUC. Jun 2025. arXiv:2506.09289.

[14] Xia et al. "Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?" UIUC. Nov 2025. arXiv:2511.13646.

[15] Wei et al. "Toward Training Superintelligent Software Agents through Self-Play SWE-RL." Meta FAIR/UIUC/CMU. Dec 2025. arXiv:2512.18552.

[16] Drammeh. "Multi-Agent LLM Orchestration Achieves Deterministic, High-Quality Decision Support for Incident Response." Jan 2026. arXiv:2511.15755.

[17] Maloyan, Namiot. "Breaking the Protocol: Security Analysis of the Model Context Protocol." Jan 2026. arXiv:2601.17549.

[18] Maloyan, Namiot. "Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis." Jan 2026. arXiv:2601.17548.

[19] Lin et al. "AgentRaft: Automated Detection of Data Over-Exposure in LLM Agents." Sun Yat-sen/UCF. Mar 2026. arXiv:2603.07557.

[20] Xu, Yan. "Agent Skills for Large Language Models: Architecture, Acquisition, Security." Zhejiang. Feb 2026. arXiv:2602.12430. (Synthesizing Liu et al. SkillScan and behavioral verification studies.)

[21] Wang et al. "OpenClaw-RL: Train Any Agent Simply by Talking." Princeton/NUS. Mar 2026. arXiv:2603.10165.

[22] Liu et al. "Agentic Critical Training." UMD. Mar 2026. arXiv:2603.08706.

[23] Zhang et al. "One Tool Is Enough: Reinforcement Learning of LLM Agents for Repository-Level Code Navigation." PKU/Baidu. Jan 2026. arXiv:2512.20957.

[24] Ehtesham et al. "A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, ANP." May 2025. arXiv:2505.02279.

[25] Su et al. "Difficulty-Aware Agentic Orchestration for Query-Specific Multi-Agent Workflows." WWW '26. arXiv:2509.11079.

[26] Arunkumar et al. "Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents." Jan 2026. arXiv:2601.12560.

[27] Hou et al. "SMCP: Secure Model Context Protocol." HUST. Feb 2026. arXiv:2602.01129.

[28] Jiang et al. "SoK: Agentic Skills — Beyond Tool Use in LLM Agents." UTS/CSIRO. Feb 2026. arXiv:2602.20867.

[29] Xu, Yan. "Agent Skills for Large Language Models." Zhejiang. Feb 2026. arXiv:2602.12430.

[30] Tran et al. "Multi-Agent Collaboration Mechanisms: A Survey of LLMs." UCC. Jan 2025. arXiv:2501.06322.

[31] Gao et al. "A Survey of Self-Evolving Agents." TMLR, Jan 2026. arXiv:2507.21046.

[32] Zhang et al. "A Survey of Reinforcement Learning for Large Reasoning Models." Tsinghua/Shanghai AI Lab. Oct 2025. arXiv:2509.08827.

[33] Anthropic. "2026 Agentic Coding Trends Report." January 2026.

[34] OWASP. "Top 10 for LLM Applications." 2025 edition.

[35] Simon Willison. "The Lethal Trifecta: Private Data Access, Untrusted Content, External Communication." June 2025.
