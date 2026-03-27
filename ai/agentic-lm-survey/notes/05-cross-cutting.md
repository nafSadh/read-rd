# 05 · Cross-Cutting — Skills, Configuration Standards, and the Portable Agent Layer

> Deep-dive covering the emerging cross-vendor configuration and skills layer. Based on web research, documentation analysis, and synthesis across Sections 1–4.

---

## Section Overview

The most surprising development in the agentic AI ecosystem isn't any single model, benchmark, or protocol. It's the emergence of a *portable configuration layer* that works across competing vendor tools. SKILL.md files, CLAUDE.md project configs, AGENTS.md agent instructions — these seemingly mundane markdown files represent a quiet standardization that may matter more than MCP or A2A for practical adoption.

**Key numbers:**
- 1,300+ skills in Antigravity Awesome Skills (v8.6.0, March 2026)
- 22,000+ GitHub stars; 40+ named contributors; skills sourced from 20+ community repositories
- 8 AI coding tools supported from a single SKILL.md format
- Official contributions from Anthropic, Vercel Labs, OpenAI, Supabase, Microsoft, Google DeepMind, Sentry, Trail of Bits, Expo, Hugging Face
- Universal installation: `npx antigravity-awesome-skills --claude` (or `--gemini`, `--cursor`, `--codex`)

---

## The SKILL.md Format

### What It Is

A SKILL.md file is a Markdown document with YAML frontmatter that teaches an AI agent how to perform a specific workflow. It's the unit of portable agent capability.

