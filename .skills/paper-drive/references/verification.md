# Verification Scripts

Run these after building any HTML deliverable — deep-dives, papers, or slides. They catch the issues that visual inspection misses.

---

## SVG Overflow Check

Catches text that extends beyond viewBox or containing rect boundaries. Run after every build.

```python
import re, html as htmlmod

def check_svgs(filename):
    with open(filename) as f:
        c = f.read()

    all_svgs = list(re.finditer(
        r'(<svg[^>]*viewBox="([^"]*)"[^>]*>)(.*?)(</svg>)', c, re.DOTALL))
    issues = []

    for i, m in enumerate(all_svgs):
        vb = m.group(2).split()
        if len(vb) < 4 or float(vb[2]) < 100:
            continue
        vw, vh = float(vb[2]), float(vb[3])
        body = m.group(3)

        # 1. Background rect must match viewBox
        bg = re.search(
            r'<rect[^>]*x="0"[^>]*y="0"[^>]*width="([^"]*)"[^>]*height="([^"]*)"', body)
        if bg:
            bw, bh = float(bg.group(1)), float(bg.group(2))
            if bw != vw or bh != vh:
                issues.append(f'SVG [{i}]: bg rect {bw}×{bh} ≠ viewBox {vw}×{vh}')

        # 2. Text overflow check
        for tm in re.finditer(r'<text\s+([^>]*)>(.*?)</text>', body, re.DOTALL):
            attrs = tm.group(1)
            text = htmlmod.unescape(re.sub(r'<[^>]+>', '', tm.group(2).strip()))
            if not text:
                continue

            x_m = re.search(r'\bx="([^"]*)"', attrs)
            y_m = re.search(r'\by="([^"]*)"', attrs)
            fs_m = re.search(r'font-size="([^"]*)"', attrs)
            anchor_m = re.search(r'text-anchor="([^"]*)"', attrs)

            x = float(x_m.group(1)) if x_m else 0
            y = float(y_m.group(1)) if y_m else 0
            fs = float(fs_m.group(1)) if fs_m else 10
            anchor = anchor_m.group(1) if anchor_m else 'start'

            # Character width: mono ≈ fs×0.62, sans ≈ fs×0.52
            cpx = fs * 0.62 if 'Mono' in attrs else fs * 0.52
            tw = len(text) * cpx

            if anchor == 'middle':
                tl, tr = x - tw / 2, x + tw / 2
            elif anchor == 'end':
                tl, tr = x - tw, x
            else:
                tl, tr = x, x + tw

            if tr > vw - 3:
                issues.append(
                    f'SVG [{i}] RIGHT overflow: "{text[:35]}" '
                    f'(margin={vw - tr:.0f}px)')
            if tl < 2:
                issues.append(
                    f'SVG [{i}] LEFT overflow: "{text[:35]}" '
                    f'(margin={tl:.0f}px)')
            if y > vh - 3:
                issues.append(
                    f'SVG [{i}] BOTTOM overflow: "{text[:35]}" '
                    f'(margin={vh - y:.0f}px)')

    if issues:
        print(f'⚠️  {filename}: {len(issues)} issues')
        for iss in issues:
            print(f'  {iss}')
        return False
    else:
        print(f'✓ {filename}: all SVGs clean')
        return True
```

Usage:
```python
check_svgs('s3-agents.dd.html')
check_svgs('survey-paper.html')
```

Or batch:
```python
import glob
all_ok = True
for f in sorted(glob.glob('*.html')):
    if not check_svgs(f):
        all_ok = False
print('\n' + ('✅ ALL CLEAN' if all_ok else '⚠️ Fix issues above'))
```

---

## Link Integrity Check

Catches unbalanced `<a>` tags, links inside SVG, nested links, and links inside font declarations.

