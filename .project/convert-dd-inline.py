#!/usr/bin/env python3
"""
convert-dd-inline.py
Converts JS-array-based dd.html files to inline HTML content.

Usage:
  python3 .project/convert-dd-inline.py [--dry-run] [--file path/to/file.dd.html]
"""

import os
import re
import sys
import json
import subprocess

DRY_RUN = '--dry-run' in sys.argv
SINGLE_FILE = None
for i, arg in enumerate(sys.argv):
    if arg == '--file' and i + 1 < len(sys.argv):
        SINGLE_FILE = sys.argv[i + 1]

# ─── Constants ───────────────────────────────────────────────────────────────

DETAIL_BTN_SVG = '<svg width="14" height="14" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>'

DETAIL_NUM_SVG = '<svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>'

CTRL_OPEN_SVG = '<svg width="16" height="16" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>'

CTRL_CLOSE_SVG = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><line x1="6.5" y1="4" x2="13" y2="4"/><line x1="3" y1="8" x2="13" y2="8"/><line x1="6.5" y1="12" x2="13" y2="12"/></svg>'

INTERACTION_JS_WITH_DETAILS = """
// Theme
const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);
document.getElementById('theme-btn').onclick = () => {
  const next = document.body.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
  document.body.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
};

// Sidebar navigation
const sidebarItems = document.querySelectorAll('.sidebar-item');
const sectionBlocks = document.querySelectorAll('.section-block');
const mainScroll = document.getElementById('main-scroll');

function scrollToSection(idx) {
  if (sectionBlocks[idx]) sectionBlocks[idx].scrollIntoView({behavior:'smooth',block:'start'});
}
sidebarItems.forEach((item, idx) => { item.onclick = () => scrollToSection(idx); });

// Sidebar tooltip (detail-open mode)
const sidebarTip = document.getElementById('sidebar-tooltip');
const sidebarEl = document.querySelector('.sidebar');
const sidebarNav = document.getElementById('sidebar-nav');
let tipActive = false;
sidebarNav.addEventListener('mouseleave', () => { tipActive = false; sidebarTip.classList.remove('visible'); });
sidebarNav.addEventListener('mousemove', (e) => {
  if (!document.body.classList.contains('detail-open')) {
    if (tipActive) { tipActive = false; sidebarTip.classList.remove('visible'); }
    return;
  }
  const item = e.target.closest('.sidebar-item');
  if (!item) { if (tipActive) { tipActive = false; sidebarTip.classList.remove('visible'); } return; }
  const rect = item.getBoundingClientRect();
  const sRight = sidebarEl.getBoundingClientRect().right;
  sidebarTip.textContent = item.getAttribute('data-label');
  sidebarTip.style.left = (sRight - 1) + 'px';
  sidebarTip.style.top = rect.top + 'px';
  sidebarTip.style.height = rect.height + 'px';
  if (!tipActive) { tipActive = true; sidebarTip.classList.add('visible'); }
});

// Detail panel
let lastDetailIdx = 0;
const rightPanel = document.getElementById('right');
const stickyTitle = document.getElementById('right-sticky-title');

function openDetail(idx) {
  lastDetailIdx = idx;
  document.querySelectorAll('.detail').forEach(d => d.style.display = 'none');
  document.getElementById('detail-' + idx).style.display = 'block';
  rightPanel.classList.remove('closed');
  document.body.classList.add('detail-open');
  rightPanel.scrollTop = 0;
  stickyTitle.classList.remove('visible');
}
function closeRight() {
  rightPanel.classList.add('closed');
  document.body.classList.remove('detail-open');
}

// Detail buttons in section blocks
document.querySelectorAll('.s-detail-btn').forEach((btn, idx) => { btn.onclick = () => openDetail(idx); });

// Toggle detail button
document.getElementById('detail-btn').onclick = () => {
  if (document.body.classList.contains('detail-open')) closeRight();
  else openDetail(lastDetailIdx);
};

// Compact header + scroll spy
mainScroll.addEventListener('scroll', () => {
  document.querySelector('.main-head').classList.toggle('compact', mainScroll.scrollTop > 40);
  let activeIdx = 0;
  sectionBlocks.forEach((b, i) => {
    if (b.getBoundingClientRect().top < mainScroll.getBoundingClientRect().top + 120) activeIdx = i;
  });
  sidebarItems.forEach((item, i) => item.classList.toggle('active', i === activeIdx));
});

// Sticky header in right panel
rightPanel.addEventListener('scroll', () => {
  const activeDetail = rightPanel.querySelector('.detail[style*="display: block"], .detail[style*="display:block"]');
  if (!activeDetail) return;
  const h2 = activeDetail.querySelector('.detail-header h2') || activeDetail.querySelector('h2');
  if (!h2) return;
  const rect = h2.getBoundingClientRect();
  const panelRect = rightPanel.getBoundingClientRect();
  const topbar = document.querySelector('.right-topbar');
  if (rect.bottom < panelRect.top + 56) {
    stickyTitle.textContent = h2.textContent;
    stickyTitle.classList.add('visible');
    topbar.classList.add('scrolled');
  } else {
    stickyTitle.classList.remove('visible');
    topbar.classList.remove('scrolled');
  }
});

// ESC closes detail panel
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeRight(); });
"""

