// Deep-dive shared scaffold
// Expects: DD_CONFIG = { badge, heroTitle, subtitle }, sections[], summaries[], details[]

function initDeepDive() {
  const cfg = (typeof DD_CONFIG !== 'undefined' ? DD_CONFIG : null) || { badge: 'Attachment Theory', heroTitle: 'Deep <em>Dive</em>', subtitle: '' };

  const shell = document.createElement('div');
  shell.className = 'shell';
  shell.innerHTML = `
    <div class="ctrl-group" id="ctrl-group">
      <button class="ctrl-btn theme-btn" onclick="toggleTheme()"></button>
      <button class="ctrl-btn detail-btn" id="detail-btn" onclick="toggleDetail()">
        <span class="icon-open"><svg width="16" height="16" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg></span>
        <span class="icon-close"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><line x1="6.5" y1="4" x2="13" y2="4"/><line x1="3" y1="8" x2="13" y2="8"/><line x1="6.5" y1="12" x2="13" y2="12"/></svg></span>
      </button>
    </div>
    <nav class="sidebar" id="sidebar">
      <div class="sidebar-head"><div class="sidebar-logo">A<em>t</em></div></div>
      <div class="sidebar-nav" id="sidebar-nav"></div>
    </nav>
    <div class="main" id="main">
      <div class="main-head">
        <div class="main-head-inner">
          <div class="hero-badge"><span class="dot"></span> ${cfg.badge}</div>
          <div class="hero-title">${cfg.heroTitle}</div>
          <div class="masthead-rule"></div>
          <div class="masthead-sub"><span>${cfg.subtitle}</span></div>
        </div>
      </div>
      <div class="main-scroll" id="main-scroll"></div>
    </div>
    <div class="right closed" id="right">
      <div class="right-topbar"><span class="sticky-title" id="right-sticky-title"></span></div>
      <div class="right-inner" id="right-inner"></div>
    </div>
  `;
  document.body.appendChild(shell);

  const sidebarNav = document.getElementById('sidebar-nav');
  sections.forEach((sec, idx) => {
    const item = document.createElement('div');
    item.className = 'sidebar-item' + (idx === 0 ? ' active' : '');
    item.setAttribute('data-label', sec.short);
    item.innerHTML = `<span class="sidebar-num">${sec.num}</span><span class="sidebar-label">${sec.short}</span>`;
    item.onclick = () => scrollToSection(idx);
    sidebarNav.appendChild(item);
  });

  const sidebarTip = document.createElement('div');
  sidebarTip.className = 'sidebar-tooltip';
  document.body.appendChild(sidebarTip);
  const sidebarEl = document.querySelector('.sidebar');
  let tipActive = false;
  sidebarNav.addEventListener('mouseleave', () => { tipActive = false; sidebarTip.classList.remove('visible'); });
  sidebarNav.addEventListener('mousemove', (e) => {
    if (!document.body.classList.contains('detail-open')) { if (tipActive) { tipActive = false; sidebarTip.classList.remove('visible'); } return; }
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

  const mainScroll = document.getElementById('main-scroll');
  const mainInner = document.createElement('div');
  mainInner.className = 'main-scroll-inner';
  mainScroll.appendChild(mainInner);
  sections.forEach((sec, idx) => {
    const block = document.createElement('div');
    block.className = 'section-block';
    block.innerHTML = `<div class="s-num"><span>${sec.num}</span><button class="s-detail-btn" onclick="openDetail(${idx})"><svg width="14" height="14" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg></button></div><h2>${sec.title}</h2>${summaries[idx]}`;
    mainInner.appendChild(block);
  });

  const rightInner = document.getElementById('right-inner');
  sections.forEach((sec, idx) => {
    const detailDiv = document.createElement('div');
    detailDiv.className = 'detail';
    detailDiv.id = `detail-${idx}`;
    detailDiv.innerHTML = details[idx];
    rightInner.appendChild(detailDiv);
  });

  mainScroll.addEventListener('scroll', () => {
    document.querySelector('.main-head').classList.toggle('compact', mainScroll.scrollTop > 40);
    const blocks = mainScroll.querySelectorAll('.section-block');
    const items = document.querySelectorAll('.sidebar-item');
    let activeIdx = 0;
    blocks.forEach((b, i) => { if (b.getBoundingClientRect().top < mainScroll.getBoundingClientRect().top + 120) activeIdx = i; });
    items.forEach((item, i) => item.classList.toggle('active', i === activeIdx));
  });

  const rightPanelOuter = document.getElementById('right');
  const stickyTitle = document.getElementById('right-sticky-title');
  rightPanelOuter.addEventListener('scroll', () => {
    const activeDetail = rightPanelOuter.querySelector('.detail[style*="display: block"], .detail[style*="display:block"]');
    if (!activeDetail) return;
    const h2 = activeDetail.querySelector('.detail-header h2') || activeDetail.querySelector('h2');
    if (!h2) return;
    const rect = h2.getBoundingClientRect();
    const panelRect = rightPanelOuter.getBoundingClientRect();
    const topbar = document.querySelector('.right-topbar');
    if (rect.bottom < panelRect.top + 56) { stickyTitle.textContent = h2.textContent; stickyTitle.classList.add('visible'); topbar.classList.add('scrolled'); }
    else { stickyTitle.classList.remove('visible'); topbar.classList.remove('scrolled'); }
  });

  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeRight(); });
}

let lastDetailIdx = 0;
function scrollToSection(idx) { const blocks = document.querySelectorAll('.section-block'); if (blocks[idx]) blocks[idx].scrollIntoView({behavior:'smooth',block:'start'}); }
function openDetail(idx) { lastDetailIdx = idx; document.querySelectorAll('.detail').forEach(d => d.style.display = 'none'); document.getElementById(`detail-${idx}`).style.display = 'block'; document.getElementById('right').classList.remove('closed'); document.body.classList.add('detail-open'); document.getElementById('right').scrollTop = 0; document.getElementById('right-sticky-title').classList.remove('visible'); }
function closeRight() { document.getElementById('right').classList.add('closed'); document.body.classList.remove('detail-open'); }
function toggleDetail() { if (document.body.classList.contains('detail-open')) { closeRight(); } else { openDetail(lastDetailIdx); } }
function toggleTheme() { const current = document.body.getAttribute('data-theme'); const next = current === 'light' ? 'dark' : 'light'; document.body.setAttribute('data-theme', next); localStorage.setItem('theme', next); }

const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);
