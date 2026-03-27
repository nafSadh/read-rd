// Build script for s2-s7 deep-dive HTML files
// Run with: node _build-sections.js
const fs = require('fs');
const path = require('path');

// Read the CSS+HTML header from s1 (lines 1-32)
const s1 = fs.readFileSync(path.join(__dirname, 's1-ancient.dd.html'), 'utf8');
const headerEnd = s1.indexOf('<script>');
const footerStart = s1.indexOf('\n// === DOM BUILDING');
const footer = s1.slice(footerStart);

const sectionData = [
  {
    file: 's2-logical.dd.html',
    title: 'S2: Logical Paradoxes — Paradoxes Survey',
    logo: 'S<em>2</em>',
    badge: 'Section 02 · Logical Paradoxes',
    heroTitle: 'Logical <em>Paradoxes</em>',
    subtitle: 'Russell, Gödel, Curry, Grelling-Nelson · 1901–1936 · 9 sources',
    sections: `[
  { num: '01', short: 'Liar', title: 'The Liar <em>Paradox</em>' },
  { num: '02', short: 'Russell', title: "Russell's <em>Paradox</em>" },
  { num: '03', short: 'Crisis', title: 'The Foundational <em>Crisis</em>' },
  { num: '04', short: 'Curry', title: "Curry's <em>Paradox</em>" },
  { num: '05', short: 'Grelling', title: 'Grelling-Nelson &amp; <em>Berry</em>' },
  { num: '06', short: 'Gödel', title: "Gödel's <em>Theorems</em>" },
  { num: '07', short: 'Diagonal', title: 'The Diagonal <em>Pattern</em>' }
]`,
    summaries: `[
  \`<p>"This sentence is false." If true, it's false. If false, it's true. The Liar Paradox, attributed to Eubulides of Miletus around 400 BCE, seems like a verbal trick&mdash;until you realize it sits at the foundation of every logical system that attempts to talk about its own truth. No consistent assignment of truth values is possible.</p>
  <div class="s-stat">
    <div class="st"><div class="sv">~400 BCE</div><div class="sl">Eubulides</div></div>
    <div class="st"><div class="sv">1931</div><div class="sl">Gödel's version</div></div>
    <div class="st"><div class="sv">1936</div><div class="sl">Turing's version</div></div>
  </div>\`,
  \`<p>In 1901, Bertrand Russell discovered that naive set theory&mdash;the foundation Frege had built his life's work upon&mdash;contains a fatal contradiction. Consider the set of all sets that do not contain themselves. Does it contain itself? If yes, then by definition it doesn't. If no, then by definition it does. Russell's letter to Frege left the foundations of mathematics in ruins.</p>
  <ul class="s-list">
    <li><strong>The Barber</strong> &mdash; A barber shaves all and only those who don't shave themselves. Who shaves the barber?</li>
    <li><strong>The Catalog</strong> &mdash; A catalog of all catalogs that don't list themselves. Does it list itself?</li>
    <li><strong>Frege's Response</strong> &mdash; "A scientist can hardly encounter anything more undesirable than to have the foundation give way just as the work is finished"</li>
  </ul>\`,
  \`<p>Russell's paradox triggered a thirty-year crisis in the foundations of mathematics. The response came in three waves: Russell and Whitehead's type theory (Principia Mathematica, 1910&ndash;13), Zermelo and Fraenkel's axiomatic set theory (1908&ndash;22), and Gödel's devastating proof (1931) that no sufficiently powerful formal system can be both complete and consistent.</p>
  <div class="s-stat">
    <div class="st"><div class="sv">1908</div><div class="sl">Zermelo's axioms</div></div>
    <div class="st"><div class="sv">1910</div><div class="sl">Principia begins</div></div>
    <div class="st"><div class="sv">362 pp</div><div class="sl">To prove 1+1=2</div></div>
  </div>\`,
  \`<p>"If this sentence is true, then Santa Claus exists." Curry's paradox (1942) shows that self-reference plus a conditional can prove <em>anything</em>&mdash;without requiring negation. This matters because some proposed solutions to the Liar restrict negation; Curry shows the problem runs deeper. Any system that allows self-referential conditionals is trivial (proves everything) unless it restricts some inference rule.</p>
  <div class="s-chips">
    <span class="s-chip">No negation needed</span><span class="s-chip">Proves anything</span><span class="s-chip">Affects type theory</span><span class="s-chip">Challenges paraconsistency</span>
  </div>\`,
  \`<p>The Grelling-Nelson paradox (1908): "heterological" describes words that don't describe themselves ("long" is not long). Is "heterological" heterological? Berry's paradox: "the smallest integer not definable in under sixty letters" is defined in under sixty letters. Both exploit the same diagonal structure as Russell's paradox, applied to natural language rather than sets.</p>
  <div class="feat-grid">
    <div class="feat"><h4>Grelling-Nelson</h4><p>Autological vs. heterological. Self-describing vs. not-self-describing. Same structure as Russell's, applied to adjectives.</p></div>
    <div class="feat"><h4>Berry's Paradox</h4><p>Definability applied self-referentially. Reveals that "definable" is treacherous when used about itself.</p></div>
  </div>\`,
  \`<p>In 1931, Kurt Gödel proved two theorems that permanently changed our understanding of formal systems. First: any consistent system powerful enough for arithmetic contains true statements it cannot prove. Second: no such system can prove its own consistency. The method was a formalized Liar Paradox: a sentence that says "I am not provable in this system."</p>
  <div class="s-stat">
    <div class="st"><div class="sv">1st</div><div class="sl">Incompleteness</div></div>
    <div class="st"><div class="sv">2nd</div><div class="sl">Consistency</div></div>
    <div class="st"><div class="sv">25</div><div class="sl">Gödel's age</div></div>
  </div>\`,
  \`<p>Every paradox in this section shares Cantor's diagonal structure: construct an object that differs from every item in a list by differing from the nth item in its nth property. The Liar differs from every truth assignment. Russell's set differs from every set regarding self-membership. Gödel's sentence differs from every provable sentence. Turing's halting problem differs from every decidable computation. One pattern, four domains, four impossibility results.</p>
  <div class="s-chips">
    <span class="s-chip">Cantor (1891)</span><span class="s-chip">Russell (1901)</span><span class="s-chip">Gödel (1931)</span><span class="s-chip">Turing (1936)</span><span class="s-chip">One pattern</span>
  </div>\`
]`,
    details: `[
  \`<div class="detail-header"><div class="num"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>Section 01 &mdash; Details</div><h2>The Liar <em>Paradox</em></h2></div>
  <p>The Liar Paradox is the simplest self-referential paradox and the ancestor of all the others. "This sentence is false" cannot be consistently true (it would be false) or consistently false (it would be true). Unlike Epimenides' statement, which can be simply false without contradiction, the Liar creates a genuine logical impossibility.</p>
  <h3>Strengthened Liar</h3>
  <p>Attempts to resolve the Liar by introducing a third truth value ("neither true nor false") are defeated by the Strengthened Liar: "This sentence is not true." If it's neither-true-nor-false, then it's not true, which is exactly what it says&mdash;so it IS true. The strengthened version blocks any finite hierarchy of truth values.</p>
  <h3>Tarski's Hierarchy</h3>
  <p>Alfred Tarski (1933) proposed separating object-language from meta-language. A sentence in language L can only be called "true" or "false" in a meta-language M. The Liar sentence tries to talk about its own truth within the same language, which Tarski's hierarchy forbids. This works formally but seems artificial&mdash;natural languages don't come with built-in hierarchies.</p>\`,
  \`<div class="detail-header"><div class="num"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>Section 02 &mdash; Details</div><h2>Russell's <em>Paradox</em></h2></div>
  <p>In June 1902, Bertrand Russell sent a letter to Gottlob Frege pointing out a contradiction in Frege's Grundgesetze der Arithmetik&mdash;specifically in Axiom V, which allowed unrestricted set comprehension. The contradiction: define R as the set of all sets that are not members of themselves. Is R a member of R? Both answers lead to contradiction.</p>
  <h3>The Barber Formulation</h3>
  <p>Russell popularized the paradox through the Barber: in a village, the barber shaves all and only those men who do not shave themselves. Who shaves the barber? If he shaves himself, he doesn't (by the rule). If he doesn't, he does. The barber formulation is more accessible but loses some mathematical precision&mdash;the "barber" simply cannot exist, while the "set of all non-self-membered sets" seems like it should exist in any reasonable set theory.</p>
  <h3>Frege's Response</h3>
  <p>Frege added an appendix to Volume 2 of Grundgesetze acknowledging the problem. His response showed remarkable intellectual honesty. He attempted a fix (restricting Axiom V), but it was later shown to still be inconsistent. Frege never fully recovered from the blow and published little significant work afterward.</p>
  <div class="callout"><h4>Lawrence Paulson's Revisionism (2024)</h4><p>Paulson argues that the "mythology" around Russell's paradox overstates its impact. Zermelo independently discovered the paradox before Russell and was already developing axioms to handle it. The crisis narrative, while dramatic, may overstate how devastating the paradox actually was to working mathematicians.</p></div>\`,
  \`<div class="detail-header"><div class="num"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>Section 03 &mdash; Details</div><h2>The Foundational <em>Crisis</em></h2></div>
  <p>The foundational crisis of mathematics (Grundlagenkrise der Mathematik) lasted roughly from 1900 to 1930. At stake was whether mathematics could be grounded in logic without contradiction, and whether all mathematical truths could in principle be proved.</p>
  <h3>Three Programs</h3>
  <div class="feat-grid">
    <div class="feat"><h4>Logicism (Frege, Russell)</h4><p>Reduce all mathematics to pure logic. Principia Mathematica attempted this but was defeated by Gödel's incompleteness theorems.</p></div>
    <div class="feat"><h4>Formalism (Hilbert)</h4><p>Treat mathematics as manipulation of formal symbols. Hilbert's program sought a consistency proof for arithmetic. Gödel showed this is impossible within the system.</p></div>
    <div class="feat"><h4>Intuitionism (Brouwer)</h4><p>Mathematics is a mental construction. Reject the law of excluded middle and non-constructive proofs. Mathematically viable but produces a weaker system.</p></div>
    <div class="feat"><h4>The Outcome</h4><p>None of the three programs fully succeeded. Modern mathematics largely uses ZFC set theory as a foundation, accepting Gödel's limits pragmatically.</p></div>
  </div>\`,
  \`<div class="detail-header"><div class="num"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>Section 04 &mdash; Details</div><h2>Curry's <em>Paradox</em></h2></div>
  <p>Haskell Curry discovered in the 1940s that self-referential conditionals can prove any statement without using negation. Consider a sentence X defined as: "If X is true, then Y" (where Y is any statement). Assume X is true. Then "If X is true then Y" is true, and since X is true, Y follows by modus ponens. We've derived Y from the assumption of X, which means "If X then Y" is true&mdash;which IS X. So X is true. Therefore Y.</p>
  <h3>Why This Matters</h3>
  <p>Many proposed solutions to the Liar Paradox work by restricting negation or truth predicates. Curry's paradox shows that self-reference alone, combined with conditional reasoning, is sufficient to trivialize a system. This means the problem is not negation but self-reference itself (or contraction/absorption rules that allow a hypothesis to be used multiple times).</p>
  <h3>Responses</h3>
  <p>Curry-incompleteness: accept that Curry-complete theories are trivial, and restrict self-reference (this is what ZFC does). Curry-completeness: reject some inference rule (typically contraction) to allow self-reference without triviality. This is the approach of some substructural logics.</p>\`,
  \`<div class="detail-header"><div class="num"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>Section 05 &mdash; Details</div><h2>Grelling-Nelson &amp; <em>Berry</em></h2></div>
  <p>Kurt Grelling and Leonard Nelson (1908) defined: an adjective is <em>autological</em> if it describes itself ("short" is short, "English" is English) and <em>heterological</em> if it doesn't ("long" is not long, "French" is not French). Is "heterological" heterological? If yes, it describes itself, making it autological&mdash;contradiction. If no, it doesn't describe itself, making it heterological&mdash;contradiction.</p>
  <h3>Berry's Paradox</h3>
  <p>"The smallest positive integer not definable in fewer than sixty letters." This very phrase defines such an integer in fewer than sixty letters. The paradox reveals that "definable" is not a well-defined predicate when applied self-referentially. Berry's paradox is sometimes dismissed as merely revealing informal language's looseness, but it played a role in the development of algorithmic information theory (Kolmogorov complexity).</p>
  <h3>The Semantic-Set Theory Divide</h3>
  <p>Frank Ramsey (1926) distinguished semantic paradoxes (Liar, Grelling-Nelson, Berry) from set-theoretic paradoxes (Russell, Burali-Forti). Semantic paradoxes involve truth and definability; set-theoretic ones involve membership and size. Both use diagonal self-reference, but they may require different solutions. Tarski's hierarchy addresses the semantic family; ZFC addresses the set-theoretic family.</p>\`,
  \`<div class="detail-header"><div class="num"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>Section 06 &mdash; Details</div><h2>Gödel's <em>Theorems</em></h2></div>
  <p>In 1931, at age 25, Kurt Gödel published "On Formally Undecidable Propositions of Principia Mathematica and Related Systems." The paper contained two theorems that permanently changed the landscape of mathematics and philosophy.</p>
  <h3>First Incompleteness Theorem</h3>
  <p>Any consistent formal system F that can express basic arithmetic contains a sentence G that is true but not provable in F. The sentence G effectively says: "I am not provable in F." If G is provable, then F proves a falsehood (G says it's not provable, but it was proved), making F inconsistent. So G is not provable. But then G is true (it correctly says it's not provable). Therefore F contains a true sentence it cannot prove.</p>
  <h3>Second Incompleteness Theorem</h3>
  <p>No consistent formal system F can prove its own consistency (Cons(F)). The proof uses the First Theorem: if F could prove Cons(F), it could prove G, contradicting the First Theorem. This defeated Hilbert's program, which aimed to prove the consistency of mathematics using finitary methods.</p>
  <h3>The Gödel Numbering Trick</h3>
  <p>Gödel's key technical innovation: assign a unique number to every symbol, formula, and proof in F. Metamathematical statements about provability become arithmetic statements about numbers. The sentence "I am not provable" becomes an arithmetic sentence that F can express. Self-reference is achieved not through informal language but through rigorous number theory.</p>
  <div class="callout"><h4>The Philosophical Import</h4><p>Gödel showed that mathematical truth outruns mathematical proof. No finite set of axioms can capture all mathematical truths. This doesn't mean mathematics is unreliable&mdash;it means mathematics is inexhaustible. There will always be true mathematical statements that require new axioms or methods to prove.</p></div>\`,
  \`<div class="detail-header"><div class="num"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg>Section 07 &mdash; Details</div><h2>The Diagonal <em>Pattern</em></h2></div>
  <p>Georg Cantor (1891) proved that the real numbers are uncountable using a diagonal argument: given any list of real numbers, construct a new number that differs from the nth number in its nth digit. This number is not on the list. The same structural trick underlies every paradox in this section.</p>
  <h3>The Pattern Applied</h3>
  <div class="feat-grid">
    <div class="feat"><h4>Cantor (1891)</h4><p>Given any list of reals, diagonalize to find one not on the list. Proves uncountability.</p></div>
    <div class="feat"><h4>Russell (1901)</h4><p>Given any set-to-boolean mapping, diagonalize via self-membership. Proves naive set theory is inconsistent.</p></div>
    <div class="feat"><h4>Gödel (1931)</h4><p>Given any enumeration of provable sentences, diagonalize to find a true but unprovable one. Proves incompleteness.</p></div>
    <div class="feat"><h4>Turing (1936)</h4><p>Given any algorithm that decides halting, diagonalize to find a program it gets wrong. Proves undecidability.</p></div>
  </div>
  <p>One pattern, discovered in four different contexts over 45 years, each time revealing a fundamental impossibility. The diagonal argument is arguably the most powerful proof technique in the foundations of mathematics and computer science.</p>\`
]`
  },
  // Additional sections follow the same pattern...
];

