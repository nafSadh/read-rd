# GenAI 2026 and After — Deep Dive Notes

> Synthesized from 51 sources across 9 dimensions. What the discourse says, where sources agree, and where they contradict each other.

---

## 1. The Technology Frontier

### 1.1 LLMs: Capability vs Cost Deflation

The raw capability story is well established: GPQA scores went from ~50% to 75%+ in 18 months. GPT-4-level performance now costs 1/100th of its 2023 price (~$30/M tokens → <$1/M). 500+ models are tracked. But the more interesting story is what's changing structurally.

**Context windows plateaued.** After rapid expansion from 8K (ChatGPT, Nov 2022) to 2M tokens (Gemini 1.5 Pro, Feb 2024), growth has stalled. Kai Williams at Understanding AI notes that Anthropic hasn't changed its default context since Claude 2.1, GPT-5.2's 400K window is smaller than GPT-4.1's, and Google actually shrank its largest window back to 1M. The transformer architecture hits diminishing returns at extreme context lengths, and "context rot" degrades quality before you hit the limit.

**Chinese open-source dominance.** Qwen2.5-1.5B-Instruct has 8.85M downloads — one of the most widely used pretrained LLMs. MIT Technology Review: "In 2026, expect more Silicon Valley apps to quietly ship on top of Chinese open models." DeepSeek's playbook (open-weight, competitive performance) has forced even OpenAI to release open-source models (Aug 2025). The geopolitical implications: Chinese firms gain trust advantage through openness while the US-China antagonism continues.

**The commodity thesis.** IBM's Gabe Goodhart: "We're going to hit a bit of a commodity point" for AI models in 2026. The competition shifts from models to systems. Nielsen predicts the "Large World Model" era replacing the LLM era — text-only will be "as archaic as a DOS command line."

### 1.2 Multimodal: First-Class Everything

By end of 2026, "frontier model" will mean a single system that speaks, listens, sees, imagines, and edits, with every modality first-class (Nielsen). Google Veo 3.1 does video + audio. OpenAI Sora 2 generates synchronized dialogue and sound effects. Scaling laws proven for video → emergent physics understanding.

IBM's Baughman: "These models will be able to perceive and act in a world much more like a human. They'll bridge language, vision and action, all together."

Stanford's Altman (not Sam) raises the fundamental question for science: early fusion (one massive model for all data types) vs late fusion (separate models integrated afterward). Early fusion is more powerful but you rebuild everything on every update. Late fusion is modular but may lose cross-modal insights. "In the next year, we may get clarity."

### 1.3 The Efficiency Counter-Narrative

The NVIDIA position paper (Belcak & Heinrich, arXiv:2506.02153) argues SLMs (7B) are 10-30× cheaper and sufficient for most agentic sub-tasks. "Insisting on LLMs for all tasks reflects a misallocation of computational resources." IBM's El Maghraoui predicts 2026 as "the year of frontier versus efficient model classes" — alongside huge models, efficient hardware-aware models running on modest accelerators will appear. Edge AI moves from hype to reality.

Stanford's Landay: "We have huge models, but we've seen better models that are smaller than the huge ones. It seems like we have reached some amount of peak data." More effort on curating smaller, higher-quality datasets.

---

## 2. AI Agents: Hype Meets Reality

### 2.1 The Bull Case

Gartner: 40% of enterprise apps will include task-specific agents by 2026. IDC: 40% of G2000 job roles will involve working with AI agents. CB Insights identifies five high-momentum agent markets with 115+ companies in customer service AI alone, 6 at $100M+ revenue. Salesforce CIO adoption up 282%.

METR's task-length doubling: Claude Opus 4.5 can complete tasks that take humans ~5 hours (at 50% success rate). If the faster trend holds, by end 2026: 50% reliability on 20-hour tasks (half a SWE work week).

### 2.2 The Bear Case

**Gartner also predicts 40% of agentic AI projects will be canceled by end 2027.** MIT Sloan (Davenport & Bean): agents are "the most-hyped trend since, well, generative AI." GenAI is now in Gartner's trough of disillusionment. Agents heading there in 2026. "They just aren't generally ready for prime-time business. Various experiments by vendor and university researchers — including Anthropic and Carnegie Mellon — have found that AI agents make too many mistakes for businesses to rely on them for any process involving big money."

Forrester: 25% of planned AI spend will be deferred by 2027 due to ROI concerns. IBM: "Every agentic AI program should attach to clear KPIs and a defensible ROI model before scaling."

### 2.3 The Anti-MCP Prediction

Understanding AI's Andrew Lee (CEO of Tasklet) makes a contrarian prediction at 90% confidence: "Major AI companies like OpenAI and Anthropic will stop investing in MCP." His argument: modern LLMs can reason about APIs directly, MCP descriptions are already in training data, and agents built to access APIs directly are simpler. "By end of 2026, MCP will be seen as an unnecessary abstraction."

