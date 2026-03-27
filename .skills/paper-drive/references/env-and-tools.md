# Environment & External Tools

## .env file
Location: `read-rd/.env` (gitignored — never commit)

Contains:
- `GEMINI_API_KEY` — Google Gemini API key

Auto-loaded by `.project/gemini-audit.py`.

## gemini-audit.py
Location: `.project/gemini-audit.py`

Runs a Gemini NPOV/rigor audit on all paper files (`*paper*.html`).
Writes `gemini-npov-rvw.md` next to each paper. Does NOT edit files.
After it runs, use Claude agents to read the reviews and apply fixes.

```bash
python3 .project/gemini-audit.py            # audit all papers
python3 .project/gemini-audit.py --dry-run  # list files only
python3 .project/gemini-audit.py --force    # re-audit already reviewed
python3 .project/gemini-audit.py --file path/to/paper.html
```

Current model: `gemini-3-flash-preview`
