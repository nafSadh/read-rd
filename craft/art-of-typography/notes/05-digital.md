# S5: Digital Typography — Deep Dive Notes

> 11 sources. PostScript, TrueType, OpenType, and the web — how type went from metal to math.

---

## PostScript (1984-1985)

### Origins
- Charles Geschke and John Warnock left Xerox PARC (1982) to found Adobe
- PostScript: page description language that treated text and graphics as mathematical outlines
- Type 1 fonts: scalable outlines with "hinting" instructions for low-resolution rendering

### Impact
- Apple licensed PostScript for the LaserWriter (January 1985)
- First time a desktop printer could produce near-typesetting-quality output
- Adobe controlled the font format — and charged handsomely for it
- Type 1 specification was proprietary until 1990 (Adobe published it under pressure)

## TrueType (~1991)

### The Apple Response
- Apple developed TrueType to break Adobe's PostScript monopoly
- Licensed to Microsoft immediately
- Key difference: quadratic B-splines (simpler math) vs PostScript's cubic Bezier curves
- Each font included its own rendering instructions (hinting was built-in)

### The Font Wars
- Apple bundled TrueType with System 7 (1991)
- Microsoft bundled it with Windows 3.1 (1992)
- Adobe responded by publishing the Type 1 specification
- For a decade, three incompatible font formats coexisted: Type 1, TrueType, and bitmap

## OpenType (Mid-1990s)

### The Merger
- Adobe and Microsoft jointly developed OpenType starting ~1996
- Design goal: unify Type 1 and TrueType into a single cross-platform format
- Led by David Lemon (Adobe) and Bill Hill (Microsoft)

### Technical Advances
- Up to 65,536 glyphs per font (vs 256 for Type 1)
- Advanced typographic features: contextual alternates, ligatures, small caps, old-style figures, stylistic sets
- Cross-platform: same file works on Mac and Windows
- Can contain either PostScript or TrueType outlines inside
- Unicode support for multilingual typography

### Adoption
- Became the standard format by mid-2000s
- Adobe converted entire library to OpenType
- PostScript fonts effectively deprecated by 2023

## Variable Fonts (2016)

### The Innovation
- Introduced in OpenType 1.8 specification
- Jointly developed by Adobe, Apple, Google, Microsoft
- Single font file contains multiple design axes

### How It Works
- **Axes**: weight, width, slant, optical size, and custom axes
- Designer defines master outlines at axis extremes (e.g., Thin and Black)
- Software interpolates intermediate values
- User/developer can request any value on any axis

### Benefits
- **Performance**: one file replaces 10-20 static font files
- **Flexibility**: fine-grained control over weight, width, etc.
- **Responsive design**: type can adapt to viewport/context
- **Creative freedom**: animation along axes, fluid transitions

### Status in 2026
- Google endorsing variable fonts as new standard (Google Sans Flex)
- All major browsers support font-variation-settings
- Google Fonts serving variable versions by default
- Progressive enhancement pattern: static fallback, variable for capable browsers

## Desktop Publishing Revolution (1984-1985)

### The Convergence
1. **Apple Macintosh** (January 1984): WYSIWYG display, Susan Kare's bitmap fonts
2. **Apple LaserWriter** (January 1985): 300dpi PostScript output
3. **Aldus PageMaker** (July 1985): first DTP software

### Paul Brainerd's Term
- Aldus founder coined "desktop publishing" as marketing term
- Professional typesetting ($100K+ equipment) replaced by $7,000 setup
- The "Mac + LaserWriter + PageMaker" trinity

### Consequences
- Designers gained direct control over type (no more typesetter intermediary)
- Non-designers also gained control — not always a benefit
- "Desktop publishing" became the dominant production method by late 1980s
- Thousands of new typefaces created as digital type design became accessible

## Google Fonts Democratization

### Launch and Growth
- Google Fonts launched 2010
- Free, open-source font families hosted on Google's CDN
- 1,500+ families available by 2026
- 70+ trillion font serves total

### Impact
- Demolished the web-safe font constraint (previously ~12 reliable fonts)
- Any website could use professional typography at zero cost
- Enabled typographic diversity across the web

### Concerns
- **Privacy**: each font request sends data to Google (IP, referrer, user agent)
- **GDPR**: German courts ruled Google Fonts tracking violates GDPR (2022)
- **Performance**: external font requests add latency
- **Self-hosting**: growing trend to download and host fonts locally

## Web Typography in 2026

### CSS clamp() and Fluid Type
```css
h1 { font-size: clamp(2rem, 2.4rem + 1vw, 3.2rem); }
```
Replaces breakpoint-based responsive type. Smooth scaling without media queries.

### System Font Stacks
```css
font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", sans-serif;
```
Zero-latency fallback using the OS's native font. Performance benefit: no font download at all.

### Best Practices
- WOFF2 as standard compression format
- font-display: swap to prevent invisible text during loading
- preconnect to font CDNs
- Subset fonts to include only needed characters
- Minimum 16px body text
- 4.5:1 contrast ratio (WCAG AA)
- 1.4-1.6 line-height for body text

### The EB Garamond + Jost + IBM Plex Mono Stack
This project uses:
- **EB Garamond**: Georg Duffner's open-source revival of Claude Garamond's 16th-century type. Serif for headings and prose.
- **Jost**: Owen Earl's geometric sans-serif inspired by Paul Renner's Futura. Body text and UI.
- **IBM Plex Mono**: Mike Abbink/Bold Monday for IBM. Monospace for data, stats, code.

Three fonts, three roles, three centuries of type history in a single stack.
