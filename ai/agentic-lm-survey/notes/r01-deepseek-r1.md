# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
**arXiv:2501.12948 | DeepSeek-AI + 199 authors | Jan 2025 | Published in Nature**

## Core Thesis
Reasoning abilities of LLMs can be incentivized through *pure reinforcement learning*, without human-labeled reasoning trajectories. This was the first demonstration that self-reflection, verification, and dynamic strategy adaptation emerge naturally from RL training.

## Architecture
- **Base model:** DeepSeek-V3-Base
- **RL algorithm:** Group Relative Policy Optimization (GRPO) — simpler than PPO, drops the critic/value model entirely
- **Reward signal:** Solely based on correctness of final predictions vs ground truth — no process supervision
- **Key design choice:** Bypass conventional SFT phase before RL. Hypothesis: human-defined reasoning patterns may *limit* model exploration

## GRPO Mechanics
- Samples multiple responses {o1, o2,..., oG} for each query q
- Evaluates each via reward model (rule-based or learned)
- Computes relative advantages from intra-group reward distribution
- Updates policy to maximize expected reward while minimizing KL divergence from reference
- No separate value network needed — efficiency advantage over PPO

## Training Details
- Learning rate: 3e-6, KL coefficient: 0.001, sampling temperature: 1
- 16 outputs per question, max length 32,768 tokens (→ 65,536 after step 8.2k)
- Batch: 32 unique questions per step = 512 samples
- Reference model replaced every 400 steps
- Total: 10,400 steps = 1.6 training epochs
- 8,192 outputs per rollout, split into 16 mini-batches, single inner epoch

## Key Results
- **AIME 2024:** pass@1 from 15.6% → 71.0%; with majority voting → 86.7% (matches OpenAI o1-0912)
- DeepSeek-R1 (with cold-start SFT) comparable to OpenAI o1-1217

## The "Aha Moment"
The model learns to rethink using anthropomorphic tone — self-reflection emerges naturally. Reflective terms ("wait", "mistake", "however", "retry", "verify", "wrong", "check") increase in frequency during training. Different model families develop different reflection vocabularies based on pretraining data.

## R1-Zero vs R1 Pipeline
1. **R1-Zero:** Pure RL on base model. Powerful but poor readability, language mixing
2. **R1:** Multi-stage pipeline:
   - Cold-start SFT (small amount of reasoning data)
   - Reasoning-oriented RL
   - Rejection sampling + new SFT
   - RL for all scenarios (reasoning + general)

## Distillation Results
- 6 dense models distilled (1.5B, 7B, 8B, 14B, 32B, 70B) from R1 to Qwen and Llama
- Key finding: "Distilling more powerful models into smaller ones yields excellent results" — distillation is more cost-effective than small-model RL
- BUT: "Advancing beyond the boundaries of intelligence may still require more powerful base models and larger-scale RL"

## Unsuccessful Attempts Disclosed
- Process Reward Models (PRM): three limitations in practice
- Extensive SFT before RL can limit exploration
- These failure disclosures are unusually transparent for the field

## Significance for Agentic LLMs
- Proved reasoning can be a *learned* capability, not just engineered scaffolding
- Set the template: if reasoning can be internalized via RL, so can planning, tool use, memory
- Open-weights release catalyzed massive follow-on research (Agent-R1, ARLArena, etc.)
- GRPO became the default algorithm for agentic RL research
