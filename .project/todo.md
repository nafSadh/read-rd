# read-rd — TODO

## Current Structure

```
read-rd/
├── index.html                       ← collapsible tree portal
├── manifest.json
├── .project/
│
├── courses/                         ← structured syllabi
│   ├── scpd.html                    ← course portal
│   ├── scpd-ml/                     ← XCS229 (26 files)
│   └── scpd-deep-gen-ai/           ← XCS236 (14 files)
│
├── digests/                         ← time-series, daily
│   ├── index.html
│   ├── 2026-02/*.md
│   └── 2026-03/*.md
│
├── ai/                              ← AI research, trends, industry
│   ├── trending-ai.dd.html
│   ├── agentic-llm-survey.slides.html
│   └── ml-blog.dd.html
│
├── physics/                         ← physics
│   ├── block-universe.dd.html
│   ├── nonlinear-time.dd.html
│   └── time-travel-fiction.dd.html
│
├── neuro/                           ← neuroscience
│   └── brain-energy.dd.html
│
├── philosophy/                      ← philosophy, psychology
│   ├── dark-psychology.dd.html
│   ├── stoicism.dd.html             ★ TBA
│   └── religion.dd.html             ★ TBA
│
├── craft/                           ← creative practice, book studies
│   ├── poetry-syllabus.dd.html
│   ├── poetry-collection.dd.html
│   └── project-hail-mary.dd.html
│
├── self/                            ← personal growth, identity
│   ├── audhd.dd.html
│   ├── how-to-know-a-person.dd.html
│   ├── wellbeing.dd.html
│   └── career.dd.html
│
└── (future: music/, tech/, cs/)
```

## Migration — Complete ✅

Executed in Session 10:

- [x] Move + flatten `papers/` files → `ai/`
- [x] Flatten `physics/` (remove nested topic dirs)
- [x] Move `poetry/` → `craft/`, flatten
- [x] Flatten `self/` (remove nested topic dirs)
- [x] Move `project-hail-mary.dd.html` → `craft/`
- [x] Update all file paths in manifest.json
- [x] Update index.html (rebuilt with collapsible tree)
- [x] Remove old empty dirs + stale READMEs
- [x] Delete old `papers/` and `poetry/` dirs

Not migrated (deferred):
- [ ] Rename `courses/` → `~c/` *(tilde dirs problematic for GitHub Pages)*
- [ ] Rename `digests/` → `~d/`

## Open Questions

- AI/ML boundary: Is "agentic LLM survey" more `ai/` (trends) or closer to coursework? Where does ML blog go?
- CS & software eng: placeholder for now — what goes here?
- `science/` vs separate: physics stays separate; does neuroscience (brain-energy) go in `philosophy/` or its own `neuro/`?

## Files to Create

### Migrate existing — Complete ✅

- [x] `ai/trending-ai.dd.html` ← papers/trending-ai/
- [x] `ai/agentic-llm-survey.slides.html` ← papers/agentic-llm-survey/
- [x] `physics/block-universe.dd.html` ← physics/block-universe/
- [x] `sci-fi-te/nonlinear-time.dd.html` ← sci-fi-te/nonlinear-time/
- [x] `sci-fi-te/time-travel-fiction.dd.html` ← sci-fi-te/nonlinear-time/
- [x] `craft/poetry-syllabus.dd.html` ← poetry/syllabus/
- [x] `craft/project-hail-mary.dd.html` ← root
- [x] `self/audhd.dd.html` ← self/audhd/
- [x] `self/how-to-know-a-person.dd.html` ← self/how-to-know-a-person/

### New .dd.html to write

- [x] `neuro/brain-energy.dd.html` — metabolic theory of mental illness (Session 9)
- [ ] `philosophy/stoicism.dd.html` — TBA
- [ ] `philosophy/religion.dd.html` — TBA
- [x] `philosophy/dark-psychology.dd.html` — manipulation, influence, social psych (Session 9)
- [x] `ai/ml-blog.dd.html` — ML blog writing project (Session 9)
- [x] `craft/poetry-collection.dd.html` — workshop pieces, craft in practice (Session 9)
- [x] `self/wellbeing.dd.html` — mental health arc, resilience, turning points (Session 9)
- [x] `self/career.dd.html` — trajectory, growth, transitions (Session 9)

### Low priority

- [ ] `music/dj-origin.dd.html` — DJ journey, electronic music (from dj-music.html)
- [ ] `tech/gear-research.dd.html` — gadget evaluations (from tech-gadgets.html)

## Existing Content — Complete

48 topics, 52+ HTML files, 11 journeys, 29 daily digests.
All `-deep-dive.html` files renamed to `.dd.html` (Session 10).
All course .dd.html files verified against canonical architecture.
All citations verified (165 URLs).
Fact-check audit completed on non-course pages (Session 10).

---

## The Cosmos — Paper Drive Project

### Source Adequacy

| Section | Sources | Adequate? | Status |
|---------|---------|-----------|--------|
| S1: Scales | 7 | Yes | **Done** — deep-dive + hero image |
| S2: Big Bang & CMB | 7 | Yes | **Done** — deep-dive, image pending |
| S3: Dark Matter | 9 | Yes | Planned — notes ready |
| S4: Dark Energy | 9 | Yes | Planned — notes ready |
| S5: Fermi Paradox | 7 | Yes | Planned — notes ready |
| S6: Multiverse | 6 | Yes | Planned — notes ready |
| S7: Frontiers | 10 | Yes | Planned — notes ready |

### Next Steps

1. Generate S2 hero image via Claude Code (see `.project/image-gen-cosmos.md`)
2. Build S3: Dark Matter deep-dive (9 sources, notes at `notes/03-dark-matter.md`)
3. Build S4: Dark Energy deep-dive (9 sources, notes at `notes/04-dark-energy.md`)
4. Build S5–S7 deep-dives
5. After all sections: synthesis paper, slides, final index update
