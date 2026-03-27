# Methodology — Sophie's World Companion

**Document version:** March 24, 2026
**Scope:** Complete methodology for the Sophie's World companion deep-dives, executed in a single session between a human researcher and Claude (Anthropic), following the methodology established in the [Agentic LLMs Survey](../../ai/agentic-lm-survey/.project/methodology.md).

---

## 1. Research Question

**Starting point:** The user identified Sophie's World by Jostein Gaarder (1991) and its [Wikipedia article](https://en.wikipedia.org/wiki/Sophie%27s_World) as the baseline. The question: how would you create a modern companion that covers both what the book covers and the ~35 years of philosophical development since publication?

**Framing decision:** Rather than a summary or review, we chose a *companion guide* — interactive deep-dive HTML pages that both explain and extend Gaarder's philosophical curriculum. Seven sections covering 2,600 years of philosophy, from the Pre-Socratics through contemporary developments in AI ethics, consciousness studies, and decolonial thought.

---

## 2. Taxonomy Design

### 2.1 Section Structure

We divided the history of philosophy into seven sections, following Gaarder's chronological approach but with modern groupings:

| Section | Title | Period | Source |
|---------|-------|--------|--------|
| S1 | The Cradle of Wonder | 600–400 BCE | PDF chapters 1–5 |
| S2 | The Athenian Triad | 470–322 BCE | PDF chapters 6–8 |
| S3 | From Empire to Faith | 300 BCE–1400 CE | PDF chapters 9–11 |
| S4 | The Modern Turn | 1400–1800 | Web research + Gaarder's known coverage |
| S5 | Revolution & Reaction | 1800–1950 | Web research + Gaarder's known coverage |
| S6 | Existentialism & Beyond | 1940–1991 | Web research + Gaarder's known coverage |
| S7 | Philosophy After Sophie | 1991–2026 | Web research (entirely new content) |

### 2.2 What Each Section Covers Beyond Gaarder

