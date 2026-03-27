# Agentic LLMs in the Wild: A Survey of Reasoning, Acting, Interacting, and Operating

**Working title options:**
- _Agentic LLMs in the Wild_ — emphasizes the production shift
- _From Scaffolds to Systems_ — emphasizes the architectural evolution
- _The Agentic Stack_ — emphasizes the protocol/infra layer

**Positioning:** An updated survey of agentic LLM capabilities, extending and reframing Plaat et al. (arXiv:2503.23037, JAIR 2025) to account for the paradigm shifts of late 2025–2026: model-native agentic capabilities via RL, the protocol standardization wave (MCP/A2A), the explosion of agentic coding tools, the open-source agent movement, and the transition from research demos to production systems.

---

## 1. What's Changed Since Plaat et al.

Plaat et al.'s taxonomy — **Reason, Act, Interact** — was elegant and correct for early 2025. But by March 2026, several structural shifts make a pure update insufficient. The paper needs a reframing.

### 1.1 The Model-Native Shift

Plaat et al. treated agentic capabilities as largely _external_ to the model: Chain-of-Thought as prompting, tool use as API scaffolding, memory as retrieval pipelines. The biggest conceptual shift since their paper is that planning, tool use, memory, and reflection are being **internalized into model weights via reinforcement learning**.

- DeepSeek R1 (Jan 2025) demonstrated emergent self-reflection from GRPO RL training
- Kimi k1.5, QwQ, and subsequent reasoning models showed this generalizes
- Vision-Language-Action models (π0, RT-2, Octo) internalized action sequences
- The BJTU "Model-Native Agentic AI" survey frames this as the defining paradigm shift

**Implication for taxonomy:** The Reason/Act/Interact categories need a cross-cutting axis: _scaffold-based_ vs. _model-native_ for each capability. Where does the capability live — in the prompt chain or in the weights?

### 1.2 The Protocol Standardization Wave

Plaat et al.'s "Interact" category treated multi-agent systems as a research topic (Generative Agents, social simulations, game-playing). What actually happened:

- **MCP** (Anthropic, Nov 2024 → Linux Foundation AAIF, Dec 2025): 97M+ monthly SDK downloads by Feb 2026. De facto standard for agent-to-tool communication.
- **A2A** (Google, Apr 2025 → Linux Foundation, Jun 2025): Agent-to-agent discovery and task delegation. Merged with IBM's ACP in Aug 2025.
- **AAIF** (Dec 2025): OpenAI, Anthropic, Google, Microsoft, AWS, Block co-founded the Agentic AI Foundation under Linux Foundation governance.
- **Emerging:** ANP (peer-to-peer agent networking), UCP (universal commerce protocol for agent payments), A2UI (agent-to-user interface)

This is no longer a research question. It's an infrastructure and governance problem. The paper needs to treat protocol interoperability as a first-class topic.

### 1.3 The Agentic Coding Explosion

The most visible manifestation of agentic LLMs in 2026 isn't research demos — it's developers using AI agents to write software. This barely existed when Plaat et al. wrote their paper.

**The landscape as of March 2026:**

| Tool | Provider | Surface | Model | Key Innovation |
|------|----------|---------|-------|----------------|
| Claude Code | Anthropic | CLI, IDE, Desktop | Opus 4.6 | Agent Teams (parallel sub-agents), MCP-native, CLAUDE.md |
| Antigravity | Google | IDE (VS Code fork) | Gemini 3 Pro | Manager View (multi-agent orchestration), Artifacts for verification |
| Codex CLI | OpenAI | CLI, IDE | GPT-5-Codex | Rust sandbox, local-first |
| Gemini CLI | Google | CLI (open source) | Gemini 3 Pro | 1M token context, free tier, Google Search grounding |
| Cursor | Anysphere | IDE (VS Code fork) | Multi-model | Cloud agents with computer use, sub-agents |
| OpenClaw | Open source (Steinberger) | Messaging (WhatsApp, Telegram, Discord) | Any LLM | Self-extending skills, persistent memory, 24/7 daemon |
| Copilot CLI | GitHub/Microsoft | CLI | GPT-based | Native GitHub integration, PR automation |
| Aider | Open source | CLI | Any LLM | Git-native, BYOK |
| OpenCode | Open source | CLI | 75+ models | LSP integration, dual-agent architecture |
| Warp | Warp | Terminal replacement | Multi-model | Runs multiple agents simultaneously |

