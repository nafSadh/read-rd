# read-rd — Standing Instructions for All Agents

These instructions apply to every agent operating in this repo — Claude, Gemini, Antigravity, or any other orchestrator or sub-agent.

---

## Agent Tracking (MANDATORY)

**Every time a sub-agent is spawned, it must be logged in `.project/claude-agents.md`.**

This applies to:
- Claude background agents (`run_in_background: true`)
- Gemini agents (via `gemini-audit.py` or similar)
- Antigravity agents
- Any other automated agent or subprocess

### What to log

When spawning an agent, add a row to the tracking table in `.project/claude-agents.md`:

```markdown
| # | Date | Agent ID | Scope / Task | Status | Output |
|---|------|----------|--------------|--------|--------|
| N | YYYY-MM-DD | short-id | What it's doing | running / done / failed | path/to/output or notes |
```

Update the row when the agent completes (status → done/failed, add output path or summary).

### Format

`.project/claude-agents.md` uses this structure:

```markdown
# Agent Tracking — read-rd

## Active Agents
| # | Date | Agent ID | Task | Status | Output |
|---|------|----------|------|--------|--------|

## Completed Agents
| # | Date | Agent ID | Task | Status | Output |
|---|------|----------|------|--------|--------|
```

---

## NPOV Editorial Standards

All paper-drive content (survey-paper.html, tensions-paper.html, position-paper.html, *.dd.html) must follow strict NPOV:
- No second-person address ("you should", "watch for", "invest in")
- No authorial opinion as fact ("the most interesting finding is", "the honest answer is")
- No snarky or colloquial tone in scholarly sections
- Causal claims must be hedged unless sourced
- Temporal dates must reflect actual source dates, not future dates

---

## Environment

- **Gemini API key**: stored in `.env` at repo root (gitignored). Key: `GEMINI_API_KEY`. See `.project/api-keys.md`.
- **Gemini audit script**: `.project/gemini-audit.py` — audits paper HTML files, writes `gemini-npov-rvw.md` next to each paper
- **Model**: `gemini-3-flash-preview` (verified working)

---

## Project Structure

Each paper-drive project lives at `{domain}/{project-name}/` with:
- `index.html` — project landing page
- `survey-paper.html`, `tensions-paper.html`, `position-paper.html`
- `s{N}-{name}.dd.html` — section deep-dives
- `.project/` — changelog, todo, methodology
- `notes/` — synthesis and section notes
- `literature-collection.md`
- `claude-npov-rvw.md` — Claude NPOV review notes
- `gemini-npov-rvw.md` — Gemini audit notes

---

## Git Discipline

- Commit after every logical unit of work
- Push immediately after committing
- Never commit `.env` or any file with API keys
