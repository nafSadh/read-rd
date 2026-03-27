#!/usr/bin/env python3
"""Embed audio players into .dd.html files that have corresponding .mp3 files.

Injects a single <script> block before </body> that creates all audio elements
via DOM manipulation — never touches template literals or <style> tags.
"""

import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


EMBED_BLOCK = """<script>
(function(){{
  var MP3 = '{mp3_filename}';

  // 1. Inject CSS
  var css = document.createElement('style');
  css.textContent = `
    .audio-bar{{display:flex;align-items:center;gap:10px;padding:10px 0 4px;margin-top:6px;max-height:50px;overflow:hidden;transition:max-height .35s ease,padding .35s ease,opacity .25s ease}}
    .main-head.compact .audio-bar{{max-height:0;padding:0;opacity:0;margin:0;pointer-events:none}}
    .audio-bar audio{{height:32px;flex:1;min-width:0;border-radius:0;filter:contrast(.9)}}
    [data-theme="dark"] .audio-bar audio{{filter:invert(1) contrast(.85) hue-rotate(180deg)}}
    .ctrl-btn.audio-ctrl{{display:none;position:relative}}
    .ctrl-btn.audio-ctrl.playing{{color:var(--accent)}}
    .ctrl-btn.audio-ctrl.playing::after{{content:'';position:absolute;bottom:4px;left:50%;transform:translateX(-50%);width:4px;height:4px;background:var(--accent);border-radius:50%;animation:pulse 2s infinite}}
    .audio-bottom{{position:fixed;bottom:0;left:0;right:0;z-index:500;display:flex;align-items:center;gap:12px;padding:6px 24px;background:color-mix(in srgb,var(--bg2) 85%,transparent);border-top:1px solid var(--border);backdrop-filter:blur(16px) saturate(1.4);-webkit-backdrop-filter:blur(16px) saturate(1.4);box-shadow:0 -2px 12px #00000010;transform:translateY(100%);transition:transform .3s cubic-bezier(.4,0,.2,1);pointer-events:none}}
    .audio-bottom.visible{{transform:translateY(0);pointer-events:auto}}
    .audio-bottom audio{{height:32px;flex:1;min-width:0;border-radius:0;filter:contrast(.9)}}
    .audio-bottom .audio-dismiss{{cursor:pointer;color:var(--dim);font-size:13px;padding:4px 8px;border:none;background:none;font-family:var(--sans);letter-spacing:.5px;transition:color .2s}}
    .audio-bottom .audio-dismiss:hover{{color:var(--accent)}}
    [data-theme="dark"] .audio-bottom audio{{filter:invert(1) contrast(.85) hue-rotate(180deg)}}
  `;
  document.head.appendChild(css);

  // 2. Inline audio bar — insert after masthead-sub
  var bar = document.createElement('div');
  bar.className = 'audio-bar';
  bar.innerHTML = '<audio id="audio-main" controls preload="none" src="'+MP3+'"></audio>';
  var sub = document.querySelector('.masthead-sub');
  if(!sub) sub = document.querySelector('.masthead-rule');
  if(sub) sub.parentNode.insertBefore(bar, sub.nextSibling);

  // 3. Mini button in ctrl-group
  var miniBtn = document.createElement('button');
  miniBtn.className = 'ctrl-btn audio-ctrl';
  miniBtn.title = 'Play audio';
  miniBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>';
  var ctrlGroup = document.getElementById('ctrl-group');
  if(ctrlGroup) ctrlGroup.insertBefore(miniBtn, ctrlGroup.firstChild);

  // 4. Sticky bottom bar
  var bottomBar = document.createElement('div');
  bottomBar.className = 'audio-bottom';
  bottomBar.innerHTML = '<audio id="audio-bottom-el" controls preload="none" src="'+MP3+'"></audio><button class="audio-dismiss" id="audio-bottom-dismiss">\\u2715</button>';
  document.body.appendChild(bottomBar);

  var mainAudio = document.getElementById('audio-main');
  var bottomAudio = document.getElementById('audio-bottom-el');
  var bottomDismiss = document.getElementById('audio-bottom-dismiss');
  if(!mainAudio||!bottomAudio) return;

  var isCompact = false, dismissed = false;
  var head = document.querySelector('.main-head');

  if(head){{
    new MutationObserver(function(){{
      isCompact = head.classList.contains('compact');
      miniBtn.style.display = isCompact ? 'flex' : 'none';
      if(isCompact && !bottomAudio.paused && !dismissed) bottomBar.classList.add('visible');
      if(!isCompact){{
        if(!bottomAudio.paused){{
          mainAudio.currentTime = bottomAudio.currentTime;
          bottomAudio.pause();
          mainAudio.play();
        }}
        bottomBar.classList.remove('visible');
      }}
    }}).observe(head, {{attributes:true, attributeFilter:['class']}});
  }}

  mainAudio.addEventListener('play', function(){{
    miniBtn.classList.add('playing'); dismissed = false;
    if(isCompact){{
      bottomAudio.currentTime = mainAudio.currentTime;
      mainAudio.pause(); bottomAudio.play();
      bottomBar.classList.add('visible');
    }}
  }});
  mainAudio.addEventListener('pause', function(){{ miniBtn.classList.remove('playing'); }});
  mainAudio.addEventListener('ended', function(){{ miniBtn.classList.remove('playing'); }});

  bottomAudio.addEventListener('play', function(){{ miniBtn.classList.add('playing'); }});
  bottomAudio.addEventListener('pause', function(){{ miniBtn.classList.remove('playing'); }});
  bottomAudio.addEventListener('ended', function(){{ miniBtn.classList.remove('playing'); bottomBar.classList.remove('visible'); }});

  miniBtn.addEventListener('click', function(){{
    dismissed = false;
    if(bottomAudio.paused && mainAudio.paused){{ bottomAudio.play(); bottomBar.classList.add('visible'); }}
    else if(!bottomAudio.paused) bottomAudio.pause();
    else if(!mainAudio.paused) mainAudio.pause();
  }});

  bottomDismiss.addEventListener('click', function(){{
    bottomAudio.pause(); bottomBar.classList.remove('visible'); dismissed = true;
  }});
}})();
</script>"""


