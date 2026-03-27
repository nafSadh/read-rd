# Agent-R1: Training Powerful LLM Agents with End-to-End RL
**arXiv:2511.14460 | Nov 2025**

## Core Contribution
Extends standard MDP framework for multi-turn interactive LLM agents. Provides both conceptual framework and practical training infrastructure.

## Key Ideas
- Adapts MDP components (state space, action space, transitions, rewards) for multi-turn agents
- Distinguishes **cognitive actions** (reasoning steps) from **environmental actions** (tool calls, API requests)
- This distinction is critical: RL must handle both thinking and doing differently
- Modular framework designed for adaptation across diverse task scenarios
- Validated on Multihop QA benchmarks

## Why It Matters
Makes explicit the formal gap between single-turn reasoning RL (DeepSeek-R1) and full agentic RL with environmental interaction. The cognitive/environmental action distinction maps directly to the model-native vs. scaffold-based axis.

---

# ARLArena & SAMPO (OpenClaw-RL)
**arXiv:2603.10165 | Wang, Chen et al. | Mar 2026**

## Core Problem
Training instability (collapse) is the dominant failure mode for agentic RL. Models that work fine in supervised settings collapse during RL training on agentic tasks.

## ARLArena Framework
- Systematic analysis framework for training stability
- Decomposes policy gradient into **4 core design dimensions**
- Standardized testbed for controlled, reproducible experiments
- Enables apples-to-apples comparison of RL techniques

## SAMPO (Stable Agentic Policy Optimization)
- Designed to mitigate dominant instability sources in ARL
- Achieves consistently stable training across diverse tasks
- Works for terminal, GUI, SWE, and tool-call agent settings

## OpenClaw-RL Connection
- Track 1: Fully async framework for personalized OpenClaw optimization (Binary RL + OPD)
- Track 2: Scalable agentic RL for general agents in real-world settings
- Key innovation: trains from natural conversation feedback — no manual labeling

## Key Stats
- Supports local GPU and cloud deployment
- LoRA training supported for efficiency
- Community contributions integrating SDFT/SDPO methods

---

# Enhancing Agentic RL with Progressive Reward Shaping and VSPO
**arXiv:2512.07478 | Su et al. | Dec 2025, v2 Jan 2026**

## Two Problems Addressed
1. **Sparse rewards:** Binary 0/1 signals provide limited guidance for intermediate steps
2. **Gradient degradation in GRPO:** Identical rewards within rollout group → zero advantage → wasted samples

## Solutions
**PRS (Progressive Reward Shaping):**
- Curriculum-inspired dense feedback
- Stage-wise: first master parseable tool calls, then correct logic, then final answer
- Instantiated for short-form QA (length-aware BLEU) and long-form QA (LLM-as-judge)

**VSPO (Value-based Sampling Policy Optimization):**
- Enhanced GRPO variant
- Replaces zero-advantage samples with prompts selected by task-value metric (balancing difficulty + uncertainty)
- Value-smoothing clipping for stable gradient updates

## Results
- PRS consistently outperforms binary rewards
- VSPO beats SFT, PPO, and GRPO baselines in stability, convergence speed, and final performance
- Together, PRS + VSPO yield agents that generalize better across domains

---

# Agent-Omit: Adaptive Thought and Observation Omission
**arXiv:2602.04284 | Ning et al. | Feb 2026**

## Core Insight
Most agents treat all interaction turns equally. But thought necessity and observation utility vary — some turns are redundant. Train agents to *skip* unnecessary reasoning.

## Three Paradigms in Literature
- **Thought Management (TM):** Compress thought token length (ToolLight, DEPO)
- **Observation Management (OM):** Prune historical observations (Observation-Mask, DeepMiner)
- **Thought & Observation Management (TOM):** Joint compression (MEM-Agent, ReSum)
- All treat trajectories equally — Agent-Omit does it *adaptively*

## Method
1. **Omission turn identification:** Forward traversal + rollout to find turns that can be skipped without accuracy loss
2. **Cold-start data:** Single-turn + multi-turn omission scenarios
3. **Omit-aware agentic RL:** Dual sampling + tailored omission reward
4. **Theoretical guarantee:** Policy deviation bounded by KL-divergence

## Benchmarks (5 tasks)
- DeepSearch (search engines for knowledge-intensive queries)
- WebShop (e-commerce navigation)
- TextCraft (Minecraft-inspired long-horizon planning)
- BabyAI (instruction following in grid worlds)
- SciWorld (scientific discovery simulations)

## Results
- Agent-Omit-8B matches 7 frontier LLM agents on accuracy
- Best effectiveness-efficiency trade-off among 7 efficient methods

---

# Demystifying Reinforcement Learning in Agentic Reasoning
**arXiv:2510.11701 | Oct 2025**

## Focus
Systematic investigation of GRPO variants for agentic settings. Three key improvement dimensions:

1. **Loss Aggregation Granularity:** Token-level vs sequence-level vs trajectory-level optimization
2. **Reward Shaping:** Dense vs sparse, curriculum-based approaches
3. **Clipping Strategy:** How aggressively to constrain policy updates

## Key Finding on Training Data
Real end-to-end trajectories provide qualitatively richer learning signals than synthetic stitch-style data (e.g., ReTool). Synthetic data replaces selected reasoning steps with tool calls but misses critical decision cues: not only *how* to call a tool, but *when*, *why*, and *what to do next*.

## Reasoning Mode Analysis
Open puzzles around:
- Turn budget allocation
- Trade-off between response length and tool-call efficiency
- Impact of long-CoT predispositions on multi-turn reasoning
- Overthinking (long inefficient loops) vs underthinking (premature tool reliance)

---

# Scaling Behaviors of LLM RL Post-Training
**arXiv:2509.25300 | v3 Dec 2025**

## Setup
63 LLMs fine-tuned with RL on 50K math problems across full Qwen2.5 series (0.5B–72B).

## Four Key Findings
1. Larger models have **superior learning efficiency** (compute + data)
2. Test loss follows **predictive power-laws** with compute and data — robust across base and instruct models
3. Efficiency gains from scale **diminish gradually** — saturation for largest models
4. **Data reuse is highly effective** in data-constrained regime

## Agentic Implication
"Agentic mechanisms will markedly improve scaling behavior of RL-trained LLMs: by offloading deterministic computations to tools and focusing learning on high-level decision making, these models could achieve much higher efficiency, effectively shifting the performance frontier upward."

---

# Recursive Language Models (Prime Intellect)
**arXiv:2512.24601 | Blog: primeintellect.ai/blog/rlm**

## Core Idea
Instead of external memory or context summarization, let the model manage its own context by delegating to Python scripts and sub-LLMs. The RLM can branch execution, spawn sub-processes, return self-chosen summaries — all learned via RL.

## Context Rot Problem
- Claude Code, Codex, and similar tools use file-system scaffolding + LLM summarization at regular intervals
- This creates "succession of agents" connected by prompts and file state
- Performance degrades as context grows — "context rot"

## RLM Approach
- "Context folding" — model actively manages its own context window
- Limits REPL output to 8192 chars per turn, forcing model to use Python/sub-LLMs for data processing
- Model learns to pro-actively delegate rather than passively accumulate context
- Compatible with file-based scaffolding as an additional layer

## Key Claim
"Teaching models to manage their own context end-to-end through reinforcement learning will be the next major breakthrough, enabling agents to solve long-horizon tasks spanning weeks to months."

## Significance
Directly addresses the operational challenge (context rot) that affects production agentic systems. Bridges REASON and OPERATE sections of the survey.