```python
import re

def check_links(filename):
    with open(filename) as f:
        c = f.read()

    issues = []

    # 1. Balanced tags
    opens = len(re.findall(r'<a ', c))
    closes = len(re.findall(r'</a>', c))
    if opens != closes:
        issues.append(f'Unbalanced: {opens} opens, {closes} closes')

    # 2. Links inside SVG
    for m in re.finditer(r'<svg.*?</svg>', c, re.DOTALL):
        svg_links = m.group(0).count('<a href')
        if svg_links:
            issues.append(f'{svg_links} link(s) inside SVG')

    # 3. Nested links
    nested = len(re.findall(r'<a [^>]*<a ', c))
    if nested:
        issues.append(f'{nested} nested <a> tag(s)')

    # 4. Links in font-family
    font_links = len(re.findall(r'font-family[^>]*<a ', c))
    if font_links:
        issues.append(f'{font_links} link(s) in font-family')

    ext = len(re.findall(r'href="https?://', c))
    internal = len(re.findall(r'href="s[0-9]', c))

    if issues:
        print(f'⚠️  {filename}: {", ".join(issues)}')
        return False
    else:
        print(f'✓ {filename}: {ext} external, {internal} internal links')
        return True
```

Usage:
```python
import glob
for f in sorted(glob.glob('*.html')):
    check_links(f)
```

---

## Combined Check (run after every build)

```python
import glob

print("=== SVG Overflow ===")
svg_ok = True
for f in sorted(glob.glob('s*.dd.html') + glob.glob('*-paper.html') + glob.glob('*-slides.html') + glob.glob('overview.dd.html')):
    if not check_svgs(f):
        svg_ok = False

print("\n=== Link Integrity ===")
link_ok = True
for f in sorted(glob.glob('s*.dd.html') + glob.glob('*-paper.html') + glob.glob('*-slides.html') + glob.glob('overview.dd.html')):
    if not check_links(f):
        link_ok = False

print('\n' + ('✅ ALL CHECKS PASSED' if svg_ok and link_ok else '⚠️ FIX ISSUES ABOVE'))
```

---

## Source Link Density Check

Papers and slides must have proper source hyperlinking. This check catches deliverables where sources are mentioned by name but not linked.

```python
import re

def check_source_density(filename):
    with open(filename) as f:
        c = f.read()

    link_count = len(re.findall(r'<a\s+href=', c))
    # Exclude nav/sidebar/footer links (rough heuristic: links in <nav>, sidebar, footer)
    # Count external links (to actual sources)
    ext_links = len(re.findall(r'href="https?://', c))
    
    issues = []

    # Papers should have 20+ source links for multi-section papers
    if '-paper.html' in filename:
        if ext_links < 20:
            issues.append(f'Only {ext_links} external links — expected 20+ for a paper')

        # Check for dd.html references (papers must not link to deep-dives)
        dd_refs = re.findall(r'["\']s\d+-[^"\']*\.dd\.html', c)
        if dd_refs:
            issues.append(f'{len(dd_refs)} deep-dive reference(s) found — papers must be standalone: {dd_refs[:3]}')
    
    # Slides should also have source links
    if '-slides.html' in filename:
        if ext_links < 10:
            issues.append(f'Only {ext_links} external links — expected 10+ for slides')

    if issues:
        print(f'⚠️  {filename}: {"; ".join(issues)}')
        return False
    else:
        print(f'✓ {filename}: {ext_links} external source links')
        return True
```

Usage:
```python
import glob
for f in sorted(glob.glob('*-paper.html') + glob.glob('*-slides.html')):
    check_source_density(f)
```

---

## Full Verification Suite (run before every push)

```python
import glob

all_files = sorted(
    glob.glob('s*.dd.html') + 
    glob.glob('*-paper.html') + 
    glob.glob('*-slides.html') + 
    glob.glob('overview.dd.html')
)

print("=== SVG Overflow ===")
svg_ok = all(check_svgs(f) for f in all_files)

print("\n=== Link Integrity ===")
link_ok = all(check_links(f) for f in all_files)

print("\n=== Source Link Density (papers & slides) ===")
src_ok = True
for f in sorted(glob.glob('*-paper.html') + glob.glob('*-slides.html')):
    if not check_source_density(f):
        src_ok = False

all_ok = svg_ok and link_ok and src_ok
print('\n' + ('✅ ALL CHECKS PASSED' if all_ok else '⚠️ FIX ISSUES ABOVE'))
```