def mp3_filename_for(html_path: Path) -> str:
    stem = html_path.stem
    for suffix in ['.dd', '.slides', '.guide']:
        if stem.endswith(suffix):
            stem = stem[:-len(suffix)]
            break
    return f"{stem}.mp3"


def embed_audio_in_file(html_path: Path, dry_run: bool = False) -> bool:
    mp3_name = mp3_filename_for(html_path)
    mp3_path = html_path.parent / mp3_name

    if not mp3_path.exists():
        return False

    src = html_path.read_text(encoding='utf-8')

    if 'audio-main' in src:
        print(f"  Already embedded: {html_path.name}")
        return True

    if '</body>' not in src:
        print(f"  No </body> found: {html_path.name}")
        return False

    if dry_run:
        print(f"  [DRY RUN] {html_path.name} <- {mp3_name}")
        return True

    block = EMBED_BLOCK.format(mp3_filename=mp3_name)
    new_src = src.replace('</body>', block + '\n</body>', 1)
    html_path.write_text(new_src, encoding='utf-8')
    print(f"  {html_path.name} <- {mp3_name}")
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Embed audio players into .dd.html files')
    parser.add_argument('path', nargs='?', default=None, help='Filter by path prefix')
    parser.add_argument('--dry-run', action='store_true', help='Preview without modifying')
    args = parser.parse_args()

    root = Path(__file__).parent
    patterns = ['**/*.dd.html', '**/*.slides.html', '**/*.guide.html']
    files = []
    for pat in patterns:
        files.extend(root.glob(pat))
    skip = ['.project', 'node_modules', 'courses', 'digests', 'hiking', '.claude']
    files = [f for f in files if not any(s in str(f).replace('\\', '/') for s in skip)]
    if args.path:
        files = [f for f in files
                 if str(f.relative_to(root)).replace('\\', '/').startswith(args.path.replace('\\', '/'))]
    files.sort()

    embedded = skipped = 0
    for f in files:
        if embed_audio_in_file(f, dry_run=args.dry_run):
            embedded += 1
        else:
            skipped += 1

    print(f"\nEmbedded: {embedded}, Skipped (no MP3): {skipped}")


if __name__ == '__main__':
    main()
