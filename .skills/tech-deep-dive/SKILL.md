---
name: tech-deep-dive
description: Generate rich, interactive deep-dive HTML pages about AI tools, platforms, and agent frameworks. Use when the user asks to research, compare, or create a visual overview of any AI tool (Claude Code, Cowork, Cursor, Antigravity, Gemini CLI, OpenClaw, smolagents, etc.), wants a "deep dive" on any technology product, or asks for an interactive research page. Also triggers for phrases like "make me a research page about X", "deep dive on X", "compare these tools visually", "create an overview HTML for X", or any request to produce polished research documentation as HTML. This skill produces standalone HTML files with dark theme, expandable sections, SVG architecture diagrams, animated elements, and a consistent design system inspired by nafsadh.com/flags.fyi/blurple aesthetics.
---

# Tech Deep Dive Generator

Generate production-quality, interactive HTML research pages about technology tools and platforms.

## When to Use

- User asks for a "deep dive" on any tech tool or platform
- User wants to compare multiple tools visually
- User requests an interactive research page or overview
- User says "create an HTML about X" for any technology product
- User wants to understand a tool "from different perspectives"

## Process

### Step 1: Research Deeply

Before writing ANY HTML, do genuine research. Read the reference file at `references/research-checklist.md` for the full checklist. The key principle: **every expandable section must contain content that goes DEEPER than what a surface-level summary would cover.** This means:

- Technical internals (how does it actually work? what are the failure modes?)
- Gotchas and limitations the marketing doesn't mention
- Real configuration examples with actual syntax
- Architecture diagrams showing data flow, not just boxes
- Comparison to alternatives on specific technical dimensions
- Community complaints and workarounds
- Pricing edge cases and hidden costs
- State management, persistence, and recovery behavior

Use web_search for each tool to find: official docs, changelog/release notes, community blog posts about real-world usage, GitHub issues revealing limitations, benchmark comparisons. Do at least 3-4 searches per tool to get beyond surface-level.

### Step 2: Read the Design System

Read `references/design-system.md` for the complete CSS, HTML patterns, and component library. Key principles:

- **Dark theme** with tool-specific accent color
- **Instrument Serif** for hero headings (italic for accent), **Satoshi** for body, **IBM Plex Mono** for code/labels
- **Film grain overlay** via SVG noise filter
- **Expandable sections** with smooth CSS transitions (max-height trick)
- **SVG architecture diagrams** inline (not images), with animated dashed edges for data flow
- **Staggered fade-up animations** on page load
- **Stats bar** below hero with key metrics
- Each tool gets a unique `--accent` color

### Step 3: Structure the Content

Every deep dive page follows this skeleton (but sections should be customized per tool):

1. **Hero** — Name, badge (company + open/closed source), one-paragraph hook, key stats bar
2. **Architecture & Internals** — How it actually works under the hood. SVG diagram. Not marketing copy.
3. **Key Features** — Feature grid with genuinely useful detail per feature (gotchas, config syntax, limitations)
4. **Technical Deep Dive** — Installation, configuration, permission model, CLI flags, API details, state management
5. **Evolution / Timeline** — Visual timeline of major releases and trajectory
6. **Real-World Usage** — What works well, what breaks, community patterns, failure modes
7. **Honest Assessment** — Pro/con with specifics, not generalities
8. **Verdict & Takeaways** — Who should use this tool? What are the key patterns and ideas worth knowing about? Where is it heading?

Each section is an expandable accordion. Section 1 (Architecture) auto-opens on page load.

### Step 4: Build the HTML

- Single standalone HTML file per tool (no external dependencies except Google Fonts CDN)
- All CSS inline in `<style>` block
- All JS inline in `<script>` block at bottom
- SVG diagrams inline (not `<img>` tags)
- File naming: `deep-dive-{tool-name}.html`
- Save to the workspace/outputs folder

### Step 5: Build the Overview (if multiple tools)

If generating pages for multiple tools, also create a `landscape-overview.html` page with:
- Card grid showing all tools
- Comparison table (features × tools)
- Summary of each tool's niche and strengths
- Links to individual deep dives (conceptual — they're separate files)

## Accent Colors by Tool

| Tool | --accent | Badge |
|------|----------|-------|
| Claude Code | #5865F2 (blurple) | Anthropic · Closed Source |
| Cowork | #43b581 (green) | Anthropic · Research Preview |
| OpenClaw | #ed4245 (coral) | Open Source · Self-Hosted |
| Antigravity | #00d4aa (cyan) | Google · Free Preview |
| Gemini CLI | #4285f4 (google blue) | Google · Apache 2.0 |
| Cursor | #c084fc (purple) | Anysphere · Closed Source |
| smolagents | #ff6f00 (orange) | HuggingFace · Open Source |
| (new tool) | pick a distinctive unused color | (determine from research) |

## Quality Checklist

Before delivering any deep dive HTML:

- [ ] Does EVERY expandable section contain content that goes deeper than a blog post summary?
- [ ] Is there at least one SVG diagram with animated data flow?
- [ ] Are there real code examples (install commands, config syntax, CLI usage)?
- [ ] Are gotchas and limitations documented with specifics (not "can be slow")?
- [ ] Does the Verdict section give a clear, opinionated take on who this tool is for?
- [ ] Does the page load with staggered animations?
- [ ] Does Section 01 auto-open?
- [ ] Is the accent color unique to this tool?
- [ ] Does it work on mobile (responsive grid)?

## Important Notes

- Never produce shallow content. If you can't research deeply enough in current context, say so and suggest continuing in a new chat rather than delivering surface-level work.
- The goal is to produce pages someone would actually bookmark and refer back to — not a glorified README.
- If the user specifies a particular project context (e.g. evaluating tools for their own project), add a relevance section analyzing how the tool relates to their needs.
