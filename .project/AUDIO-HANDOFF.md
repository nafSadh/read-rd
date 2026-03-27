# Audio Generation — Hand-off

## What was done

Built a TTS pipeline using Gemini API (`gemini-2.5-flash-preview-tts`) to generate audio narrations of deep-dive papers, with per-topic British voice styles and embedded HTML audio players.

### Scripts
- **`generate_audio.py`** — Extracts text from `.dd.html` (or markdown papers when available), sends to Gemini TTS in chunks, outputs MP3 (48kbps via lameenc). Supports `--overviews-only`, `--workers N`, `--dry-run`, `--samples`, per-topic voice/style mapping.
- **`embed_audio.py`** — Injects a single `<script>` block before `</body>` that creates all audio elements via DOM. Never touches template literals or `<style>` tags.

## Key learnings

1. **`.dd.html` files build DOM via JS template literals** — you cannot inject HTML into `</style>` or `<div class="masthead-sub">` because those strings live inside backtick template literals in `<script>` blocks. The only safe injection point is a new `<script>` before `</body>`.

2. **Glob patterns pick up `.claude/worktrees/`** — always add `.claude` to skip list when globbing `**/*.dd.html` from the repo root.

3. **Gemini TTS quota: 100 RPD** — even on paid Tier 1, `gemini-2.5-flash-preview-tts` has 100 requests/day. Each file takes 1–10 API calls (one per ~6K char chunk). Plan for multi-day generation or request quota increase.

4. **WAV is way too large** — raw PCM from Gemini is ~15MB per chunk. Must encode to MP3. 48kbps is fine for voice narration (~350KB/min).

5. **Markdown papers > HTML extraction** — when a project has a synthesis paper (e.g. `geometry-of-feeling.md`, `survey-paper.md`), use that as narration source. HTML-extracted text from `summaries[]` + `details[]` arrays works but reads less naturally.

6. **Structured style prompts help** — Gemini TTS responds well to Audio Profile + Scene + Director's Notes format (accent, pacing, style). Per-topic prompts make a real difference.

7. **Audio player UX** — inline bar in expanded header, sticky bottom bar when scrolled (with playback transfer between them), mini speaker icon in ctrl-group. All created via `document.createElement` after DOM is built.

## Status

### Generated (19/37 overview+standalone files)
- AI: genai-2026-overview, ml-blog, trending-ai
- Anthropology: flag-history, religion-today overview
- Cog-Sci: attachment-theory, brain-energy, religion-psychology, science-of-humor, sleep-and-dreams, stoicism-in-practice (all overviews)
- Craft: art-of-typography, constructed-languages, poetry-collection, poetry-syllabus, project-hail-mary, science-of-music (overviews)
- Philosophy: dark-psychology, sophie's-world-reader/01-awakening

### Not generated (quota hit)
- Physics: block-universe, the-cosmos
- Sci-Fi Thought Experiments: retrocausal-emotion, time-travel-fiction, nonlinear-time
- Self: audhd, career, wellbeing, how-to-know-a-person
- Philosophy: paradoxes, stoicism-landscape, sophie's world reader 02–07

### Voice mapping
| Directory | Voice | Style |
|---|---|---|
| physics | Enceladus | BBC physicist-narrator |
| philosophy | Charon | Authoritative lecturer |
| self | Algieba | Warm, empathetic |
| neuro | Schedar | Clinical, precise |
| ai | Gacrux | Tech journalist |
| craft | Sadaltager | Literate, appreciative |
| cog-sci | Iapetus | Clear cognitive scientist |
| anthro | Charon | Documentary narrator |

### Skipped (by request)
courses/, digests/, hiking/

## To resume

```bash
# Generate remaining files (after quota resets)
python3 generate_audio.py --overviews-only --workers 2

# Embed players into newly generated files
python3 embed_audio.py

# Commit
git add -A && git commit -m "Add audio for remaining files"
```

## Cost / quota
- Tier 1: 100 requests/day for `gemini-2.5-flash-preview-tts`
- 37 overview files = ~184 API calls = 2 days at free tier
- Consider: larger chunks, paid quota increase, Cloud TTS, or alternative providers

## How to update skills

### read-aid
- After generating a `.dd.html`, optionally run `generate_audio.py` on it and `embed_audio.py` to add the player
- The embed is idempotent (checks for `audio-main` before injecting)
- Could add an `--audio` flag to read-aid that triggers TTS after build

### paper-drive
- At project completion (all sections built), run `generate_audio.py` on overview + section files
- Markdown synthesis papers (`*-paper.md`, `00-synthesis.md`) are preferred narration sources
- Could add audio generation as a final phase in the paper-drive workflow
- Multi-speaker TTS (professor + student, narrator + characters) would suit course material and book studies — requires reformatting text into dialogue with speaker tags

### Both skills
- `embed_audio.py` should be run from the repo root (not a worktree) to avoid `.claude/worktrees` glob issues
- The `generate_audio.py` voice/style mapping lives in the script — update `VOICE_MAP` and `STYLE_MAP` dicts when adding new topic directories
