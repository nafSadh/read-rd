#!/usr/bin/env python3
"""Generate section deep-dive HTML files from the overview template CSS."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# Read CSS from overview
with open(os.path.join(BASE, 'overview.dd.html'), 'r', encoding='utf-8') as f:
    overview = f.read()

# Extract CSS block (everything up to and including </style>\n</head>\n<body>)
css_end = overview.index('<body>')
css_block = overview[:css_end + len('<body>')]

# JS boilerplate (shared DOM building + interaction code)
JS_BOILERPLATE = r"""
// Build DOM
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
    <div class="sidebar-head">
      <div class="sidebar-logo">${LOGO}</div>
    </div>
    <div class="sidebar-nav" id="sidebar-nav"></div>
  </nav>
  <div class="main" id="main">
    <div class="main-head">
      <div class="main-head-inner">
        <div class="hero-badge"><span class="dot"></span> ${BADGE}</div>
        <div class="hero-title">${HERO_TITLE}</div>
        <div class="masthead-rule"></div>
        <div class="masthead-sub"><span>${SUBTITLE}</span></div>
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

// Build sidebar
const sidebarNav = document.getElementById('sidebar-nav');
sections.forEach((sec, idx) => {
  const item = document.createElement('div');
  item.className = 'sidebar-item' + (idx === 0 ? ' active' : '');
  item.setAttribute('data-label', sec.short);
  item.innerHTML = '<span class="sidebar-num">' + sec.num + '</span><span class="sidebar-label">' + sec.short + '</span>';
  item.onclick = () => scrollToSection(idx);
  sidebarNav.appendChild(item);
});

// Sidebar hover tooltip
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

// Build main scroll
const mainScroll = document.getElementById('main-scroll');
const mainInner = document.createElement('div');
mainInner.className = 'main-scroll-inner';
mainScroll.appendChild(mainInner);
sections.forEach((sec, idx) => {
  const block = document.createElement('div');
  block.className = 'section-block';
  block.innerHTML = '<div class="s-num"><span>' + sec.num + '</span><button class="s-detail-btn" onclick="openDetail(' + idx + ')"><svg width="14" height="14" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg></button></div><h2>' + sec.title + '</h2>' + summaries[idx];
  mainInner.appendChild(block);
});

// Build details
const rightInner = document.getElementById('right-inner');
sections.forEach((sec, idx) => {
  const detailDiv = document.createElement('div');
  detailDiv.className = 'detail';
  detailDiv.id = 'detail-' + idx;
  detailDiv.innerHTML = details[idx];
  rightInner.appendChild(detailDiv);
});

// Functions
let lastDetailIdx = 0;
function scrollToSection(idx) { const blocks = document.querySelectorAll('.section-block'); if (blocks[idx]) blocks[idx].scrollIntoView({behavior:'smooth',block:'start'}); }
function openDetail(idx) { lastDetailIdx = idx; document.querySelectorAll('.detail').forEach(d => d.style.display = 'none'); document.getElementById('detail-' + idx).style.display = 'block'; document.getElementById('right').classList.remove('closed'); document.body.classList.add('detail-open'); document.getElementById('right').scrollTop = 0; document.getElementById('right-sticky-title').classList.remove('visible'); }
function closeRight() { document.getElementById('right').classList.add('closed'); document.body.classList.remove('detail-open'); }
function toggleDetail() { if (document.body.classList.contains('detail-open')) { closeRight(); } else { openDetail(lastDetailIdx); } }
function toggleTheme() { const current = document.body.getAttribute('data-theme'); const next = current === 'light' ? 'dark' : 'light'; document.body.setAttribute('data-theme', next); localStorage.setItem('theme', next); }

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);

// Compact main header + sidebar scroll spy
mainScroll.addEventListener('scroll', () => {
  document.querySelector('.main-head').classList.toggle('compact', mainScroll.scrollTop > 40);
  const blocks = mainScroll.querySelectorAll('.section-block');
  const items = document.querySelectorAll('.sidebar-item');
  let activeIdx = 0;
  blocks.forEach((b, i) => { if (b.getBoundingClientRect().top < mainScroll.getBoundingClientRect().top + 120) activeIdx = i; });
  items.forEach((item, i) => item.classList.toggle('active', i === activeIdx));
});

// Sticky header in right panel
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

