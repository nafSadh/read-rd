# Methodology — Mathematics for Machine Learning

## Study Question
How do the mathematical foundations (linear algebra, calculus, probability, optimization) connect to and enable four core ML algorithms (linear regression, PCA, GMMs, SVMs)?

## Scope
**In scope:** All 11 numbered chapters of the textbook (Ch 2–12). Chapter 1 (Introduction) is skipped as it contains no substantive math content.

**Out of scope:** Implementation code, alternative textbooks, ML algorithms beyond those in Part II.

## Source Strategy
Primary source: the textbook PDF (mml-book.github.io/book/mml-book.pdf). Each chapter deep-dive is built directly from the chapter, supplemented by:
- The book's official exercises and solutions (GitHub)
- Supplementary notes in the `notes/` directory as understanding develops

This is a textbook study project, not a literature survey — source adequacy assessment is per-chapter, not across external sources.

## Study Approach
Each chapter gets:
1. A markdown notes file (`notes/{NN}-{name}.md`) with key definitions, theorems, worked intuitions, and connections to other chapters
2. An interactive HTML deep-dive (`c{N}-{name}.dd.html`) with expandable panels, SVG diagrams, and cross-chapter links

Chapters are studied in order (C2 → C12) since Part II depends on Part I.

## Chapter Order
1. C2: Linear Algebra
2. C3: Analytic Geometry
3. C4: Matrix Decompositions
4. C5: Vector Calculus
5. C6: Probability & Distributions
6. C7: Continuous Optimization
7. C8: When Models Meet Data
8. C9: Linear Regression
9. C10: PCA
10. C11: GMMs
11. C12: SVMs

## Deliverables Plan
- 11 chapter deep-dives (c2-linear-algebra.dd.html … c12-svms.dd.html)
- 11 markdown notes files
- Running synthesis notes (notes/00-synthesis.md) — cross-chapter connections

No papers or slides planned (study project, not survey output).

---
*Started: 2026-04-09. Updated each session.*