INTERACTION_JS_NO_DETAILS = """
// Theme
const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);
document.getElementById('theme-btn').onclick = () => {
  const next = document.body.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
  document.body.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
};

// Sidebar navigation
const sidebarItems = document.querySelectorAll('.sidebar-item');
const sectionBlocks = document.querySelectorAll('.section-block');
const mainScroll = document.getElementById('main-scroll');

function scrollToSection(idx) {
  if (sectionBlocks[idx]) sectionBlocks[idx].scrollIntoView({behavior:'smooth',block:'start'});
}
sidebarItems.forEach((item, idx) => { item.onclick = () => scrollToSection(idx); });

// Compact header + scroll spy
mainScroll.addEventListener('scroll', () => {
  document.querySelector('.main-head').classList.toggle('compact', mainScroll.scrollTop > 40);
  let activeIdx = 0;
  sectionBlocks.forEach((b, i) => {
    if (b.getBoundingClientRect().top < mainScroll.getBoundingClientRect().top + 120) activeIdx = i;
  });
  sidebarItems.forEach((item, i) => item.classList.toggle('active', i === activeIdx));
});
"""

SECTION_NAV_CSS = """
  .section-nav{display:flex;justify-content:space-between;align-items:center;padding:32px 0 16px;border-top:1px solid var(--border);margin-top:32px;font-family:var(--mono);font-size:11px;letter-spacing:1px;text-transform:uppercase}
  .section-nav a{color:var(--dim);text-decoration:none;border-bottom:1px dotted var(--border)}
  .section-nav a:hover{color:var(--accent);border-bottom-color:var(--accent)}"""

# ─── Find files ──────────────────────────────────────────────────────────────

def find_files():
    if SINGLE_FILE:
        return [SINGLE_FILE]
    result = subprocess.run(
        ['grep', '-rlE', 'const sections\\s*=\\s*\\[', '--include=*.dd.html', '.'],
        capture_output=True, text=True
    )
    files = [f.lstrip('./') for f in result.stdout.strip().split('\n') if f]
    # Exclude worktrees and .claude directories
    files = [f for f in files if '.claude/' not in f and 'claude/worktrees' not in f]
    return sorted(files)

# ─── Parse JS arrays ─────────────────────────────────────────────────────────

def extract_backtick_strings(text, var_name):
    """Extract array of backtick template literal strings from JS source."""
    # Find the array declaration
    pattern = rf'const {var_name}\s*=\s*\['
    m = re.search(pattern, text)
    if not m:
        return None

    # Find balanced brackets
    start = m.end() - 1  # position of [
    depth = 0
    i = start
    while i < len(text):
        if text[i] == '[':
            depth += 1
        elif text[i] == ']':
            depth -= 1
            if depth == 0:
                break
        i += 1

    array_body = text[start + 1:i]

    # Extract backtick strings
    strings = []
    in_backtick = False
    current = []
    j = 0
    while j < len(array_body):
        c = array_body[j]
        if c == '`' and not in_backtick:
            in_backtick = True
            current = []
        elif c == '`' and in_backtick:
            in_backtick = False
            strings.append(''.join(current))
        elif in_backtick:
            # Handle \` escape
            if c == '\\' and j + 1 < len(array_body) and array_body[j + 1] == '`':
                current.append('`')
                j += 1
            else:
                current.append(c)
        j += 1

    return strings if strings else None


