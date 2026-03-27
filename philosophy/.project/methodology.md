# Methodology — Sophie's World Reader

**Document version:** March 24, 2026
**Scope:** Deep-dive interactive reading companion for Jostein Gaarder's *Sophie's World* (pages 1–177), covering the history of Western philosophy from the Pre-Socratics through the Middle Ages.

---

## 1. Source Material

**Primary source:** *Sophie's World* by Jostein Gaarder (1991), pages 1–177 of the PDF edition. This covers the first half of the novel, spanning from the opening "Garden of Eden" chapter through the end of the Middle Ages chapter.

**Coverage:** 15 book chapters, ~177 pages, covering approximately 2,500 years of Western philosophy (from mythological worldview through St. Thomas Aquinas).

---

## 2. Section Architecture

The 15 chapters are grouped into 7 thematic deep-dive sections based on philosophical eras and conceptual coherence:

| Section | Title | Book Chapters | Pages | Philosophical Era |
|---------|-------|--------------|-------|-------------------|
| 01 | The Awakening | Garden of Eden, The Top Hat | 3–21 | Meta: Wonder & Questions |
| 02 | From Myth to Matter | The Myths, Natural Philosophers, Democritus | 22–46 | Pre-Socratics (~600–400 BC) |
| 03 | Athens & the Good Life | Fate, Socrates, Athens | 47–76 | Classical Athens (~470–399 BC) |
| 04 | The World of Ideas | Plato, The Major's Cabin | 77–100 | Plato (~428–348 BC) |
| 05 | The System Builder | Aristotle | 101–116 | Aristotle (~384–322 BC) |
| 06 | Twilight & Crossroads | Hellenism, The Postcards, Two Cultures | 117–157 | Hellenism → Early Christianity |
| 07 | Faith Meets Reason | The Middle Ages | 158–177 | Medieval Philosophy (~400–1400) |

### Cross-cutting Thread: The Hilde Mystery

The novel weaves a meta-narrative — mysterious letters, postcards from a UN soldier, objects belonging to "Hilde Møller Knag" — that deepens with each chapter. This mystery layer is tracked within each section rather than separated out, as it's integral to the reading experience.

---

## 3. Reading Process

### 3.1 PDF Reading

The full PDF (177 pages) was read in batches:
- Pages 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–177
- Each batch was read visually (PDF image extraction) and cross-referenced with text extraction from a previous session

### 3.2 Note-Taking Strategy

Per the user's guidance: **iterative notes per chapter**. Each chapter gets a structured markdown note capturing:
- Key philosophical concepts and arguments
- Gaarder's pedagogical analogies and metaphors
- The narrative frame (Sophie's reactions, Alberto's teaching style)
- Hilde mystery developments
- Connections to other chapters

### 3.3 Deep-Dive Construction

Each section's deep-dive HTML is built from the chapter notes using the reading-assist skill's deep-dive template:
- Three-panel layout: sidebar navigation, summary center, expandable detail right panel
- SVG diagrams for key philosophical concepts
- Light/dark theme toggle
- Jost / EB Garamond / IBM Plex Mono typography

---

## 4. Pedagogical Approach

This is a **reading companion**, not a replacement for the book. The goal:

1. **Illuminate the philosophy** — make the actual philosophical concepts clear, with diagrams showing relationships between thinkers and ideas
2. **Surface Gaarder's craft** — highlight the brilliant analogies (white rabbit, Lego, cookie mold, cave) that make abstract ideas concrete
3. **Track the mystery** — map the meta-narrative clues (Hilde, the Major, Alberto's nature) that reward attentive reading
4. **Connect the dots** — show how each philosopher responds to the previous ones, building a continuous intellectual conversation across 2,500 years

---

## 5. Deliverables

| Deliverable | Format | Location |
|------------|--------|----------|
| Chapter notes (per section) | Markdown | `notes/01-awakening.md` through `notes/07-middle-ages.md` |
| Section deep-dives | HTML | `01-awakening.dd.html` through `07-middle-ages.dd.html` |
| Project index | HTML | `index.html` |
| README | Markdown | `README.md` |
| Project metadata | Markdown | `../.project/` (methodology, changelog, todo) |

---

## 6. Tooling

- **Repository:** github.com/nafSadh/read-rd, subfolder `philosophy/sophies-world-reader/`
- **Template:** Reading-assist skill deep-dive format (CSS ~26K, JS ~7.7K)
- **Build:** Python scripts generating standalone HTML from template + content arrays
- **Execution:** Claude in a single extended Cowork session with human direction
