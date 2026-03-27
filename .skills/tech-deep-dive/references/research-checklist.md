# Research Checklist

For each tool, research ALL of the following before writing HTML. Do 3-4 web searches minimum per tool, targeting different angles.

## Search Queries to Run

For tool X, search for:
1. `{X} architecture how it works internals 2026` — official docs and technical blogs
2. `{X} limitations problems complaints github issues` — real-world failure modes
3. `{X} vs {competitor} comparison benchmark` — head-to-head technical comparisons
4. `{X} changelog release notes latest features` — evolution and trajectory
5. `{X} tutorial setup configuration guide` — installation gotchas, real config syntax

## Content Depth Requirements Per Section

### Architecture & Internals
- What is the execution model? (ReAct loop, CodeAct, custom?)
- What tools/capabilities does it have built-in?
- How does it manage context? (token counting, compaction, sliding window?)
- How does authentication work? (OAuth, API key, QR code?)
- What's the permission/safety model?
- Draw an SVG showing actual data flow, not just conceptual boxes

### Key Features
- For each feature: what does it ACTUALLY do, not what marketing says
- What are the configuration options? Show real syntax.
- What are the limitations of each feature?
- What breaks? Under what conditions?
- What's the workaround when it breaks?

### Technical Deep Dive
- Exact install commands for each platform
- Real configuration file examples (settings.json, config files, etc.)
- CLI flags and their actual behavior
- API pricing with real per-message cost estimates
- State management: what persists across sessions? What doesn't?
- Error handling: what happens on failure? Auto-retry? Manual recovery?

### Real-World Usage
- What do power users actually use it for? (not marketing use cases)
- What are the common failure patterns?
- What do GitHub issues reveal about real problems?
- Community workarounds and hacks
- Token/cost consumption patterns at realistic usage levels

### Evolution Timeline
- Key version milestones with dates
- What changed architecturally (not just feature lists)
- What's the trajectory? Where is this heading?
- How fast is development moving? (releases per month)

### Honest Assessment
- SPECIFIC strengths (not "good at coding" — say "80.8% SWE-bench, best in class for refactoring tasks")
- SPECIFIC weaknesses (not "can be expensive" — say "Pro plan rate limits hit after ~40 complex queries/day")
- Direct comparison to closest alternative on each dimension

### Verdict & Takeaways
- Who is the ideal user for this tool?
- What specific patterns or ideas from this tool are worth knowing about?
- Where is the tool heading? What's the bet the team is making?
- If the user has a specific project context, how does this tool fit in?

## Red Flags for Shallow Content

If your deep dive contains any of these, it's too shallow:
- "Supports multiple models" without listing which ones and their tradeoffs
- "Easy to set up" without showing the actual setup commands
- "Has memory" without explaining what persists and what doesn't
- "Extensible" without showing the extension mechanism (MCP config, plugin format, etc.)
- Feature descriptions under 2 sentences
- No code examples anywhere in the page
- No specific numbers (token limits, rate limits, pricing, benchmark scores)
- Pros/cons that could apply to any AI tool