**Cross-cutting patterns:**
- **Skills/Rules as portable configuration:** SKILL.md format, CLAUDE.md, AGENTS.md, Cursor Rules — converging toward a standard way to configure agent behavior per-project
- **Antigravity Awesome Skills:** 868+ skills portable across Claude Code, Gemini CLI, Codex, Cursor via a shared SKILL.md format. Includes official skills from Anthropic, Vercel, OpenAI, Microsoft, Google DeepMind
- **Multi-agent as default architecture:** Claude Code's Agent Teams, Antigravity's Manager View, Cursor's sub-agents all support spawning parallel workers
- **The developer as "mission controller":** Shift from writing code to reviewing agent output, approving plans, and orchestrating agent fleets

### 1.4 The Open-Source Agent Movement

OpenClaw (formerly Clawdbot/Moltbot) is the emblematic case:
- 68K+ GitHub stars in 72 hours, 100K+ by Feb 2026
- Local-first, self-extending via code generation
- Skills ecosystem with ClawHub marketplace (but: supply chain attacks within weeks)
- Connected to messaging platforms (WhatsApp, Telegram, Discord) — agents as always-on daemons
- Security nightmare: prompt injection via messaging, 21K+ exposed gateways found by Censys, malicious skills on ClawHub
- Creator (Steinberger) joined OpenAI in Feb 2026; project moved to open-source foundation

OpenClaw represents a fundamentally different agentic paradigm from the research systems Plaat et al. surveyed: messy, viral, consumer-facing, and immediately dangerous. The paper needs to grapple with agents in the wild, not just agents in the lab.

### 1.5 Production Reality

- 57% of surveyed organizations have agents in production (LangChain State of AI Agents, Dec 2025)
- Quality is the #1 barrier (32%), replacing cost from the prior year
- 89% have implemented observability for agents
- Multi-model is the norm: 75%+ use multiple models in production
- Context rot (degradation of model recall as tokens accumulate) is a real operational problem
- Cost/token management ("FinOps for agents") is an emerging discipline

---

## 2. Proposed Taxonomy: Reason, Act, Interact, Operate

Extend Plaat et al.'s three-part taxonomy with a fourth category that acknowledges the engineering reality:

### 2.1 Reason (updated)
_How agents think._

- **Scaffold-based reasoning:** Chain-of-Thought, Tree-of-Thought, ReAct, Reflexion — external prompt management
- **Model-native reasoning:** RL-trained reasoning (DeepSeek R1, Kimi k1.5), implicit search, extended thinking
- **Inference-time compute scaling:** Test-time compute budgets, PETS (principled test-time self-consistency)
- **Agentic RL training stability:** ARLArena, SAMPO — addressing training collapse in agentic RL

**Key update from Plaat:** The boundary between "prompting technique" and "learned capability" has blurred. The survey needs to track which reasoning capabilities have moved from scaffolds into weights.

### 2.2 Act (updated)
_How agents do things._

- **Tool use:** MCP as the standard interface; function calling as model-native capability
- **Agentic coding:** The dominant "Act" category in 2026 — agents writing, testing, and deploying software
  - CLI agents (Claude Code, Codex CLI, Gemini CLI, Aider)
  - IDE agents (Cursor, Antigravity, Windsurf, Copilot)
  - General-purpose agents (OpenClaw, Goose)
  - Skills/rules configuration as a cross-tool standard
