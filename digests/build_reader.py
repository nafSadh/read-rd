#!/usr/bin/env python3
"""Generates a standalone offline HTML reader from markdown digest files."""

import json
import os
import glob
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent
FOLDERS = ["2026-02", "2026-03"]
OUT = ROOT / "index.html"

# ── Collect files ──────────────────────────────────────────────────────────────
entries = {}  # date_str -> markdown content

for folder in FOLDERS:
    for md_path in sorted((ROOT / folder).glob("*.md")):
        date_str = md_path.stem  # e.g. "2026-03-22"
        entries[date_str] = md_path.read_text(encoding="utf-8")

sorted_dates = sorted(entries.keys())
most_recent = sorted_dates[-1] if sorted_dates else ""

# Group by month  (e.g. "2026-03")
months = defaultdict(list)
for d in sorted_dates:
    month = d[:7]
    months[month].append(d)

# Month display names
MONTH_NAMES = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December",
}

def month_label(m):  # "2026-03" -> "March 2026"
    y, mo = m.split("-")
    return f"{MONTH_NAMES[mo]} {y}"

def day_label(d):  # "2026-03-22" -> "Mar 22"
    parts = d.split("-")
    mo = MONTH_NAMES[parts[1]][:3]
    return f"{mo} {int(parts[2])}"

# ── Build sidebar HTML ─────────────────────────────────────────────────────────
sidebar_items = []
for month in sorted(months.keys(), reverse=True):
    dates = sorted(months[month], reverse=True)
    is_current = most_recent[:7] == month
    open_attr = " open" if is_current else ""
    items_html = "\n".join(
        f'          <li><a href="#" class="date-link" data-date="{d}">{day_label(d)}</a></li>'
        for d in dates
    )
    sidebar_items.append(f"""      <details{open_attr} class="month-group">
        <summary>{month_label(month)}</summary>
        <ul>
{items_html}
        </ul>
      </details>""")

sidebar_html = "\n".join(sidebar_items)

# ── Embed content as JS ────────────────────────────────────────────────────────
entries_json = json.dumps(entries, ensure_ascii=False)
most_recent_json = json.dumps(most_recent)

# ── marked.js inline fallback (minimal renderer if CDN fails) ─────────────────
# We'll use a CDN link with an inline minimal fallback loaded via onerror.
# The inline fallback is a simple but functional markdown-to-HTML converter.

MINIMAL_MARKED = r"""
// Minimal markdown renderer (fallback if CDN unavailable)
window.marked = window.marked || {
  parse: function(src) {
    var out = src
      // fenced code blocks
      .replace(/```(\w*)\n([\s\S]*?)```/g, function(_, lang, code) {
        return '<pre><code class="language-' + lang + '">' +
          code.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;') + '</code></pre>';
      })
      // inline code
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      // headings
      .replace(/^(#{1,6})\s+(.+)$/gm, function(_, hashes, text) {
        var level = hashes.length;
        return '<h' + level + '>' + text + '</h' + level + '>';
      })
      // horizontal rule
      .replace(/^---+$/gm, '<hr>')
      // bold
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      // italic
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      // blockquote
      .replace(/^>\s+(.+)$/gm, '<blockquote>$1</blockquote>')
      // links
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
      // unordered list items (wrap later)
      .replace(/^[\*\-]\s+(.+)$/gm, '<li>$1</li>')
      // ordered list items
      .replace(/^\d+\.\s+(.+)$/gm, '<li>$1</li>')
      // wrap consecutive <li> in <ul>
      .replace(/(<li>[\s\S]+?<\/li>)(\n(?!<li>)|$)/g, function(m) {
        return '<ul>' + m + '</ul>';
      })
      // paragraphs: blank-line-separated non-tag blocks
      .replace(/\n\n(?!<)(.+?)(?=\n\n|$)/gs, function(_, p) {
        p = p.trim();
        if (p && !p.startsWith('<')) return '\n\n<p>' + p + '</p>';
        return '\n\n' + p;
      });
    return out;
  }
};
"""

