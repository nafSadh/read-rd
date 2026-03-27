# 03 · INTERACT — Protocols & Multi-Agent Systems

> Deep-dive literature excerpt for survey section. Based on reading 5 papers totaling ~106 pages + protocol specs + industry sources.

---

## Section Overview

Plaat et al.'s "Interact" category treated multi-agent systems as a research topic — Generative Agents, social simulations, game-playing. By March 2026, interaction has become primarily an engineering and governance problem. The defining development: standardized protocols (MCP, A2A, ACP, ANP) now govern how agents talk to tools, how agents talk to each other, and how they're discovered and authenticated. The Linux Foundation's Agentic AI Foundation (AAIF) — co-founded by OpenAI, Anthropic, Google, Microsoft, AWS, and Block — governs these standards.

Simultaneously, multi-agent orchestration has moved from academic design patterns to production architectures. Graph-based "flow engineering" replaces open-ended chat loops. Difficulty-aware routing assigns different LLMs to different parts of a workflow based on query complexity. And empirical evidence shows multi-agent systems achieve deterministic quality impossible with single agents.

**Key numbers:**
- MCP: 97M+ monthly SDK downloads by Feb 2026 (Python + TypeScript)
- A2A: Adopted by Google, Microsoft, AWS, IBM; merged with ACP Aug 2025
- AAIF: Co-founded Dec 2025 by 6 major AI companies under Linux Foundation
- Multi-agent orchestration: 100% actionable vs 1.7% single-agent; 80× specificity improvement
- DAAO: +3.2–10.2% accuracy at 41% inference cost vs baselines
- 500+ works synthesized in collaboration mechanisms survey

---

## Paper 1: A Survey of Agent Interoperability Protocols (MCP, ACP, A2A, ANP)

**Ehtesham, Singh, Gupta, Kumar · Kent State / Cleveland State / Youngstown State / Northeastern · arXiv:2505.02279v2 · May 2025 · 21 pages**

### The N×M Integration Problem

Before protocols, connecting N AI models to M external tools required N×M custom integrations. Ten models, ten tools = 100 integrations. Each fragile, each proprietary, each a maintenance burden. The four protocols solve this at different layers.

### MCP (Model Context Protocol) — Agent-to-Tool

Launched by Anthropic November 2024. JSON-RPC 2.0 client-server interface.

**Architecture:** Three-layer stack.
- **Protocol layer:** JSON-RPC 2.0 message semantics (requests, results, errors, notifications)
- **Transport layer:** Local via Stdio, network via HTTP + Server-Sent Events (SSE)
- **Capability layer:** Four core primitives:
  - **Tools** (model-controlled): LLM invokes external APIs/services, sometimes with user approval
  - **Resources** (application-controlled): Structured documents/datasets selected by the client app
  - **Prompts** (user-controlled): Reusable interaction templates for consistent behavior
  - **Sampling** (server-initiated): Server can request text generation from the LLM

**Lifecycle security threats (Table 3 in paper):**
- **Creation phase:** Installer spoofing, supply-chain backdoors, name collision, no auth handshake
- **Operation phase:** Tool poisoning, credential theft, sandbox escape, remote access control, command injection, tool redefinition ("rug pull"), cross-server shadowing
- **Update phase:** Version rollback, config drift
- Mitigations: SBOMs, digital signatures, OAuth 2.1 + PKCE, syscall filters, AppArmor, scoped namespaces

### A2A (Agent-to-Agent Protocol) — Agent-to-Agent

Launched by Google April 2025. Donated to Linux Foundation June 2025. Merged with IBM's ACP August 2025.

**Core concept: Agent Cards.** High-level descriptors capturing overall agent capabilities — not detailed tool lists, but what the agent can *do*. Enables discovery without exposing implementation.

**Task lifecycle:** Discovery (client reviews Agent Cards, selects remote agent) → Authorization (secure access, permission scoping) → Communication (tasks dispatched via HTTPS, JSON-RPC envelope, SSE for streaming)

**Key features:**
- Peer-to-peer delegation: Direct task handoffs without centralized bottlenecks
- Dynamic negotiation: Propose, accept, counter-offer workflows
- Streamed information: Real-time synchronization of event logs and agent states
- Standardized identity: Unified agent addressing and cryptographic identity

### ACP (Agent Communication Protocol) — IBM → Merged into A2A

REST-native messaging with MIME-typed multipart messages. Supports both synchronous and asynchronous interactions. Lightweight, runtime-independent. Merged into A2A August 2025 when IBM contributed it to the Linux Foundation.

### ANP (Agent Network Protocol) — Peer-to-Peer