// ESC closes detail panel
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeRight(); });
"""

# ============================================================
# SECTION DEFINITIONS
# ============================================================

SECTIONS = {
    's1-history': {
        'title_tag': 'S1: A History of Language Invention',
        'logo': 'H<em>L</em>',
        'badge': 'CONLANGS &middot; S1 &middot; 11 SOURCES',
        'hero': 'A History of Language <em>Invention</em>',
        'subtitle': 'From Lingua Ignota to Esperanto &mdash; and why most invented languages failed',
        'sections_js': """[
  { num: '01', short: 'Overview', title: 'A History of Language <em>Invention</em>' },
  { num: '02', short: 'Lingua Ignota', title: 'The First Known <em>Conlang</em>' },
  { num: '03', short: 'Philosophical', title: 'Philosophical <em>Languages</em>' },
  { num: '04', short: 'Volapuk', title: 'Volapuk: Rise &amp; <em>Fall</em>' },
  { num: '05', short: 'Esperanto', title: 'Esperanto: The <em>Survivor</em>' },
  { num: '06', short: 'Also-Rans', title: 'Ido, Interlingua, <em>Lojban</em>' },
  { num: '07', short: 'Failure', title: 'Why Most <em>Failed</em>' },
  { num: '08', short: 'Consensus', title: 'What Sources <em>Agree On</em>' }
]""",
        'summaries_js': r"""[
  `<p>This section traces the history of constructed languages from their earliest documented example &mdash; Hildegard von Bingen&rsquo;s mystical alphabet in the 1150s &mdash; through the philosophical languages of the Enlightenment, the international auxiliary language movement of the 19th century, and the spectacular rise and fall of Volapuk.</p>
   <p>The central finding: <strong>community matters more than grammar.</strong> Volapuk had a more complex grammar than Esperanto and still died. Esperanto survived because Zamenhof released it to its speakers.</p>
   <div class="s-stat">
     <div class="st"><div class="sv">~870 yrs</div><div class="sl">of conlang history</div></div>
     <div class="st"><div class="sv">283</div><div class="sl">Volapuk clubs at peak</div></div>
     <div class="st"><div class="sv">~100K</div><div class="sl">Esperanto speakers</div></div>
     <div class="st"><div class="sv">16</div><div class="sl">Esperanto grammar rules</div></div>
   </div>`,

  `<p>Hildegard von Bingen, a Benedictine abbess, created the <em>Lingua Ignota</em> (&ldquo;Unknown Language&rdquo;) in the 12th century &mdash; the earliest documented constructed language. It consists of approximately 1,000 words with a glossary and an alphabet. The vocabulary draws from Latin and German but is otherwise original.</p>
   <p>Hildegard&rsquo;s purpose was mystical, not communicative. She sought to transcend everyday language to reach closer to God. What makes Lingua Ignota significant: it establishes that the impulse to create language is <strong>at least 870 years old</strong> and precedes any practical motivation. The first conlang was art, not engineering.</p>`,

  `<p>The 17th century saw a wave of &ldquo;philosophical languages&rdquo; &mdash; attempts to create a perfect language that would reveal the true nature of reality. John Wilkins&rsquo; <em>An Essay towards a Real Character, and a Philosophical Language</em> (1668) divided all knowledge into <strong>40 main categories</strong>, each subdivided recursively.</p>
   <p>The ambition: you could deduce a word&rsquo;s meaning from its spelling alone. The project failed for a fundamental reason: <em>knowledge is not a tree.</em> Categories overlap, contexts shift, and new discoveries require restructuring the entire system. But the impulse influenced Leibniz and, through him, formal logic itself.</p>`,

  `<p>Johann Martin Schleyer, a Catholic priest, created Volapuk in 1879. By his account, God instructed him during a sleepless night. Within a decade: <strong>283 clubs worldwide, 25 periodicals, 316 textbooks</strong> in 25 languages. The third Volapuk congress (Paris, 1889) was conducted entirely in Volapuk.</p>
   <p>The collapse was equally dramatic. Schleyer <strong>refused to cede control</strong> when the Volapuk Academy proposed reforms. The Academy abandoned Volapuk. Most speakers defected. By the mid-1890s, Volapuk was dead &mdash; killed not by a better language but by its own creator.</p>
   <div class="callout"><h4>The Volapuk Lesson</h4><p>A constructed language lives or dies by its community, and a community cannot survive a founder who refuses to let go.</p></div>`,

  `<p>L.L. Zamenhof published <em>Lingvo Internacia</em> in 1887. His motivation: growing up in multilingual Bialystok, he believed a neutral language could foster peace. Esperanto&rsquo;s design: <strong>16 grammar rules, no exceptions</strong>; agglutinative word formation; phonetic spelling; vocabulary from Romance, Germanic, and Slavic.</p>
   <p>Zamenhof made a crucial decision Schleyer did not: <strong>he relinquished control.</strong> Today Esperanto has ~100,000 speakers, original literature, annual world congresses (since 1905), UNESCO recognition, and a small number of native speakers. It is by far the most successful IAL &mdash; and still tiny compared to any natural language.</p>`,

  `<p><strong>Ido</strong> (1907): A reformed Esperanto that caused a devastating schism. Pulled speakers from Esperanto without gaining enough of its own. <strong>Interlingua</strong> (1951): Extracts common elements of European languages. Readable to Romance speakers but excludes the non-European world.</p>
   <p><strong>Lojban</strong> (1987): A logical language based on predicate logic, designed to test the Sapir-Whorf hypothesis. ~1,000 active users. Lojban connects the IAL tradition to the cognitive science questions explored in <a href="s4-relativity.dd.html">Section 4</a>.</p>
   <div class="s-chips"><span class="s-chip">Ido 1907</span><span class="s-chip">Interlingua 1951</span><span class="s-chip">Lojban 1987</span><span class="s-chip">Toki Pona 2001</span></div>`,

  `<p>The failure modes are remarkably consistent across every failed IAL:</p>
   <ul class="s-list con">
     <li><strong>Chicken-and-egg:</strong> Nobody learns a language without speakers; nobody speaks without learners</li>
     <li><strong>Culture gap:</strong> Language cannot be separated from culture. Purely functional languages lack emotional pull</li>
     <li><strong>English won:</strong> The rise of English as global lingua franca removed the practical motivation</li>
     <li><strong>Schism problem:</strong> Every successful conlang attracts reformers. Reform destroys or splits the community</li>
     <li><strong>False neutrality:</strong> Esperanto claimed neutrality but is overwhelmingly European in vocabulary and grammar</li>
   </ul>`,

  `<p>Across 11 sources, five points of convergence:</p>
   <ul class="s-list pro">
     <li>Lingua Ignota is the first documented conlang (~1150s)</li>
     <li>Volapuk&rsquo;s failure was caused primarily by founder control, not linguistic deficiencies</li>
     <li>Esperanto&rsquo;s survival is exceptional among IALs</li>
     <li>The practical need for an IAL diminished as English became dominant</li>
     <li>Community matters more than grammatical elegance</li>
   </ul>`
]""",
        'details_js': r"""[
  `<div class="detail-header"><div class="num">01</div><h2>A History of Language <em>Invention</em></h2></div>
   <h3>Why This Section Matters</h3>
   <p>The history of constructed languages is often told as a series of failed utopian projects. That framing misses the point. The IAL tradition &mdash; from Volapuk to Esperanto to Lojban &mdash; was an experiment in whether humans could deliberately create a shared language. The experiment largely failed, but it produced invaluable data about what makes languages work and why communities adopt or reject them.</p>
   <p>This section provides the historical context for everything that follows. Tolkien&rsquo;s languages (<a href="s2-tolkien.dd.html">S2</a>) were a deliberate rejection of the utilitarian tradition. Media conlangs (<a href="s3-media.dd.html">S3</a>) found a purpose the IAL movement never imagined. And Nicaraguan Sign Language (<a href="s5-sign.dd.html">S5</a>) proved that the most successful language creation happens without any designer at all.</p>
   <h3>Source Assessment</h3>
   <p>11 sources covering the full arc from Lingua Ignota to Lojban. Wikipedia provides factual grounding; the Beinecke Library (Yale) and Public Domain Review provide archival context for Volapuk; Cambridge Blog and HistoryRise provide accessible overviews; Omniglot and Medium provide analytical frameworks for IAL failure.</p>`,

  `<div class="detail-header"><div class="num">02</div><h2>The First Known <em>Conlang</em></h2></div>
   <h3>Hildegard von Bingen</h3>
   <p>Hildegard (1098&ndash;1179) was a Benedictine abbess, mystic, composer, philosopher, and polymath. The Lingua Ignota appears in a manuscript alongside the Litterae Ignotae (Unknown Letters), a 23-character alphabet that resembles a mixture of Greek, Cyrillic, and Roman cursive.</p>
   <p>The ~1,000 words are organized hierarchically, beginning with divine and celestial terms and ending with mundane objects. This ordering reflects Hildegard&rsquo;s mystical purpose: the language was structured to reflect the order of creation, with God at the top and earthly things at the bottom.</p>
   <h3>Why It Matters for Conlang History</h3>
   <p>Lingua Ignota establishes that the impulse to create language is ancient and precedes any utilitarian motivation. Hildegard was not trying to bridge nations or build a world. She was trying to speak to God in a tongue uncorrupted by human politics. The first conlang was an act of devotion, not engineering.</p>
   <div class="callout"><h4>The Significance</h4><p>Every subsequent conlang tradition &mdash; philosophical, utopian, artistic, computational &mdash; can be understood as a different answer to the same question Hildegard asked: what would a language look like if we could start from scratch?</p></div>`,

  `<div class="detail-header"><div class="num">03</div><h2>Philosophical <em>Languages</em></h2></div>
   <h3>The Dream of a Perfect Language</h3>
   <p>The 17th century philosophical language movement was animated by a specific dream: that language could be made to mirror reality so precisely that understanding a word would mean understanding the thing it names. John Wilkins&rsquo; 1668 essay was the most ambitious attempt.</p>
   <p>Wilkins divided all knowledge into 40 genera, each subdivided into differences and species. Each concept received a unique combination of letters and marks. The result: a word&rsquo;s spelling would tell you exactly where it sat in the tree of knowledge.</p>
   <h3>Why It Failed</h3>
   <p>The project assumed that knowledge has a single, stable, hierarchical structure. It does not. Is a whale a fish or a mammal? Is light a wave or a particle? Wilkins&rsquo; categories would need restructuring every time scientific understanding changed. A language that encodes a taxonomy of knowledge is only as good as the taxonomy &mdash; and taxonomies are always provisional.</p>
   <p>But the failure was productive. Wilkins influenced Leibniz&rsquo;s work on formal notation, which influenced Boole&rsquo;s logic, which influenced modern computing. The dream of a perfect language evolved into the reality of formal programming languages &mdash; a connection explored in <a href="s6-programming.dd.html">Section 6</a>.</p>`,

  `<div class="detail-header"><div class="num">04</div><h2>Volapuk: Rise &amp; <em>Fall</em></h2></div>
   <h3>The Numbers</h3>
   <p>At its peak (1889), Volapuk had: 283 clubs across Europe and the Americas, 25 periodicals, 316 textbooks in 25 languages, and an Academy with authority to manage the language. Newspapers printed columns in Volapuk. Shop signs appeared in it. The third international congress (Paris, 1889) was conducted entirely in Volapuk. No constructed language before or since has achieved this level of public visibility in such a short time.</p>
   <h3>The Schism</h3>
   <p>Auguste Kerckhoffs, president of the Volapuk Academy, proposed reforms to simplify the grammar. Schleyer, who considered Volapuk his personal creation and divine mission, rejected them absolutely. He insisted on retaining complete control. When the Academy moved ahead without him, he declared their reforms illegitimate. The community fractured. The Academy abandoned Volapuk for Idiom Neutral. Most speakers defected to Esperanto.</p>
   <h3>The Lesson</h3>
   <p>Volapuk&rsquo;s failure was not linguistic. Its grammar was more sophisticated than Esperanto&rsquo;s. Its decline was a governance failure &mdash; a founder who could not distinguish between creating a language and owning it. This pattern recurs throughout conlang history and even in programming language communities.</p>
   <div class="diagram-wrap"><svg viewBox="0 0 400 150" xmlns="http://www.w3.org/2000/svg">
     <text x="200" y="18" text-anchor="middle" font-size="10" class="lbl" letter-spacing="1.5" style="font-size:10px">VOLAPUK POPULARITY CURVE</text>
     <line x1="40" y1="30" x2="360" y2="30" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>
     <polyline points="60,120 120,100 180,50 220,40 260,80 300,110 340,125" fill="none" stroke="var(--accent)" stroke-width="2"/>
     <circle cx="220" cy="40" r="4" fill="var(--accent)"/>
     <text x="220" y="32" text-anchor="middle" font-size="8" class="lbl-hi" style="font-size:8px">1889 Peak</text>
     <text x="60" y="135" font-size="7" class="lbl" style="font-size:7px">1879</text>
     <text x="340" y="135" font-size="7" class="lbl" style="font-size:7px">1900</text>
     <text x="280" y="95" font-size="7" class="lbl" style="font-size:7px">Schism</text>
   </svg></div>`,

  `<div class="detail-header"><div class="num">05</div><h2>Esperanto: The <em>Survivor</em></h2></div>
   <h3>Design Principles</h3>
   <p>Zamenhof&rsquo;s 16 rules: every noun ends in -o, every adjective in -a, verbs conjugate regularly (-as present, -is past, -os future), no grammatical gender beyond an optional feminine suffix -ino. The agglutinative system lets speakers build complex words from simple roots without memorizing irregularities.</p>
   <h3>Why It Survived</h3>
   <p>Three factors distinguish Esperanto from every other IAL:</p>
   <p><strong>1. Founder humility.</strong> Zamenhof published under a pseudonym and explicitly stated the language belonged to its speakers. He refused to be its dictator &mdash; the exact opposite of Schleyer.</p>
   <p><strong>2. Cultural development.</strong> Esperanto developed its own literature, music, traditions, and community identity. It stopped being just a communication tool and became a culture. Languages need culture to survive.</p>
   <p><strong>3. Community infrastructure.</strong> Annual world congresses (since 1905), local clubs, magazines, and eventually the internet all maintained the community through periods when Esperanto had no practical advantage over natural languages.</p>
   <h3>The Limitation</h3>
   <p>Esperanto&rsquo;s vocabulary and grammar are overwhelmingly European. It is not a neutral bridge language for the world &mdash; it is a simplified European language. This Eurocentrism is Esperanto&rsquo;s deepest structural limitation, even as it claims universality.</p>`,

  `<div class="detail-header"><div class="num">06</div><h2>Ido, Interlingua, <em>Lojban</em></h2></div>
   <h3>The Reform Trap</h3>
   <p>Ido (1907) illustrates a recurring pattern: a group of reformers identifies genuine flaws in a successful conlang, proposes improvements, and in doing so splits the community without gaining a new one. The Ido movement pulled speakers from Esperanto&rsquo;s community but never built a critical mass of its own. By the 1920s, it was a cautionary tale about perfectionism &mdash; the grammar was arguably better, but the community was dead.</p>
   <h3>Interlingua: The Naturalistic Approach</h3>
   <p>Interlingua (1951) took a fundamentally different approach: instead of designing a new grammar, extract the common vocabulary and structures from major European languages. The result is immediately readable to any speaker of a Romance language &mdash; but essentially excludes speakers of non-European languages. It is the most honest IAL in one sense: it does not pretend to be universal.</p>
   <h3>Lojban: Language as Experiment</h3>
   <p>Lojban connects the IAL tradition to the cognitive science questions explored in <a href="s4-relativity.dd.html">Section 4</a>. Designed to be syntactically unambiguous and based on predicate logic, Lojban was originally conceived to test whether speakers of a perfectly logical language would think more logically. The community (~1,000 active) is too small for rigorous study, but the project represents the most systematic attempt to use a constructed language as a scientific instrument.</p>`,

  `<div class="detail-header"><div class="num">07</div><h2>Why Most <em>Failed</em></h2></div>
   <h3>Five Failure Modes</h3>
   <p><strong>1. The chicken-and-egg problem.</strong> Nobody learns a language without speakers, and nobody becomes a speaker without learners. Natural languages escape this through birth and immigration. Constructed languages have no such mechanism. They must create demand from nothing.</p>
   <p><strong>2. Language cannot be separated from culture.</strong> Zamenhof understood this &mdash; Esperanto developed its own culture. Languages that remained purely functional tools never developed the emotional attachment needed for survival. You don&rsquo;t fight for a grammar; you fight for a community.</p>
   <p><strong>3. English won.</strong> The rise of English as global lingua franca removed the practical motivation for an IAL. Why learn Esperanto when English gives you access to far more people, content, and economic opportunity?</p>
   <p><strong>4. The schism problem.</strong> Every successful conlang attracts reformers. Reform either destroys the community (Volapuk) or creates painful splits (Ido). Natural languages evolve gradually; constructed languages face demands for revolution.</p>
   <p><strong>5. Political neutrality is impossible.</strong> Esperanto is overwhelmingly European. Interlingua is even more Eurocentric. No language can be truly neutral because language embeds cultural assumptions in its vocabulary, metaphors, and categories.</p>`,

  `<div class="detail-header"><div class="num">08</div><h2>What Sources <em>Agree On</em></h2></div>
   <h3>Points of Consensus</h3>
   <p>Despite approaching the topic from different angles &mdash; historical, linguistic, sociological &mdash; the sources converge on five points:</p>
   <p><strong>1.</strong> Lingua Ignota (~1150s) is the earliest documented constructed language.</p>
   <p><strong>2.</strong> Volapuk&rsquo;s failure was a governance failure, not a linguistic one. The language worked; the governance didn&rsquo;t.</p>
   <p><strong>3.</strong> Esperanto&rsquo;s survival is exceptional and instructive. It is the only IAL to develop a living culture.</p>
   <p><strong>4.</strong> The practical need for an IAL has diminished as English became the de facto world language.</p>
   <p><strong>5.</strong> Community matters more than grammatical elegance. The most important property of a language is having people who want to speak it.</p>
   <div class="callout"><h4>The Implication</h4><p>If community matters more than grammar, then the art of conlanging is not primarily linguistic. It is social. The best grammar in the world is worthless without a community that loves the language enough to speak it.</p></div>`
]"""
    },
    's2-tolkien': {
        'title_tag': 'S2: Tolkien &mdash; The Philologist&#39;s Art',
        'logo': 'T<em>L</em>',
        'badge': 'CONLANGS &middot; S2 &middot; 8 SOURCES',
        'hero': 'Tolkien: The Philologist&rsquo;s <em>Art</em>',
        'subtitle': 'The man who built languages so beautiful he had to invent a world for them',
        'sections_js': """[
  { num: '01', short: 'Overview', title: 'The Philologist&rsquo;s <em>Art</em>' },
  { num: '02', short: 'Languages First', title: 'Languages First, Stories <em>Second</em>' },
  { num: '03', short: 'Quenya', title: 'Quenya: The Finnish <em>Connection</em>' },
  { num: '04', short: 'Sindarin', title: 'Sindarin: The Welsh <em>Inspiration</em>' },
  { num: '05', short: 'Family Tree', title: 'The Language <em>Family Tree</em>' },
  { num: '06', short: 'Scripts', title: 'Tengwar &amp; <em>Cirth</em>' },
  { num: '07', short: 'Depth', title: 'Depth Without <em>Limit</em>' },
  { num: '08', short: 'Legacy', title: 'The Lesson for <em>Conlanging</em>' }
]""",
        'summaries_js': r"""[
  `<p>Tolkien&rsquo;s languages are the single greatest achievement in conlang history. Not because they are the most spoken (they are not) or the most practical (they are entirely impractical), but because they have the <strong>depth, beauty, and internal consistency</strong> of natural languages. This section explains how a professional philologist built a language family that generated an entire world.</p>
   <div class="s-stat">
     <div class="st"><div class="sv">~20</div><div class="sl">languages/dialects</div></div>
     <div class="st"><div class="sv">50 yrs</div><div class="sl">of continuous work</div></div>
     <div class="st"><div class="sv">2</div><div class="sl">complete writing systems</div></div>
     <div class="st"><div class="sv">10</div><div class="sl">Quenya noun cases</div></div>
   </div>`,

  `<p>The most important fact: <strong>the languages came first.</strong> Tolkien&rsquo;s own words: &ldquo;The invention of languages is the foundation. The &lsquo;stories&rsquo; were made rather to provide a world for the languages than the reverse.&rdquo; Middle-earth exists <em>because of</em> the languages, not the other way around.</p>
   <p>Tolkien began inventing languages as a child, inspired by Gothic, Finnish, and Welsh. He was a professional philologist at Oxford &mdash; a specialist in Old English. This is not a novelist dabbling in linguistics. It is a linguist channeling his expertise into fiction.</p>`,

  `<p>Quenya, the High Elvish language, draws its aesthetic from <strong>Finnish</strong>: agglutinative morphology, vowel-rich phonology, liquid consonants. It functions as an archaic literary language in Middle-earth &mdash; the Latin of the Elves.</p>
   <p>Tolkien&rsquo;s Quenya includes: <strong>ten cases</strong> (nominative, accusative, genitive, dative, possessive, ablative, allative, locative, instrumental, respective), full verbal conjugation, dual number, and multiple declension classes. This is not a sketch. It is a complete grammatical system.</p>`,

  `<p>Sindarin takes its character from <strong>Welsh</strong>: consonant mutation, fusional morphology, the distinctive dh/th/ch sounds. Unlike Quenya&rsquo;s agglutination, Sindarin changes word forms through <em>internal modification</em> &mdash; directly inspired by Welsh lenition.</p>
   <p>Sindarin is the &ldquo;living&rdquo; Elvish language of the Third Age. Its relationship to Quenya mirrors Welsh to Latin: one is the language of everyday life, the other of learning and ceremony.</p>`,

  `<p>Tolkien used real <strong>comparative philology</strong> to construct his language family. From Primitive Quendian (the proto-language) through Common Eldarin to Quenya, Sindarin, and Telerin &mdash; with specified sound changes, morphological innovations, and borrowings at each branch.</p>
   <div class="diagram-wrap"><svg viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
     <text x="200" y="18" text-anchor="middle" font-size="10" class="lbl" letter-spacing="1.5" style="font-size:10px">TOLKIEN&rsquo;S ELVISH LANGUAGE FAMILY</text>
     <rect x="140" y="30" width="120" height="22" rx="3" class="node-hi"/><text x="200" y="45" text-anchor="middle" font-size="9" class="node-text" style="font-size:9px">Primitive Quendian</text>
     <line x1="200" y1="52" x2="200" y2="65" class="edge"/>
     <rect x="140" y="65" width="120" height="22" rx="3" class="node"/><text x="200" y="80" text-anchor="middle" font-size="9" class="node-text" style="font-size:9px">Common Eldarin</text>
     <line x1="150" y1="87" x2="80" y2="105" class="edge-hi"/><line x1="200" y1="87" x2="200" y2="105" class="edge"/><line x1="250" y1="87" x2="320" y2="105" class="edge"/>
     <rect x="30" y="105" width="100" height="22" rx="3" class="node-hi"/><text x="80" y="120" text-anchor="middle" font-size="9" class="node-text" style="font-size:9px">Quenya</text>
     <text x="80" y="140" text-anchor="middle" font-size="7" class="lbl" style="font-size:7px">Finnish-inspired</text>
     <rect x="150" y="105" width="100" height="22" rx="3" class="node"/><text x="200" y="120" text-anchor="middle" font-size="9" class="node-text" style="font-size:9px">Telerin</text>
     <rect x="270" y="105" width="100" height="22" rx="3" class="node-hi"/><text x="320" y="120" text-anchor="middle" font-size="9" class="node-text" style="font-size:9px">Sindarin</text>
     <text x="320" y="140" text-anchor="middle" font-size="7" class="lbl" style="font-size:7px">Welsh-inspired</text>
     <line x1="40" y1="87" x2="40" y2="160" class="edge" stroke-dasharray="3,3"/><text x="45" y="168" font-size="7" class="lbl" style="font-size:7px">Avarin (stayed behind)</text>
   </svg></div>`,

  `<p><strong>Tengwar</strong>: A featural writing system where letter shapes encode phonetic information. Manner and place of articulation are visually represented. Multiple modes for different languages. Strikingly modern &mdash; featural scripts were rare in Tolkien&rsquo;s era.</p>
   <p><strong>Cirth</strong>: Angular runes designed for carving in stone or wood, used primarily by Dwarves. Less linguistically sophisticated than Tengwar but practically suited to its medium.</p>`,

  `<p>What distinguishes Tolkien from all other conlangers: <strong>depth.</strong> Full etymological histories tracing words through sound changes. Dialectal variation. Register differences. Poetry in multiple meters. Internal documents written <em>in</em> the languages. The Etymologies &mdash; a massive posthumous document tracing roots through the entire family tree.</p>
   <p>His languages were never &ldquo;finished&rdquo; because he kept revising them. New phonological ideas cascaded through the entire system. Like natural languages, they were always in flux.</p>`,

  `<p>Tolkien&rsquo;s key innovations for conlanging:</p>
   <ul class="s-list pro">
     <li><strong>Diachronic construction:</strong> Build not just a language but its history &mdash; sound changes, borrowings, dialectal splits</li>
     <li><strong>Narrative integration:</strong> Language and story reinforce each other</li>
     <li><strong>Aesthetic primacy:</strong> The sound and feel matter as much as the grammar</li>
     <li><strong>Professional rigor:</strong> Apply real linguistic methods, not amateur improvisation</li>
   </ul>
   <p>No conlanger since has matched Tolkien&rsquo;s depth. Peterson and Frommer create excellent languages, but they work under deadlines. Tolkien worked for fifty years.</p>`
]""",
        'details_js': r"""[
  `<div class="detail-header"><div class="num">01</div><h2>The Philologist&rsquo;s <em>Art</em></h2></div>
   <h3>Why This Section Matters</h3>
   <p>Tolkien represents the gold standard of conlanging &mdash; the proof that a constructed language can have the depth, beauty, and internal consistency of a natural language. Understanding his method is essential context for evaluating every subsequent conlang, from Klingon to Dothraki to Heptapod B.</p>
   <p>His approach was fundamentally different from the IAL tradition (<a href="s1-history.dd.html">S1</a>). Where Zamenhof designed for simplicity and adoption, Tolkien designed for beauty and depth. Where Esperanto aimed to be spoken by everyone, Quenya was never intended to be spoken by anyone. The artistic tradition in conlanging begins here.</p>
   <h3>Source Assessment</h3>
   <p>8 sources: Wikipedia for factual grounding, Tolkien Estate scholarship (Hostetter, Smith) for authoritative linguistic analysis, academic papers (Coker, NCUR) for systematic study, and popular sources (Multilingual, Oxford Open Learning) for biographical context.</p>`,

  `<div class="detail-header"><div class="num">02</div><h2>Languages First, Stories <em>Second</em></h2></div>
   <h3>The Inversion</h3>
   <p>Most people assume Tolkien created languages to enrich his fiction. The truth is the exact opposite. Quenya and Sindarin required speakers, history, migrations, wars, and cultural divisions to explain their divergence from a common ancestor. The Silmarillion is, at its deepest level, a linguistic history dressed in narrative.</p>
   <p>This inversion has profound implications for the relationship between language and worldbuilding. If language comes first, then the world it generates will have a linguistic coherence that no amount of retroactive naming can achieve. The place names, character names, and cultural terms in Middle-earth are not decorative labels &mdash; they are organic products of the languages&rsquo; phonology and etymology.</p>
   <h3>The Biographical Evidence</h3>
   <p>Tolkien began inventing languages as a schoolboy, long before any narrative existed. His professional career as a philologist at Oxford gave him the technical tools to develop his childhood hobby into something with the rigor of real linguistic reconstruction. The combination of lifelong obsession and professional expertise is what produced the unprecedented depth.</p>`,

  `<div class="detail-header"><div class="num">03</div><h2>Quenya: The Finnish <em>Connection</em></h2></div>
   <h3>Morphological Depth</h3>
   <p>Quenya&rsquo;s ten-case system (nominative, accusative, genitive, dative, possessive, ablative, allative, locative, instrumental, respective) is more complex than Latin (six cases) and comparable to Finnish (fifteen cases). Each case has regular endings but multiple declension classes, creating the kind of systematic-with-exceptions pattern that characterizes real languages.</p>
   <p>The agglutinative morphology allows Tolkien to build complex words from simple roots: <em>Eldalieva</em> (&ldquo;of the Eldar&rdquo;) combines root, plural marker, and genitive suffix in a single word. This mirrors Finnish&rsquo;s productive word-building system.</p>
   <h3>Aesthetic Choices</h3>
   <p>Quenya&rsquo;s sound palette &mdash; rich in vowels, liquids (l, r), and nasals, with few harsh consonant clusters &mdash; was chosen for beauty, not communicative efficiency. Tolkien wanted Quenya to sound like what an archaic, ceremonial language <em>should</em> sound like: elevated, musical, and slightly alien to modern ears.</p>`,

  `<div class="detail-header"><div class="num">04</div><h2>Sindarin: The Welsh <em>Inspiration</em></h2></div>
   <h3>Consonant Mutation</h3>
   <p>The defining feature of Sindarin is its system of consonant mutation, directly inspired by Welsh. In Welsh, the word for &ldquo;cat&rdquo; (<em>cath</em>) becomes <em>gath</em> after certain particles (soft mutation), <em>nghath</em> after others (nasal mutation), and <em>chath</em> after still others (aspirate mutation). Sindarin implements a similar system with soft, nasal, and mixed mutations.</p>
   <p>This gives Sindarin a fundamentally different character from Quenya. Where Quenya builds meaning by adding suffixes (agglutination), Sindarin changes the form of words themselves (fusion). The contrast mirrors the real-world difference between Finnish and Welsh &mdash; and provides Middle-earth with two Elvish languages that feel genuinely different, not just vocabulary swaps.</p>`,

  `<div class="detail-header"><div class="num">05</div><h2>The Language <em>Family Tree</em></h2></div>
   <h3>Comparative Philology in Action</h3>
   <p>Tolkien applied the same methods used to reconstruct Proto-Indo-European. He started with Primitive Quendian&rsquo;s phonological system and specified the sound changes needed for each daughter language. For example: the proto-language&rsquo;s *kw becomes p in Sindarin but is preserved in Quenya &mdash; exactly paralleling how Latin <em>qu-</em> became Welsh <em>p-</em> while remaining in Italian.</p>
   <p>This is not decoration. It means that cognates between Quenya and Sindarin are systematically related, just as Latin <em>aqua</em> and Welsh <em>dwr</em> (water) are systematically related through documented sound changes. A linguist can examine Tolkien&rsquo;s word pairs and verify that the sound correspondences are consistent.</p>
   <h3>The Result</h3>
   <p>Middle-earth&rsquo;s languages have the feel of a real language family because they <em>are</em> one &mdash; constructed using the same methods that historical linguists use to study natural language families. This is Tolkien&rsquo;s unique contribution: treating conlanging as a branch of comparative philology rather than as vocabulary invention.</p>`,

  `<div class="detail-header"><div class="num">06</div><h2>Tengwar &amp; <em>Cirth</em></h2></div>
   <h3>Featural Design</h3>
   <p>Tengwar is a featural writing system: the visual shape of each letter systematically encodes its phonetic properties. Letters for stops in the same place of articulation share a stem shape. Voiced and voiceless pairs are distinguished by a consistent visual modification. This is remarkably sophisticated &mdash; Korean Hangul (1443) is the only widely-used natural-language script with comparable featural properties.</p>
   <p>The system supports multiple &ldquo;modes&rdquo; &mdash; different mappings of letters to sounds for different languages. The same Tengwar script can write Quenya, Sindarin, or even English, with mode-specific rules for which letter represents which sound. This is analogous to how the Latin alphabet is used with different conventions for different languages.</p>
   <h3>Cirth: The Practical Script</h3>
   <p>Where Tengwar was designed for pen and brush (calligraphy), Cirth was designed for carving &mdash; angular strokes that can be cut into wood or stone. The distinction mirrors the real-world difference between Roman capitals (designed for inscriptions) and medieval minuscule (designed for manuscripts).</p>`,

  `<div class="detail-header"><div class="num">07</div><h2>Depth Without <em>Limit</em></h2></div>
   <h3>What &ldquo;Depth&rdquo; Means</h3>
   <p>Most conlangs create enough vocabulary and grammar for their purpose. Tolkien created: full etymological histories for individual words, tracing them through multiple stages of sound change. Dialectal variation within both Quenya and Sindarin. Register differences (formal vs. informal, archaic vs. modern). Poetry in multiple meters. Internal documents &mdash; letters, inscriptions, songs &mdash; composed <em>in</em> the languages.</p>
   <p>The Etymologies, published posthumously in <em>The Lost Road</em>, is a massive document tracing hundreds of word roots through the entire family tree. Each entry shows how a Primitive Quendian root evolved differently in each daughter language. It is the equivalent of an etymological dictionary for a natural language family &mdash; except that Tolkien invented every entry.</p>
   <h3>The Never-Finished Quality</h3>
   <p>Tolkien never published a definitive grammar of Quenya or Sindarin. He kept revising: new phonological ideas would cascade through the entire system, requiring updates to etymology, poetry, and narrative. Scholars debate which version represents his &ldquo;final&rdquo; intent &mdash; but the constant revision may be the point. Natural languages are never finished either.</p>`,

  `<div class="detail-header"><div class="num">08</div><h2>The Lesson for <em>Conlanging</em></h2></div>
   <h3>Four Innovations</h3>
   <p><strong>1. Diachronic construction.</strong> Build not just a language but its history. Sound changes, borrowings, dialectal splits. This gives the language the consistency and depth of a natural language because it was built using the same processes that shape natural languages.</p>
   <p><strong>2. Narrative integration.</strong> Language and story reinforce each other. The languages generate the stories; the stories justify the languages. This creates a coherence that neither could achieve alone.</p>
   <p><strong>3. Aesthetic primacy.</strong> The sound and feel of a language matter as much as its grammar. Tolkien chose Finnish and Welsh as models not for their grammatical properties but for their <em>beauty</em>.</p>
   <p><strong>4. Professional rigor.</strong> Tolkien applied the methods of comparative philology &mdash; the same methods used to reconstruct Proto-Indo-European &mdash; to his constructed languages. The result has the consistency of real linguistic reconstruction.</p>
   <div class="callout"><h4>The Standard</h4><p>No conlanger since has matched Tolkien&rsquo;s depth. Peterson and Frommer create excellent languages for media, but they work under deadlines and budgets. Tolkien worked for fifty years with no deadline but his own mortality. His languages set a standard that may never be equaled.</p></div>`
]"""
    },
    's3-media': {
        'title_tag': 'S3: Media Conlangs',
        'logo': 'M<em>C</em>',
        'badge': 'CONLANGS &middot; S3 &middot; 10 SOURCES',
        'hero': 'Media <em>Conlangs</em>',
        'subtitle': 'Klingon, Dothraki, Na&rsquo;vi &mdash; how Hollywood learned to take invented languages seriously',
        'sections_js': """[
  { num: '01', short: 'Overview', title: 'Media <em>Conlangs</em>' },
  { num: '02', short: 'Klingon', title: 'Klingon: The Accidental <em>Community</em>' },
  { num: '03', short: 'Peterson', title: 'David Peterson: First Full-Time <em>Conlanger</em>' },
  { num: '04', short: "Na'vi", title: 'Na&rsquo;vi: The Linguist&rsquo;s <em>Showcase</em>' },
  { num: '05', short: 'LCS', title: 'The Language Creation <em>Society</em>' },
  { num: '06', short: 'Hollywood', title: 'Why Hollywood Hires <em>Conlangers</em>' },
  { num: '07', short: 'Communities', title: 'The Community <em>Phenomenon</em>' },
  { num: '08', short: 'Consensus', title: 'What Sources <em>Agree On</em>' }
]""",
        'summaries_js': r"""[
  `<p>Media conlangs represent a phase transition in the field. When Marc Okrand created Klingon in 1984, conlanging was a private hobby. When David Peterson created Dothraki in 2011, it had become a <strong>professional career</strong>. This section traces how Hollywood went from dubbing alien dialogue with gibberish to hiring professional linguists.</p>
   <div class="s-stat">
     <div class="st"><div class="sv">40+</div><div class="sl">Peterson&rsquo;s conlangs</div></div>
     <div class="st"><div class="sv">4,000+</div><div class="sl">Dothraki words</div></div>
     <div class="st"><div class="sv">20-30</div><div class="sl">fluent Klingon speakers</div></div>
     <div class="st"><div class="sv">2007</div><div class="sl">LCS founded</div></div>
   </div>`,

  `<p>Marc Okrand, a Berkeley-trained linguist, created Klingon for Star Trek III (1984) to sound as alien as possible while remaining pronounceable. Design choices: <strong>OVS word order</strong> (rare among natural languages), unusual phonemes, no copula. Nobody expected fans to learn it.</p>
   <p>By 1992, the <strong>Klingon Language Institute</strong> was founded. Today: Shakespeare translated, Bible partially translated, original fiction written, annual conferences held. The most successful fictional language community in history.</p>`,

  `<p>When HBO needed languages for Game of Thrones, the <strong>Language Creation Society</strong> organized a competition. Peterson won and went on to become the <em>only person known to earn a living solely from conlanging</em>. Over <strong>40 conlangs</strong> created for film and TV.</p>
   <p>Peterson&rsquo;s approach differs from Okrand&rsquo;s: he builds languages that mirror how real human languages work. Full morphological paradigms, naturalistic sound changes, systematic irregularity. His Valyrian language family &mdash; with a proto-language and daughter languages &mdash; is directly inspired by Tolkien.</p>`,

  `<p>Paul Frommer, a USC linguist, created Na&rsquo;vi for James Cameron&rsquo;s Avatar (2009). Features: <strong>ejective consonants</strong>, tripartite case alignment (rare), infix system. Cameron provided 30 Polynesian-inspired starter words.</p>
   <p>Na&rsquo;vi was designed to sound unfamiliar but beautiful. Frommer continues expanding it for the Avatar sequels. Some fans have achieved conversational ability.</p>`,

  `<p>The <strong>Language Creation Society</strong> (2007) is the institutional backbone of professional conlanging: a 501(c)(3) nonprofit that organizes conferences, connects conlangers with Hollywood, and hosts publications. It ran the competition that selected Peterson for Game of Thrones.</p>
   <p>Before the LCS, creating languages was a private hobby. Now it is a recognized field with institutional support, professional standards, and career paths.</p>`,

  `<p>The shift happened gradually over decades:</p>
   <div class="timeline">
     <div class="tl-item"><div class="tl-date">1960s-80s</div><div class="tl-text">Star Trek: ad hoc gibberish, then Okrand&rsquo;s Klingon</div></div>
     <div class="tl-item"><div class="tl-date">2001-03</div><div class="tl-text">Lord of the Rings: Tolkien&rsquo;s existing languages used directly</div></div>
     <div class="tl-item"><div class="tl-date">2009</div><div class="tl-text">Avatar: Cameron hires a professional linguist for Na&rsquo;vi</div></div>
     <div class="tl-item"><div class="tl-date">2011</div><div class="tl-text">Game of Thrones: Peterson selected via LCS competition</div></div>
     <div class="tl-item"><div class="tl-date">Post-2015</div><div class="tl-text">Professional conlanging becomes standard Hollywood practice</div></div>
   </div>`,

  `<p>The most striking feature of media conlangs: they develop <strong>real communities</strong>. KLI for Klingon, LearnNa&rsquo;vi.org for Na&rsquo;vi, Duolingo courses for Valyrian. These communities evolve the languages beyond their creators&rsquo; original scope, echoing natural language dynamics.</p>
   <p>Klingon speakers needed vocabulary for everyday Earth life. Na&rsquo;vi speakers needed words Cameron never imagined. The languages, once released, take on lives of their own.</p>`,

  `<ul class="s-list pro">
     <li>Professional conlanging is now an established career path</li>
     <li>David Peterson is the most prolific working conlanger</li>
     <li>Fan communities are essential to a media conlang&rsquo;s longevity</li>
     <li>Quality has increased dramatically since the 1960s</li>
     <li>Real linguistic knowledge produces better results than ad hoc invention</li>
   </ul>`
]""",
        'details_js': r"""[
  `<div class="detail-header"><div class="num">01</div><h2>Media <em>Conlangs</em></h2></div>
   <h3>Why This Section Matters</h3>
   <p>Media conlangs are the most visible form of conlanging in contemporary culture. More people have heard Klingon or Dothraki than have heard of Esperanto. But they also represent a genuine innovation: the professionalization of a hobby into a career, and the demonstration that audiences can tell the difference between gibberish and a real constructed language.</p>
   <h3>Source Assessment</h3>
   <p>10 sources covering Klingon (Wikipedia, KLI, Marc Okrand interviews), Peterson (Wikipedia, TED Ideas, Babbel interview), Na'vi (Salon, SNExplores, Campfire Writing), and the LCS (conlang.org, Unsung Science). Strong coverage across the major media conlangs and the institutional infrastructure that supports them.</p>`,

  `<div class="detail-header"><div class="num">02</div><h2>Klingon: The Accidental <em>Community</em></h2></div>
   <h3>Design Philosophy</h3>
   <p>Okrand's brief was specific: make the language sound as alien as the Klingons' ridged foreheads. His design choices were deliberately counter-intuitive to English speakers. OVS word order is used by perhaps 1% of the world's languages. The phoneme inventory includes sounds rare in European languages. There is no verb 'to be' in the conventional sense.</p>
   <p>The genius of Klingon was not in its grammar but in its <em>alienness</em>. It sounds wrong to English ears in a specific, consistent way. That consistency is what makes it feel like a real language rather than random sounds.</p>
   <h3>The Community That Nobody Expected</h3>
   <p>When fans started learning Klingon, it was initially a joke. Then it became serious. The KLI certifies proficiency levels. Speakers attend annual conferences (qep'a'). They write original fiction, compose songs, argue politics, and fall in love &mdash; all in Klingon. The community transformed what was designed as a film prop into a living, evolving language.</p>`,

  `<div class="detail-header"><div class="num">03</div><h2>David Peterson: First Full-Time <em>Conlanger</em></h2></div>
   <h3>The New Professional</h3>
   <p>Peterson represents something genuinely new: a person who earns a living solely by creating languages. His career path &mdash; from hobbyist conlanger to LCS competition winner to professional with 40+ credits &mdash; could not have existed before the 2000s. The entertainment industry's growing demand for authentic-sounding alien and fantasy languages created a job that didn't exist before.</p>
   <p>His book, <em>The Art of Language Invention</em> (2015), codified the craft for the first time. It covers phonology, morphology, syntax, and writing systems with examples from his own languages. It is the first professional manual for conlanging.</p>
   <h3>The Valyrian Innovation</h3>
   <p>Peterson's most Tolkien-like achievement is the Valyrian language family: a proto-language (High Valyrian) with multiple daughter languages (Astapori, Meereenese, etc.) showing systematic sound changes and grammatical divergence. This diachronic approach, directly inspired by Tolkien, gives the Game of Thrones world linguistic depth that a single monolithic language could not provide.</p>`,

  `<div class="detail-header"><div class="num">04</div><h2>Na&rsquo;vi: The Linguist&rsquo;s <em>Showcase</em></h2></div>
   <h3>Linguistic Features</h3>
   <p>Na'vi's ejective consonants (sounds made by compressing air in the throat) are common in many non-European languages but startling to English speakers. Cameron specifically wanted the language to feel unfamiliar but beautiful &mdash; a constraint that pushed Frommer toward phonological systems outside the European mainstream.</p>
   <p>The tripartite case alignment (where agents, patients, and intransitive subjects each get different marking) is extremely rare among the world's languages. It makes Na'vi genuinely unusual from a typological perspective, not just from an English-speaker's perspective.</p>
   <p>The infix system &mdash; grammatical modifications inserted <em>inside</em> words rather than added to the beginning or end &mdash; is another typological rarity that gives Na'vi a distinctive feel without making it unpronounceable.</p>`,

  `<div class="detail-header"><div class="num">05</div><h2>The Language Creation <em>Society</em></h2></div>
   <h3>Institutional Impact</h3>
   <p>The LCS's most visible achievement was organizing the competition that selected Peterson for Game of Thrones. But its broader impact is in professionalizing the field: establishing ethical standards for media conlanging, creating publication venues for conlang scholarship, and building a network that connects hobbyist conlangers with industry opportunities.</p>
   <p>The biennial Language Creation Conference (LCC) brings together conlangers from the artistic, media, logical, and programming traditions. It is one of the few venues where these different traditions interact directly.</p>`,

  `<div class="detail-header"><div class="num">06</div><h2>Why Hollywood Hires <em>Conlangers</em></h2></div>
   <h3>The Business Case</h3>
   <p>Four factors drive the shift toward professional conlanging in entertainment:</p>
   <p><strong>Authenticity.</strong> Audiences can distinguish real language from gibberish. Social media means any fakery will be called out immediately.</p>
   <p><strong>Merchandising.</strong> A real language generates books, courses, apps, and fan content. Duolingo's High Valyrian course is a revenue stream that gibberish could never produce.</p>
   <p><strong>Cultural cachet.</strong> Having a &ldquo;real&rdquo; language signals serious worldbuilding. It is a marker of prestige production.</p>
   <p><strong>Fan engagement.</strong> Learning Na'vi or Dothraki extends franchise engagement between releases. It creates a deeper relationship with the fictional world than passive viewing.</p>`,

  `<div class="detail-header"><div class="num">07</div><h2>The Community <em>Phenomenon</em></h2></div>
   <h3>Beyond the Creator's Intent</h3>
   <p>The most striking feature of media conlang communities is how they evolve the languages beyond their creators' original scope. Klingon was designed for warrior dialogue in outer space. Its speakers needed words for ordering coffee, discussing weather, and declaring love. Na'vi was designed for a forest world. Its fans needed vocabulary for Earth concepts Cameron never imagined.</p>
   <p>This process echoes natural language evolution: communities shape languages to meet their communicative needs, regardless of the original designer's intent. It is the strongest evidence that media conlangs, despite their artificial origins, can behave like natural languages once adopted by a community.</p>`,

  `<div class="detail-header"><div class="num">08</div><h2>What Sources <em>Agree On</em></h2></div>
   <h3>Points of Consensus</h3>
   <p>Professional conlanging is here to stay. The entertainment industry has learned that audiences value linguistic authenticity, and the infrastructure (LCS, trained conlangers, industry relationships) now exists to deliver it. Peterson's career proves the business model works. Fan communities prove the cultural model works. The question is no longer <em>whether</em> to hire a conlanger but <em>when</em>.</p>
   <div class="callout"><h4>The Remaining Question</h4><p>Whether any media conlang will achieve the depth of Tolkien's languages remains doubtful. Tolkien worked for fifty years with no deadline. Media conlangers work under production schedules measured in months. The depth gap may be inherent to the medium.</p></div>`
]"""
    },
    's4-relativity': {
        'title_tag': 'S4: Heptapod B &amp; Linguistic Relativity',
        'logo': 'L<em>R</em>',
        'badge': 'CONLANGS &middot; S4 &middot; 10 SOURCES',
        'hero': 'Heptapod B &amp; Linguistic <em>Relativity</em>',
        'subtitle': 'Does the language you speak shape how you think?',
        'sections_js': """[
  { num: '01', short: 'Overview', title: 'Heptapod B &amp; Linguistic <em>Relativity</em>' },
  { num: '02', short: 'Chiang', title: 'Ted Chiang&rsquo;s <em>Story</em>' },
  { num: '03', short: 'Sapir-Whorf', title: 'Strong vs. Weak <em>Whorf</em>' },
  { num: '04', short: 'Color', title: 'Color <em>Perception</em>' },
  { num: '05', short: 'Time & Space', title: 'Time, Space &amp; <em>Causality</em>' },
  { num: '06', short: 'Thought Exp.', title: 'The Conlang as Thought <em>Experiment</em>' },
  { num: '07', short: 'Arrival', title: 'Arrival: The <em>Film</em>' },
  { num: '08', short: 'Consensus', title: 'The Modern <em>Consensus</em>' }
]""",
        'summaries_js': r"""[
  `<p>Does the language you speak shape how you think? This question connects Tolkien (language generates narrative), Chiang (language restructures time perception), Boroditsky (language influences spatial and temporal cognition), and Iverson (notation shapes mathematical thought). The answer: <strong>yes, but less than fiction suggests.</strong></p>
   <div class="s-stat">
     <div class="st"><div class="sv">1998</div><div class="sl">Chiang&rsquo;s novella</div></div>
     <div class="st"><div class="sv">2016</div><div class="sl">Arrival film</div></div>
     <div class="st"><div class="sv">Weak</div><div class="sl">Whorf supported</div></div>
     <div class="st"><div class="sv">Strong</div><div class="sl">Whorf = fiction</div></div>
   </div>`,

  `<p>Ted Chiang&rsquo;s &ldquo;Story of Your Life&rdquo; (1998) is the most intellectually rigorous fictional exploration of the Sapir-Whorf hypothesis. Linguist Louise Banks learns <strong>Heptapod B</strong> &mdash; a semasiographic writing system that represents meaning directly, non-linearly, with no connection to speech.</p>
   <p>As Louise learns Heptapod B, she begins perceiving time non-linearly. Chiang uses <strong>Fermat&rsquo;s principle of least time</strong> as a structural metaphor: just as light &ldquo;knows&rdquo; its endpoint, the heptapods experience all moments as co-present.</p>`,

  `<p>The Sapir-Whorf hypothesis exists on a spectrum. <strong>Strong version</strong> (linguistic determinism): language <em>determines</em> thought. Few linguists support this. <strong>Weak version</strong> (linguistic relativity): language <em>influences</em> thought, making some ideas easier or harder. Substantial evidence supports this.</p>
   <p>Chiang&rsquo;s story deliberately engages the strong version as a thought experiment. This is acknowledged as science fiction, not science. But it raises a genuine question: how far <em>could</em> a radically different language go in reshaping cognition?</p>`,

  `<p>The strongest evidence for linguistic relativity comes from <strong>color perception</strong>. Russian has two basic terms for blue: <em>goluboy</em> (light) and <em>siniy</em> (dark). Russian speakers discriminate between them <strong>significantly faster</strong> than English speakers. fMRI confirms language processing areas activate during the task.</p>
   <p>The Piraha language lacks abstract color terms entirely. Speakers describe colors through comparison. Cross-linguistic studies confirm that color category boundaries vary with language and affect perception speed.</p>`,

  `<p><strong>Lera Boroditsky</strong> (Stanford/UCSD) has demonstrated linguistic effects across multiple domains. Mandarin speakers use vertical metaphors for time and process temporal relationships differently from English speakers. Speakers of Kuuk Thaayorre (which uses absolute directions) maintain constant cardinal direction awareness.</p>
   <p>English emphasizes agents (&ldquo;He broke the vase&rdquo;); Spanish and Japanese omit them. English speakers remember <em>who</em> caused an accident; Spanish speakers remember <em>that</em> it happened.</p>`,

  `<p>Heptapod B is the most sophisticated conlang-as-thought-experiment. But it is not the only one:</p>
   <div class="feat-grid">
     <div class="feat"><h4>Lojban</h4><p>Syntactically unambiguous. Based on predicate logic. Designed to test whether logical language produces logical thinking.</p></div>
     <div class="feat"><h4>Toki Pona</h4><p>~120 root words. Forces decomposition of complex concepts. Users report a meditative, simplifying effect.</p></div>
     <div class="feat"><h4>Ithkuil</h4><p>Ultra-precise. Maximum information in minimum words. So complex even its creator cannot speak it fluently.</p></div>
     <div class="feat"><h4>APL</h4><p>Programming notation that genuinely changes how its users think about computation. Iverson: &ldquo;notation as a tool of thought.&rdquo;</p></div>
   </div>`,

  `<p>Denis Villeneuve&rsquo;s <em>Arrival</em> (2016) made Heptapod B visual: circular ink-splashes (logograms). Jessica Coon (McGill linguist) consulted on linguistic fieldwork accuracy. The film brought linguistic relativity to a mass audience.</p>
   <p>Academic reception was mixed: praised for popularizing linguistics, criticized for implying strong Whorf more literally than evidence supports.</p>`,

  `<p>The current scientific consensus:</p>
   <ul class="s-list pro">
     <li>Language influences perception, memory, and reasoning &mdash; consistently demonstrated</li>
     <li>Effects are real but modest &mdash; language biases cognition without imprisoning it</li>
     <li>Effects strongest when language is actively engaged (verbal interference eliminates them)</li>
     <li>Bayesian framework: language provides default expectations that influence perception under uncertainty</li>
     <li>Strong Whorf remains unsubstantiated as science but powerful as fiction</li>
   </ul>`
]""",
        'details_js': r"""[
  `<div class="detail-header"><div class="num">01</div><h2>Heptapod B &amp; Linguistic <em>Relativity</em></h2></div>
   <h3>Why This Section Matters</h3>
   <p>Linguistic relativity is the thread connecting multiple sections of this survey. Tolkien intuited that language shapes thought: his languages shaped his narratives. Chiang made it explicit with Heptapod B. Boroditsky provided empirical evidence. Iverson argued it for programming. This section synthesizes the evidence and separates science from fiction.</p>
   <h3>Source Assessment</h3>
   <p>10 sources spanning the spectrum from fiction (Chiang's novella, the Arrival film) through linguistic analysis (Emory, McGill, Academia.edu) to empirical research (Winawer et al., Boroditsky, Berkeley computational models). The combination of fiction and science is deliberate: Heptapod B is the most influential fictional engagement with a real scientific hypothesis.</p>`,

  `<div class="detail-header"><div class="num">02</div><h2>Ted Chiang&rsquo;s <em>Story</em></h2></div>
   <h3>The Linguistic Architecture</h3>
   <p>Chiang's design for Heptapod B is extraordinarily precise. It is semasiographic: it represents meaning directly without encoding speech sounds. Its symbols are two-dimensional and must be perceived holistically &mdash; there is no reading direction. A complete Heptapod B sentence is apprehended all at once, like a painting rather than a sentence.</p>
   <p>The connection to time perception is rigorous within the story's logic: if your writing system requires you to know the entire message before you can begin writing it (because the symbols interact holistically), then your cognition must be non-sequential. You must perceive outcomes and intentions simultaneously. This is strong Whorf taken to its logical extreme.</p>
   <h3>Fermat's Principle as Metaphor</h3>
   <p>Chiang uses Fermat's principle of least time (light follows the path that minimizes travel time, implying it "knows" where it's going) as a structural metaphor for heptapod cognition. The heptapods don't predict the future; they experience all moments as co-present, just as light doesn't "choose" the fastest path but simply follows it.</p>`,

  `<div class="detail-header"><div class="num">03</div><h2>Strong vs. Weak <em>Whorf</em></h2></div>
   <h3>The Historical Debate</h3>
   <p>The Sapir-Whorf hypothesis (named after Edward Sapir and Benjamin Lee Whorf) was influential in the mid-20th century, fell out of favor in the Chomskyan era (which emphasized universal grammar over linguistic diversity), and was revived in the 1990s-2000s by researchers like Boroditsky, Levinson, and Lucy.</p>
   <p>The revival was made possible by better experimental methods. Earlier studies tried to prove strong Whorf (impossible, because you can always teach someone a new concept regardless of their language) or disprove any linguistic effect (impossible, because the experimental evidence is now robust). The modern approach asks: <em>how much</em> does language influence thought, in what domains, and through what mechanisms?</p>`,

  `<div class="detail-header"><div class="num">04</div><h2>Color <em>Perception</em></h2></div>
   <h3>The Russian Blues Experiment</h3>
   <p>Winawer et al. (2007) presented Russian and English speakers with triads of blue squares and asked them to identify which two matched. Russian speakers, whose language forces a distinction between goluboy (light blue) and siniy (dark blue), performed the task significantly faster when the squares crossed the goluboy/siniy boundary. English speakers showed no such advantage.</p>
   <p>Critically, the advantage disappeared when subjects performed a concurrent verbal task (counting out loud), but not when they performed a spatial task. This shows that the effect is mediated by language: it requires active engagement of the language faculty, not just passive knowledge of color terms.</p>
   <p>fMRI data confirmed that language-processing brain areas activated during the discrimination task for Russian speakers, providing neuroimaging evidence that language literally participates in visual perception.</p>`,

  `<div class="detail-header"><div class="num">05</div><h2>Time, Space &amp; <em>Causality</em></h2></div>
   <h3>Boroditsky's Research Program</h3>
   <p>Lera Boroditsky has documented linguistic effects across three major cognitive domains, creating the most comprehensive case for weak Whorf in contemporary cognitive science.</p>
   <p><strong>Time:</strong> Mandarin speakers use vertical metaphors for time. When primed with vertical spatial cues, they process temporal relationships faster than when primed horizontally. English speakers show the opposite pattern. Aymara speakers place the past in front (visible, known) and gesture forward when referring to past events.</p>
   <p><strong>Space:</strong> Speakers of Kuuk Thaayorre use absolute directions (north/south/east/west) instead of relative ones (left/right). They maintain constant awareness of cardinal directions and can point north accurately even in unfamiliar buildings. Their spatial cognition is fundamentally restructured by their language.</p>
   <p><strong>Causality:</strong> English emphasizes agents. Spanish and Japanese more readily use agentless constructions. English speakers are more likely to remember who caused an accident; Spanish speakers are more likely to remember it as an event without a specific agent.</p>`,

  `<div class="detail-header"><div class="num">06</div><h2>The Conlang as Thought <em>Experiment</em></h2></div>
   <h3>Beyond Heptapod B</h3>
   <p>Several constructed languages have been explicitly designed to test or explore linguistic relativity, each targeting a different cognitive domain.</p>
   <p><strong>Lojban</strong> tests logical clarity: if every sentence is syntactically unambiguous, does reasoning become more precise? The community is too small for rigorous study, but Lojban speakers report increased awareness of ambiguity in natural language.</p>
   <p><strong>Toki Pona</strong> tests cognitive minimalism: with only ~120 root words, speakers must decompose every complex concept into simple components. Users report a meditative simplification of thought. This is weak Whorf in action: the language doesn't prevent complex thinking but makes simple thinking easier.</p>
   <p><strong>Ithkuil</strong> tests the limits of precision: designed to express maximum information in minimum space, it is so complex that even its creator cannot speak it fluently. It demonstrates that human cognition has limits on how much linguistic precision it can handle in real time.</p>`,

  `<div class="detail-header"><div class="num">07</div><h2>Arrival: The <em>Film</em></h2></div>
   <h3>From Page to Screen</h3>
   <p>Denis Villeneuve's Arrival (2016) faced the challenge of making a fundamentally intellectual story &mdash; about linguistics and the philosophy of time &mdash; work as a mainstream film. The solution: make Heptapod B visual. The film's circular ink-splash logograms, designed by artists Martine Bertrand and Marcus Nispel, became one of the most iconic science fiction designs of the decade.</p>
   <p>Jessica Coon, a syntactician at McGill University, consulted on the film's representation of linguistic fieldwork. Her input shaped the scenes of Louise decoding the alien language, making them the most accurate depiction of field linguistics in any major film.</p>
   <h3>Reception and Criticism</h3>
   <p>The film brought linguistic relativity to a mass audience &mdash; Google searches for "Sapir-Whorf hypothesis" spiked after the film's release. Linguists praised the visibility but debated the accuracy. The film implies a stronger version of linguistic relativity than the evidence supports, but as a thought experiment rather than a science lesson, it succeeds brilliantly.</p>`,

  `<div class="detail-header"><div class="num">08</div><h2>The Modern <em>Consensus</em></h2></div>
   <h3>What We Know</h3>
   <p>The current scientific consensus, synthesized from experimental research across multiple labs and languages:</p>
   <p><strong>1.</strong> Language does influence perception, memory, and reasoning. The evidence is consistent across color, time, space, and causality domains.</p>
   <p><strong>2.</strong> The effects are real but modest. Language biases cognition without imprisoning it. You can always override the bias with explicit effort.</p>
   <p><strong>3.</strong> Effects are strongest when language is actively engaged. Verbal interference (counting aloud) eliminates the Russian blue advantage. The effect requires the language faculty to be online.</p>
   <p><strong>4.</strong> A computational framework (Bayesian priors) explains the mechanism: language provides default expectations that influence perception under conditions of uncertainty. When the signal is clear, language effects diminish. When the signal is ambiguous, language tips the balance.</p>
   <p><strong>5.</strong> Strong Whorf remains unsubstantiated as science but remains a powerful tool for fiction. Heptapod B works as a thought experiment precisely because it takes a real phenomenon to an extreme that reality does not support.</p>
   <div class="callout"><h4>The Implication for Conlangs</h4><p>If weak Whorf is true, then every constructed language &mdash; from Esperanto to APL &mdash; subtly shapes the cognition of its users. The conlang is never just a communication tool. It is always, at some level, a tool of thought.</p></div>`
]"""
    },
    's5-sign': {
        'title_tag': 'S5: Sign Languages &amp; Natural Construction',
        'logo': 'S<em>L</em>',
        'badge': 'CONLANGS &middot; S5 &middot; 8 SOURCES',
        'hero': 'Sign Languages &amp; Natural <em>Construction</em>',
        'subtitle': 'When children in Nicaragua invented a language, they proved something about the human mind',
        'sections_js': """[
  { num: '01', short: 'Overview', title: 'Sign Languages &amp; Natural <em>Construction</em>' },
  { num: '02', short: 'NSL', title: 'Nicaraguan Sign <em>Language</em>' },
  { num: '03', short: 'Evidence', title: 'What NSL <em>Proves</em>' },
  { num: '04', short: 'ABSL', title: 'Al-Sayyid Bedouin Sign <em>Language</em>' },
  { num: '05', short: 'Natural vs MC', title: 'Natural vs. Manually <em>Coded</em>' },
  { num: '06', short: 'Visual Grammar', title: 'The Linguistics of Visual <em>Grammar</em>' },
  { num: '07', short: 'Implications', title: 'Implications for <em>Conlang Theory</em>' }
]""",
        'summaries_js': r"""[
  `<p>This section challenges the entire framing of &ldquo;constructed&rdquo; vs. &ldquo;natural&rdquo; language. Nicaraguan Sign Language and Al-Sayyid Bedouin Sign Language are <strong>natural languages that emerged from scratch</strong>, in observable time, without prior input. They are &ldquo;constructed&rdquo; by their communities in real time &mdash; but no individual designed them.</p>
   <div class="s-stat">
     <div class="st"><div class="sv">~50</div><div class="sl">children who created NSL</div></div>
     <div class="st"><div class="sv">4%</div><div class="sl">deaf in Al-Sayyid (vs 0.1%)</div></div>
     <div class="st"><div class="sv">~75 yrs</div><div class="sl">ABSL development</div></div>
     <div class="st"><div class="sv">150</div><div class="sl">ABSL deaf signers</div></div>
   </div>`,

  `<p>In 1977, Nicaragua opened its first schools for deaf children. Before this, each child had only idiosyncratic &ldquo;home signs.&rdquo; When 50 children were gathered, they <strong>spontaneously created a new language</strong>. First cohort: pidgin. Second cohort: grammatically regular creole. Each subsequent generation added complexity.</p>
   <p>This is the only documented case of a language created from scratch, in observable time, by a community &mdash; without external input, instruction, or design.</p>`,

  `<p>NSL is cited as the <strong>strongest evidence for the language instinct</strong> &mdash; the idea that humans are biologically predisposed to create language.</p>
   <ul class="s-list pro">
     <li>Language emerges without a complete model as input</li>
     <li>Children drive the creolization process &mdash; adults retain the pidgin</li>
     <li>Grammar is not taught &mdash; it emerges from acquisition itself</li>
     <li>Complexity increases with each generation</li>
   </ul>`,

  `<p>A second natural experiment in the Negev desert. Al-Sayyid is a Bedouin village where <strong>4% of the population is deaf</strong> (vs 0.1% typical). A sign language emerged ~75 years ago in near-isolation. Both deaf and hearing residents sign. Word order (SOV) differs from all surrounding languages.</p>
   <p>ABSL provides independent confirmation: given a community with a need to communicate, language emerges. The specific structures differ from NSL, but the process is the same.</p>`,

  `<p>A crucial distinction: <strong>manually coded languages</strong> (Signed English) transliterate a spoken language word-by-word into signs. <strong>Natural sign languages</strong> (ASL, BSL, ISN) have their own grammars, exploit the visual-spatial modality, and are acquired naturally by deaf children.</p>
   <p>Sign languages demonstrate that language is <em>not tied to the vocal-auditory channel.</em> The language faculty operates on whatever modality is available.</p>`,

  `<p>Sign languages exploit their modality in ways spoken languages cannot: <strong>simultaneous expression</strong> (hand shape + movement + location + facial expression at once), <strong>spatial grammar</strong> (referents established in physical space), <strong>classifier predicates</strong> (handshapes depicting object properties), and <strong>iconicity</strong> balanced with arbitrariness.</p>
   <p>ASL poetry uses handshape rhyme, movement rhythm, visual perspective shifts, and spatial metaphor &mdash; artistic expression that exploits the specific properties of the visual medium.</p>`,

  `<p>NSL and ABSL challenge the constructed/natural binary:</p>
   <ul class="s-list">
     <li>A language can emerge naturally without being designed, in an observable timeframe</li>
     <li>The structures that emerge reflect cognitive biases and communicative pressures</li>
     <li>Children are the primary architects of grammatical structure</li>
     <li>A community of 50&ndash;100 people can generate a full language</li>
     <li>Modality (spoken vs. signed) does not constrain structural richness</li>
   </ul>`
]""",
        'details_js': r"""[
  `<div class="detail-header"><div class="num">01</div><h2>Sign Languages &amp; Natural <em>Construction</em></h2></div>
   <h3>Why This Section Matters</h3>
   <p>Every other section in this survey examines languages that were deliberately created by individuals or small groups. This section examines languages that were created by communities without any individual designer. The contrast is revelatory: the most structurally rich and fastest-developing languages in our survey are the ones nobody designed.</p>
   <h3>Source Assessment</h3>
   <p>8 sources spanning Wikipedia for factual grounding, academic research (Senghas & Coppola at Columbia, Sandler et al. at Haifa, NCUR student research), research lab documentation (Haifa University Sign Language Research Lab), and accessible overviews (Serious Science, United Language Group).</p>`,

  `<div class="detail-header"><div class="num">02</div><h2>Nicaraguan Sign <em>Language</em></h2></div>
   <h3>The Natural Experiment</h3>
   <p>The circumstances that created NSL were unique and unrepeatable. Before 1977, deaf Nicaraguans had no shared language. Each child developed idiosyncratic home signs to communicate with hearing family members. When the Sandinista government opened schools for deaf children, bringing 50 children together for the first time, the conditions for language emergence were met: a community with a desperate need to communicate and no prior language model.</p>
   <h3>The Generational Pattern</h3>
   <p>The first cohort (late 1970s-early 1980s) combined their home signs into a pidgin &mdash; functional but grammatically inconsistent. The second cohort (mid-1980s) took this pidgin input and spontaneously restructured it into a grammatically regular system. They introduced consistent word order, morphological marking, and spatial grammar. This is creolization happening in a single generation.</p>
   <p>Each subsequent cohort has added further complexity: more systematic use of space, more regular temporal marking, more productive morphology. The language is becoming more structured, more expressive, and more regular with each generation &mdash; exactly the opposite of what you would expect if language were simply a social convention.</p>`,

  `<div class="detail-header"><div class="num">03</div><h2>What NSL <em>Proves</em></h2></div>
   <h3>The Language Instinct Argument</h3>
   <p>NSL is cited by linguists like Kegl and Senghas as the strongest evidence for the language instinct &mdash; the idea that the human brain is innately predisposed to create and acquire structured language.</p>
   <p>The key observation is that children did something their input could not explain. The first cohort produced a pidgin. The second cohort, whose only input was the pidgin, produced a full language. Where did the grammar come from? The nativist answer: from the children's brains. The grammatical structure was not in the input; it was imposed by the process of acquisition.</p>
   <p>The alternative explanation &mdash; that general cognitive biases rather than language-specific neural architecture drive the regularization &mdash; is debated. But either way, NSL demonstrates that human brains reliably produce structured language given minimal input and a communicative community.</p>`,

  `<div class="detail-header"><div class="num">04</div><h2>Al-Sayyid Bedouin Sign <em>Language</em></h2></div>
   <h3>A Second Data Point</h3>
   <p>ABSL emerged in a completely different context: a small Bedouin community in the Negev desert where hereditary deafness is unusually common (4% vs. 0.1% typical). The community has existed for about 200 years, and ABSL has developed over approximately 75 years.</p>
   <p>ABSL developed with minimal influence from surrounding languages. Its SOV word order differs from Arabic (SVO), Hebrew (SVO), and Israeli Sign Language. This confirms that the structures emerging in new sign languages are not simply borrowed from the surrounding spoken languages &mdash; they arise from the communicative needs of the signing community.</p>
   <h3>Community Integration</h3>
   <p>Unlike many deaf communities, Al-Sayyid's deaf members are fully socially integrated. Marriage between deaf and hearing is common. A significant proportion of hearing community members sign. ABSL is not a minority language within the community; it is a shared medium. This social integration may be one reason the language has developed rapidly &mdash; it has a large, active user base relative to the number of deaf speakers.</p>`,

  `<div class="detail-header"><div class="num">05</div><h2>Natural vs. Manually <em>Coded</em></h2></div>
   <h3>A Critical Distinction</h3>
   <p>Manually coded languages (Signed English, SEE) are artificial systems that transliterate a spoken language word-by-word into manual signs. They are created by hearing educators, learned through instruction, and do not exploit the visual-spatial modality. They are, in fact, constructed languages in the traditional sense &mdash; designed by individuals for a specific purpose.</p>
   <p>Natural sign languages (ASL, BSL, ISN, ABSL) are fundamentally different. They have their own grammars unrelated to the surrounding spoken languages. They exploit simultaneous information channels. They are acquired naturally by deaf children who achieve native-like fluency if exposed early enough. They are full natural languages that happen to use a different modality.</p>
   <p>The distinction matters for conlang theory because it shows that the modality of a language (spoken vs. signed) does not determine its status as natural or artificial. What matters is how it originated: through individual design or through community evolution.</p>`,

  `<div class="detail-header"><div class="num">06</div><h2>The Linguistics of Visual <em>Grammar</em></h2></div>
   <h3>Simultaneity</h3>
   <p>The most distinctive feature of sign language grammar is simultaneity. A signer can convey information through hand shape, hand movement, hand location, facial expression, body tilt, and eye gaze &mdash; all at the same time. Spoken language is largely sequential. Sign language is highly parallel.</p>
   <p>This has profound implications for linguistic theory: it shows that the human language faculty is not inherently sequential. Sequentiality is a property of the vocal-auditory channel, not of language itself.</p>
   <h3>ASL Poetry</h3>
   <p>ASL has developed a rich literary tradition that exploits the visual modality. Rhyme in ASL is based on shared handshapes, movements, or locations rather than shared sounds. Meter involves rhythm of movement and alternation of hands. Visual punning exploits the similarity of signs. The existence of sign language poetry demonstrates that aesthetic expression through language is not dependent on any particular modality.</p>`,

  `<div class="detail-header"><div class="num">07</div><h2>Implications for <em>Conlang Theory</em></h2></div>
   <h3>The Challenge to the Constructed/Natural Binary</h3>
   <p>NSL and ABSL demonstrate that the boundary between constructed and natural language is not a clear line but a gradient. These are natural languages that emerged in observable time without design. Meanwhile, Modern Hebrew was deliberately revived from a liturgical language. Programming languages are designed but evolve organically through community use.</p>
   <p>The implication: what makes a language "natural" is not whether anyone designed it but whether a community uses it for genuine communication and passes it to a new generation. By this criterion, Klingon (with its native-speaking children) is arguably more natural than Interlingua (which exists primarily in writing).</p>
   <div class="callout"><h4>The Deepest Finding</h4><p>The most structurally rich languages in this survey &mdash; NSL and ABSL &mdash; are the ones nobody designed. The language instinct, given a community and a need, produces language that is more complex, more regular, and more expressive than most individual designers achieve. Communities are better language creators than individuals.</p></div>`
]"""
    },
    's6-programming': {
        'title_tag': 'S6: Programming Languages as Conlangs',
        'logo': 'P<em>L</em>',
        'badge': 'CONLANGS &middot; S6 &middot; 8 SOURCES',
        'hero': 'Programming Languages as <em>Conlangs</em>',
        'subtitle': 'Code is language design &mdash; the most successful constructed languages run on silicon',
        'sections_js': """[
  { num: '01', short: 'Overview', title: 'Programming Languages as <em>Conlangs</em>' },
  { num: '02', short: 'APL', title: 'APL: Radical <em>Notation</em>' },
  { num: '03', short: 'Brainfuck', title: 'Brainfuck: Minimalism as <em>Art</em>' },
  { num: '04', short: 'Esolangs', title: 'The Esoteric Language <em>Tradition</em>' },
  { num: '05', short: 'Dijkstra', title: 'Dijkstra vs. Natural Language <em>Programming</em>' },
  { num: '06', short: 'Parallels', title: 'The <em>Parallel</em>' },
  { num: '07', short: 'Regex', title: 'Regex: The Worst <em>Conlang</em>' },
  { num: '08', short: 'Consensus', title: 'What Sources <em>Agree On</em>' }
]""",
        'summaries_js': r"""[
  `<p>Programming languages are constructed languages. They have syntax, semantics, and pragmatics. They are learned, they form communities, and they evolve. Yet the conlang and programming communities <strong>rarely recognize each other</strong>. This section argues that they should.</p>
   <div class="s-stat">
     <div class="st"><div class="sv">1,000+</div><div class="sl">documented esolangs</div></div>
     <div class="st"><div class="sv">8</div><div class="sl">Brainfuck commands</div></div>
     <div class="st"><div class="sv">1962</div><div class="sl">APL published</div></div>
     <div class="st"><div class="sv">1978</div><div class="sl">Dijkstra&rsquo;s critique</div></div>
   </div>`,

  `<p>Kenneth Iverson&rsquo;s <strong>APL</strong> (1962) is the most conlang-like programming language. A custom symbol set requiring a special keyboard. Array-oriented operations. Right-to-left evaluation. Extreme conciseness. His Turing Award lecture: &ldquo;<em>Notation as a Tool of Thought</em>&rdquo; &mdash; a direct application of the Sapir-Whorf hypothesis to programming.</p>
   <p>APL&rsquo;s argument: the notation you use shapes how you think about problems. APL notation makes array insights visible that procedural languages obscure.</p>`,

  `<p>Urban Muller created <strong>Brainfuck</strong> (1993) with a single goal: the smallest possible compiler. Eight commands: <code>&gt; &lt; + - . , [ ]</code>. Turing-complete. Writing even simple programs is agonizing.</p>
   <p>Brainfuck is the purest demonstration that a Turing-complete language can be impossibly minimal. It is a <strong>reductio ad absurdum</strong> of language design and, arguably, art &mdash; a constructed language that deliberately frustrates its users to make a point.</p>`,

  `<p><strong>INTERCAL</strong> (1972) was the first esolang, parodying FORTRAN and COBOL. The tradition that followed:</p>
   <div class="s-chips"><span class="s-chip">Befunge 1993</span><span class="s-chip">Shakespeare 2001</span><span class="s-chip">Piet 2001</span><span class="s-chip">Whitespace 2003</span><span class="s-chip">LOLCODE 2007</span></div>
   <p>Over <strong>1,000 esolangs</strong> documented. They parallel the conlang community: hobbyist creators, shared design challenges, aesthetic standards, appreciation for language design as art.</p>`,

  `<p>Dijkstra (1978): formal symbolism is <strong>essential</strong> to precise thought. Greek mathematics stalled because it was verbal. Natural language programming is a contradiction. Making programming resemble natural language (COBOL) is a step backward.</p>
   <p>Then came LLMs. In 2025-26, people write code by describing what they want in English. Brooker&rsquo;s response: <em>Dijkstra&rsquo;s &ldquo;foolishness&rdquo; has been partially vindicated.</em> But formal languages remain necessary for precision.</p>`,

  `<p>The structural parallels between conlang and programming language communities are striking:</p>
   <div class="feat-grid">
     <div class="feat"><h4>Esperanto &harr; Python</h4><p>Utility-focused, community-driven, pragmatic design philosophy</p></div>
     <div class="feat"><h4>Quenya &harr; Haskell</h4><p>Mathematically beautiful, intellectually deep, relatively few practitioners</p></div>
     <div class="feat"><h4>Klingon &harr; JavaScript</h4><p>Grew wildly beyond original purpose, huge community, messy but alive</p></div>
     <div class="feat"><h4>Volapuk &harr; Failed PLs</h4><p>Destroyed by governance failures and community splits</p></div>
   </div>`,

  `<p>Regular expressions: universally used, universally hated. Syntactically dense to the point of being write-only. Learned by memorizing arcane symbols. Essential despite being terrible.</p>
   <p>Regex is the <strong>Volapuk of programming</strong>: it works, but everyone wishes it were better. Billions of lines of code depend on it. Nobody would design it this way from scratch. It evolved from theory (Chomsky hierarchy) through practice (Unix) into a horrible necessity.</p>`,

  `<ul class="s-list pro">
     <li>Programming languages are designed formal systems with syntax and semantics</li>
     <li>APL demonstrates that notation genuinely shapes thought</li>
     <li>Esolangs parallel conlangs as creative/artistic language design</li>
     <li>The natural language programming debate was transformed by LLMs</li>
     <li>Programming communities mirror conlang communities structurally</li>
   </ul>`
]""",
        'details_js': r"""[
  `<div class="detail-header"><div class="num">01</div><h2>Programming Languages as <em>Conlangs</em></h2></div>
   <h3>Why This Section Matters</h3>
   <p>This section makes an argument that few in either community have made explicitly: programming languages and constructed languages are instances of the same fundamental activity. Both involve designing a formal system for expressing meaning. Both face the same trade-offs between expressiveness and learnability, between elegance and practicality, between creator vision and community adoption.</p>
   <p>The parallels are deep and underexplored. Both communities argue about design philosophy, have holy wars, value elegance, and create things most people will never use. The difference is that programming languages actually achieved what IALs dreamed of: universal adoption of constructed formal systems.</p>
   <h3>Source Assessment</h3>
   <p>8 sources: Wikipedia and Esolang Wiki for factual grounding on esoteric languages, Dijkstra's primary essay (EWD 667), Marc Brooker's 2025 response, The Outline for cultural analysis, and AWWSmm for a survey of unusual languages. The connection between conlangs and programming languages is original analysis rather than established scholarship.</p>`,

  `<div class="detail-header"><div class="num">02</div><h2>APL: Radical <em>Notation</em></h2></div>
   <h3>Notation as a Tool of Thought</h3>
   <p>Iverson's 1979 Turing Award lecture made an argument that directly parallels the Sapir-Whorf hypothesis: the notation you use to express ideas shapes the ideas you can have. APL's array-oriented notation makes certain mathematical insights visible &mdash; patterns in data transformation that procedural languages bury under loops and indices.</p>
   <p>This is weak Whorf applied to programming. APL doesn't prevent you from thinking procedurally (you can always write a loop), but it makes array thinking the path of least resistance. The notation biases cognition toward certain patterns. This is exactly what Boroditsky's research shows for natural languages.</p>
   <h3>The Design Philosophy</h3>
   <p>APL's willingness to depart completely from conventional syntax &mdash; using a unique character set, right-to-left evaluation, and implicit mapping over arrays &mdash; makes it the most conlang-like programming language. It is designed from first principles rather than from convention, just as Tolkien's languages were designed from linguistic principles rather than from existing language patterns.</p>`,

  `<div class="detail-header"><div class="num">03</div><h2>Brainfuck: Minimalism as <em>Art</em></h2></div>
   <h3>The Minimal Language</h3>
   <p>Brainfuck's eight commands implement a Turing machine: move a pointer left/right, increment/decrement a cell, read input, write output, and loop. That's it. It is Turing-complete &mdash; theoretically capable of computing anything. In practice, even "Hello World" requires dozens of cryptic characters.</p>
   <p>Brainfuck is a reductio ad absurdum: it proves that you can build a universal computation system from almost nothing. The question it poses &mdash; what is the minimum required for a language to work? &mdash; is the same question that minimal conlangs like Toki Pona ask. The answer in both domains: less than you think, but at a cost in usability that makes the exercise theoretical.</p>
   <h3>Art Object</h3>
   <p>Brainfuck is used to teach Turing machines, to challenge programmers, and as a starting point for compiler exercises. But it is also, arguably, a work of conceptual art. It is a constructed language that deliberately frustrates its users to make a philosophical point about the relationship between notation and computation. In this, it parallels the most experimental conlangs.</p>`,

  `<div class="detail-header"><div class="num">04</div><h2>The Esoteric Language <em>Tradition</em></h2></div>
   <h3>A Parallel Community</h3>
   <p>The esolang community mirrors the conlang community in striking ways. Both consist of hobbyist creators working primarily for intellectual satisfaction. Both have shared design challenges (How minimal can a language be? How beautiful? How weird?). Both value elegance and ingenuity. Both produce artifacts that most people will never use but that push the boundaries of what language can be.</p>
   <p>Over 1,000 esolangs are documented on the Esolang Wiki. They range from the minimal (Brainfuck, 8 commands) to the visual (Piet, where programs are bitmap images) to the literary (Shakespeare, where programs read as plays) to the absurd (LOLCODE, written in internet cat speak). Each represents a different answer to the question: what can a programming language be?</p>`,

  `<div class="detail-header"><div class="num">05</div><h2>Dijkstra vs. Natural Language <em>Programming</em></h2></div>
   <h3>The 1978 Argument</h3>
   <p>Dijkstra's essay (EWD 667) is one of the most influential critiques of the idea that programming should resemble natural language. His argument: formal symbolism is not a limitation of programming &mdash; it is its greatest strength. The history of science is a history of freeing thought from the imprecision of natural language through formal notation.</p>
   <p>COBOL tried to make programming resemble English. SQL attempted it for databases. AppleScript tried it for automation. None achieved true natural language understanding. The gap between human ambiguity and computational precision seemed permanent.</p>
   <h3>The LLM Reversal</h3>
   <p>In 2025-2026, people routinely write code by describing what they want in natural English. Marc Brooker's response to Dijkstra: natural language programming has been partially achieved, but Dijkstra was right that formal languages remain essential for precision, verification, and debugging. The LLM doesn't eliminate the need for formal programming languages; it provides a natural-language interface to them.</p>`,

  `<div class="detail-header"><div class="num">06</div><h2>The <em>Parallel</em></h2></div>
   <h3>Deep Structural Similarities</h3>
   <p>The parallels between conlang and programming language communities go beyond surface similarity. Both face the same fundamental design tensions: expressiveness vs. learnability, elegance vs. practicality, creator vision vs. community needs. Both have governance challenges (Python's BDFL model, Rust's team model, Java's corporate model). Both experience schisms and forks.</p>
   <p>The deepest parallel: both are engaged in the same fundamental activity &mdash; designing formal systems for expressing meaning. A programming language is a conlang whose audience is a compiler rather than a human listener. An artistic conlang is a programming language whose output is aesthetic experience rather than computation.</p>`,

  `<div class="detail-header"><div class="num">07</div><h2>Regex: The Worst <em>Conlang</em></h2></div>
   <h3>Why Regex Matters</h3>
   <p>Regular expressions deserve special attention because they are the programming world's most widely-used and most universally-despised constructed language. Every programmer encounters regex. Every programmer hates it. Yet billions of lines of production code depend on it.</p>
   <p>Regex is what happens when a theoretical construct (regular languages in the Chomsky hierarchy) becomes a practical tool through decades of accretion rather than deliberate design. It is the Volapuk of programming: successful despite its flaws, surviving because the alternatives are worse, and universally recognized as something nobody would design from scratch.</p>`,

  `<div class="detail-header"><div class="num">08</div><h2>What Sources <em>Agree On</em></h2></div>
   <h3>Points of Consensus</h3>
   <p>The sources converge on five points, though the connection between conlangs and programming languages is drawn more from original analysis than from any single source.</p>
   <p><strong>1.</strong> Programming languages are designed formal systems. They fit the definition of constructed languages.</p>
   <p><strong>2.</strong> APL demonstrates that notation genuinely shapes thought. This is the Sapir-Whorf hypothesis applied to formal systems, and it works.</p>
   <p><strong>3.</strong> Esolangs parallel the conlang tradition as creative, artistic language design.</p>
   <p><strong>4.</strong> The natural language programming debate has been transformed, though not resolved, by LLMs.</p>
   <p><strong>5.</strong> Programming language communities mirror conlang communities in their dynamics, debates, and social structures.</p>
   <div class="callout"><h4>The Provocation</h4><p>By any measure &mdash; speakers, utility, economic impact &mdash; programming languages are the most successful constructed languages ever created. Python has more active users than Esperanto ever dreamed of. The conlang community and the programming language community are engaged in the same activity. They should talk to each other more.</p></div>`
]"""
    }
}

def build_dd(key, cfg):
    title_tag = cfg['title_tag']
    # Replace the title line in the CSS block
    css = css_block.replace(
        '<title>Constructed Languages — Overview Deep Dive</title>',
        '<title>' + title_tag + '</title>'
    )

    js_shell = JS_BOILERPLATE
    js_shell = js_shell.replace('${LOGO}', cfg['logo'])
    js_shell = js_shell.replace('${BADGE}', cfg['badge'])
    js_shell = js_shell.replace('${HERO_TITLE}', cfg['hero'])
    js_shell = js_shell.replace('${SUBTITLE}', cfg['subtitle'])

    html = css + '\n<script>\n'
    html += 'const sections = ' + cfg['sections_js'] + ';\n\n'
    html += 'const summaries = ' + cfg['summaries_js'] + ';\n\n'
    html += 'const details = ' + cfg['details_js'] + ';\n\n'
    html += js_shell + '\n'
    html += '</script>\n</body>\n</html>\n'

    path = os.path.join(BASE, key + '.dd.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Written: {key}.dd.html ({len(html)} chars)')

for key, cfg in SECTIONS.items():
    build_dd(key, cfg)

print('Done! All 6 section deep-dives generated.')
