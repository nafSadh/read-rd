/**
 * Nano Banana — AI Image Placeholder System
 *
 * Usage: Define NB_IMAGES array before loading this script.
 * Each entry: { target, type, prompt, file? }
 *   target: 'hero' | 'detail-hero' | CSS selector
 *   type:   'hero' | 'section' | 'square' | 'wide'
 *   prompt: Nano Banana prompt string
 *   file:   optional path to local image (relative to page), e.g. 'img/hero.png'
 *
 * If `file` is set, the image auto-loads. If loading fails, falls back to placeholder.
 */

(function nanoBananaInit() {
  // Inject CSS if not already present
  if (!document.getElementById('nb-css')) {
    const depth = (window.NB_CSS_PATH || findCssPath());
    const link = document.createElement('link');
    link.id = 'nb-css';
    link.rel = 'stylesheet';
    link.href = depth;
    document.head.appendChild(link);
  }

  function findCssPath() {
    const scripts = document.querySelectorAll('script[src*="nano-banana"]');
    if (scripts.length) {
      const src = scripts[scripts.length - 1].getAttribute('src');
      return src.replace('nano-banana.js', 'nano-banana.css');
    }
    return '/nano-banana.css';
  }

  function createPlaceholder(cfg) {
    const el = document.createElement('div');
    el.className = `nb-img nb-${cfg.type || 'section'}`;
    const copyBtn = document.createElement('button');
    copyBtn.className = 'nb-prompt-copy';
    copyBtn.textContent = 'copy prompt';
    copyBtn.onclick = (e) => {
      e.stopPropagation();
      navigator.clipboard.writeText(cfg.prompt).then(() => {
        copyBtn.textContent = 'copied';
        copyBtn.classList.add('copied');
        setTimeout(() => { copyBtn.textContent = 'copy prompt'; copyBtn.classList.remove('copied'); }, 1500);
      });
    };
    el.appendChild(copyBtn);
    el.dataset.prompt = cfg.prompt;

    // Try loading local image
    const src = cfg.src || cfg.file;
    if (src) {
      const img = new Image();
      img.onload = () => {
        el.style.backgroundImage = `url(${src})`;
        el.classList.add('nb-loaded');
      };
      // On error, stays as placeholder — no action needed
      img.src = src;
    }

    return el;
  }

  function inject() {
    if (typeof NB_IMAGES === 'undefined' || !NB_IMAGES.length) return;

    NB_IMAGES.forEach(cfg => {
      const el = createPlaceholder(cfg);

      if (cfg.target === 'hero') {
        const scrollInner = document.querySelector('.main-scroll-inner') ||
                            document.querySelector('.main-scroll');
        if (scrollInner) {
          scrollInner.insertBefore(el, scrollInner.firstChild);
        }
      } else if (cfg.target === 'detail-hero') {
        if (!window._nbDetailImages) window._nbDetailImages = [];
        window._nbDetailImages.push(cfg);
      } else {
        const target = document.querySelector(cfg.target);
        if (target) {
          if (cfg.position === 'before') {
            target.parentNode.insertBefore(el, target);
          } else if (cfg.position === 'prepend') {
            target.insertBefore(el, target.firstChild);
          } else {
            target.appendChild(el);
          }
        }
      }
    });
  }

  // Hook into detail panel opens to inject section images
  const origOpen = window.openDetail;
  if (origOpen) {
    window.openDetail = function(idx) {
      origOpen(idx);
      if (window._nbDetailImages) {
        setTimeout(() => {
          const inner = document.getElementById('right-inner');
          if (!inner) return;
          window._nbDetailImages.forEach(cfg => {
            if (cfg.sectionIdx === idx && !inner.querySelector('.nb-img')) {
              const detailHeader = inner.querySelector('.detail-header');
              if (detailHeader) {
                const el = createPlaceholder(cfg);
                detailHeader.parentNode.insertBefore(el, detailHeader.nextSibling);
              }
            }
          });
        }, 100);
      }
    };
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => setTimeout(inject, 200));
  } else {
    setTimeout(inject, 200);
  }
})();
