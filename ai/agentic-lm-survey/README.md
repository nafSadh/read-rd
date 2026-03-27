# Agentic LLMs in the Wild — Survey Literature Collection

> Extending [Plaat et al. "Agentic Large Language Models, a survey"](https://arxiv.org/abs/2503.23037) (JAIR 2025) with a four-part taxonomy: **Reason, Act, Interact, Operate**

## What This Is

A structured literature collection and deep-dive analysis for a survey paper on agentic LLMs, covering the paradigm shifts of late 2025–2026:

- Model-native agentic capabilities via RL (scaffold → weights migration)
- The agentic coding explosion (Claude Code, Antigravity, Codex, Gemini CLI, OpenClaw)
- Protocol standardization (MCP, A2A, AAIF)
- Production reality (safety, security, observability, economics)

## Structure

| Section | Topic | Status |
|---------|-------|--------|
| [01 — REASON](html/01-reason.dd.html) | Model-Native Reasoning & Agentic RL | ✅ Done |
| 02 — ACT | Agentic Coding & Tool Use | 🔲 Planned |
| 03 — INTERACT | Protocols & Multi-Agent Systems | 🔲 Planned |
| 04 — OPERATE | Safety, Security, Reliability | 🔲 Planned |
| 05 — Cross-Cut | Skills & Configuration Standards | 🔲 Planned |

Each section has:
- **Markdown** (`md/*.md`) — full text, agent-readable
- **Deep-dive HTML** (`html/*.dd.html`) — interactive three-panel layout with sidebar nav, expandable detail panels, stats, and diagrams

## Artifacts

- [`index.html`](index.html) — Landing page
- [`agentic-llm-survey-proposal.md`](agentic-llm-survey-proposal.md) — Full paper proposal
- [`literature-collection.md`](literature-collection.md) — ~85 entries organized by taxonomy section

## Section 01: REASON — Papers Read

| Paper | Authors | Venue | Pages |
|-------|---------|-------|-------|
| The Landscape of Agentic RL for LLMs | Zhang et al. (25 authors) | TMLR 01/2026 | 95 |
| Agent-R1: End-to-End RL Training | Cheng et al. (USTC) | arXiv 11/2025 | 13 |
| Scaling Behaviors of LLM RL Post-Training | Tan et al. | arXiv 12/2025 | 27 |
| Agent-Omit: Adaptive Omission via Agentic RL | Ning et al. (HKUST/DiDi) | arXiv 02/2026 | 20 |
| Demystifying RL in Agentic Reasoning | Yu et al. (NUS/Princeton) | arXiv 10/2025 | 24 |
| OpenClaw-RL: Train Any Agent by Talking | Wang et al. (Princeton/NUS) | arXiv 03/2026 | 24 |
| A Survey of RL for Large Reasoning Models | Zhang et al. (Tsinghua) | arXiv 10/2025 | 120 |

All papers were downloaded as PDFs and text-extracted for reading (PDFs not committed to repo).