Structure (from Google's Antigravity Codelab):
```
my-skill/
├── SKILL.md          # Definition file (required)
├── scripts/          # Optional executables
│   ├── run.py
│   └── util.sh
├── references/       # Optional docs/templates
│   └── api-docs.md
└── assets/           # Optional static assets
```

### Why It Matters

The same SKILL.md works in `.claude/skills/`, `.gemini/skills/`, `.cursor/skills/`, and `.codex/skills/` without modification. The format decouples skill content from tool-specific invocation conventions. This is the first genuine cross-vendor standard in agentic AI.

**Progressive Disclosure:** Unlike system prompts (always loaded), skills are loaded on-demand when the agent determines relevance. This optimizes context window usage — critical for agents with dozens of potential capabilities. The agent sees lightweight metadata ("menu") and loads full instructions only when needed.

### Design Philosophy

From Google's documentation: "If the Agent Manager is the brain and the Editor is the canvas, Skills are the specialized training modules." Skills occupy a middle ground between Rules (passive, always-on guardrails) and Workflows (active, user-triggered macros). Skills are *agent-triggered*: the model detects intent and dynamically equips the specific expertise required.

---

## Antigravity Awesome Skills

### The Library

The largest cross-tool skill collection. Started as a curated list, evolved into an installable library with CLI, bundles, workflows, and validation infrastructure.

**v8.6.0 (March 2026):** 1,300+ skills. 22K+ GitHub stars. MIT licensed. Official contributions from Anthropic, Vercel Labs, OpenAI, Supabase, Microsoft, Google DeepMind, Sentry, Trail of Bits, Expo, and Hugging Face.

**Key community sources:**
- rmyndharis/antigravity-skills: 300+ enterprise skills + catalog generation logic
- zebbern/claude-code-guide: ~60 security-focused skills
- VoltAgent/awesome-agent-skills: 61 high-quality skills including official team contributions

### Bundles and Workflows

**Bundles** = curated skill groups by role: Web Wizard, Security Engineer, OSS Maintainer, Full-Stack Developer, QA & Testing, DevOps & Cloud.

**Workflows** = ordered execution sequences: "Building a SaaS MVP" = Essentials + Full-Stack Developer + QA & Testing. "Hardening production" = Security Developer + DevOps & Cloud + Observability & Monitoring.

Bundles help you *choose* skills. Workflows help you *execute* them in order.

### Installation

```bash
# Universal (default: ~/.gemini/antigravity/skills)
npx antigravity-awesome-skills

# Tool-specific
npx antigravity-awesome-skills --claude   # → .claude/skills/
npx antigravity-awesome-skills --gemini   # → .gemini/skills/
npx antigravity-awesome-skills --cursor   # → .cursor/skills/
npx antigravity-awesome-skills --codex    # → .codex/skills/
npx antigravity-awesome-skills --path ./my-skills  # Custom
```

### Validation

`python3 scripts/validate_skills.py` — contributors must run before PRs. GitHub Actions workflow pinned for PRs touching SKILL.md files. Schema validation against agentskills.io specification and Anthropic best practices.

---

## CLAUDE.md — Per-Project Agent Configuration

### What It Is

Claude Code's per-project configuration file. Lives at project root. Defines:
- Coding standards and style rules
- Workflow constraints (e.g., "always run tests before committing")
- Tool access permissions
- Project-specific context and terminology
- File/directory access patterns

### Why It Matters

CLAUDE.md transforms a general-purpose agent into a project-specific one. Without it, the agent makes generic decisions. With it, the agent follows the team's established practices. This is the difference between "a senior engineer on day one" and "a senior engineer who knows the codebase."

### Adoption Beyond Claude

The concept has been adopted across tools:
- **Cursor:** `.cursorrules` (same concept, different filename)
- **GitHub Copilot:** `.github/copilot-instructions.md`
- **OpenAI Codex:** Supports `AGENTS.md`
- **Gemini CLI:** `.gemini/settings.json` + project-level instructions

The convergence toward per-project agent configuration is tool-agnostic, even though filenames differ.

---

## AGENTS.md — Standardized Agent Instructions

### What It Is

OpenAI's contribution to AAIF (donated December 2025). A standardized format for defining agent behavior, tool access, and project instructions at the repository root.

### Adoption

Adopted by Cursor, OpenAI Codex, OpenCode, and others. Complementary to CLAUDE.md — some projects ship both files for cross-tool compatibility.

### The Convergence

CLAUDE.md (Anthropic), AGENTS.md (OpenAI), `.cursorrules` (Cursor), `.github/copilot-instructions.md` (GitHub) — four different filenames doing the same thing. The skill portability layer (SKILL.md) has achieved format standardization. The config layer hasn't yet, but the semantic convergence is clear.

---

## Pi's Self-Extension Philosophy

### The Anti-Skill Approach

Pi (the engine under OpenClaw, created by Armin Ronacher of Flask fame) takes the opposite approach to skills: no MCP, no skill marketplace, no SKILL.md files.

Philosophy: "If you want the agent to do something that it doesn't do yet, you ask the agent to extend itself." Pi generates its own tools via code. This "celebrates the idea of code writing and running code" — the ultimate self-extending agent.

### Connection to Live-SWE-agent

Pi's philosophy directly parallels Live-SWE-agent's approach from Section 2: instead of pre-defined tools, let the agent create tools on the fly. Both demonstrate that self-generated capabilities can outperform pre-configured ones — but both also require sufficiently capable base models to work.

### The Security Tradeoff

Pi's approach gives maximum capability (unlimited tool creation) at maximum risk (arbitrary code execution). Claude Code's approach gives curated capability (pre-defined skills with permission scopes) at lower risk. The OpenClaw security incidents from Section 4 demonstrate what happens when Pi's philosophy meets adversarial conditions.

---

## Cross-Cutting Themes

### Theme 1: The Portable Agent Layer Is Vendor-Neutral

The most significant quiet achievement: 1,300+ skills that work across 8 competing tools via a single format. Official contributions from companies that compete on models and IDE features but cooperate on skill definitions. This is a de facto standard emerging from the community, not imposed by any standards body.

### Theme 2: Configuration > Prompting

The shift from "clever prompting" to "structured configuration" mirrors the broader software engineering trend from scripts to infrastructure-as-code. CLAUDE.md/AGENTS.md are the equivalent of Dockerfiles or Kubernetes manifests — declarative specifications of desired agent behavior that can be version-controlled, reviewed, and shared.

### Theme 3: Progressive Disclosure Solves Context Bloat

The SKILL.md format's key architectural insight: agents see a menu of skill metadata (lightweight) and load full instructions only when relevant. This prevents the "tool bloat" problem where dozens of loaded capabilities degrade reasoning performance. It's the agentic equivalent of lazy loading in software design.

### Theme 4: The Skill Supply Chain Problem

Section 4 documented the OpenClaw/ClawHub malware incidents. The same risk applies to any skill ecosystem: Antigravity Awesome Skills has 1,300+ skills from 40+ contributors and 20+ community repos. Validation scripts and GitHub Actions workflows help, but the security challenge grows with scale. The skill layer needs the same supply chain security rigor as npm/pip — but the tooling is nascent.

### Theme 5: Self-Extension vs. Pre-Configuration

Two competing philosophies: Pi/Live-SWE-agent (let agents create their own tools) vs. SKILL.md/CLAUDE.md (pre-configure agent capabilities). The evidence from Section 2 suggests self-extension produces better results (77.4% vs hand-crafted scaffolds) — but Section 4 shows pre-configuration is safer. The winning approach will likely combine both: a base of curated, signed skills with the ability to create ad-hoc tools within a sandbox.

---

## Summary: The Five Configuration Layers

| Layer | Standard | Scope | Who Controls | Security Model |
|-------|----------|-------|-------------|----------------|
| **Model Config** | System prompt | Per-model | Provider | Trusted (provider-defined) |
| **Project Config** | CLAUDE.md / AGENTS.md | Per-repo | Team | Version-controlled, reviewed |
| **Skills** | SKILL.md | Cross-project | Community | Validation scripts, emerging signing |
| **Tools (MCP)** | MCP servers | Per-integration | Developer | OAuth 2.1, AttestMCP (proposed) |
| **Agent-to-Agent** | A2A Agent Cards | Cross-org | Protocol | Capability-based discovery |

Each layer has different trust boundaries, different governance, and different security requirements. The stack is emerging organically rather than by design — but the layering is becoming clear.

---

## Paper 1 (Forward Citation): SoK: Agentic Skills — Beyond Tool Use in LLM Agents

**Jiang, Li, Deng, Ma, Wang, Wang, Yu · UTS / CSIRO Data61 · arXiv:2602.20867 · Feb 2026 · 20 pages**

### Formal Definition

The first rigorous formalization: an agentic skill is a four-tuple **S = (C, π, T, R)** where:
- **C**: Applicability condition — predicate determining if skill is appropriate for current context
- **π**: Executable policy — mapping from observations/history to actions or skill invocations (NL, code, learned controller, or hybrid)
- **T**: Termination condition — when the skill has completed relative to current goal
- **R**: Reusable callable interface — (name, params, returns)

This distinguishes skills from tools (atomic, no internal decision-making), plans (one-time, session-scoped), episodic memory (retrieval, no execution), and prompt templates (static text, no termination logic).

### Seven Design Patterns

| # | Pattern | Representative Systems | Primary Risk |
|---|---------|----------------------|-------------|
| 1 | Metadata-driven progressive disclosure | Claude Code, Semantic Kernel, LangChain | Metadata poisoning |
| 2 | Code-as-skill (executable scripts) | Voyager, CodeAct, SWE-agent | Code injection |
| 3 | Workflow enforcement | TDD agents, LATS | Rule bypass via prompt injection |
| 4 | Self-evolving skill libraries | Voyager, DEPS, CRADLE | Skill drift; poisoned distillation |
| 5 | Hybrid NL+code macros | Claude skills, ReAct prompts | Inconsistent interpretation |
| 6 | Meta-skills (skills that create skills) | Self-Instruct, skill generators | Recursive error amplification |
| 7 | Plugin/marketplace distribution | GPT Store, MCP servers, ClawHub | Malicious packages (ClawHavoc) |

### Skill Lifecycle Model

Seven stages: Discovery → Practice → Distillation → Storage → Composition → Evaluation → Update. Maps 24 systems across these stages (Table 2 in paper). Key insight: most systems only cover 3-4 stages; no system covers the full lifecycle.

### ClawHavoc Case Study

Detailed analysis of the OpenClaw/ClawHub malicious skills incident. Grounded in the Pattern 7 (marketplace) risk profile. Used to motivate the trust-tiered execution model.

### Security and Governance

Supply-chain risks, prompt injection via skill payloads, trust-tiered execution. Pattern-specific risk matrix showing which design patterns are vulnerable to which attack types.

---

## Paper 2 (Forward Citation): Agent Skills Survey — Architecture, Acquisition, Security

**Xu, Yan · Zhejiang University · arXiv:2602.12430 · Feb 2026 · 12 pages**

### SKILL.md Progressive Disclosure Architecture

Three-level loading:
- **Level 1 (Always loaded):** YAML frontmatter metadata (~30 tokens/skill). Acts as menu for intent matching.
- **Level 2 (On trigger):** Full SKILL.md body (200–2K tokens). Injected when skill matches user intent.
- **Level 3 (On demand):** Scripts, references, assets. Loaded only if Level 2 instructions call for them.

This is the first paper to formally document the progressive disclosure architecture with token cost estimates.

### Skills + MCP Complementarity

| Dimension | Agent Skills | MCP |
|-----------|-------------|-----|
| Primary role | Procedural knowledge | Tool connectivity |
| Unit | Directory w/ SKILL.md | Server w/ endpoints |
| Loaded by | Agent on trigger | Client on config |
| Modifies | Context + permissions | Available tools/data |
| Spec status | Open std (Dec 2025) | Linux Found. (Dec 2025) |

"Skills and MCP are not competing standards but orthogonal layers of an emerging agentic stack."

### Skill Acquisition Taxonomy

| Method | Representative Work | Key Result |
|--------|-------------------|------------|
| Human-authored | Anthropic Skills | 62K+ GitHub stars |
| RL with skill library | SAGE (GRPO + sequential rollout) | +8.9% on AppWorld, -59% tokens |
| Autonomous exploration | SEAgent | 11.3% → 34.5% success on OSWorld |
| Structured skill base | CUA-Skill | 57.5% SOTA on WindowsAgentArena |
| Compositional synthesis | Agentic Proposing | 91.6% on AIME 2025 (30B solver) |

### Skill Trust and Lifecycle Governance Framework

Original contribution: maps four skill acquisition pathways through a four-stage verification pipeline (G1–G4) to four trust tiers (T1–T4) determining deployment permissions via least privilege. Empirical motivation from three independent security studies.

### Security Statistics

- **26.1% of community skills contain vulnerabilities** (42,447 skills analyzed via SkillScan)
- 14 distinct vulnerability patterns across 4 categories
- **157 confirmed malicious skills with 632 vulnerabilities** (behavioral verification of 98,380 skills)
- Skills with executable scripts: **2.12× more likely to contain vulnerabilities**