- **Computer use:** Browser agents (Claude's computer use, Antigravity's browser-in-the-loop), GUI agents
- **Embodied agents:** VLAs (π0, RT-2), robotics — Plaat et al. covered this well, update with recent VLA progress
- **Commerce agents:** Shopping agents, agent payments (Google's UCP/AP2)

**Key update from Plaat:** "Act" is no longer primarily about robotics and hypothetical assistants. The dominant action domain is software development, and the dominant interface is the terminal/IDE.

### 2.3 Interact (updated)
_How agents talk to each other and to humans._

- **Agent-to-agent protocols:** A2A (Google → Linux Foundation), ACP (IBM → merged into A2A), ANP (peer-to-peer)
- **Agent-to-tool protocols:** MCP (Anthropic → Linux Foundation)
- **Agent-to-user protocols:** A2UI (Anthropic, announced), conversational interfaces, messaging-platform agents
- **Multi-agent orchestration:** Supervisor patterns, specialist routing, parallel execution, agent teams
- **Social simulation:** Updated Generative Agents work, emergent behavior studies, MACHIAVELLI benchmark
- **Agent identity and discovery:** Agent Cards (A2A), capability advertisement, cross-organizational trust

**Key update from Plaat:** Interaction is now primarily an engineering/protocol problem, not just a research topic. The Linux Foundation governance and cross-vendor standardization are the defining developments.

### 2.4 Operate (NEW)
_How agents are deployed, monitored, governed, and made reliable._

This is the entirely new category that Plaat et al. punted on as "future work."

- **Observability:** Agent tracing, step-by-step logging, context provenance
- **Evaluation:** LLM-as-judge, human review, SWE-bench, agent benchmarks
- **Safety and security:**
  - Prompt injection (especially via messaging platforms — OpenClaw's attack surface)
  - Supply chain attacks on skill/plugin ecosystems
  - Permission models (sandboxing, allow/deny lists for commands)
  - The OWASP MCP Top 10
- **Reliability:**
  - Context rot and long-context degradation
  - Hallucination accumulation in multi-step tasks
  - Self-verification and self-consistency methods
- **Economics:**
  - Token cost management ("FinOps for agents")
  - Model routing (Gemini for planning, Claude for coding, small models for classification)
  - Distillation from large to small agent models
- **Governance:**
  - AAIF (Linux Foundation) as neutral governance for protocols
  - Enterprise compliance (SOC2, data residency)
  - Agent identity, authorization, and audit trails
  - Legal liability for agent actions

---

## 3. Paper Structure

### Abstract
Background: Agentic LLMs have transitioned from research prototypes to production systems. Objectives: We survey the state of the field as of mid-2026 and propose a four-part taxonomy. Methods: Systematic literature review (Nov 2025–May 2026) supplemented by industry data, framework analysis, and protocol specifications. Results: [findings]. Conclusions: [research agenda].

### 1. Introduction
- Frame the shift from "can agents reason?" to "can agents operate reliably at scale?"
- Cite Plaat et al. as the baseline, explain what's changed
- Introduce the four-part taxonomy: Reason, Act, Interact, Operate

### 2. Background and Related Surveys
- Plaat et al. (JAIR 2025) — the baseline
- BJTU "Model-Native Agentic AI" survey — the RL/internalization framing
- LangChain State of AI Agents reports (2025, 2026) — industry data
- Agent interoperability survey (MCP/A2A/ACP/ANP comparative)
- Li (CoLing 2025) — tool use, planning, feedback learning paradigms

### 3. Reason
- Model-native reasoning via RL (DeepSeek R1, Kimi k1.5, successors)
- Scaffold-based reasoning (CoT, ToT, ReAct, Reflexion) — still widely used
- Inference-time compute scaling: test-time budgets, PETS, self-consistency
- Training stability for agentic RL (ARLArena, SAMPO)
- Open question: can LLMs do truly internal self-reflection?

### 4. Act
- **4.1 Tool use and MCP** — the standard interface
- **4.2 Agentic coding** — the dominant action domain
  - CLI agents: Claude Code, Codex CLI, Gemini CLI, Aider, OpenCode
  - IDE agents: Cursor, Antigravity, Windsurf, Copilot
  - General-purpose: OpenClaw, Goose
  - Cross-tool standards: SKILL.md, CLAUDE.md, AGENTS.md
  - Multi-agent coding: Agent Teams, Manager View, sub-agents
  - Case studies: Rakuten (7h autonomous, 12.5M LOC), Anthropic C compiler, TELUS (13K custom solutions)
- **4.3 Computer use and GUI agents**
- **4.4 Embodied agents and VLAs**
- **4.5 Commerce and real-world action**

### 5. Interact
- Agent-to-agent: A2A, ACP (merged), ANP
- Agent-to-tool: MCP architecture and ecosystem
- Protocol stack: the TCP/IP analogy (A2A as network layer, MCP as resource layer)
- Multi-agent orchestration patterns
- Social simulation and emergent behavior (updated)
- Agent identity, discovery, and trust

### 6. Operate
- Observability and evaluation
- Safety: prompt injection, supply chain, sandboxing, OWASP MCP Top 10
- Reliability: context rot, hallucination accumulation, self-verification
- Economics: token management, model routing, distillation
- Governance: AAIF, enterprise compliance, legal liability
- The OpenClaw cautionary tale: what happens when agents go viral without guardrails

### 7. The Virtuous Cycle (updated)
- Update Plaat et al.'s virtuous cycle diagram to include the Operate layer
- Reason feeds Act (reasoning improves tool use and coding)
- Act feeds Reason (inference-time action generates training data)
- Interact feeds Operate (multi-agent systems create governance needs)
- Operate feeds everything (reliable systems enable more ambitious agents)

### 8. Research Agenda
- **Training:** Agentic RL stability, data generation via agent action, VLA generalization
- **Internalization:** Which capabilities should be model-native vs. scaffold-based?
- **Protocol maturity:** Security, identity, provenance across MCP/A2A/ANP
- **Reliability at scale:** Context rot mitigation, long-horizon task completion
- **Economics:** Cost-performance Pareto frontier for agent fleets
- **Governance:** Legal frameworks for agent liability, cross-organizational trust
- **The skill ecosystem:** Portable skills, supply chain security, quality curation
- **Agent-to-agent emergence:** What happens when millions of agents interact via A2A?
- **Human-agent teaming:** The "mission controller" role — how does SE practice change?

### 9. Conclusion

---

## 4. Methodology

### 4.1 Literature Collection
- **Systematic search:** Semantic Scholar API + arXiv, filtered for agentic AI, agent frameworks, MCP, A2A, agentic coding (Nov 2025–May 2026)
- **Backward/forward citation tracking** from Plaat et al. and BJTU survey
- **Conference proceedings:** NeurIPS 2025, ICLR 2026, ICML 2026 (accepted papers), ACL 2026
- **Preprints:** Given the speed of the field, arXiv papers with significant community engagement (citations, GitHub stars, HuggingFace models)

### 4.2 Industry Data
- LangChain State of AI Agents Report (2025, 2026)
- Anthropic 2026 Agentic Coding Trends Report
- Gartner agentic AI projections
- Deloitte 2026 Tech Trends (agentic AI section)
- GitHub Copilot usage data, VS Code Marketplace adoption metrics

### 4.3 Framework and Tool Analysis
- Hands-on evaluation of major agentic coding tools (Claude Code, Antigravity, Codex CLI, Gemini CLI, Cursor, OpenClaw)
- Protocol specification analysis (MCP spec, A2A spec, ANP spec)
- Skill ecosystem analysis (Antigravity Awesome Skills registry, ClawHub, Claude Skills)

### 4.4 Practitioner Input
- Developer survey (optional, increases impact significantly)
- Interviews with agent framework maintainers
- Analysis of developer community discussions (GitHub Issues, Discord, Reddit, X)

---

## 5. Differentiation from Plaat et al.

| Dimension | Plaat et al. (2025) | This paper |
|-----------|-------------------|------------|
| Taxonomy | Reason, Act, Interact | Reason, Act, Interact, **Operate** |
| Framing | Research capabilities | Research + production systems |
| "Act" focus | Robotics, hypothetical assistants | **Agentic coding** as dominant domain |
| "Interact" focus | Social simulation, games | **Protocol standardization** (MCP/A2A) |
| Agent architecture | External scaffolding assumed | **Model-native vs. scaffold-based** axis |
| Evidence base | Academic papers | Papers + industry data + tool analysis |
| Safety | "Open problem" (brief) | **Full section** with real incidents (OpenClaw) |
| Coding tools | Not covered | **Central topic** (15+ tools compared) |
| Protocols | Not covered | **Central topic** (MCP/A2A/ANP/AAIF) |
| Skills/config | Not covered | **Emerging standard** (SKILL.md portability) |

---

## 6. What Makes This Publishable

### Venue options
- **JAIR** (where Plaat et al. published) — natural successor venue
- **ACM Computing Surveys** — if the scope/rigor warrants it
- **TMLR** — faster turnaround, ML-focused audience
- **NeurIPS / ICML survey track** — if they accept survey submissions
- **Blog post series or technical report** — fastest path, widest reach (especially for the agentic coding section which practitioners care about most)

### Novel contributions
1. **Four-part taxonomy** extending Plaat et al. with Operate
2. **Model-native vs. scaffold-based** as a cross-cutting analytical axis
3. **First comprehensive survey of agentic coding tools** as a category
4. **Protocol stack analysis** treating MCP/A2A/ANP as layers
5. **Production evidence integration** — industry data as first-class evidence
6. **The skills portability story** — SKILL.md as an emerging cross-tool standard (directly relevant given Antigravity Awesome Skills including Google DeepMind contributions)

---

## 7. Insider Angle: DeepMind Perspective

Given your position working on Gemini's agentic capabilities and API at DeepMind, there are angles you could bring that no external researcher can:

- **Antigravity's design philosophy:** Why agent-first IDE vs. CLI? How does Manager View relate to the multi-agent research literature?
- **A2A design decisions:** Why client-server, not peer-to-peer? How does Agent Card design reflect lessons from service discovery in distributed systems?
- **Gemini CLI's open-source bet:** Why give away 1,000 req/day for free? What's the strategic logic?
- **The skills convergence:** Antigravity Awesome Skills includes Google DeepMind contributions alongside Anthropic and OpenAI skills. What does cross-vendor skill portability mean for the ecosystem?
- **Model-native agentic capabilities in Gemini 3:** What reasoning and tool-use capabilities are now in the weights vs. in the scaffolding?

**Caveat:** Internal knowledge would need to be published only as already-public information or cleared through your publication review process. But the _framing_ — knowing which questions matter — is the real advantage.

---

## 8. Execution Plan

### Option A: Full academic paper (3–6 months)
- Literature collection and coding: 4–6 weeks
- Writing: 4–6 weeks
- Internal review and revision: 2–4 weeks
- Submission and peer review: 2–4 months
- **Total:** 5–8 months to publication

### Option B: Technical report / preprint (6–10 weeks)
- Literature collection: 2–3 weeks
- Writing: 3–4 weeks
- Internal review: 1–2 weeks
- Post to arXiv: immediate
- **Total:** 6–10 weeks

### Option C: Blog post series (2–4 weeks per post)
- Part 1: The taxonomy update (Reason, Act, Interact, Operate)
- Part 2: The agentic coding landscape
- Part 3: The protocol stack (MCP/A2A/ANP)
- Part 4: Operate — safety, reliability, governance
- Part 5: Research agenda
- **Total:** 2–3 months for full series, but Part 1 ships in 2–4 weeks

### Recommendation
Start with **Option C** (blog series) to establish the framing and get feedback, then consolidate into **Option B** (arXiv preprint) once the content is stable. The field is moving too fast for a 6-month academic publication cycle — by the time JAIR publishes, the landscape will have shifted again.

---

## 9. Open Questions for You

1. **Scope:** Should the paper cover _all_ agentic LLM applications (medicine, finance, robotics, etc.) like Plaat et al., or focus narrowly on the agentic coding + protocol layer where the most dramatic change has occurred?

2. **Co-authors:** Would you want to recruit collaborators? A DeepMind + external researcher team would have both insider and outsider perspectives.

3. **DeepMind publication process:** What's the clearance path for a survey paper that touches on Gemini capabilities, Antigravity, and A2A? A survey citing only public information should be straightforward, but worth confirming early.

4. **The Anthropic elephant:** Given that you'd be writing about Claude Code, MCP, and other Anthropic products as a DeepMind employee, how do you want to handle the competitive dynamics? The academic framing (survey, not advocacy) helps, but it's worth being intentional.

5. **Timeline pressure:** The BJTU "Model-Native Agentic AI" survey already covers some of this ground. What's your window to publish before someone else does a comprehensive update?
