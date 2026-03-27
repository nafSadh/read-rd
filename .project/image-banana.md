# Nano Banana Image Generation Recommendations

Every project in the repository contains one or more deep dive (`.dd.html`) files. They can all benefit from `nano-banana.js` injected images, not just for hero art, but also for **academic-looking diagrams** to accompany theoretical papers, courses, and complex concepts.

Below is a systematic breakdown project-by-project, detailing where to inject images, what type they should be, and the corresponding prompts.

---

## 1. AI & Agentic Systems (`ai/agentic-lm-survey/`)
*This directory surveys papers and model architectures. It is perfect for academic/system architecture diagrams.*

- **Overview (`overview.dd.html` if exists, or `s1-reason.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** A high-level system architecture diagram showing a multi-agent LLM framework, with nodes labeled for Planning, Tool Action, Memory, and Reflection, elegant academic chart style, minimalist ink lines

- **ACT / Tool Use Papers (`s2-act.dd.html`)**
  - **Target:** `'detail-hero'` (or `'.diagram-wrap'`)
  - **Type:** `'wide'`
  - **Prompt:** Flowchart showing an AI agent executing a loop: Observation -> Thought -> Action -> Environment Feedback, clean technical diagram style, geometric and precise, academic paper aesthetic

- **INTERACT & Multi-Agent (`s3-interact.dd.html`)**
  - **Target:** `'detail-hero'`
  - **Type:** `'wide'`
  - **Prompt:** Network topology diagram of multiple AI agents communicating through a central message bus, elegant dotted lines and data pack representations, technical drawing

## 2. Stanford Machine Learning (`courses/scpd-ml/`)
*Perfect for mathematical intuition and algorithmic diagrams.*

- **Support Vector Machines (`svm-kernels.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** Math plotted in 3D: a hyperplane cleanly separating two classes of geometric shapes on a surface transformed by a kernel function, sleek lines, mathematical textbook style

- **PCA & ICA (`pca-ica.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** Abstract data visualization showing a cloud of data points being projected onto principal component axes, minimizing orthogonal distance, clean academic diagram style

- **Neural Networks (`neural-networks.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** A clean graph theory diagram of a multi-layer perceptron, showing input layers, hidden layers, and output layers with connected weights, minimal geometric style

## 3. Stanford Deep Generative Models (`courses/scpd-deep-gen-ai/`)

- **Diffusion Models (`diffusion.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** A process diagram showing an image slowly gaining Gaussian noise forward in time, and being iteratively denoised backward in time, represented by an abstract geometric shape, academic style

- **Variational Autoencoders (`vae.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** An encoder-decoder bottleneck architecture diagram mapping high dimensional data into a multivariate Gaussian latent space, elegant academic line art

## 4. Cognitive Science Series (`cog-sci/` & `neuro/`)
*Best for psychological theory models and neurobiological diagrams.*

- **Brain Energy (`cog-sci/brain-energy/overview.dd.html` & `neuro/`)**
  - **Target:** `'hero'`
  - **Prompt:** A metabolic pathway diagram stylized inside the silhouette of a human brain, focusing on mitochondrial ATP production and neural synapses, technical medical illustration style

- **Science of Humor (`cog-sci/science-of-humor/overview.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** A conceptual diagram showing the incongruity-resolution theory of humor: two intersecting logical planes with a sudden paradigm shift, abstract academic figure

- **Attachment Theory (`cog-sci/attachment-theory/overview.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** A 2x2 psychological matrix mapping anxiety versus avoidance, showing the four attachment styles as clusters of social nodes, clean behavior science graph style

- **Sleep & Dreams (`cog-sci/sleep-and-dreams/overview.dd.html`)**
  - **Target:** `'detail-hero'` (near section on Sleep Stages)
  - **Type:** `'wide'`
  - **Prompt:** A hypnogram chart showing the cycling of human sleep stages over 8 hours, dipping into REM and deep slow-wave sleep, elegant scientific data visualization

## 5. Anthropological & Cultural Studies (`anthro/` and `craft/`)

- **Religion Today (`anthro/religion-today/overview.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** A demographical map of the globe rendered in stylized contours, overlaid with shifting secularization and belief trends, elegant statistical style

- **Constructed Languages (`craft/constructed-languages/overview.dd.html`)**
  - **Target:** `'hero'`
  - **Prompt:** A linguistic syntax tree diagram mapping the morphological structure of an invented word, minimal typographic and graphic design

- **The Art of Typography (`craft/art-of-typography/overview.dd.html`)**
  - **Target:** `'detail-hero'`
  - **Type:** `'wide'`
  - **Prompt:** An anatomical diagram of a serif letterform, labeling the x-height, ascender, baseline, and counter, clean technical typographic chart

## 6. The Cosmos (`physics/the-cosmos/`)
*(Note: Has some existing images, but can add more academic charts)*

- **Dark Matter (`s3-darkmatter.dd.html`)**
  - **Target:** `'.diagram-wrap'` (Injecting into existing text)
  - **Type:** `'section'`
  - **Prompt:** A chart plotting rotational velocity vs. distance from galactic center: the expected Keplerian decline versus the observed flat rotation curve, styled as a modern academic data plot

---

### Implementation Guide: "Academic Looking Diagrams"

For the academic/paper diagrams, the `nano-banana.js` properties should be adjusted to fit seamlessly into the content flow rather than sitting at the top:

```javascript
{
  target: '.diagram-wrap', // Or any specific section paragraph
  position: 'after',       // Place it immediately after the target element
  type: 'wide',            // Academic diagrams often span full width
  prompt: '[Concept description], precise technical drawing, academic paper figure, clean sparse lines, mathematical textbook style, sans-serif labels, crisp vector style'
}
```

**Common Style Suffix to append for Academic Diagrams:**
`, precise technical drawing, academic paper figure, clean sparse lines, geometric, mathematical textbook style, crisp vector style, single accent color, no photorealism`