def extract_sections(text):
    """Extract sections array objects [{num, short, title}, ...]."""
    pattern = r'const sections\s*=\s*\['
    m = re.search(pattern, text)
    if not m:
        return None

    # Find the closing ]
    start = m.end() - 1
    depth = 0
    i = start
    while i < len(text):
        if text[i] == '[': depth += 1
        elif text[i] == ']':
            depth -= 1
            if depth == 0: break
        i += 1

    array_body = text[start + 1:i]

    # Parse each object
    sections = []
    for obj_match in re.finditer(r'\{([^}]*)\}', array_body):
        obj_str = obj_match.group(1)
        num = re.search(r"num:\s*'([^']*)'", obj_str)
        short = re.search(r"short:\s*'([^']*)'", obj_str)
        title = re.search(r"title:\s*'((?:[^'\\]|\\.)*)'", obj_str)
        if not title:
            # Try backtick-delimited title
            # Find title: ` ... ` in the object
            title_bt = re.search(r'title:\s*`([^`]*)`', obj_str)
            title_val = title_bt.group(1) if title_bt else ''
        else:
            title_val = title.group(1).replace("\\'", "'")

        sections.append({
            'num': num.group(1) if num else '',
            'short': short.group(1) if short else '',
            'title': title_val,
        })

    return sections if sections else None


def extract_defined_num_svg(text):
    """Extract the defined_num_svg constant."""
    m = re.search(r'const defined_num_svg\s*=\s*`([^`]*)`', text)
    return m.group(1) if m else DETAIL_NUM_SVG


def extract_dd_config(text):
    """Extract DD_CONFIG object."""
    m = re.search(r'(?:window\.)?DD_CONFIG\s*=\s*\{', text)
    if not m:
        return None

    start = m.end() - 1
    depth = 0
    i = start
    while i < len(text):
        if text[i] == '{': depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0: break
        i += 1

    obj_str = text[start + 1:i]

    def extract_field(name):
        # Try single quotes
        p = re.search(rf"{name}:\s*'((?:[^'\\]|\\.)*)'", obj_str)
        if p: return p.group(1).replace("\\'", "'")
        # Try backtick
        p = re.search(rf'{name}:\s*`([^`]*)`', obj_str)
        if p: return p.group(1)
        return ''

    return {
        'logo': extract_field('logo'),
        'badge': extract_field('badge'),
        'heroTitle': extract_field('heroTitle'),
        'subtitle': extract_field('subtitle'),
    }


def extract_hero_from_shell(text):
    """Extract hero badge, title, subtitle, logo from inline shell template."""
    badge = ''
    hero_title = ''
    subtitle = ''
    logo = ''

    # Find all matches and prefer ones without ${...} interpolation
    for m in re.finditer(r'hero-badge[^>]*><span class="dot"></span>\s*(.*?)(?:</div>)', text):
        val = m.group(1).strip()
        if '${' not in val:
            badge = val
            break
    if not badge:
        for m in re.finditer(r'hero-badge[^>]*>(.*?)(?:</div>)', text):
            val = m.group(1).strip()
            val = re.sub(r'<span class="dot"></span>\s*', '', val)
            if '${' not in val:
                badge = val
                break

    for m in re.finditer(r'hero-title[^>]*>(.*?)</(?:div|h1)>', text, re.DOTALL):
        val = m.group(1).strip()
        if '${' not in val:
            hero_title = val
            break

    for m in re.finditer(r'masthead-sub[^>]*><span>(.*?)</span>', text, re.DOTALL):
        val = m.group(1).strip()
        if '${' not in val:
            subtitle = val
            break

    for m in re.finditer(r'sidebar-logo[^>]*>(.*?)</div>', text, re.DOTALL):
        val = m.group(1).strip()
        if '${' not in val:
            logo = val
            break

    return badge, hero_title, subtitle, logo


