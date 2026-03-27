# Nano Banana Image Opportunities — Art of Typography

**Status:** Has 10 images (overview + s1). Images are v2 sketch style on disk.

## PROMPT MISMATCH — needs fixing

The HTML `NB_IMAGES` prompt fields still contain v1 photorealistic descriptions. The actual images were regenerated with sketch suffix. The prompts should be updated to match what was actually generated.

### overview.dd.html — current (wrong) vs corrected prompts

| Image | Current (v1) prompt in HTML | Should be (v2 sketch) |
|-------|----------------------------|----------------------|
| `img/hero.png` | "cinematic overhead view of a vintage letterpress workshop... photorealistic" | A vintage letterpress workshop seen from above: wooden type drawers, brass matrices, ink rollers, freshly printed sheets with Garamond letterforms |
| `img/s01-history.png` | "Timeline montage of typography evolution... sepia-to-color gradient" | Timeline of typography evolution: Gutenberg movable type transitioning through Art Nouveau to modern variable fonts on digital screens |
| `img/s02-anatomy.png` | "Technical anatomy diagram of the letter g... engraving style" | Anatomy of the lowercase letter g in Garamond: x-height, ascender, descender, bowl, ear, link, and loop labeled with thin callout lines |
| `img/s03-helvetica.png` | "Split-screen comparison: Helvetica Neue on a Swiss railway timetable" | The word Helvetica set in Helvetica against a Swiss design grid, red and white accents, modernist poster |
| `img/s04-cognition.png` | "Close-up of a human eye reading text... cinematic macro photography" | Neural pathways processing letterforms, brain scan aesthetic with typography elements |
| `img/s05-digital.png` | "modern screen showing variable font axes... product design screenshot" | Variable font axes being adjusted: weight, width, and optical size sliders, dark UI with glowing accents |
| `img/s06-culture.png` | "World map composed entirely of different scripts" | World map with different writing systems in their regions: Arabic calligraphy, Chinese characters, Devanagari, Latin serifs |

### s1-history.dd.html

| Image | Current (v1) prompt | Should be (v2 sketch) |
|-------|---------------------|----------------------|
| `img/s1-hero.png` | "Dramatic chiaroscuro scene of Johannes Gutenberg... Renaissance oil painting" | Johannes Gutenberg inspecting a freshly printed page, workshop with wooden type cases, a screw press in background |
| `img/s1-cuneiform.png` | "Ancient Sumerian cuneiform tablet... archaeological photography" | Sumerian cuneiform tablet with stylus marks, clay surface |
| `img/s1-woodblock.png` | "Chinese woodblock printing workshop... historical illustration" | Chinese woodblock printing: artisan carving characters into pear-wood block, ink brushes and rice paper scrolls |

## Notes
- All prompts above should have the sketch suffix appended when regenerating
- The s2-s4 section pages (`s2-anatomy`, `s3-helvetica`, `s4-cognition`) also have images with stale prompts — same fix needed
