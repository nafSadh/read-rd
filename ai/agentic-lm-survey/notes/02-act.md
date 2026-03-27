# 02 · ACT — Agentic Coding & Tool Use

> Deep-dive literature excerpt for survey section. Based on reading 7 papers + industry sources totaling ~150 pages of academic content + extensive tool/report analysis.

---

## Section Overview

"Act" is the most dramatically transformed pillar since Plaat et al. In their 2025 survey, acting meant robotics, hypothetical assistants, and tool-use demos. By March 2026, the dominant action domain is software development — agents writing, testing, debugging, and deploying code. This section covers the benchmarking ecosystem that measures these capabilities, the self-improving agents that push the frontier, and the production tools that millions of developers use daily.

**Key numbers from the literature:**
- SWE-Bench Pro: 1,865 problems across 41 repos, 123 languages; best model <45% Pass@1
- SWE-EVO: GPT-5 achieves only 21% (vs 65% on SWE-Bench Verified) on long-horizon evolution tasks
- Live-SWE-agent: 77.4% on SWE-Bench Verified — state-of-the-art, zero offline training cost
- UTBoost: Found 345 erroneous patches mislabeled as passing in original SWE-Bench
- RepoNavigator: 7B model outperforms 14B baselines; single "jump" tool + RL
- Claude Code: $1B ARR by Nov 2025; leads VS Code Marketplace for agent extensions
- Anthropic report: Engineers use AI in 60% of work, fully delegate only 0–20%

---

## Paper 1: SWE-Bench Pro — Long-Horizon Enterprise SE

**Deng, Da et al. (22 authors) · Scale AI · arXiv:2509.16941v2 · Nov 2025 · 20 pages**

### The Problem with SWE-Bench

The original SWE-Bench (2023) and SWE-Bench Verified (2024) have a critical flaw: 161 out of 500 problems require only 1–2 line modifications. Industrial software engineering demands multi-file modifications spanning hundreds of lines. The benchmark doesn't reflect real work.

### What SWE-Bench Pro Does Differently

**Scale and diversity:** 1,865 problems from 41 actively maintained repositories spanning Python, JavaScript, TypeScript, and Go. Business applications, B2B platforms, and developer tools.

**Three-tier access control for contamination resistance:**
- Public set: 731 instances from copyleft-licensed (GPL) repos, openly available
- Commercial set: 276 problems from startup codebases (purchased engineering repos), results public but code private
- Held-out set: 858 problems, entirely private, reserved for future overfitting checks

**Task complexity:** All problems require substantial, multi-file modifications. Average reference solution: 107.4 lines of code across 4.1 files. Minimum 10 lines of change; 100+ tasks exceed 100 lines.

**Human augmentation:** Every problem includes human-verified task descriptions with requirements and interface specifications. Without these augmentations, model performance drops dramatically (GPT-5: 25.9% → 8.4%; Claude Opus 4.1: 22.7% → 8.2%).

### Key Results

Under a unified scaffold (SWE-Agent), best performance remains **below 45% Pass@1**. Failure mode analysis reveals:
- Claude Opus 4.1: 74.2% submission rate, but 50.3% of submissions are wrong solutions, 31.3% incorrect instruction following
- GPT-5: Only 27.2% submission rate; 96.4% of non-submitted cases are "stuck in loop"
- Performance degrades sharply beyond 3-file problems; the gap between frontier and smaller models widens dramatically with file count

**Programming language matters:** Go and Python show higher resolve rates. JavaScript/TypeScript are more variable. Repository-specific factors (complexity, documentation quality) significantly impact performance.

---

## Paper 2: SWE-EVO — Software Evolution Benchmarking

**Thai, Le, Nguyen, Phan, Bui · FPT Software AI Center / U. Melbourne · arXiv:2512.18470v4 · Jan 2026 · 27 pages**

### The Core Insight

SWE-Bench tests single-issue resolution. Real software engineering is 80% maintenance and evolution — iterative modifications across interdependent modules, versions, and specifications. SWE-EVO tests this.

### Construction

Built from release notes and version histories of 7 mature open-source Python projects (scikit-learn, pydantic, dask, dvc, requests, modin, conan). 48 evolution tasks requiring agents to interpret release notes and implement comprehensive changes spanning multiple PRs, features, and bug fixes to evolve a codebase to a new version.

