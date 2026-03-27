# Continuation Prompt — GenAI 2026 Outlook

Paste this into a new thread to resume.

---

## Prompt

I'm continuing work on a research project: **GenAI 2026 and After**.

**Repo:** https://github.com/nafSadh/read-rd (PAT token is in the git remote URL)
**Subfolder:** `ai/genai-2026-outlook/`
**Live:** https://read.sadh.app/ai/genai-2026-outlook/

### What this project is

A multi-section literature survey of what people are saying/predicting about generative AI across 8 dimensions: LLMs & foundation models, multimodal & diffusion, AI agents, workplace adoption, employment & labor, public perception & trust, regulation & governance, economics & infrastructure.

The goal is 8 section deep-dives (markdown + interactive HTML each), plus papers (survey paper, tensions paper, possibly scenarios paper), plus a slide deck.

### Methodology

We follow a **paper-drive** workflow documented in `.project/paper-drive-methodology.md`. The key discipline: **before building any section deep-dive, assess whether sources are sufficient. If not, search for what's missing. Only proceed when adequate.** Minimum 5-6 sources per section. Record verdict in `.project/todo.md` source adequacy table.

Each section gets:
- `notes/{NN}-{name}.md` — markdown deep-dive (synthesis across sources, ending with agreements + disagreements)
- `s{N}-{name}.dd.html` — interactive HTML using reading-assist deep-dive template (three-panel: sidebar, summary center, detail right). **Body must be empty — JS builds entire DOM.** Python script injects `sections[]`, `summaries[]`, `details[]` arrays into template CSS/JS extracted to `/home/claude/survey/template_css.txt` and `/home/claude/survey/template_js.txt`.

Hero content is patched into the template JS by replacing `← CHANGE` markers.

### Current state

**Completed:**
- `literature-collection.md` — 53 sources across 8 sections + 6 key tensions
- `genai-2026-overview.dd.html` — 9-section overview deep-dive (all dimensions)
- `notes/00-synthesis.md` — cross-section synthesis
- **S1: LLMs & Foundation Models** — DONE (8 sources, `notes/01-llms.md` + `s1-llms.dd.html`)

**Next:**
- **S2: Multimodal & Diffusion** — assessed NOT ENOUGH (only 3 sources). Need 4-6 more covering: model benchmarks, diffusion trajectory (Sora/Veo/SD), video/audio generation, deepfake/safety, world models research. **Search for gaps first, then build.**
- S3-S8: not yet assessed. Follow the same pattern: assess sources → search gaps → build markdown → build HTML.

**After all sections:** Write survey paper, tensions paper. Build slides. Build index page.

### Template system

The HTML deep-dives use a template from the reading-assist skill. CSS and JS are cached at:
- `/home/claude/survey/template_css.txt` (26K)
- `/home/claude/survey/template_js.txt` (7.7K)

If these don't exist in the container, extract them from `/mnt/skills/user/reading-assist/references/deep-dive-reference.html` (it's a working HTML file — pull the CSS from `<style>` and JS from the last `<script>` block).

### Related project

There's a completed **Agentic LLM Survey** in the same repo at `ai/agentic-lm-survey/` with its own index, 5 section deep-dives, paper, and slides. It follows the same methodology and template system. Use it as a reference for quality and structure.

### What to do now

Start with S2: Multimodal & Diffusion. Assess sources, search for gaps, build when adequate. Then continue through S3-S8 in order, assessing each before building.