The most decentralized option. Uses W3C Decentralized Identifiers (DIDs) and JSON-LD graphs for open-network agent discovery. Unlike A2A's client-server model, ANP enables peer-to-peer communication between agents on the same network without centralized infrastructure.

### Phased Adoption Roadmap

The paper proposes a practical deployment sequence:
1. **Start with MCP** for tool integration (most mature, highest adoption)
2. **Add A2A** when cross-agent collaboration is needed
3. **Layer ACP** for multimodal or REST-heavy environments
4. **Integrate ANP** for fully decentralized, cross-organizational agent networks

### The Protocol Stack Analogy

The Cisco blog and Subhadip Mitra's analysis both frame this as the TCP/IP moment for agentic AI:
- **MCP = resource layer** (like HTTP for content)
- **A2A = network layer** (like TCP for reliable delivery)
- They compose, not compete. MCP for precise tool-level execution, A2A for scalable agent-level routing.

LangGraph v0.2 (shipped January 2026) added A2A and MCP as first-class protocol targets. AgentMaster (July 2025) was the first framework to use both in production.

---

## Paper 2: Multi-Agent Collaboration Mechanisms: A Survey of LLMs

**Tran, Dao, Nguyen, Pham, O'Sullivan, Nguyen · UCC / Pusan NU / Trinity College Dublin · arXiv:2501.06322 · Jan 2025 · 35 pages**

### The Collaboration Framework

This survey's core contribution is a five-dimensional framework for characterizing multi-agent collaboration:

**1. Actors:** Who is involved? Homogeneous agents (same LLM, different prompts) vs. heterogeneous (different models, different capabilities). The trend is toward heterogeneity.

**2. Types:**
- **Cooperation:** Agents work toward shared goals. Most common in task-solving systems.
- **Competition:** Agents oppose each other (debate, adversarial verification). Used for improving reasoning quality.
- **Coopetition:** Agents cooperate on some dimensions while competing on others. Least studied but arguably most realistic.

