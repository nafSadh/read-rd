# The Landscape of Agentic Reinforcement Learning for LLMs: A Survey
**arXiv:2509.02547 | Zhang, Geng et al. (25 authors) | Sep 2025, v3 Nov 2025**

## Core Thesis
Formalizes the paradigm shift from conventional LLM-RL (single-step MDPs) to Agentic RL (temporally extended POMDPs). RL is the critical mechanism for transforming agentic capabilities from static heuristic modules into adaptive, robust behavior.

## Key Framing: LLM-RL vs Agentic RL
- **LLM-RL:** Degenerate single-step MDPs — generate response, get reward, done
- **Agentic RL:** Temporally extended POMDPs — multi-turn interaction, partial observability, sequential decisions with environmental feedback
- This distinction is the conceptual bridge between DeepSeek-R1-style training and full agent training

## Twofold Taxonomy
**By capability:**
1. Planning — decomposition, search, lookahead
2. Tool use — function calling, API invocation, code execution
3. Memory — episodic, semantic, working memory across turns
4. Reasoning — CoT, reflection, verification (building on DeepSeek-R1)
5. Self-improvement — learning from own trajectories, self-play
6. Perception — multimodal grounding, visual/audio input

**By application domain:** coding, web navigation, robotics, scientific discovery, games, etc.

## Central Argument
RL serves as the *unifying mechanism* for all six capabilities. Without RL, these capabilities remain static prompt-engineering tricks. With RL, they become learned, adaptive behaviors that improve with experience.

## Scope
- Synthesizes 500+ recent works
- Consolidates open-source environments, benchmarks, and frameworks
- Highlights both opportunities and challenges for scalable, general-purpose AI agents

## Significance for the Survey
This is the most comprehensive taxonomy of *how* agentic capabilities are trained via RL. It complements Plaat et al.'s taxonomy of *what* agents do (Reason/Act/Interact) with a taxonomy of *how they learn*. Essential reference for Section 1 (REASON) of our survey.