**Scale comparison with SWE-Bench (mean values):**
- Issue text length: 2,390 words vs 195 words
- Gold patch lines edited: 610 vs 32
- Gold patch files edited: 21 vs 1.7
- Gold patch functions edited: 51 vs 3
- Fail-to-pass tests: 81 vs 9
- Total tests per instance: 874 vs 121

### The Capability Gap

**GPT-5 with OpenHands achieves only 21% on SWE-EVO versus 65% on SWE-Bench Verified.** This is the most striking result: a 44 percentage-point drop from single-issue to evolution tasks.

Results with release note + PR/issue context:
| Model | SWE-EVO (OpenHands) | SWE-EVO (SWE-agent) | SWE-Bench Verified |
|-------|---------------------|----------------------|--------------------|
| GPT-5 (medium) | 18.75% | 20.83% | 65.00% |
| GPT-5-mini | 10.42% | 10.42% | 59.80% |
| DeepSeek-R1 | 10.42% | 8.33% | 57.60% |
| GLM-4p5 | 16.67% | 16.67% | 54.20% |
| Kimi-K2 | 16.67% | 18.75% | 43.80% |

**Failure mode analysis:** Stronger models primarily fail on instruction following (misinterpreting nuanced release notes). Weaker models fail on tool use and syntax. SWE-EVO's difficulty is semantic reasoning, not interface competence.

**Difficulty correlates with PR count:** Instances never solved (r=0) average 14.84 PRs. Instances solved by 10+ models average only 1.67 PRs.

### Fix Rate Metric

Binary resolved/not-resolved misses partial progress. SWE-EVO introduces Fix Rate: what fraction of failing tests does the agent actually fix? GPT-5 gets 27.64% Fix Rate vs 18.75% Resolved — meaning it makes meaningful partial progress even when it doesn't fully solve the task.

---

## Paper 3: SWE-bench Goes Live!

**Zhang, He, Zhang et al. · Microsoft · arXiv:2505.23419v2 · Jun 2025 · 24 pages**

### The Problem

SWE-Bench hasn't been updated since release. Only 12 repositories. Heavy manual effort for construction. This creates contamination risk and limits diversity.

### REPOLAUNCH Pipeline

A fully automated pipeline for benchmark construction:
1. **Repository selection:** Start with 8,577 Python repos with 1,000+ stars → filter to 3,316 with sufficient activity → 2,609 with valid open-source licenses
2. **Issue-PR pair extraction:** Automatic crawling of issue-resolution pairs
3. **Automated environment setup:** REPOLAUNCH — an agentic approach using LLMs to read README files, CI configs, and auto-configure Docker environments
4. **Test validation:** Multiple rounds of execution to verify consistent issue-resolving behavior

### Result

1,319 tasks from 93 repositories — 7.75x more repos than SWE-Bench. All from issues created since 2024, ensuring no contamination from pre-training data. Each task comes with a dedicated Docker image.

**Key finding:** State-of-the-art models show a "substantial performance gap compared to static benchmarks like SWE-bench, even under controlled evaluation conditions." This suggests existing models may be overfitting to the static benchmark, underscoring the importance of live, continuously updated evaluation.

---

## Paper 4: Saving SWE-Bench — Benchmark Mutation

**Garg, Steenhoek, Huang · Microsoft · arXiv:2510.08996v4 · CAIN '26 conference · 11 pages**

### The Core Problem

GitHub issues (which SWE-Bench uses) don't reflect how developers actually communicate with chat-based coding agents. Analysis of telemetry from a popular coding agent reveals dramatic differences:

- **User queries:** 10–30 words, succinct, share error stacks and file paths
- **GitHub issues:** 100+ words, contain reproduction code, expected behavior, environment details

Users communicate more with targeted information (file paths, error stacks) rather than providing exhaustive context upfront.

### Benchmark Mutation Method

Transform formal GitHub issue descriptions into realistic user-style queries using systematic analysis of developer interaction patterns. This creates "mutated" benchmarks that better reflect actual usage.

### Results

