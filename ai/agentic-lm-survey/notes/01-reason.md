# 01 · REASON — Model-Native Reasoning & Agentic RL

> Deep-dive literature excerpt for survey section. Based on reading 6 papers + 1 blog post totaling ~300 pages.

---

## Section Overview

Between January 2025 (DeepSeek-R1) and March 2026, reasoning in agentic LLMs underwent a paradigm shift. The central development: capabilities previously implemented as external prompt scaffolding are being internalized into model weights via reinforcement learning. A full academic ecosystem has formed around this shift, formalizing it mathematically (MDPs → POMDPs), discovering scaling laws, addressing training instability, and optimizing for efficiency.

**Key numbers from the literature:**
- 95-page survey synthesizing 500+ works (Zhang et al., TMLR 01/2026)
- 63 models trained in scaling law experiments across Qwen2.5 0.5B–72B (Tan et al.)
- Agent-Omit-8B matches frontier agents at a fraction of token cost (Ning et al.)
- 4B models achieving competitive agentic reasoning via proper RL recipes (Yu et al.)
- OpenClaw-RL: fully async RL from live conversation feedback (Wang et al., Mar 2026)

---

## Paper 1: The Landscape of Agentic RL for LLMs: A Survey

**Zhang, Geng, Yu et al. (25 authors) · TMLR 01/2026 · arXiv:2509.02547v4 · 95 pages · 500+ works synthesized**

**Institutions:** Oxford, Shanghai AI Lab, NUS, UIUC, UCL, Imperial College, Brown, UCSD, UCSB, Georgia, CUHK, CAS, Dalian UT

### Core Thesis

The paper's central argument is a formal distinction between two paradigms:

**Preference-Based RL Fine-Tuning (PBRFT)** — what we traditionally call RLHF — is a *degenerate single-step MDP*:
- State space: single prompt; episode ends immediately after one response
- Action space: pure text sequences  
- Transition: deterministic (append token to sequence)
- Reward: single scalar at end of generation
- Horizon: T = 1

**Agentic RL** is a *temporally extended POMDP*:
- State space: evolves over multiple time steps; agent receives partial observations o_t = O(s_t)
- Action space: A_text ∪ A_action (language generation + tool invocations/environment interactions)
- Transition: stochastic; state evolves as s_{t+1} ~ P(s_{t+1} | s_t, a_t)
- Reward: step-wise R(s_t, a_t) combining sparse task rewards and dense sub-rewards
- Horizon: T > 1 with discount factor γ

This is the formal definition:

> "Agentic Reinforcement Learning (Agentic RL) refers to a paradigm in which LLMs, rather than being treated as static conditional generators optimized for single-turn output alignment or benchmark performance, are conceptualized as learnable policies embedded within sequential decision-making loops, where RL endows them with autonomous agentic capabilities."

### Twofold Taxonomy

The survey organizes around two axes:

**Capability axis** (Section 3):
1. **Planning** — RL as external guide (MCTS-based value critics like RAP, LATS) vs. RL as internal driver (directly evolving the LLM's planning policy)
2. **Tool Use** — Three-stage evolution: ReAct-style prompting → SFT-based tool calling (Toolformer, FireAct) → RL-optimized Tool-Integrated Reasoning (TIR). Current frontier: multi-turn TIR with temporal credit assignment
3. **Memory** — Three categories with RL enhancement: RAG-style external stores (MemoryBank, HippoRAG → RL-guided: Prospect, Memory-R1, Mem-α), Token-level memory (MemAgent, MEM1, ReSum, Context Folding), Structured memory (Zep temporal graphs, A-MEM atomic notes, G-Memory hierarchical graphs)
4. **Self-Improvement** — From verbal self-correction (Reflexion, Self-Refine) → RL-driven self-play (Star, Agent Q, self-evolving curricula) → Collective bootstrapping (SiriuS, MALT)
5. **Reasoning** — Fast (System 1) vs. Slow (System 2); DeepSeek-R1, o1/o3, QwQ as exemplars of slow reasoning via RL
6. **Perception** — Vision RL: GRPO adapted with IoU rewards; grounding-driven, tool-driven, and generation-driven active perception

**Task axis** (Section 4):
Search agents, Code agents (generation/refinement/automated SWE), Math agents (informal/formal), GUI agents, Vision agents, Embodied agents, Multi-agent systems

### RL Algorithm Landscape

The paper provides the most comprehensive comparison of RL algorithm variants for LLMs:

**PPO family:** PPO, VAPO (adaptive KL + variance control), LitePPO (stable advantage), PF-PPO (policy filtration), VinePPO (unbiased value estimates), PSGPO (process supervision)

**DPO family:** DPO, β-DPO (dynamic KL coefficient), SimPO (avg log-prob as implicit reward), IPO, KTO, ORPO, Step-DPO, LCPO

**GRPO family:** GRPO, DAPO (decoupled clip + dynamic sampling), GSPO (sequence-level clipping), GMPO (geometric mean token rewards), ProRL (reference policy reset), Posterior-GRPO (reward only successful processes), Dr.GRPO (eliminate bias)

GRPO's core mechanism: sample a group of outputs, use their *relative* rewards to compute advantages, eliminating the need for a value critic. This is sample-efficient but vulnerable to high variance.

### Open Challenges (Section 6)

1. **Trustworthiness** — Agents have expanded attack surface (tools, memory, planning modules) beyond standard prompt injection. Multi-agent systems compound these risks. Sycophancy is particularly dangerous in agentic settings.

2. **Scaling Agentic Training** — Agent RL Scaling Law shows longer training horizons improve tool-use frequency, reasoning depth, and accuracy. ProRL reveals RL training expands reasoning boundaries beyond what's accessible to base models. But entropy collapse and capability narrowing threaten larger models.

3. **Scaling Environments** — ALFWorld and ScienceWorld are insufficient for training general agents. Two strategies: automate reward function design (train explorer agent → build reward model) and automate curriculum generation (EnvGen-style feedback loops).

4. **The Mechanistic Debate** — Two competing explanations: RL as "amplifier" (surfaces pre-existing capabilities) vs. RL as "creator" (teaches genuinely new reasoning patterns). This is unresolved and fundamental.

---

## Paper 2: Agent-R1 — Training Powerful LLM Agents with End-to-End RL

**Cheng et al. · USTC · arXiv:2511.14460 · Nov 2025 · 13 pages**

### Core Contribution

Agent-R1 makes the MDP extension for LLM agents concrete and practical. The paper provides a side-by-side comparison (Table 1 in the paper) that crystallizes the differences:

| MDP Component | Static LLM | LLM Agent |
|---|---|---|
| State Space | s_t = (w_p, w_1, ..., w_t) — current textual context | s_t = (w_p, T_1, ..., T_k, T_{k+1}^partial) — full multi-turn interaction history |
| Action Space | Next token from vocabulary V | Token generation, but specific sequences trigger tool invocations |
| Transition | Deterministic: append token | Two types: deterministic generative transitions (P_G) and stochastic environmental transitions (P_E) from tool use |
| Reward | Sparse, end-of-generation quality score | Rich: final outcome reward (r_f) + intermediate process rewards (r_p) for tool execution |

The key conceptual move: distinguishing "cognitive actions" (reasoning steps — deterministic) from "environmental actions" (tool calls — stochastic). The RL training loop must handle both.

### Framework

Agent-R1 is a modular training framework built on this formalization. Validated on multi-hop QA benchmarks. The framework is deliberately extensible — designed for adaptation across diverse task scenarios and interactive environments.

The paper explicitly frames the taxonomy of agent architectures (Figure 1): Workflows (human-designed routing) → Agentic Workflows (ReAct-style iterative loops, still with prompt engineering) → Fully Autonomous Agents (no predefined workflow, end-to-end RL, proactive environment interaction).

---

## Paper 3: Scaling Behaviors of LLM RL Post-Training

**Tan, Geng, Yu et al. · USTC, Shanghai AI Lab, Oxford, Imperial · arXiv:2509.25300v3 · Dec 2025 · 27 pages**

### Core Finding

The first systematic scaling law study for RL post-training. 63 models across the full Qwen2.5 dense series (0.5B to 72B), all trained with RL on 50,000 math problems.

**The scaling formula:**

```
log L(N, X) = -k(N) · log X + E(N)
```

Where L is test loss, N is model size, X is resource budget (compute C or data D), k(N) is learning efficiency, and E(N) is the initial performance baseline.

### Four Key Findings

1. **Larger models have superior learning efficiency** in both compute and data metrics. A 72B model extracts more value from the same compute budget than a 7B model.

2. **The power-law is predictive** — you can fit it on 0.5B–32B and extrapolate to 72B with good accuracy. Works for both base and instruction-tuned models.

3. **Efficiency saturates.** The learning efficiency k(N) doesn't grow indefinitely with model scale. It follows a saturation formula: k(N) = k_∞ · (1 - e^{-N/N_0}). The marginal gains from bigger models diminish.

4. **Data reuse works.** In data-limited settings, "repeated exposure to a small dataset is nearly as effective as using larger corpora." Final performance is governed by total optimization steps, not unique data volume.

### Implication for Agentic Systems

The paper explicitly connects to agents: "Agentic mechanisms will markedly improve the scaling behavior of RL-trained LLMs: by offloading deterministic computations to tools and focusing learning on high-level decision making, these models could achieve much higher efficiency, effectively shifting the performance frontier upward for a given compute or data budget."

In other words, the scaling laws they measured for pure reasoning RL will be *different* — and likely better — when agents can use tools. Understanding these agentic scaling laws is flagged as a key open question.

---

## Paper 4: Agent-Omit — Adaptive Thought and Observation Omission

**Ning, Fang, Tan, Liu · HKUST(GZ), DiDi · arXiv:2602.04284 · Feb 2026 · 20 pages**

### The Problem

Agent interactions have a massive token waste problem. From their quantitative analysis on WebShop using Qwen3-8B:
- **Thought tokens: 45.1%** of total cost
- **Observation tokens: 52.2%** of total cost  
- **Action tokens: only 2.7%**

The bottleneck isn't executing actions — it's thinking and reading observations. And critically, not all thinking/observation is equally useful:
- Early thoughts (high-level planning) are front-loaded and critical
- Later thoughts become redundant once execution is clear
- Early observations are necessary for initial reasoning
- Later observations accumulate as noise during final answer generation

Using Monte Carlo rollouts, they show that selectively omitting turns below the Pass@1 baseline saves tokens without hurting accuracy.

### Method: Two-Stage Training

**Stage 1: Cold-start data synthesis.** They identify omittable turns by forward traversal — omit a thought/observation, re-run the remaining trajectory, check if accuracy is preserved. If yes, mark as omittable. Generate both single-turn and multi-turn omission training examples.

**Stage 2: Omit-aware agentic RL.** A dual sampling mechanism: the agent learns to produce both standard and omission-aware trajectories. A tailored omission reward incentivizes skipping when it's safe. They prove the deviation of the omission policy is upper-bounded by KL-divergence.

### Results

Agent-Omit-8B matches the performance of seven frontier LLM agents while achieving the best effectiveness-efficiency trade-off among seven efficient methods. Tested on five benchmarks: DeepSearch (knowledge-intensive queries), WebShop (e-commerce navigation), TextCraft (Minecraft-inspired long-horizon planning), BabyAI (grid-world navigation), SciWorld (scientific discovery simulations).

### Significance for the Survey

This paper represents the shift from "can agents reason?" to "can agents reason *efficiently*?" — directly relevant to the "Operate" section's economics concerns. Token costs are a real production constraint, and Agent-Omit shows that RL can optimize for efficiency, not just accuracy.

---

## Paper 5: Demystifying RL in Agentic Reasoning

**Yu, Yang, Zou, Yan, Wang · NUS, Princeton, UIUC · arXiv:2510.11701 · Oct 2025 · 24 pages**

### The Three Axes

This paper takes a practitioner-oriented approach, systematically investigating three dimensions that determine agentic RL success:

**1. Data (Section 3)**

The critical finding: *real end-to-end trajectories dramatically outperform synthetic stitched data for SFT initialization.*

Current agentic training pipelines often use "stitch-style" synthesis — take an existing reasoning trace, replace selected steps with tool invocations. But this misses critical decision cues: "not only how to call a tool, but also when, why, and what to do next."

They compare real vs. synthetic trajectories on Qwen2.5-7B-Instruct and Qwen3-4B-Instruct. Real trajectories provide qualitatively richer learning signals and stronger initialization for subsequent RL.

For the RL stage, *data diversity* is key. High-diversity, model-aware datasets sustain exploration and prevent mode collapse. They construct datasets with diversity metrics to ensure the RL training data covers the space.

**2. Algorithm (Section 4)**

They compare three key improvement techniques over GRPO:
- **Loss aggregation granularity:** token-level vs. sequence-level vs. trajectory-level
- **Reward shaping:** how to transform sparse outcome rewards into denser signals
- **Clipping strategy:** how aggressively to constrain policy updates

Key insight: **exploration-friendly techniques are crucial.** Specifically:
- "Clip higher" — relaxing the upper clip bound allows more exploration
- Overlong reward shaping — don't just penalize long outputs, provide shaped rewards that guide length
- Maintaining adequate policy entropy — preventing premature convergence

**3. Reasoning Mode (Section 5)**

A surprising finding: **a deliberative strategy with fewer tool calls outperforms both frequent tool calling and verbose self-reasoning.**

There's an optimal balance: too many tool calls create dependency and slow things down. Too much internal reasoning (long CoT without tool verification) leads to hallucination accumulation. The sweet spot is deliberate, strategic tool use interleaved with concise reasoning.

### Practical Impact

With these recipes, **4B-sized models achieve superior agentic reasoning** on AIME2024, AIME2025, GPQA-Diamond, and LiveCodeBench-v6. They release both SFT and RL datasets, plus the DemyAgent-4B model.

---

## Paper 6: OpenClaw-RL — Train Any Agent Simply by Talking

**Wang, Chen, Jin, Wang, Yang · Princeton, NUS · arXiv:2603.10165 · Mar 2026 · 24 pages**

### Core Insight

Every deployed AI agent already discards the training signal it needs to improve. After each action a_t, the agent receives a next-state signal s_{t+1} — a user reply, tool execution result, GUI state change, test verdict. Current systems treat this as context for the next action. OpenClaw-RL treats it as a *learning signal*.

Two forms of recoverable "waste":

1. **Evaluative signals** — The next-state implicitly scores the preceding action. A user re-query signals dissatisfaction. A passing test signals success. An error trace signals failure. This forms a natural process reward requiring no separate annotation.

2. **Directive signals** — Beyond scoring, next-states often carry directional information. A user saying "you should have checked the file first" specifies not just what was wrong but how to fix it at the token level.

### Architecture: Fully Asynchronous

Four decoupled components that never block each other:
- **Policy Server (SGLang)** — serves live requests
- **PRM Server** — judges ongoing interactions asynchronously  
- **Training Engine (Megatron)** — updates policy in background
- **Environment Server** — manages sessions and context

The model continues serving while training runs. Judging happens concurrently with new interactions. Zero coordination overhead.

### Two Learning Methods

**Binary RL (for personal agents):** PRM judge constructed via majority vote. Standard GRPO-style objective using evaluative signals as rewards.

**Hindsight-Guided On-Policy Distillation (OPD):** This is the novel contribution. They extract textual hints from the next state, construct an enhanced "teacher context," and provide *token-level directional advantage supervision* — richer than any scalar reward. This recovers directive signals that would otherwise be lost.

### Unified Across Interaction Types

The same framework supports:
- Personal agents (OpenClaw conversations via WhatsApp/Telegram/Discord)
- Terminal agents (bash command execution)
- GUI agents (browser/desktop interaction)
- SWE agents (code editing and test execution)
- Tool-call agents (API invocation)

They demonstrate effectiveness with concrete scenarios: a student using OpenClaw for homework, a teacher grading assignments, a developer debugging code.

### Connection to Broader Ecosystem

OpenClaw-RL builds on the THUDM SLiMe framework for training and SGLang for inference. It uses SETA's dataset for terminal RL, OSWorld's evaluation for GUI RL, and mini-swe-agent for SWE RL. This positions it as an integrative framework rather than a standalone method.

---

## Paper 7: A Survey of RL for Large Reasoning Models

**Zhang et al. (30+ authors) · Tsinghua, Shanghai AI Lab, SJTU, PKU, USTC, HIT, UW, UCL · arXiv:2509.08827 · 120 pages**

### Scope

The most exhaustive survey focused specifically on RL for reasoning (as opposed to broader agentic behavior). 120 pages covering:

**Foundational Components (Section 3):**
- **Reward Design:** Verifiable rewards (rule-based verification), Generative rewards (LLM-as-judge), Dense rewards (step-level process rewards), Unsupervised rewards (self-generated), Reward shaping
- **Policy Optimization:** Policy gradient objectives, Critic-based (PPO family), Critic-free (GRPO family), Off-policy optimization, Regularization objectives
- **Sampling Strategy:** Dynamic and structured sampling, sampling hyperparameters

**Foundational Problems (Section 4):**
- **RL's Role: Sharpening or Discovery?** — Does RL merely surface pre-existing capabilities or teach genuinely new ones? Evidence supports both views depending on context.
- **RL vs. SFT: Generalize or Memorize?** — RL produces better generalization; SFT tends toward memorization of specific patterns.
- **Training Dynamics** — Entropy collapse, reward hacking, mode collapse as key failure modes. The paper catalogs specific stability techniques.

**Applications (Section 6):** Math, Code, Science, Multi-Agent, Robotics, Medical

**Future Directions (Section 7):** Continual RL for LLMs (lifelong learning), Memory-based RL (integrating persistent memory), Model-based RL (world models for planning)

### Key Distinction from the ARL Survey

While Zhang et al. (2509.02547) focuses on the *agentic* shift (POMDP framing, multi-turn interaction, tool use), this survey focuses on the *reasoning* shift (how RL transforms LLMs into reasoning engines). The two surveys are complementary: this one provides depth on the RL algorithm landscape, while the ARL survey provides breadth on the agent architecture landscape.

---

## Blog Post: Recursive Language Models (Prime Intellect)

**Prime Intellect · arXiv:2512.24601 · Blog post 2026**

### The Context Problem

Long-running agentic systems (Claude Code, OpenAI Codex, OpenClaw) all face context rot: performance degradation as the context window fills up. Current solutions:
- File-system scaffolding + LLM summarization at regular intervals (Claude Code, Codex)
- Context folding — branching the rollout and returning self-chosen summaries

### The RLM Proposal

The Recursive Language Model takes a different approach: let the model manage its own context via code delegation.

- The prompt goes into the RLM's context window
- Extra input data is available *only programmatically* (not injected into context)
- The RLM must use Python REPL and sub-LLMs to access data
- REPL output is limited to 8192 characters per turn, forcing the model to process data incrementally
- The model learns to delegate context management to scripts and sub-processes

### Why This Matters

Prime Intellect argues this is "more in line with The Bitter Lesson" — instead of engineering complex context management, let the model learn to manage context end-to-end through RL. They believe "teaching models to manage their own context end-to-end through reinforcement learning will be the next major breakthrough, enabling agents to solve long-horizon tasks spanning weeks to months."

This directly connects to the broader model-native thesis: context management, like reasoning and tool use, can be internalized rather than scaffolded.

---

## Cross-Cutting Themes

### Theme 1: The Scaffold → Weights Migration

Every paper in this section documents a version of the same story: capabilities that were once external prompt engineering are becoming RL-trained model capabilities.

- Planning: from prompt-based CoT → RL-trained planning policies
- Tool use: from ReAct prompting → RL-optimized TIR
- Memory: from static RAG → RL-controlled memory management  
- Self-improvement: from verbal reflection → RL-driven self-correction
- Context management: from file-system scaffolding → RLM code delegation

### Theme 2: The Training Stability Crisis

Agentic RL training is *hard*. Multiple papers document:
- Entropy collapse (models converge prematurely to narrow solutions)
- Reward hacking (exploiting reward signal without improving real capability)
- Mode collapse (losing diversity of behavior)
- Training collapse (complete failure of learning, especially at scale)

ARLArena/SAMPO (OpenClaw-RL) is the most direct response, proposing a systematic stability analysis framework. Demystifying RL prescribes specific algorithmic recipes (clip higher, entropy management, overlong reward shaping). The scaling law paper shows efficiency saturates for larger models, suggesting diminishing returns.

### Theme 3: The Data Question

Two distinct findings:
1. Real end-to-end trajectories are far better than synthetic stitched data for SFT initialization (Demystifying RL)
2. Data reuse is highly effective for RL — total optimization steps matter more than unique data volume (Scaling Laws)

These suggest a practical recipe: invest in high-quality real trajectory collection for cold start, then rely on RL with data reuse for the training phase.

### Theme 4: Efficiency as a First-Class Concern

Agent-Omit demonstrates that efficiency isn't just an operational concern — it can be a training objective. The shift from "maximize accuracy" to "maximize accuracy per token" signals maturation of the field from capability research toward production readiness.

---

## Reading List by Priority

**Must-read (defines the framing):**
1. Zhang et al. "The Landscape of Agentic RL for LLMs" (TMLR 2026) — the canonical survey, 95 pages
2. Yu et al. "Demystifying RL in Agentic Reasoning" — the practitioner's guide

**Important (key results):**
3. Tan et al. "Scaling Behaviors of LLM RL Post-Training" — scaling laws
4. Ning et al. "Agent-Omit" — efficiency via omission
5. Wang et al. "OpenClaw-RL" — unified async training from live interaction

**Reference (foundational):**
6. Zhang et al. "A Survey of RL for Large Reasoning Models" — 120-page deep reference on RL algorithms
7. Cheng et al. "Agent-R1" — clean MDP formalization
8. Prime Intellect "Recursive Language Models" — future direction for context management
