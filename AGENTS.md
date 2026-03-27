# Agent Instructions — read-rd

This file is read by all agents (Claude, Gemini, Antigravity, etc.) operating in this repo.
The canonical version lives at repo root: `CLAUDE.md`. This file mirrors the key rules.

---

## MANDATORY: Log every agent in `.project/claude-agents.md`

Any time you spawn a sub-agent or are yourself a sub-agent, log it:

```markdown
| # | Date | Agent ID | Task | Status | Output |
|---|------|----------|------|--------|--------|
| N | YYYY-MM-DD | id | description | running/done/failed | output path |
```

Update on completion.

---

## NPOV Standards
- No second-person address
- No opinion-as-fact
- Hedge causal claims
- No future dates as publication dates

## Environment
- Gemini API: `.env` → `GEMINI_API_KEY`
- Gemini model: `gemini-3-flash-preview`
- Audit script: `.project/gemini-audit.py`

See `CLAUDE.md` at repo root for full instructions.