This directly contradicts the 97M+ monthly SDK downloads and AAIF governance trajectory documented in our agentic LLM survey. It's a minority view but worth tracking.

### 2.4 The Resolution

The most likely path: agents work in narrow, well-defined domains (customer service, coding, incident response) but fail in open-ended business processes. MIT Sloan: "We are confident that AI agents will handle most transactions in many large-scale business processes within, say, five years" — more optimistic than Karpathy's 10 years, but acknowledging it's not 2026.

---

## 3. Workplace: From Evangelism to Evaluation

### 3.1 The Stanford Thesis

Stanford HAI's faculty converge on: **"The era of AI evangelism is giving way to an era of AI evaluation."** The question shifts from "Can AI do this?" to "How well, at what cost, and for whom?"

Specific predictions:
- Legal AI: standardized domain-specific benchmarks, ROI-tied evaluation, multi-document reasoning
- Healthcare: frameworks for evaluating the "tsunami of noise" from AI startups
- AI sovereignty: countries building own LLMs or running others' on own GPUs
- Failed projects: "In 2026 we'll hear more companies say that AI hasn't yet shown productivity increases, except in certain target areas like programming and call centers"

### 3.2 The Individual vs Enterprise Gap

MIT Sloan identifies the key tension: individual Copilot-style use (write emails, PowerPoints, spreadsheets) delivers "incremental and mostly unmeasurable" productivity gains. The value comes from enterprise-level implementation — embedded in organizational workflows, not bolted on as individual tools. But most companies are still at the individual stage.

The Anthropic 2026 Agentic Coding Trends Report provides the clearest data: engineers use AI in ~60% of work but fully delegate only 0-20%. 67% more PRs merged per day. The "60/20 paradox" isn't failure — it's the natural contour of effective human-AI collaboration.

### 3.3 Adoption Numbers

- ITSM.tools survey: Only 2% report no AI use. 82% of end-users use free AI tools at work (up from 71% in 2025). Trust increased for 62%. But only 16% fully trust AI for autonomous operational decisions.
- Microsoft: AI coworkers, not just tools. "Repository intelligence" in coding. AI joining scientific discovery.
- Anthropic: Case studies — Fountain (50% faster), Rakuten (7h autonomous), TELUS (500K hours saved).

---

## 4. Employment: The Codified vs Tacit Knowledge Split

### 4.1 The Dallas Fed Framework

The most insightful framework comes from the Dallas Fed's February 2026 economic letter. AI simultaneously aids AND replaces workers, depending on knowledge type:

- **Codified knowledge** (textbook/rules-based): automatable. AI substitutes for entry-level workers who primarily have book learning.
- **Tacit knowledge** (experiential/judgment): complemented. AI augments experienced workers by automating their routine tasks, making their expertise more valuable.

Result: "Wages are rising in AI-exposed occupations that place a high value on a worker's tacit knowledge and experience." But the career ladder model is breaking — entry-level development via codifiable tasks is becoming "cost-ineffective." Long-term unsustainable: how do workers gain tacit knowledge if entry-level positions disappear?

### 4.2 The Numbers

**Goldman Sachs:** Young tech workers already affected. 20-30 year olds in tech-exposed occupations: unemployment up ~3pp since start of 2025. But only 9.3% of companies actually report using GenAI. If current AI use cases were expanded: 2.5% of US employment at risk. With wide adoption: 6-7%. Historically, disruption effects are temporary (2 years).

**Yale Budget Lab (the contrarian):** "No discernible disruption" to the broader labor market 33 months after ChatGPT. No clear growth in AI exposure among unemployed. "Historically, widespread technological disruption in workplaces tends to occur over decades, rather than months or years."

**Brookings:** 37.1M highly AI-exposed workers. But 70% (26.5M) have HIGH adaptive capacity. The vulnerable: 6.1M clerical/admin workers with LOW adaptive capacity — office clerks (2.5M), secretaries (1.7M), receptionists (965K).

**BLS:** Approaches AI same as other technologies. "Displacement tends to take longer than technologists typically expect." Methods "not designed to capture extremely rapid technological change."

**WEF:** 85-92M jobs displaced globally by 2030, BUT 97-170M new roles created. Net positive at macro level. The problem: access to new jobs requires skills most displaced workers don't have.

### 4.3 The Gender and Generational Dimension

79% of employed women in US work in jobs at high automation risk (vs 58% men). Workers 18-24 are 129% more likely than those over 65 to worry about AI job loss. 49% of Gen Z believe AI has reduced the value of their college education. The entry-level job crisis is both economic and psychological.

---

## 5. Public Perception: The Trust-Use Gap

### 5.1 The KPMG/Melbourne Landmark Study

48,000 people across 47 countries. The headline finding: **people use AI but don't trust it.**

- 66% use AI regularly
- 83% believe AI will deliver wide benefits
- **Only 46% willing to trust AI systems**
- 70% believe regulation is needed
- **66% rely on AI output without evaluating accuracy**
- **56% report making mistakes in work due to AI**