def extract_nav_links(text):
    """Extract prev/next navigation links."""
    nav_prev = ''
    nav_next = ''

    # Look for ← ... <a href="...">...</a>
    m = re.search(r'[←&larr;]\s*<a\s+href="([^"]*)"[^>]*>([^<]*)</a>', text)
    if m: nav_prev = f'<a href="{m.group(1)}">{m.group(2)}</a>'

    # Look for <a href="...">...</a> ... → or &rarr;
    m = re.search(r'<a\s+href="([^"]*)"[^>]*>([^<]*)</a>\s*[→&rarr;]', text)
    if m: nav_next = f'<a href="{m.group(1)}">{m.group(2)}</a>'

    return nav_prev, nav_next

# ─── Extract all data ─────────────────────────────────────────────────────────

def extract_data(html):
    """Extract all data needed for conversion."""
    # Get all inline script content
    script_blocks = []
    for m in re.finditer(r'<script(?:\s[^>]*)?>(?!<)([\s\S]*?)</script>', html):
        tag = html[m.start():m.start() + m.group(0).index('>') + 1]
        if ' src=' in tag:
            continue
        script_blocks.append(m.group(1))

    all_script = '\n'.join(script_blocks)

    if not re.search(r'const sections\s*=\s*\[', all_script):
        return None

    uses_shared_js = 'dd-shared.js' in html
    has_details = 'const details = [' in all_script or 'const details=[' in all_script

    # Extract arrays
    sections = extract_sections(all_script)
    if not sections:
        return None

    summaries = extract_backtick_strings(all_script, 'summaries')
    details = extract_backtick_strings(all_script, 'details') if has_details else None

    # Resolve ${defined_num_svg} in details
    num_svg = extract_defined_num_svg(all_script)
    if details:
        details = [d.replace('${defined_num_svg}', num_svg) for d in details]

    # Extract hero content
    cfg = extract_dd_config(all_script)
    if cfg:
        badge = cfg['badge']
        hero_title = cfg['heroTitle']
        subtitle = cfg['subtitle']
        logo = cfg['logo']
    else:
        badge, hero_title, subtitle, logo = extract_hero_from_shell(all_script)

    # Extract nav links
    nav_prev, nav_next = extract_nav_links(all_script)

    # Extract <head> content
    head_match = re.search(r'<head>([\s\S]*?)</head>', html)
    head_content = head_match.group(1) if head_match else ''

    return {
        'sections': sections,
        'summaries': summaries,
        'details': details,
        'head_content': head_content,
        'badge': badge,
        'hero_title': hero_title,
        'subtitle': subtitle,
        'logo': logo,
        'nav_prev': nav_prev,
        'nav_next': nav_next,
        'uses_shared_js': uses_shared_js,
    }

# ─── Build HTML ───────────────────────────────────────────────────────────────

