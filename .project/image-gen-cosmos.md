# Image Generation — The Cosmos Project

Instructions for Claude Code agents to generate hero images for The Cosmos deep-dives.

## Setup

```bash
cd /path/to/read-rd
npm install @google/generative-ai
```

## API Details

- **Model:** `gemini-2.0-flash-preview-image-generation`
- **API Key:** Use environment variable `GEMINI_API_KEY`
- **Config:** `{ responseModalities: ['IMAGE', 'TEXT'] }`
- **Output:** PNG, save to `physics/the-cosmos/img/`

## Style Suffix (append to every prompt)

```
, minimal ink line drawing on warm cream paper, single violet accent color,
clean sparse lines, editorial sketch style, playful and elegant, no photorealism
```

See `.project/image-style-ref.md` for full style guide.

## Images Needed

### S2: The Big Bang & CMB
- **File:** `physics/the-cosmos/img/s2-hero.png`
- **Prompt:** `Cosmic microwave background radiation oval projection map of the whole sky, showing tiny temperature anisotropies as subtle variations, concentric rings of acoustic oscillations faintly visible, the universe's baby photo at 380000 years old, with data visualization aesthetic`
- **Already wired:** `s2-bigbang.dd.html` has `NB_IMAGES` config pointing to `img/s2-hero.png`

### S3: Dark Matter (when built)
- **File:** `physics/the-cosmos/img/s3-hero.png`
- **Prompt:** `Galaxy rotation curve diagram: a spiral galaxy seen edge-on with velocity arrows showing flat rotation, dark matter halo surrounding it as a diffuse cloud, gravitational lensing arcs visible behind`

### S4: Dark Energy (when built)
- **File:** `physics/the-cosmos/img/s4-hero.png`
- **Prompt:** `The fate of the universe: three diverging paths from a central point labeled Now, one path expanding forever into cold darkness (Big Freeze), one tearing apart (Big Rip), one curving back (Big Crunch), with timeline markers`

### S5: Fermi Paradox (when built)
- **File:** `physics/the-cosmos/img/s5-hero.png`
- **Prompt:** `The Great Silence: a radio telescope dish pointed at a star field full of galaxies and stars, with radio waves emanating outward but no signal returning, vast emptiness and silence conveyed through negative space`

### S6: Multiverse (when built)
- **File:** `physics/the-cosmos/img/s6-hero.png`
- **Prompt:** `Eternal inflation bubble universes: soap-bubble-like spheres of different sizes floating in a quantum foam, each bubble containing a different set of physical constants shown as abstract patterns`

### S7: Frontiers (when built)
- **File:** `physics/the-cosmos/img/s7-hero.png`
- **Prompt:** `Observatory instruments of the future: JWST hexagonal mirror, LIGO interferometer arms, IceCube detector strings in Antarctic ice, Vera Rubin Observatory dome, all arranged as a constellation of tools pointing at the cosmos`

## Generation Script Template

```javascript
import { GoogleGenerativeAI } from "@google/generative-ai";
import fs from "fs";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash-preview-image-generation" });

const STYLE = `, minimal ink line drawing on warm cream paper, single violet accent color, clean sparse lines, editorial sketch style, playful and elegant, no photorealism`;

async function generateImage(prompt, outputPath) {
  const maxRetries = 4;
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const result = await model.generateContent({
        contents: [{ role: "user", parts: [{ text: prompt + STYLE }] }],
        generationConfig: { responseModalities: ["IMAGE", "TEXT"] }
      });
      const parts = result.response.candidates[0].content.parts;
      for (const part of parts) {
        if (part.inlineData) {
          const buf = Buffer.from(part.inlineData.data, "base64");
          fs.writeFileSync(outputPath, buf);
          console.log(`Saved ${outputPath}: ${buf.length} bytes`);
          return;
        }
      }
      console.log(`No image data on attempt ${attempt + 1}`);
    } catch (e) {
      const delay = 3000 * Math.pow(2, attempt);
      console.log(`Attempt ${attempt + 1} failed: ${e.message}. Retrying in ${delay}ms...`);
      await new Promise(r => setTimeout(r, delay));
    }
  }
  console.error(`Failed after ${maxRetries} attempts`);
}

// Generate S2 hero
await generateImage(
  "Cosmic microwave background radiation oval projection map of the whole sky, showing tiny temperature anisotropies as subtle variations, concentric rings of acoustic oscillations faintly visible",
  "physics/the-cosmos/img/s2-hero.png"
);
```

## Notes

- 503 errors are frequent under load — exponential backoff essential
- Some responses return empty (no `inlineData`) — null check required
- Sketch style works well for diagrams and conceptual illustrations
- Space/sci-fi prompts sometimes override sketch style toward concept art — acceptable
- Images are square from API, cropped by CSS `object-fit: cover`
