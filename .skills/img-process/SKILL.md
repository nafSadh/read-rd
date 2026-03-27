---
name: img-process
description: Process AI-generated sketch images (from Gemini, DALL-E, etc.) for web page integration. Removes cream/paper backgrounds to create transparent PNGs, generates dark-mode variants that preserve violet/purple accent colors, and outputs HTML with light/dark theme switching. Use whenever the user has generated images and wants them cleaned up for a web page, needs background removal from sketch-style images, wants dark mode image variants, or says things like "process this image", "make it transparent", "create dark mode version", "add this image to the page".
---

# Image Processing for Web Sketches

Process AI-generated ink sketch images for seamless web integration. Designed for the style: **minimal ink line drawing on warm cream paper, single violet accent color**.

## What This Skill Does

1. **Backup** originals to `bak/` subfolder
2. **Remove cream background** → transparent PNG
3. **Create dark-mode variant** (`-dark.png`) preserving violet hue
4. **Add HTML** with light/dark theme switching

## Step-by-Step

### 1. Backup

Always copy the original to `bak/` before processing:

```python
import shutil, os
os.makedirs(os.path.join(dest_dir, "bak"), exist_ok=True)
shutil.copy2(src_path, os.path.join(dest_dir, "bak", os.path.basename(src_path)))
```

### 2. Background Removal

Detect the paper color by averaging the four corner pixels, then set any pixel within a threshold to transparent.

```python
from PIL import Image

img = Image.open(src_path).convert("RGBA")
w, h = img.size

# Sample corners (5px inset to avoid edge artifacts)
corners = [img.getpixel((5,5)), img.getpixel((w-5,5)),
           img.getpixel((5,h-5)), img.getpixel((w-5,h-5))]
avg_r = sum(c[0] for c in corners) // 4
avg_g = sum(c[1] for c in corners) // 4
avg_b = sum(c[2] for c in corners) // 4

# Remove background
pixels = img.load()
threshold = 35  # RGB distance tolerance
for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if (abs(r - avg_r) < threshold and
            abs(g - avg_g) < threshold and
            abs(b - avg_b) < threshold):
            pixels[x, y] = (r, g, b, 0)

img.save(os.path.join(dest_dir, output_name + ".png"), "PNG")
```

The threshold of 35 works well for Gemini-generated sketches on cream paper. Increase to ~45 if faint paper texture remains; decrease to ~25 if ink lines are getting eaten.

### 3. Dark Mode Variant

From the already-transparent light PNG, create a dark variant. The key insight: simple `filter: invert(1)` in CSS turns purple to green. Instead, process pixel-by-pixel:

- **Violet/purple pixels** (HSV hue 0.55-0.9, saturation >0.15): keep the hue, brighten for dark backgrounds
- **Non-violet pixels** (ink lines): convert to light grey
- **Transparent pixels**: leave untouched

```python
import colorsys

# Load the TRANSPARENT light version (not the original)
img = Image.open(light_png_path).convert("RGBA")
pixels = img.load()
w, h = img.size

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if a == 0:
            continue

        rf, gf, bf = r/255.0, g/255.0, b/255.0
        h_val, s, v = colorsys.rgb_to_hsv(rf, gf, bf)

        if s > 0.15 and 0.55 < h_val < 0.9:
            # Violet — keep hue, brighten
            new_v = min(1.0, 0.4 + v * 0.5)
            nr, ng, nb = colorsys.hsv_to_rgb(h_val, s * 0.8, new_v)
            pixels[x, y] = (int(nr*255), int(ng*255), int(nb*255), a)
        else:
            # Non-violet ink — make light grey
            lum = 0.299*rf + 0.587*gf + 0.114*bf
            new_lum = max(0.5, 1.0 - lum * 0.7)
            pixels[x, y] = (int(new_lum*255), int(new_lum*250), int(new_lum*245), a)

img.save(os.path.join(dest_dir, output_name + "-dark.png"), "PNG")
```

### 4. HTML Integration

Add both image variants with CSS-based theme switching:

```html
<div class="section-img">
  <img class="light-img" src="img/name.png" alt="...">
  <img class="dark-img" src="img/name-dark.png" alt="...">
</div>
```

Required CSS (add once):

```css
.section-img .dark-img { display: none }
[data-theme="dark"] .section-img .light-img { display: none }
[data-theme="dark"] .section-img .dark-img { display: block }
```

## Notes

- **Accent color**: The hue range 0.55-0.9 covers violet/purple/indigo. If the accent color is different (e.g., teal), adjust the hue range accordingly.
- **Large images**: Gemini outputs can be 2816x1536+. The processing handles any size but may take 10-30 seconds for large images.
- **Batch processing**: When processing multiple images, loop through all files and call the same steps. The `bak/` folder prevents accidental data loss.
- **File format**: Always output PNG (not WebP) since transparency support is critical. The original WebP files go in `bak/`.