**3. Structures:**
- **Centralized:** Single coordinator manages all agents (AutoGen with human-in-the-loop)
- **Decentralized/Peer-to-peer:** Agents communicate directly without hierarchy (CAMEL's inception prompting)
- **Hierarchical:** Supervisor-worker patterns with delegation chains (MetaGPT's SOP-based waterfall)

**4. Strategies:**
- **Role-based:** Fixed roles assigned upfront (Product Manager, Engineer, Tester in ChatDev)
- **Rule-based:** Turn-taking, voting, structured workflows
- **Model-based:** RL or learning-based coordination (DyLAN's importance-scored routing)

**5. Coordination protocols:** How agents actually exchange information — message passing, shared memory/documents, structured handoffs, debate formats.

### Key Applications

The survey covers applications across 5G/6G networks, Industry 5.0, question answering, and social/cultural simulation. The breadth demonstrates that multi-agent collaboration isn't just an AI research topic — it's being adopted across engineering and social science domains.

### Gap from Our Perspective

This survey focuses on collaboration *mechanisms* but doesn't cover the *protocol standardization* wave (MCP/A2A were just emerging when it was written in Jan 2025). The interplay between academic multi-agent design patterns and production protocol infrastructure is the central theme of our INTERACT section.

---

## Paper 3: Multi-Agent LLM Orchestration for Incident Response

**Drammeh · Independent · arXiv:2511.15755v2 · Jan 2026 · 10 pages**

### The Experiment

348 controlled trials comparing single-agent vs. multi-agent LLM orchestration on an identical incident scenario (auth-service failure with database connection pool exhaustion). All using TinyLlama (1B parameters) to enable consumer-hardware reproducibility.

**Single-agent setup:** One LLM call with a comprehensive prompt asking for diagnosis, remediation, and risk assessment simultaneously.

**Multi-agent setup:** Three sequential, focused agents:
1. **Diagnosis Specialist:** Analyzes telemetry, identifies root cause
2. **Remediation Planner:** Given root cause, generates specific remediation steps with exact commands
3. **Risk Assessor:** Evaluates risks of proposed actions given production context

A non-LLM coordinator aggregates the three outputs into a structured incident brief.

### The Decision Quality (DQ) Metric

A novel three-component metric:
- **Validity** (V): Are actions technically feasible? (Both systems achieve 1.0)
- **Specificity** (S): Contains concrete identifiers? Version numbers, exact commands like `kubectl rollout undo`? (Single: 0.007, Multi: 0.557 — an 80× improvement)
- **Correctness** (R): Alignment with ground truth via token overlap? (Single: 0.003, Multi: 0.417 — a 140× improvement)

### The Core Result

| Metric | Single-Agent | Multi-Agent |
|--------|-------------|-------------|
| Actionable (DQ > 0.5) | 1.7% | **100%** |
| Quality variance | σ = 0.023 | **σ ≈ 0** |
| Latency | 41.61s | 40.31s |
| DQ Score | 0.403 | **0.692** |

**The value is quality and determinism, not speed.** Both systems take ~40 seconds. But multi-agent produces 100% actionable recommendations with zero variance, while single-agent produces vague "check logs" recommendations 98.3% of the time.

**The reframing:** Multi-agent orchestration isn't a performance optimization — it's a production-readiness requirement. If you need reliable, specific, actionable outputs, a single agent fundamentally cannot deliver them, regardless of model size.

### Limitations

Single incident scenario, single model (TinyLlama 1B), automated evaluation only. Phase 2 (Q1-Q2 2026) will test generalization across incident types, model scales, and human expert evaluation. But the architectural insight — decomposition produces determinism — is likely robust.

---

## Paper 4: Difficulty-Aware Agentic Orchestration (DAAO)

**Su, Lan, Xia et al. · SCNU / UT Health / HKUST(GZ) / UCSD / PKU / U Toronto · WWW '26 · 12 pages**

### The Problem with Static Workflows

Existing multi-agent systems are either:
- **Task-level:** Same heavy pipeline for every query. Over-processes simple questions. Wastes compute.
- **Query-level (MaAS):** Input-specific adaptation, but granularity is insufficient for hard queries.
- **LLM-homogeneous:** Single model backbone for all agents. Misses the complementary strengths of different models.

### The DAAO Architecture

Three interdependent modules, all conditioned on a latent difficulty embedding z:

**1. Difficulty Estimator (VAE):** Maps each query to a k-dimensional latent difficulty representation using a variational autoencoder. No manual difficulty labels needed — learns from workflow success/failure via a self-adjusting policy. Higher d → more complex workflow; lower d → simpler.

**2. Operator Allocator:** Selects which agentic operators (reasoning tools) to activate per workflow layer. Uses cumulative confidence thresholding — operators activated in descending score order until evidence exceeds threshold τ. Adaptive layer width: high confidence = more operators; low = fewer.

**3. LLM Router:** Pairs each selected operator with the optimal LLM from a candidate set. Uses temperature-scaled softmax over model candidates, conditioned on query difficulty and operator context. This enables heterogeneous LLM usage — expensive models for hard subtasks, cheap models for easy ones.

### Results

Tested on six benchmarks: GSM8K, MATH (math); HumanEval, MBPP (code); GAIA, HotpotQA (general reasoning).

- **Accuracy:** Surpasses prior multi-agent systems by 3.2–10.2%
- **Cost:** Uses only 41% of the inference cost and 64% of the training cost vs. best baselines
- **Generalization:** Strong transfer to unseen LLM backbones and across datasets

The key insight: matching workflow complexity to query difficulty is more important than having a uniformly powerful pipeline. Simple queries should get simple workflows with cheap models. Hard queries get complex workflows with expensive models. This requires *knowing* the difficulty before solving the problem — hence the VAE.

---

## Paper 5: Agentic AI — Architectures, Taxonomies, and Evaluation

**Arunkumar, Gangadharan, Buyya · Anna University / NIT / U Melbourne · arXiv:2601.12560 · Jan 2026 · 28 pages**

### The Unified Architecture

The paper proposes A = ⟨S, O, M, T, π⟩ — a POMDP-based agent control loop with:
- **Perception (Φ):** Multimodal observation from partial environment state
- **Memory Update (μ):** Persistent context across interactions (vector DBs, RAG)
- **Reasoning/Planning (ρ):** From linear CoT to native inference-time reasoning models
- **Action Policy (π):** Conditioned on reasoning trace, grounded in internal plan

### Multi-Agent Framework Comparison (Table 5)

A comprehensive comparison of production frameworks:

| Framework | Topology | Role Structure | Communication | Ideal Use |
|-----------|----------|---------------|---------------|-----------|
| CAMEL | 1-to-1 mesh | Symmetric | Inception prompting | Ideation |
| AutoGen | Star or mesh | Dynamic | Message passing | Prototyping tools |
| MetaGPT | Chain (waterfall) | Static SOP roles | SOP documents | Complex SE |
| ChatDev | Chain | Static phases | Waterfall handoffs | App generation |
| DyLAN | Dynamic graph | Dynamic selection | LLM-optimized routing | Focused reasoning |
| LangGraph | Workflow graph | Developer-defined | State machine | Production flow |
| Swarm | Star with handoffs | Lightweight specialists | Handoff routines | Controllable coordination |
| MAKER | Hierarchical | Supervisor+worker | Cross-examination | High-reliability logic |

### The Flow Engineering Shift

The paper identifies a critical industry trend: from "open-ended multi-agent chat loops toward explicit workflow graphs." LangGraph is the exemplar — agent execution as graph traversal with explicit state, typed transitions, and developer-defined guardrails.

This is the "controllable orchestration" paradigm: developers specify state transitions and guardrails; models fill in local decisions. It prioritizes debuggability, checkpointing, and human approvals over full autonomy.

### MCP and Computer Use

The paper treats MCP as the standardized connector layer replacing ad-hoc function calling. It notes that "standardized connector layers (e.g., MCP) further increase the need for governance at integration boundaries, including allowlists, authentication, and audit logging."

On computer use: agents interpreting screenshots and executing mouse/keyboard actions represent "high-bandwidth observation channels" that amplify prompt injection risk. The attack surface grows linearly with the richness of the agent's sensory interface.

### CLASSic Evaluation

The paper proposes evaluating agents across five dimensions:
- **C**ost: Inference spend, API calls, total compute
- **L**atency: Time to completion, including async delays
- **A**ccuracy: Task success including multi-step and tool-use scenarios
- **S**ecurity: Prompt injection resistance, tool permission enforcement
- **S**tability: Run-to-run variance, failure mode distribution

---

## Industry: The Protocol Governance Story

### AAIF (Agentic AI Foundation) — December 2025

The Linux Foundation launched AAIF co-founded by OpenAI, Anthropic, Google, Microsoft, AWS, and Block. It governs three foundational projects:
- **MCP** (from Anthropic): Agent-to-tool communication
- **Goose** (from Block): Open-source AI developer agent
- **Agents.md** (from OpenAI): Agent configuration standard

A2A was separately contributed to the Linux Foundation in June 2025 and merged with IBM's ACP in August 2025.

This is historically significant: six competing AI companies agreed to co-govern interoperability standards under neutral governance. The closest analogy is the early web standards process (W3C, IETF), but compressed into months rather than years.

### Emerging Protocols (2026)

- **UCP (Universal Commerce Protocol):** Google. Agent-to-business payments and commerce.
- **AP2 (Agent Payments Protocol):** Google. Works with A2A and MCP servers for agent-made payments within guardrails.
- **A2UI (Agent-to-User Interface):** Anthropic. Standardizing how agents present results to users.

### Adoption Numbers (Feb 2026)

- MCP: 97M+ monthly SDK downloads (Python + TypeScript combined)
- Every major AI provider has adopted MCP: Anthropic, OpenAI, Google, Microsoft, Amazon
- A2A: Growing but slower adoption curve than MCP
- LangGraph v0.2: First-class A2A + MCP protocol targets
- Google's ADK (Agent Development Kit): Native support for both

---

## Cross-Cutting Themes

### Theme 1: Interaction Is Now an Infrastructure Problem

Plaat et al. treated interaction as a research question (can agents collaborate? what emergent behaviors arise?). By 2026, interaction is an infrastructure question: what protocols do agents speak, who governs the standards, how are agents discovered and authenticated, and what happens when a malicious agent enters the network?

### Theme 2: The Compose-Not-Compete Pattern

MCP and A2A are not competing protocols — they operate at different layers and compose. MCP for tool-level precision, A2A for agent-level routing. This is the TCP/IP lesson: you need multiple protocols at different layers, not one protocol to rule them all.

### Theme 3: Flow Engineering > Full Autonomy

The production shift is toward controllable orchestration (LangGraph-style state machines) rather than fully autonomous agent loops. Developers define the control structure; agents fill in local decisions. This trades theoretical capability for practical reliability.

### Theme 4: Heterogeneous > Homogeneous

DAAO demonstrates that matching different LLMs to different subtasks based on difficulty produces better results at lower cost. The future isn't one big model doing everything — it's orchestrated fleets of specialized models.

---

## Reading List by Priority

**Must-read:**
1. Ehtesham et al. "A Survey of Agent Interoperability Protocols" — the only paper covering all four protocols
2. Drammeh "Multi-Agent LLM Orchestration" — empirical proof that decomposition produces determinism

**Important:**
3. Tran et al. "Multi-Agent Collaboration Mechanisms" — most comprehensive collaboration taxonomy
4. Su et al. "DAAO" (WWW '26) — difficulty-aware routing with heterogeneous LLMs
5. Arunkumar et al. "Agentic AI Architectures" — unified taxonomy with CLASSic evaluation framework

**Industry sources:**
6. Cisco blog "MCP and A2A: A Network Engineer's Mental Model" — the compose-not-compete framing
7. Mitra "The Agent Protocol Stack" — TCP/IP analogy, security gaps
8. The Register "Deciphering the alphabet soup" — MCP/A2A/ACP/ANP landscape overview