The 66%/46% gap (use vs trust) is the defining human challenge. People are adopting tools they don't trust, relying on outputs they don't verify, and making mistakes because of it.

### 5.2 Regional Patterns

Ipsos (30 countries): 52% excited vs 53% nervous (essentially split). Excitement correlates with economic optimism — Thailand, Indonesia, Malaysia most excited. Western countries (AU, UK, CA, FR) dominated by fear and worry. 54% trust AI not to discriminate more than humans (45%) — an unexpected finding.

University of Queensland (17 countries): Trust in AI increased since 2020 in all tracked Western countries. But NO improvement in perceived adequacy of regulations, and NO increase in confidence in entities to govern AI. Awareness up, trust up, but governance trust static.

### 5.3 The Generational Split

42% of Gen X/Millennials trust AI in Australia vs 25% of older generations. Younger workers are both more trusting of AI AND more worried about losing their jobs to it — a paradox that reflects their closer exposure.

---

## 6. Regulation & Legal

MIT Technology Review: Legal battles shifting from training (mostly won by AI companies) to deployment liability. Key unresolved questions: Can AI companies be liable for what chatbots encourage people to do? Can chatbot defamation be sued? Will insurers shun AI companies? Family of teen who died by suicide will bring OpenAI to court November 2026.

Gartner: "Death by AI" legal claims will exceed 2,000 by end of 2026. 50% of orgs will require "AI-free" skills assessments. 35% of countries locked into region-specific AI platforms by 2027.

Cornell's Grimmelmann: "Courts won't enjoin AI companies out of existence, but they will impose serious high-dollar consequences if the companies don't take reasonable steps to prevent easily predictable harms." Anthropic already paid $1.5B to settle training claims.

---

## 7. Economics & Infrastructure

$500B+ hyperscaler capex in 2026. Seven biggest tech companies = 30%+ of S&P 500 market cap. The "gigawatt ceiling" — power is the binding constraint, not compute or data.

The revenue trajectory: OpenAI targeting $30B (2026), up from $13B (2025). Anthropic targeting $15B, up from $4.7B. Understanding AI predicts both will hit targets.

The deflation counter-narrative: Stanford's Landay: "At some point, you can't tie up all the money in the world on this one thing. It seems like a very speculative bubble." MIT Sloan: AI bubble deflation is a 2026 trend.

IBM predicts: first quantum computer outperforming classical in 2026. New chip class for agentic workloads. "GPUs will remain king, but ASIC-based accelerators, chiplets, analog inference and even quantum-assisted optimizers will mature."

---

## 8. Forward Scenarios

### 8.1 AI 2027 (Fast Takeoff)

Detailed scenario from former OpenAI researcher. Predicts agents doing full SWE work by mid-2027, AI-accelerated AI R&D as inflection point. Stock market +30% in 2026. Junior SWE jobs "in turmoil." Two endings written: slowdown and race.

### 8.2 Understanding AI (Steady Progress)

"We don't believe AI is a bubble on the verge of popping, but neither do we think we're close to a 'fast takeoff.'" Models continue improving, real-world economic impacts modest. GDP growth won't exceed 3.5% (90% confidence). No AI catastrophe in 2026 (90% confidence).

### 8.3 Stanford (Reckoning)

"After years of fast expansion and billion-dollar bets, 2026 may mark the moment artificial intelligence confronts its actual utility." The year demands rigor over hype. No AGI this year.

---

## 9. The Six Tensions (Synthesis)

| # | Tension | Sources For | Sources Against | Resolution Likely In |
|---|---------|------------|----------------|---------------------|
| 1 | **Jobs: net positive vs transition pain** | WEF (+12-78M net), BLS (historically temporary) | Goldman (young workers hit), Dallas Fed (career ladder breaking) | 2028-2030 |
| 2 | **Productivity: transformative vs unmeasurable** | Microsoft, Anthropic case studies | MIT Sloan ("incremental"), Stanford ("certain target areas only") | 2026-2027 (enterprise adoption) |
| 3 | **Agent readiness: 40% of apps vs 40% canceled** | Gartner (adoption), CB Insights (revenue) | Gartner (cancellation), MIT Sloan ("not ready") | 2027 (narrow domains first) |
| 4 | **Trust: 66% use vs 46% trust** | KPMG (adoption real), Ipsos (excitement) | KPMG (56% mistakes), UQ (governance trust flat) | Structural (won't fully resolve) |
| 5 | **Model trajectory: AGI 2027 vs no disruption** | AI 2027, METR task lengths | Yale (no disruption), BLS (slow historically) | Domain-specific (SWE ≠ economy) |
| 6 | **Bubble: $500B capex vs ROI concerns** | Revenue growth (OpenAI, Anthropic), adoption | Forrester (25% deferred), Stanford ("speculative") | Late 2026 (first real ROI data) |