def build_html(data):
    has_details = data['details'] and len(data['details']) > 0

    # Sidebar items
    sidebar_items = '\n'.join(
        f'      <div class="sidebar-item{" active" if i == 0 else ""}" data-section="{i}" data-label="{s["short"]}"><span class="sidebar-num">{s["num"]}</span><span class="sidebar-label">{s["short"]}</span></div>'
        for i, s in enumerate(data['sections'])
    )

    # Section blocks
    section_blocks = []
    for i, sec in enumerate(data['sections']):
        detail_btn = f'<button class="s-detail-btn">{DETAIL_BTN_SVG}</button>' if has_details else ''
        summary = data['summaries'][i] if data['summaries'] and i < len(data['summaries']) else ''
        section_blocks.append(f'''
        <div class="section-block" data-section="{i}">
          <div class="s-num"><span>{sec['num']}</span>{detail_btn}</div>
          <h2>{sec['title']}</h2>
          {summary}
        </div>''')
    section_blocks_html = '\n'.join(section_blocks)

    # Detail panels
    detail_panels_html = ''
    if has_details:
        panels = []
        for i, sec in enumerate(data['sections']):
            detail = data['details'][i] if i < len(data['details']) else ''
            panels.append(f'''
      <div class="detail" id="detail-{i}">
        {detail}
      </div>''')
        detail_panels_html = '\n'.join(panels)

    # Nav
    nav_html = ''
    if data['nav_prev'] or data['nav_next']:
        prev_span = f'&larr; {data["nav_prev"]}' if data['nav_prev'] else ''
        next_span = f'{data["nav_next"]} &rarr;' if data['nav_next'] else ''
        nav_html = f'''
        <div class="section-nav">
          <span>{prev_span}</span>
          <span>{next_span}</span>
        </div>'''

    # Right panel
    right_panel = ''
    if has_details:
        right_panel = f'''
  <div class="right closed" id="right">
    <div class="right-topbar"><span class="sticky-title" id="right-sticky-title"></span></div>
    <div class="right-inner" id="right-inner">
{detail_panels_html}
    </div>
  </div>'''

    # Detail toggle button
    detail_btn_ctrl = ''
    if has_details:
        detail_btn_ctrl = f'''
    <button class="ctrl-btn detail-btn" id="detail-btn">
      <span class="icon-open">{CTRL_OPEN_SVG}</span>
      <span class="icon-close">{CTRL_CLOSE_SVG}</span>
    </button>'''

    sidebar_tooltip = '\n<div class="sidebar-tooltip" id="sidebar-tooltip"></div>' if has_details else ''

    # Add section-nav CSS if needed
    head_content = data['head_content']
    if (data['nav_prev'] or data['nav_next']) and not data['uses_shared_js'] and '</style>' in head_content:
        head_content = head_content.replace('</style>', SECTION_NAV_CSS + '\n  </style>')

    # Remove dd-shared.css/js link refs (CSS stays, JS ref removed — actually keep CSS link)
    # We don't need to remove the CSS link, just ensure we don't duplicate it

    interaction_js = INTERACTION_JS_WITH_DETAILS if has_details else INTERACTION_JS_NO_DETAILS

    return f'''<!DOCTYPE html>
<html lang="en">
<head>{head_content}</head>
<body data-theme="light">

<div class="shell">

  <div class="ctrl-group" id="ctrl-group">
    <button class="ctrl-btn theme-btn" id="theme-btn"></button>{detail_btn_ctrl}
  </div>

  <nav class="sidebar" id="sidebar">
    <div class="sidebar-head">
      <div class="sidebar-logo">{data['logo']}</div>
    </div>
    <div class="sidebar-nav" id="sidebar-nav">
{sidebar_items}
    </div>
  </nav>

  <div class="main" id="main">
    <div class="main-head">
      <div class="main-head-inner">
        <div class="hero-badge"><span class="dot"></span> {data['badge']}</div>
        <div class="hero-title">{data['hero_title']}</div>
        <div class="masthead-rule"></div>
        <div class="masthead-sub"><span>{data['subtitle']}</span></div>
      </div>
    </div>
    <div class="main-scroll" id="main-scroll">
      <div class="main-scroll-inner">
{section_blocks_html}
{nav_html}
      </div>
    </div>
  </div>
{right_panel}
</div>
{sidebar_tooltip}
<script>
{interaction_js}
</script>
</body>
</html>
'''

# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    files = find_files()
    print(f"Found {len(files)} files to convert{' (dry run)' if DRY_RUN else ''}")

    converted = 0
    skipped = 0
    failed = 0

    for f in files:
        try:
            html = open(f, 'r', encoding='utf-8').read()
            data = extract_data(html)

            if not data:
                print(f"  SKIP {f} (could not extract data)")
                skipped += 1
                continue

            if not data['sections']:
                print(f"  SKIP {f} (no sections)")
                skipped += 1
                continue

            new_html = build_html(data)

            det_str = f'with {len(data["details"])} details' if data['details'] else 'no details'

            if DRY_RUN:
                print(f"  OK   {f} ({len(data['sections'])} sections, {det_str})")
            else:
                with open(f, 'w', encoding='utf-8') as fh:
                    fh.write(new_html)
                print(f"  DONE {f} ({len(data['sections'])} sections)")
            converted += 1
        except Exception as e:
            print(f"  FAIL {f}: {e}")
            failed += 1

    print(f"\nResults: {converted} converted, {skipped} skipped, {failed} failed")