# ── Full HTML ──────────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Research Digest</title>
  <style>
    /* ── Reset & base ──────────────────────────────────────────────── */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    :root {{
      --bg:        #0f1117;
      --bg2:       #181c24;
      --bg3:       #1e2330;
      --border:    #2a2f3e;
      --accent:    #4f8ef7;
      --accent2:   #7ab3ff;
      --text:      #dde2f0;
      --text-muted:#7a8299;
      --sidebar-w: 220px;
      --header-h:  52px;
    }}

    html, body {{
      height: 100%;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                   "Helvetica Neue", Arial, sans-serif;
      font-size: 16px;
      line-height: 1.6;
    }}

    /* ── Layout ────────────────────────────────────────────────────── */
    .app {{
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }}

    /* ── Header ────────────────────────────────────────────────────── */
    header {{
      height: var(--header-h);
      background: var(--bg2);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      padding: 0 16px;
      gap: 12px;
      flex-shrink: 0;
      z-index: 10;
    }}

    .hamburger {{
      display: none;
      background: none;
      border: none;
      cursor: pointer;
      padding: 6px;
      border-radius: 6px;
      color: var(--text-muted);
      transition: color .2s, background .2s;
    }}
    .hamburger:hover {{ color: var(--text); background: var(--bg3); }}
    .hamburger svg {{ display: block; }}

    header h1 {{
      font-size: 1rem;
      font-weight: 600;
      color: var(--text);
      letter-spacing: .02em;
    }}
    header h1 span {{ color: var(--accent); }}

    /* ── Body (sidebar + content) ──────────────────────────────────── */
    .body {{
      display: flex;
      flex: 1;
      overflow: hidden;
    }}

    /* ── Sidebar ───────────────────────────────────────────────────── */
    .sidebar {{
      width: var(--sidebar-w);
      background: var(--bg2);
      border-right: 1px solid var(--border);
      overflow-y: auto;
      flex-shrink: 0;
      padding: 12px 0;
      transition: transform .25s ease, width .25s ease;
    }}
    .sidebar::-webkit-scrollbar {{ width: 4px; }}
    .sidebar::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 4px; }}

    .month-group {{
      margin: 0;
    }}
    .month-group summary {{
      cursor: pointer;
      padding: 7px 16px;
      font-size: .78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .08em;
      color: var(--text-muted);
      user-select: none;
      list-style: none;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: color .15s;
    }}
    .month-group summary::-webkit-details-marker {{ display: none; }}
    .month-group summary::before {{
      content: "▶";
      font-size: .6rem;
      transition: transform .2s;
      display: inline-block;
    }}
    .month-group[open] summary::before {{ transform: rotate(90deg); }}
    .month-group summary:hover {{ color: var(--text); }}

    .month-group ul {{
      list-style: none;
      padding: 2px 0 6px;
    }}
    .date-link {{
      display: block;
      padding: 5px 16px 5px 28px;
      font-size: .875rem;
      color: var(--text-muted);
      text-decoration: none;
      transition: color .15s, background .15s;
      border-left: 2px solid transparent;
    }}
    .date-link:hover {{
      color: var(--text);
      background: var(--bg3);
    }}
    .date-link.active {{
      color: var(--accent2);
      border-left-color: var(--accent);
      background: rgba(79,142,247,.08);
    }}

    /* ── Main content ──────────────────────────────────────────────── */
    main {{
      flex: 1;
      overflow-y: auto;
      padding: 0;
    }}
    main::-webkit-scrollbar {{ width: 6px; }}
    main::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 4px; }}

    .content-wrap {{
      max-width: 780px;
      margin: 0 auto;
      padding: 36px 28px 80px;
    }}

    /* ── Markdown typography ───────────────────────────────────────── */
    .md h1 {{
      font-size: 1.75rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 6px;
      line-height: 1.3;
    }}
    .md h2 {{
      font-size: 1.2rem;
      font-weight: 600;
      color: var(--text);
      margin: 2em 0 .6em;
      padding-bottom: .3em;
      border-bottom: 1px solid var(--border);
    }}
    .md h3 {{
      font-size: 1rem;
      font-weight: 600;
      color: var(--accent2);
      margin: 1.4em 0 .4em;
    }}
    .md h4, .md h5, .md h6 {{
      font-size: .95rem;
      font-weight: 600;
      margin: 1.2em 0 .4em;
    }}
    .md p {{ margin: .75em 0; color: var(--text); }}
    .md a {{
      color: var(--accent);
      text-decoration: none;
    }}
    .md a:hover {{ text-decoration: underline; color: var(--accent2); }}
    .md blockquote {{
      margin: 1em 0;
      padding: 10px 16px;
      border-left: 3px solid var(--accent);
      background: var(--bg3);
      border-radius: 0 6px 6px 0;
      color: var(--text-muted);
      font-style: italic;
    }}
    .md hr {{
      border: none;
      border-top: 1px solid var(--border);
      margin: 1.5em 0;
    }}
    .md strong {{ color: var(--text); font-weight: 600; }}
    .md em {{ color: #b0bcd8; }}
    .md code {{
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 1px 5px;
      font-size: .88em;
      font-family: "SF Mono", "Fira Code", Consolas, monospace;
      color: #e0a0ff;
    }}
    .md pre {{
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      overflow-x: auto;
      margin: 1em 0;
    }}
    .md pre code {{
      background: none;
      border: none;
      padding: 0;
      font-size: .85em;
      color: #c8d3f0;
    }}
    .md ul, .md ol {{ padding-left: 1.4em; margin: .6em 0; }}
    .md li {{ margin: .25em 0; }}
    .md table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
    .md th, .md td {{
      border: 1px solid var(--border);
      padding: 8px 12px;
      text-align: left;
    }}
    .md th {{ background: var(--bg3); font-weight: 600; }}
    .md tr:nth-child(even) {{ background: rgba(255,255,255,.02); }}

    /* ── Overlay for mobile ────────────────────────────────────────── */
    .overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,.55);
      z-index: 8;
    }}

    /* ── Responsive ────────────────────────────────────────────────── */
    @media (max-width: 640px) {{
      .hamburger {{ display: flex; }}
      .sidebar {{
        position: fixed;
        top: var(--header-h);
        left: 0;
        bottom: 0;
        z-index: 9;
        transform: translateX(-100%);
        width: 240px;
        padding-top: 8px;
        box-shadow: 4px 0 20px rgba(0,0,0,.4);
      }}
      .sidebar.open {{
        transform: translateX(0);
      }}
      .overlay.visible {{ display: block; }}
      .content-wrap {{ padding: 24px 16px 60px; }}
    }}
  </style>
