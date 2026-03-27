# Nano Banana — Image Style Reference

Style guide for AI-generated images in read-rd deep-dive pages.
All images use **Google Gemini** (`gemini-3.1-flash-image-preview`).

## Core Style

**Append this suffix to every prompt:**

```
, minimal ink line drawing on warm cream paper, single violet accent color,
clean sparse lines, editorial sketch style, playful and elegant, no photorealism
```

## Style Properties

| Property | Value |
|---|---|
| Medium | Ink line drawing |
| Surface | Warm cream paper |
| Accent color | Violet (single color, used sparingly) |
| Line quality | Clean, sparse, confident strokes |
| Tone | Playful and elegant |
| Density | Medium — not too sparse, not too busy |
| Photorealism | Explicitly excluded |

## What Works Well

- **Labeled diagrams** — Minkowski spacetime, powers-of-ten scales, letter anatomy
- **Workspace scenes** — desks with materials, tools, books (overhead or 3/4 view)
- **Landscapes with character** — trails, forests, coastlines, hilltops
- **Conceptual illustrations** — branching timelines, light cones, portals
- **Script/text specimens** — calligraphy samples, typeface comparisons

## What to Avoid

- Photorealistic prompts (the style suffix overrides, but results are inconsistent)
- Too many objects in one scene (keep compositions focused)
- Prompts that rely on color differentiation (only one accent color)
- Text-heavy prompts where readability matters (AI-generated text in images is unreliable)

## Prompt Examples by Topic

### Science / Physics
```
Minkowski spacetime block: past light cone below, future above,
the present as a thin luminous slice, worldlines as threads
```
```
Branching timelines: a river of light splitting into streams that
loop, merge, and branch, each a different shade
```
```
Deep field view of galaxies: spirals and ellipticals scattered
like jewels across the void, cosmic scale
```

### Nature / Hiking
```
Tall coastal redwood trees with sunlight filtering through, ferns
on forest floor, a hiking trail winding between trunks
```
```
A coastal cliff trail with crashing waves below, wildflowers on
the bluff edge, fog rolling in from the ocean
```
```
Night sky with Milky Way over a hilltop, city lights twinkling
in the valley, a small tent glowing warm
```

### Typography / Craft
```
A vintage letterpress type drawer with wooden letter blocks, an
ink roller, and freshly printed sheets with Garamond letterforms
```
```
Anatomy of the lowercase letter g in a serif typeface: x-height,
ascender, descender, bowl, ear, link, and loop labeled with
thin callout lines
```
```
World map with different writing systems in their regions: Arabic
calligraphy, Chinese characters, Devanagari, Latin serifs, Cyrillic
```

### Sci-Fi / Fiction
```
A lone astronaut floating inside a small spacecraft cockpit,
looking out a viewport at a dim red dwarf star
```
```
A friendly five-limbed alien made of rock-like material with no
eyes, communicating through musical tones shown as sound waves
```

### Constructed Languages
```
A scholar desk with constructed language materials: Tengwar script,
Klingon dictionary, Esperanto grammar, fountain pens, linguistic
tree diagrams
```

## Model & Parameters

- **Model:** `gemini-3.1-flash-image-preview` (Nano Banana 2 / Flash)
- **Config:** `{ responseModalities: ['IMAGE', 'TEXT'] }`
- **Output:** PNG, typically 700KB–1.2MB
- **Aspect ratio:** Controlled by CSS container, not prompt (images are square from API, cropped by `object-fit: cover`)
- **Rate limits:** 503 errors common under load; use exponential backoff (3s → 6s → 12s → 24s)

## Exception: Flag History

Flag History pages use **photorealistic** style (from run 1) which works well for
dramatic historical scenes. These do NOT use the sketch suffix. The only exception
is `s6-hero.png` (Design section) which uses sketch style.
