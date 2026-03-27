# S1: LLMs & Foundation Models

> The raw capability story is almost boring now. The interesting stories in 2026 are about what happens *around* the models: a 280× cost collapse, a power grid that can't keep up, a Chinese open-source movement rewriting the geopolitical map, and an efficiency counter-narrative that questions whether we even need the biggest models.

**Sources:** 8 (Stanford AI Index 2025, Epoch AI supercomputer trends, LLM-Stats, MIT Technology Review, IBM Think, NVIDIA SLM paper, Understanding AI, UX Tigers/Nielsen)  
**Adequacy:** Strong. Covers performance, cost, infrastructure, geopolitics, and architectural trends.

---

## 1. The Benchmark Crisis

In 2023, researchers introduced three benchmarks — MMMU, GPQA, SWE-bench — designed to stay hard for years. One year later: MMMU +18.8pp, GPQA +48.9pp, SWE-bench 4.4% → 71.7%. Stanford's Parli: "Are we measuring the right thing?"

New harder benchmarks are humbling: Humanity's Last Exam 8.8%, FrontierMath 2%, BigCodeBench 35.5% (human: 97%). Commoditization on Chatbot Arena: #1 vs #10 gap shrank from 11.9% → 5.4%. Top two models: 0.7% apart. Open vs closed gap: 8% → 1.7%.

The 142× shrinkage: hitting 60% MMLU required 540B params (PaLM, 2022) → 3.8B (Phi-3-mini, 2024).

## 2. The Deflation Curve

GPT-3.5-level inference: $20/M tokens (Nov 2022) → $0.07/M tokens (Oct 2024). 280× in 18 months. Three compounding curves: hardware +40%/yr, algorithms 3× less compute/yr, architecture 142× smaller models.

IBM: "We're hitting a commodity point." When top-10 models are within 5%, advantage shifts to integration, data quality, orchestration, governance.

## 3. The Gigawatt Ceiling

Summit (2019): 13 MW. Colossus (2025): 280 MW (uses mobile generators). 2030 projection: 9 GW — nine nuclear reactors. Power doubles every ~13 months. Industry owns 80% of compute (up from 40% in 2019). US hosts 75% globally.

RAND: AI data centers consumed 4.3 GW (2023) → 21 GW (2025) → projected 68 GW (2027). Power, not compute, is the binding constraint.

## 4. Context Window Plateau

8K (2022) → 2M (2024) → flat. Anthropic unchanged since Claude 2.1. GPT-5.2 (400K) < GPT-4.1. Google retreated 2M → 1M. Structural causes: quadratic attention scaling, context rot, economics favor retrieval. Prediction: ~1M through 2026.

## 5. The Open-Source Gambit

Chinese firms gained influence through openness. Qwen2.5-1.5B: 8.85M downloads. DeepSeek forced OpenAI to release open models. US-China benchmark gap collapsed to near parity. China leads in pubs and patents. The geopolitical irony: China gains trust through openness while the US restricts.

## 6. Beyond Text

Nielsen: by end 2026, "frontier model" = speaks, listens, sees, imagines, edits. Early fusion (one model, all modalities) vs late fusion (separate, integrated). Stanford: "We may get clarity in the next year."

## 7. Small Models, Big Ideas

NVIDIA: 7B SLMs are 10-30× cheaper and sufficient for most agentic sub-tasks. Stanford: "We've reached peak data." Evidence: RepoNavigator 7B beats 14B baselines; Agent-Omit 8B matches frontier agents by skipping 45% of tokens.

## 8. What Everyone Agrees On

1. Cost deflation: 10-30×/year, compounding. Most robust finding.
2. Models commoditizing — competition moves to systems.
3. Open-source winning strategically — trust through transparency.
4. Power is the binding physical constraint.
5. Efficiency matters as much as scale.

## 9. Where the Discourse Fractures

1. Bubble? Stanford says yes ("very speculative"). Understanding AI says no ("racing to fill orders").
2. Context plateau: structural (transformer limits) or temporary (coding models, new architectures)?
3. Multimodal timeline: Nielsen says end 2026. Others more cautious. Sora shutdown (today) shows capability ≠ product.