</head>
<body>
<div class="app">
  <header>
    <button class="hamburger" id="menuBtn" aria-label="Toggle sidebar">
      <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor"
           stroke-width="1.8" stroke-linecap="round">
        <line x1="2" y1="5" x2="18" y2="5"/>
        <line x1="2" y1="10" x2="18" y2="10"/>
        <line x1="2" y1="15" x2="18" y2="15"/>
      </svg>
    </button>
    <h1>AI Research <span>Digest</span></h1>
  </header>

  <div class="body">
    <nav class="sidebar" id="sidebar">
{sidebar_html}
    </nav>

    <div class="overlay" id="overlay"></div>

    <main id="main">
      <div class="content-wrap">
        <div class="md" id="content">
          <p style="color:var(--text-muted)">Select a date to read.</p>
        </div>
      </div>
    </main>
  </div>
</div>

<!-- marked.js from CDN; inline fallback below kicks in if offline -->
<script>
{MINIMAL_MARKED}
</script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"
        onload="window._markedLoaded=true"></script>

<script>
(function () {{
  // ── Data ──────────────────────────────────────────────────────────
  var ENTRIES = {entries_json};
  var MOST_RECENT = {most_recent_json};

  // ── DOM refs ──────────────────────────────────────────────────────
  var contentEl = document.getElementById('content');
  var sidebar   = document.getElementById('sidebar');
  var overlay   = document.getElementById('overlay');
  var menuBtn   = document.getElementById('menuBtn');

  // ── Render ────────────────────────────────────────────────────────
  function render(date) {{
    var md = ENTRIES[date];
    if (!md) {{ contentEl.innerHTML = '<p>No content for ' + date + '</p>'; return; }}

    // marked may be loaded async from CDN; use whichever is available
    var parser = (window.marked && window.marked.parse)
      ? function(s) {{ return window.marked.parse(s); }}
      : function(s) {{ return window.marked.parse(s); }};

    contentEl.innerHTML = parser(md);

    // Open links in new tab
    contentEl.querySelectorAll('a').forEach(function(a) {{
      a.setAttribute('target', '_blank');
      a.setAttribute('rel', 'noopener noreferrer');
    }});

    // Highlight active link
    document.querySelectorAll('.date-link').forEach(function(el) {{
      el.classList.toggle('active', el.dataset.date === date);
    }});

    document.getElementById('main').scrollTop = 0;
  }}

  // ── Nav clicks ───────────────────────────────────────────────────
  document.querySelectorAll('.date-link').forEach(function(el) {{
    el.addEventListener('click', function(e) {{
      e.preventDefault();
      render(this.dataset.date);
      closeSidebar();
    }});
  }});

  // ── Sidebar toggle (mobile) ───────────────────────────────────────
  function closeSidebar() {{
    sidebar.classList.remove('open');
    overlay.classList.remove('visible');
  }}
  menuBtn.addEventListener('click', function() {{
    var open = sidebar.classList.toggle('open');
    overlay.classList.toggle('visible', open);
  }});
  overlay.addEventListener('click', closeSidebar);

  // ── Initial load ──────────────────────────────────────────────────
  if (MOST_RECENT) render(MOST_RECENT);
}})();
</script>
</body>
</html>
"""

OUT.write_text(HTML, encoding="utf-8")
print(f"Written: {OUT}")
print(f"  Dates embedded: {len(entries)}")
print(f"  Default date:   {most_recent}")
print(f"  File size:      {OUT.stat().st_size:,} bytes")