- **S1–S3**: Based directly on the PDF. We supplemented with what Gaarder omits (Pythagoras, Zeno's paradoxes, Islamic philosophy, the Skeptics).
- **S4–S6**: The PDF only goes through the Middle Ages. These sections reconstruct Gaarder's treatment from his known pedagogical style and supplement heavily with modern scholarship.
- **S7**: Entirely new — covers 10 areas of contemporary philosophy that didn't exist or weren't prominent when Gaarder wrote.

---

## 3. Source Material

### 3.1 Primary Source

**Sophie's World** by Jostein Gaarder, English translation by Paulette Miller (Farrar, Straus and Giroux, 1994). Pages 1–184 of the PDF, covering chapters from "The Garden of Eden" through "The Middle Ages" (St. Augustine, Thomas Aquinas, Hildegard of Bingen).

### 3.2 PDF Extraction

The PDF (177 pages, 763KB) was text-extracted using PyMuPDF (`fitz`). Total extraction: 359,327 characters. The text was split into 11 chapter sections based on page ranges identified by ALL CAPS headings:

| Chapter | Pages | Characters |
|---------|-------|-----------|
| Garden of Eden | 3–10 | 15,477 |
| Top Hat | 11–21 | 20,791 |
| Myths | 22–28 | 13,714 |
| Natural Philosophers | 29–46 | 36,044 |
| Fate/Democritus | 47–54 | 16,101 |
| Socrates | 55–78 | 47,671 |
| Plato | 79–100 | 45,140 |
| Aristotle | 101–120 | 42,256 |
| Hellenism | 121–141 | 41,772 |
| Two Cultures | 142–160 | 39,639 |
| Middle Ages | 161–177 | 37,059 |

### 3.3 Supplementary Web Research

For sections beyond the PDF (S4–S7), we used web search across:
- Stanford Encyclopedia of Philosophy
- Internet Encyclopedia of Philosophy
- Academic sources on philosophical developments since 1991
- Contemporary scholarship on each philosophical era

---

## 4. Reading Process (Iterative, Per-Chapter)

### 4.1 Method

Following the survey methodology's iterative approach, each chapter was read and annotated separately. Seven parallel reading agents each took one chapter cluster and produced structured notes capturing:

1. **Philosophers/thinkers covered** (with dates)
2. **Key philosophical concepts** introduced
3. **Key questions** posed
4. **What Gaarder covers well** vs. **what he omits**
5. **Notable framings** (paraphrased, not verbatim)
6. **Connections to later philosophy**

### 4.2 Notes Produced

| Notes File | Covers | Size |
|-----------|--------|------|
| notes-01-intro-and-myths.md | Garden of Eden, Top Hat, Myths | 14K |
| notes-02-natural-philosophers.md | Natural Philosophers, Fate/Democritus | 20K |
| notes-03-socrates.md | Socrates chapter | 15K |
| notes-04-plato.md | Plato chapter | 13K |
| notes-05-aristotle.md | Aristotle chapter | 18K |
| notes-06-hellenism.md | Hellenism chapter | 14K |
| notes-07-two-cultures-and-middle-ages.md | Two Cultures, Middle Ages | 24K |
| notes-08-renaissance-to-existentialism.md | Web research: Renaissance → Sartre | 69K |
| notes-09-philosophy-after-sophie.md | Web research: 1991–2026 | ~50K |

Total: ~240K of structured notes from 9 files.

### 4.3 What the Notes Captured

**From the PDF chapters (notes 01–07):** Close reading of Gaarder's text, identifying his pedagogical techniques (the rabbit-in-hat metaphor, Sophie's naive questions, Alberto Knox's Socratic method), the philosophical content he presents, and gaps in his coverage (e.g., Pythagoras absent from Pre-Socratics, Skeptics absent from Hellenism, Islamic philosophy barely mentioned in Middle Ages).

**From web research (notes 08–09):** Reconstruction of Gaarder's likely treatment of Renaissance through existentialism, supplemented with contemporary scholarship. For post-1991 philosophy, original research on 10 major areas of contemporary philosophical development.

---

## 5. Build Process

### 5.1 Template System

We used the deep-dive template from the reading-assist skill: a three-panel layout (sidebar navigation, scrollable summaries, expandable detail panel) with light/dark theming, responsive design, and inline SVG diagrams.

The template CSS (26K) and JS DOM builder (7.7K) were extracted from the reference HTML and cached. Each deep-dive HTML is a standalone file: the CSS and JS are embedded directly, and the content is defined via three JavaScript arrays (`sections[]`, `summaries[]`, `details[]`).

### 5.2 Parallel Build

Seven agents built the seven deep-dive HTMLs simultaneously, each reading the relevant notes and producing a complete standalone file. A separate step built the index page.

### 5.3 Deliverables

| File | Title | Size | Sections |
|------|-------|------|----------|
| index.html | Sophie's World Companion | 17K | Landing page |
| s1-wonder.dd.html | The Cradle of Wonder | 79K | 7 sections |
| s2-athens.dd.html | The Athenian Triad | 73K | 8 sections |
| s3-faith.dd.html | From Empire to Faith | 59K | 8 sections |
| s4-modern.dd.html | The Modern Turn | 74K | 8 sections |
| s5-revolution.dd.html | Revolution & Reaction | 78K | 8 sections |
| s6-existentialism.dd.html | Existentialism & Beyond | 72K | 7 sections |
| s7-after-sophie.dd.html | Philosophy After Sophie | 68K | 8 sections |

Total output: 521K of interactive HTML across 8 files, with 54 sections containing both summary and detail views, inline SVG diagrams, and full theme support.

---

## 6. Limitations

1. **Partial source material:** Only pages 1–184 of Sophie's World were available as PDF. Chapters on Renaissance through existentialism were reconstructed from web research rather than direct reading.

2. **Single-session execution:** The entire project was built in one conversation session. A multi-session approach would allow reflection and quality iteration.

3. **No peer review:** The philosophical content was synthesized by Claude from notes and web research. Specific claims should be verified against primary sources.

4. **Western-centric baseline:** Sophie's World is explicitly a history of *Western* philosophy. While S7 addresses decolonial thought and Eastern philosophy, the overall structure reflects Gaarder's framing.

5. **Copyright considerations:** The deep-dives do not reproduce text from Sophie's World. All content is original synthesis and analysis based on the philosophical ideas Gaarder covers.

---

## 7. Reproducibility

All notes are preserved in the `notes/` directory. The methodology is documented here. The template CSS/JS are from the reading-assist skill. Any future researcher can:

1. Start from the same PDF
2. Read the structured notes
3. Compare their analysis against our deep-dives
4. Extend the work (e.g., reading the full book, adding Eastern philosophy sections)
