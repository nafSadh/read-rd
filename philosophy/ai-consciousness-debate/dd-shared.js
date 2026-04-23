const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);
document.getElementById('theme-btn').onclick = () => {
  const next = document.body.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
  document.body.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
};

const sidebarItems = document.querySelectorAll('.sidebar-item');
const sectionBlocks = document.querySelectorAll('.section-block');
const mainScroll = document.getElementById('main-scroll');

function scrollToSection(idx) {
  if (sectionBlocks[idx]) sectionBlocks[idx].scrollIntoView({behavior:'smooth',block:'start'});
}
sidebarItems.forEach((item, idx) => { item.onclick = () => scrollToSection(idx); });

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

document.querySelectorAll('.s-detail-btn').forEach((btn, idx) => { btn.onclick = () => openDetail(idx); });

document.getElementById('detail-btn').onclick = () => {
  if (document.body.classList.contains('detail-open')) closeRight();
  else openDetail(lastDetailIdx);
};

mainScroll.addEventListener('scroll', () => {
  document.querySelector('.main-head').classList.toggle('compact', mainScroll.scrollTop > 40);
  let activeIdx = 0;
  sectionBlocks.forEach((b, i) => {
    if (b.getBoundingClientRect().top < mainScroll.getBoundingClientRect().top + 120) activeIdx = i;
  });
  sidebarItems.forEach((item, i) => item.classList.toggle('active', i === activeIdx));
});

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

document.addEventListener('keydown', e => { if (e.key === 'Escape') closeRight(); });