**Existing benchmarks overestimate agent capabilities by 20–50%** for public datasets. The performance gap narrows to 10–16% for internal benchmarks (SWE-Bench C#), suggesting SWE-Bench Verified suffers not only from over-specification but also overfitting.

This is a methodological contribution: any benchmark can be "mutated" to be more realistic by transforming formal task descriptions into user-style queries based on telemetry patterns.

---

## Paper 5: UTBoost — Testing the Testers

**Yu, Zhu, He, Kang · CUHK-Shenzhen / UIUC · arXiv:2506.09289 · Jun 2025 · 13 pages**

### The Problem

SWE-Bench's manually written test cases are often insufficient. Generated patches can pass all tests without actually resolving the underlying issue. The evaluation pipeline's regex-based parser also fails to handle many test cases.

### UTBoost Framework

1. **UTGenerator:** LLM-driven test case generator that analyzes codebases and dependencies to generate additional test cases. Uses three-level localization (file → function/class → line) to provide rich context to the LLM.

2. **Intramorphic testing:** Compare behavior of gold patch (P) and generated patch (P') on both original tests (T_orig) and augmented tests (T_aug). If P(T_aug) ≠ P'(T_aug), flag as suspicious.

3. **Parser fixes:** Improved the original SWE-Bench regex parser to handle multi-line test cases and other defects.

### Impact

- Found **36 task instances with insufficient test cases**
- Uncovered **345 erroneous patches** incorrectly labeled as passed in original SWE-Bench
- These corrections impact **40.9% of SWE-Bench Lite** and **24.4% of SWE-Bench Verified** leaderboard entries
- Result in **18 and 11 ranking changes** respectively
- Amazon-Q-Developer-Agent's #1 ranking on SWE-Bench Verified was affected

This paper is a reality check: the benchmark the entire field relies on has systematic evaluation errors that inflate reported capabilities.

---

## Paper 6: Live-SWE-agent — Self-Evolving on the Fly

**Xia, Wang, Yang, Wei, Zhang · UIUC · arXiv:2511.13646v3 · Nov 2025 · 20 pages**

### The Key Idea

Software agents are themselves software that can be modified. Instead of manually designing agent scaffolds or doing expensive offline evolution (DGM costs ~$22,000 per SWE-bench run), let the agent create and use custom tools on the fly as it solves problems.

### Architecture

Live-SWE-agent starts with the most basic scaffold: mini-SWE-agent with only bash tools. For each problem, the agent:
1. Reads the issue description
2. Begins working with basic bash commands
3. **Reflects** on its trajectory and decides if a custom tool would help
4. Creates executable scripts as custom tools (search tools, analyzers, diff checkers)
5. Uses those tools to solve the remaining problem
6. Submits a patch

The reflection step is critical — without it, agents don't spontaneously create useful tools.

### Results

**SWE-bench Verified (state-of-the-art, no test-time scaling):**
| Scaffold | LLM | Resolved | Cost |
|----------|-----|----------|------|
| mini-SWE-agent | Gemini 3 Pro | 74.2% | $0.46 |
| **Live-SWE-agent** | **Gemini 3 Pro** | **77.4%** | **$0.48** |
| mini-SWE-agent | Claude 4.5 Sonnet | 70.6% | $0.56 |
| **Live-SWE-agent** | **Claude 4.5 Sonnet** | **75.4%** | **$0.68** |

**vs. Offline self-improving agents (60-problem subset):**
| Method | LLM | Resolved | Offline Cost |
|--------|-----|----------|-------------|
| SICA | GPT-5-Mini | 50.0% | infinite loop |
| DGM | GPT-5-Mini | 53.3% | 1,231 hours |
| HGM | GPT-5-Mini | 56.7% | 512 hours |
| **Live-SWE-agent** | **GPT-5-Mini** | **65.0%** | **0 hours** |

**SWE-Bench Pro:** 45.8% with Claude 4.5 Sonnet — best known solve rate, outperforming SWE-agent (43.6%) which has ~7,000 lines of handcrafted code.

### Tool Analysis

The tools agents create are diverse: edit, view, search tools with variations per problem, plus unique issue-specific tools (e.g., a Go static analyzer for the openlibrary codebase). Different repositories and languages generate different tool profiles.

**Model capability matters:** GPT-5-Nano *hurts* performance with Live-SWE-agent — it can't understand the goal of tool creation and gets stuck in loops. Improvement scales with model capability: Claude 4.5 Sonnet shows +22.6% relative improvement over base mini-SWE-agent.

### Significance

Live-SWE-agent demonstrates that the optimal agent scaffold is not fixed — it should adapt per-problem, per-repository, and per-language. This aligns with the broader model-native thesis: agent capabilities should be learned/generated, not hard-coded.

---

## Paper 7: One Tool Is Enough (RepoNavigator)

**Zhang, Duan, Zhang, Xu, Wang, Liang, Li, Liang, Xia, Huang, He, Wu · Peking U / Zhongguancun Academy / Baidu · arXiv:2512.20957 · Jan 2026 · 25 pages**

### The Insight

Existing code localization agents use multiple tools (SearchClass, SearchMethods, GetImports) that operate on high-level abstractions. But these abstractions disappear after compilation — code actually executes via sequential operations and jumps. Modern LLMs already handle sequential dependencies well. What they need help with is jumping across the repository.

### RepoNavigator

A single tool: **jump** — retrieves the precise definition of a given symbol using a language server (Pyright for Python). The agent navigates the repository by following symbol definitions, like tracing execution flow.

The tool uses:
- Syntactic analysis (AST parsing)
- Lexical scope resolution (Python's LEGB rule)
- Static type inference
- Import dependency graph

**Trained end-to-end via RL** directly from a base pretrained model, without relying on closed-source distillation. Uses verifiable rewards (string-level comparison of localization outputs).

### Results

- **7B model outperforms 14B baselines**
- **14B model surpasses 32B competitors**  
- **32B model exceeds closed-source models including GPT-5 on most metrics**

This is a striking efficiency result: a structurally grounded single tool + RL training beats multi-tool agents with much larger models. It validates both the "one good tool" philosophy and the agentic RL training approach from Section 1.

---

## Industry: Agentic Coding Tools Landscape (March 2026)

### Claude Code (Anthropic)
- **$1B ARR by Nov 2025.** Leads VS Code Marketplace for "agent" extensions.
- **Agent Teams:** Opus 4.6 enables parallel sub-agents — orchestrator decomposes task, workers handle separate parts, results merged.
- **CLAUDE.md:** Per-project configuration defining coding standards, workflow rules, tool access.
- **MCP-native:** Full Model Context Protocol integration for tool/data source connections.
- Case studies: Rakuten (7h autonomous, 12.5M LOC, 99.9% accuracy), TELUS (13K custom AI solutions, 30% velocity increase), CRED (2x speed).

### Google Antigravity
- **Agent-first IDE** (VS Code fork). Launched Nov 2025 alongside Gemini 3.
- **Manager View:** Control center for orchestrating multiple agents in parallel workspaces. Key differentiator from CLI tools.
- **Artifacts:** Task lists, implementation plans, screenshots, browser recordings — tangible deliverables for verification rather than raw tool calls.
- **Knowledge base as learning primitive:** Agents save useful context and snippets for future tasks.
- Free in public preview. Gemini 3 Pro primary model + Claude Sonnet 4.6, GPT-OSS-120B support.
- Wikipedia notes "debate as to whether it is a direct fork of VS Code, or a fork of Windsurf."

### OpenAI Codex CLI
- Rust-based, local-first sandbox. Open source.
- Runs in VS Code, Cursor, Windsurf as extensions.
- GPT-5-Codex for code-specific tasks.
- Cloud-based IDE variant in development.

### Gemini CLI (Google, open source)
- 96,600+ GitHub stars. Apache 2.0 license.
- **1M token context window** — 5x Claude Code's 200K, 8x Codex's 128K.
- Free tier: 1,000 requests/day with Google account. Zero cost barrier.
- Deep Think mode for extended reasoning. Google Search grounding for live documentation.

### OpenClaw
- 100K+ GitHub stars. Local-first, self-extending via code generation.
- **Not primarily a coding tool** — general-purpose agent accessed via WhatsApp, Telegram, Discord.
- Pi (minimal coding agent) is the engine underneath.
- ClawHub marketplace for skills — but supply chain attacks within weeks of launch (14 malicious skills).
- Creator Steinberger joined OpenAI Feb 2026; project moved to open-source foundation.

### Cursor
- VS Code fork. $1.2B ARR in 2025 — fastest-scaling SaaS product in history.
- Cloud agents with computer use (isolated VMs, accessible from web/mobile/Slack/GitHub).
- Sub-agents for parallel task handling.
- Cursor Blame (Enterprise): distinguishes code from tab completions, agent runs, and human edits in git blame.

---

## Industry: Anthropic 2026 Agentic Coding Trends Report

Published January 2026. Eight trends across three categories:

### Foundation Trends
1. **Engineering roles restructured** — from writing code to orchestrating agents. Engineers use AI in ~60% of work but fully delegate only 0–20%. ~27% of AI-assisted work consists of tasks that wouldn't have been done otherwise.
2. **Single-agent → multi-agent coordination.** Orchestrator coordinates specialists in parallel. Case study: Fountain achieved 50% faster screening, 2x candidate conversions.
3. **Human oversight scales through intelligent collaboration.** Agents detect uncertainty, flag risk, request human input at decision points rather than attempting everything end-to-end.

### Capability Trends
4. **Short tasks → long-horizon agents.** Agents planning, iterating, recovering from errors over hours or days.
5. **Agent-reviewed code.** AI reviews AI-generated code for security, consistency, defects at scale humans can't match.
6. **Beyond engineering teams.** Non-technical team members building tools, automating workflows.

### Impact Trends
7. **Security as dual-use concern.** Same capabilities help defenders and attackers. Organizations must build security into agentic system design from inception.
8. **Economic restructuring.** Project timelines collapsing from months to weeks. Dynamic "surge staffing" of engineer-agent teams.

### Four Strategic Priorities
1. Master multi-agent coordination
2. Scale human-agent oversight
3. Extend agentic coding beyond engineering
4. Embed security architecture as core design principle

---

## Cross-Cutting: The Skills Portability Story

### SKILL.md as Emerging Standard
Antigravity Awesome Skills (v5.4.0) bundles 868+ skills portable across Claude Code, Gemini CLI, Codex CLI, Cursor, GitHub Copilot, and 5 other tools. Official contributions from Anthropic, Vercel Labs, OpenAI, Supabase, Microsoft, Google DeepMind.

Universal installation: `npx antigravity-awesome-skills --claude` (or `--gemini`, `--cursor`, `--codex`).

The same SKILL.md file works in `.claude/skills/`, `.gemini/skills/`, `.cursor/skills/` without modification. The format abstraction decouples skill content from tool-specific invocation.

### CLAUDE.md / AGENTS.md
- **CLAUDE.md:** Claude Code per-project config (coding standards, workflow rules)
- **AGENTS.md:** Adopted by Cursor, OpenAI Codex, OpenCode — defines agent behavior, tool access, project instructions at repo root

### Pi's Philosophy (Armin Ronacher)
Pi (the engine under OpenClaw) takes the opposite approach: no MCP, no skill marketplace. "If you want the agent to do something that it doesn't do yet, you ask the agent to extend itself." It generates its own tools via code. This celebrates "the idea of code writing and running code" — the ultimate self-extending agent.

---

## Cross-Cutting Themes

### Theme 1: Benchmarks Are Catching Up to Reality
The SWE-Bench family has fragmented usefully: Pro (enterprise scale), EVO (long-horizon evolution), Live (continuous updates), Saving (realistic user queries), UTBoost (test adequacy). Each addresses a different failure mode. Together they paint a much more honest picture than the original benchmark.

### Theme 2: Self-Improvement > Hand-Crafted Scaffolds
Live-SWE-agent (77.4%) outperforms all manually designed agents with zero offline training cost. RepoNavigator shows one good tool + RL beats multi-tool agents with bigger models. The trend is clear: let agents learn/create their own tools rather than engineering them.

### Theme 3: The 60/20 Paradox
Engineers use AI in 60% of work but fully delegate only 0–20%. This isn't a failure — it's the nature of the collaboration. The human role shifts to architecture, review, and strategic decisions. The most productive pattern is "constant collaboration" not "full delegation."

### Theme 4: The Long-Horizon Gap
SWE-EVO's 65% → 21% drop from single-issue to evolution tasks is the clearest evidence that current agents lack sustained, multi-file reasoning. This is the frontier problem for agentic coding.

---

## Reading List by Priority

**Must-read:**
1. SWE-EVO (arXiv:2512.18470) — the long-horizon gap quantified
2. Live-SWE-agent (arXiv:2511.13646) — self-evolving agents beat everything

**Important:**
3. SWE-Bench Pro (arXiv:2509.16941) — enterprise-scale evaluation
4. One Tool Is Enough (arXiv:2512.20957) — RL + single tool philosophy
5. Anthropic 2026 Agentic Coding Trends Report — industry data

**Reference:**
6. SWE-bench Live (arXiv:2505.23419) — live benchmarking pipeline
7. Saving SWE-Bench (arXiv:2510.08996) — benchmark realism gap
8. UTBoost (arXiv:2506.09289) — test adequacy problems

---

## Paper 8 (Forward Citation): Self-Play SWE-RL (SSR)

**Wei, Sun, McMilin, Gehring, Zhang, Synnaeve, Fried, Zhang, Wang · Meta FAIR + UIUC + CMU · arXiv:2512.18552 · Dec 2025 · 22 pages**

*Found via forward citation sweep of Live-SWE-agent (arXiv:2511.13646). This paper bridges Section 1 (RL training) and Section 2 (coding agents).*

### The Core Problem

All existing software agent training — including SWE-RL, DeepSWE, and CWM — depends on human-curated data: GitHub issues, pull requests, and test suites. This creates a fundamental scalability ceiling. Agents learn to replay and refine human development traces rather than independently discovering new classes of problems.

### Self-Play Architecture

SSR trains a single LLM in a self-play setting with dual roles:

**Bug Injector:** Introduces bugs into real codebases by removing or modifying code. Each bug is formally specified by a test patch (not a natural language description). The injector also weakens existing tests to hide the bug — simulating real-world bugs that escape test suites.

**Bug Solver:** Given only the buggy codebase and the weakened tests, attempts to find and fix the bug. Test files are always reset to originals before evaluation, preventing gaming.

**Opposing Incentives:** The injector's reward penalizes bugs that are too easy (solve rate s → 1) or too hard (s → 0), targeting the goldilocks zone where the solver can learn maximally. The solver gets binary +1/-1 based on all tests passing.

### Key Results

On CWM-sft (32B pre-RL checkpoint):
- **SWE-bench Verified:** 41.0% → 51.4% (+10.4 points via SSR), vs 49.0% with human-data RL
- **SWE-Bench Pro:** 21.1% → 28.9% (+7.8 points), vs 25.3% with human-data RL
- SSR **consistently outperforms** human-data baseline throughout entire training trajectory

### Ablation Findings

- **Full self-play > injection-only > repair-only.** Joint training is essential — the injector learns to create increasingly challenging bugs while the solver learns to handle them.
- **Removal + history** bug injection strategy works best. Naive prompting collapses to trivial one-line bugs.
- **Higher-order bugs** (bugs on top of bugs) extend the training signal but are limited to second-order to avoid overlap.

### Why This Matters for the Survey

SSR is the missing link between Section 1's "scaffold → weights via RL" thesis and Section 2's coding agent ecosystem. It demonstrates that:
1. Software agents can improve without any human-curated training data
2. Self-play generates richer training signal than human-data RL
3. The path to "superintelligent" coding agents runs through autonomous curriculum generation, not bigger human datasets

Combined with Live-SWE-agent (self-evolving scaffolds, 77.4%) and RepoNavigator (single tool + RL), SSR completes the self-improvement picture: agents that create their own training data, create their own tools, and optimize their own architectures.

---

## Paper 9 (Forward Citation): Self-Evolving Agents Survey

**Gao, Geng, Hua et al. (30+ authors) · Princeton / UIUC / CMU / Tsinghua / CUHK / Edinburgh · TMLR Jan 2026 · 77 pages**

*Found via forward citation sweep. The first systematic survey of self-evolving agents — the overarching paradigm that Live-SWE-agent, SSR, DGM, and HGM all belong to.*

Defines self-evolving agents formally: f(Π, τ, r) = Π', where an evolution function f transforms agent system Π based on trajectory τ and feedback r. Organizes the field around three questions: What to evolve (model/context/tools/architecture), When to evolve (intra-test-time vs inter-test-time), How to evolve (reward-based, population-based, imitation, textual feedback). Maps 25+ systems across four evolutionary pillars. Published in TMLR, the first systematic survey dedicated to this paradigm.