// Generate each file
for (const s of sectionData) {
  const header = s1.slice(0, headerEnd).replace(
    '<title>S1: Ancient Paradoxes — Paradoxes Survey</title>',
    `<title>${s.title}</title>`
  );

  const content = `${header}<script>
const sections = ${s.sections};
const summaries = ${s.summaries};
const details = ${s.details};

// === DOM BUILDING (shared template) ===
const shell = document.createElement('div');
shell.className = 'shell';
shell.innerHTML = \`
  <div class="ctrl-group" id="ctrl-group">
    <button class="ctrl-btn theme-btn" onclick="toggleTheme()"></button>
    <button class="ctrl-btn detail-btn" id="detail-btn" onclick="toggleDetail()">
      <span class="icon-open"><svg width="16" height="16" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg></span>
      <span class="icon-close"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><line x1="6.5" y1="4" x2="13" y2="4"/><line x1="3" y1="8" x2="13" y2="8"/><line x1="6.5" y1="12" x2="13" y2="12"/></svg></span>
    </button>
  </div>
  <nav class="sidebar" id="sidebar">
    <div class="sidebar-head"><div class="sidebar-logo">${s.logo}</div></div>
    <div class="sidebar-nav" id="sidebar-nav"></div>
  </nav>
  <div class="main" id="main">
    <div class="main-head">
      <div class="main-head-inner">
        <div class="hero-badge"><span class="dot"></span> ${s.badge}</div>
        <div class="hero-title">${s.heroTitle}</div>
        <div class="masthead-rule"></div>
        <div class="masthead-sub"><span>${s.subtitle}</span></div>
      </div>
    </div>
    <div class="main-scroll" id="main-scroll"></div>
  </div>
  <div class="right closed" id="right">
    <div class="right-topbar"><span class="sticky-title" id="right-sticky-title"></span></div>
    <div class="right-inner" id="right-inner"></div>
  </div>
\`;
document.body.appendChild(shell);

const sidebarNav = document.getElementById('sidebar-nav');
sections.forEach((sec, idx) => {
  const item = document.createElement('div');
  item.className = 'sidebar-item' + (idx === 0 ? ' active' : '');
  item.setAttribute('data-label', sec.short);
  item.innerHTML = \\\`<span class="sidebar-num">\\\${sec.num}</span><span class="sidebar-label">\\\${sec.short}</span>\\\`;
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
  block.innerHTML = \\\`<div class="s-num"><span>\\\${sec.num}</span><button class="s-detail-btn" onclick="openDetail(\\\${idx})"><svg width="14" height="14" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="1" width="10" height="10" rx="1.5"/><line x1="3.5" y1="4" x2="8.5" y2="4"/><line x1="3.5" y1="6" x2="8.5" y2="6"/><line x1="3.5" y1="8" x2="6.5" y2="8"/></svg></button></div><h2>\\\${sec.title}</h2>\\\${summaries[idx]}\\\`;
  mainInner.appendChild(block);
});
const rightInner = document.getElementById('right-inner');
sections.forEach((sec, idx) => {
  const d = document.createElement('div');
  d.className = 'detail';
  d.id = 'detail-' + idx;
  d.innerHTML = details[idx];
  rightInner.appendChild(d);
});
let lastDetailIdx = 0;
function scrollToSection(idx) { const blocks = document.querySelectorAll('.section-block'); if (blocks[idx]) blocks[idx].scrollIntoView({behavior:'smooth',block:'start'}); }
function openDetail(idx) { lastDetailIdx = idx; document.querySelectorAll('.detail').forEach(d => d.style.display = 'none'); document.getElementById('detail-' + idx).style.display = 'block'; document.getElementById('right').classList.remove('closed'); document.body.classList.add('detail-open'); document.getElementById('right').scrollTop = 0; document.getElementById('right-sticky-title').classList.remove('visible'); }
function closeRight() { document.getElementById('right').classList.add('closed'); document.body.classList.remove('detail-open'); }
function toggleDetail() { if (document.body.classList.contains('detail-open')) closeRight(); else openDetail(lastDetailIdx); }
function toggleTheme() { const c = document.body.getAttribute('data-theme'); const n = c === 'light' ? 'dark' : 'light'; document.body.setAttribute('data-theme', n); localStorage.setItem('theme', n); }
const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);
mainScroll.addEventListener('scroll', () => { document.querySelector('.main-head').classList.toggle('compact', mainScroll.scrollTop > 40); const blocks = mainScroll.querySelectorAll('.section-block'); const items = document.querySelectorAll('.sidebar-item'); let ai = 0; blocks.forEach((b, i) => { if (b.getBoundingClientRect().top < mainScroll.getBoundingClientRect().top + 120) ai = i; }); items.forEach((item, i) => item.classList.toggle('active', i === ai)); });
const rightPanelOuter = document.getElementById('right');
const stickyTitle = document.getElementById('right-sticky-title');
rightPanelOuter.addEventListener('scroll', () => { const ad = rightPanelOuter.querySelector('.detail[style*="display: block"], .detail[style*="display:block"]'); if (!ad) return; const h2 = ad.querySelector('.detail-header h2') || ad.querySelector('h2'); if (!h2) return; const r = h2.getBoundingClientRect(); const pr = rightPanelOuter.getBoundingClientRect(); const tb = document.querySelector('.right-topbar'); if (r.bottom < pr.top + 56) { stickyTitle.textContent = h2.textContent; stickyTitle.classList.add('visible'); tb.classList.add('scrolled'); } else { stickyTitle.classList.remove('visible'); tb.classList.remove('scrolled'); } });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeRight(); });
</script>
</body>
</html>`;

  fs.writeFileSync(path.join(__dirname, s.file), content, 'utf8');
  console.log(`Written: ${s.file}`);
}

console.log('Done!');
