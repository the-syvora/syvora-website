/* Syvora Build Estimator. Pure client-side. Ranges consistent with /guides/. */
(function () {
  var d = document, root = d.getElementById('est');
  if (!root) return;

  var CFG = {
    webapp: { name: 'Web Application', base: [45, 75], weeks: [6, 10], guide: '/guides/web-application-development-cost/',
      qs: [
        { id: 'roles', label: 'User model', opts: [
          ['Single role', 0, 0, 0, 0], ['Multi-role with permissions', 15, 30, 1, 2], ['Multi-tenant SaaS', 30, 55, 2, 4]]},
        { id: 'realtime', label: 'Realtime needs', opts: [
          ['None', 0, 0, 0, 0], ['Live updates and notifications', 10, 20, 1, 1], ['Collaborative editing', 25, 45, 2, 3]]},
        { id: 'integr', label: 'External integrations', opts: [
          ['0 to 1', 0, 0, 0, 0], ['2 to 4', 10, 22, 1, 1], ['5 or more', 24, 45, 2, 3]]},
        { id: 'data', label: 'Data and reporting', opts: [
          ['Standard CRUD', 0, 0, 0, 0], ['Analytics and dashboards', 12, 25, 1, 2], ['Audit trails and compliance', 15, 30, 1, 2]]},
        { id: 'design', label: 'Design starting point', opts: [
          ['Design system exists', 0, 0, 0, 0], ['Design from scratch', 10, 22, 1, 2]]}
      ]},
    mobile: { name: 'Mobile App', base: [55, 85], weeks: [8, 12], guide: '/guides/mobile-app-development-cost/',
      qs: [
        { id: 'offline', label: 'Offline behavior', opts: [
          ['Online only', 0, 0, 0, 0], ['Offline cache', 12, 22, 1, 1], ['Offline-first with sync', 28, 50, 2, 3]]},
        { id: 'native', label: 'Native surface area', opts: [
          ['Standard UI', 0, 0, 0, 0], ['Camera, push, location', 8, 16, 0, 1], ['Payments, biometrics, background', 18, 35, 1, 2]]},
        { id: 'backend', label: 'Backend', opts: [
          ['API already exists', 0, 0, 0, 0], ['Build the API too', 20, 40, 2, 3]]},
        { id: 'design', label: 'Design starting point', opts: [
          ['Design system exists', 0, 0, 0, 0], ['Design from scratch', 10, 20, 1, 2]]}
      ]},
    shopify: { name: 'Shopify App', base: [16, 26], weeks: [4, 6], guide: '/guides/shopify-app-development-cost/',
      qs: [
        { id: 'dist', label: 'Distribution', opts: [
          ['Custom app, one store', 0, 0, 0, 0], ['Public App Store app', 12, 20, 1, 2]]},
        { id: 'surface', label: 'Surfaces', opts: [
          ['Admin only', 0, 0, 0, 0], ['Admin plus theme embed', 6, 12, 1, 1], ['Admin plus checkout extension', 10, 18, 1, 2]]},
        { id: 'sync', label: 'Data sync', opts: [
          ['Light', 0, 0, 0, 0], ['Heavy webhooks and bulk ops', 10, 22, 1, 2]]}
      ]},
    contracts: { name: 'Smart Contract Protocol', base: [0, 0], weeks: [0, 0], guide: '/guides/defi-protocol-development-cost/',
      qs: [
        { id: 'mech', label: 'Mechanism', opts: [
          ['Token plus vesting', 30, 50, 6, 9], ['Fork of proven mechanics', 70, 120, 8, 12], ['Novel mechanism', 130, 230, 12, 18]]},
        { id: 'audit', label: 'Audit tier', opts: [
          ['Readiness pass only', 10, 20, 1, 1], ['Boutique firm audit', 18, 40, 2, 3], ['Top-tier firm audit', 60, 120, 3, 4]]},
        { id: 'offchain', label: 'Off-chain scope', opts: [
          ['Contracts only', 0, 0, 0, 0], ['Frontend plus indexing', 35, 80, 3, 5]]},
        { id: 'chains', label: 'Chains at launch', opts: [
          ['One chain', 0, 0, 0, 0], ['Two to three', 18, 40, 1, 2], ['Four or more', 45, 90, 2, 4]]}
      ]},
    token: { name: 'Token Launch', base: [45, 70], weeks: [8, 12], guide: '/guides/token-launch-cost/',
      qs: [
        { id: 'scope', label: 'On-chain scope', opts: [
          ['Token, vesting, distribution', 0, 0, 0, 0], ['Plus staking or governance', 25, 55, 2, 3]]},
        { id: 'audit', label: 'Audit tier', opts: [
          ['Boutique firm', 18, 40, 2, 3], ['Top-tier firm', 60, 120, 3, 4]]},
        { id: 'infra', label: 'Launch infrastructure', opts: [
          ['Minimal', 0, 0, 0, 0], ['Claims site, liquidity ops, multisig ceremony', 15, 30, 1, 2]]}
      ]},
    servicenow: { name: 'ServiceNow Implementation', base: [85, 150], weeks: [8, 12], guide: '/guides/servicenow-implementation-cost/',
      multi: { id: 'modules', label: 'Beyond core ITSM (select all that apply)', opts: [
        ['ITOM and CMDB', 40, 80, 3, 5], ['HRSD or CSM', 50, 90, 3, 5], ['Custom scoped app', 30, 60, 3, 4]]},
      qs: [
        { id: 'integr', label: 'Integrations', opts: [
          ['One to two', 0, 0, 0, 0], ['Three to five', 20, 45, 1, 2], ['Six or more', 45, 90, 2, 4]]},
        { id: 'migr', label: 'Data migration', opts: [
          ['Light', 0, 0, 0, 0], ['Heavy legacy migration', 15, 35, 1, 2]]}
      ]},
    ai: { name: 'AI Automation', base: [18, 32], weeks: [3, 5], guide: null,
      qs: [
        { id: 'rag', label: 'Knowledge retrieval', opts: [
          ['Not needed', 0, 0, 0, 0], ['RAG over your corpus', 18, 40, 2, 3]]},
        { id: 'agents', label: 'Workflow shape', opts: [
          ['Linear automation', 0, 0, 0, 0], ['Agentic with human approval gates', 22, 50, 2, 4]]},
        { id: 'integr', label: 'Systems connected', opts: [
          ['One to two', 0, 0, 0, 0], ['Three to five', 10, 22, 0, 1], ['Six or more', 22, 45, 1, 2]]},
        { id: 'eval', label: 'Evaluation rigor', opts: [
          ['Basic checks', 0, 0, 0, 0], ['Full evaluation harness', 10, 20, 1, 1]]}
      ]}
  };
  var TYPE_LABELS = [['webapp','Web Application','SYV-02'],['mobile','Mobile App','SYV-04'],['shopify','Shopify App','SYV-02'],
    ['contracts','Smart Contract Protocol','SYV-01'],['token','Token Launch','SYV-01'],['servicenow','ServiceNow','SYV-03'],['ai','AI Automation','SYV-04']];

  var state = load() || { step: 0, type: null, ans: {}, mods: [], eng: 'fixed', speed: 'standard' };

  function save() { try { localStorage.setItem('syv-est-v1', JSON.stringify(state)); } catch (e) {} }
  function load() { try { return JSON.parse(localStorage.getItem('syv-est-v1')); } catch (e) { return null; } }
  function K(n) { return '$' + (Math.round(n / 5) * 5) + 'K'; }

  function calc() {
    var c = CFG[state.type], lo = c.base[0], hi = c.base[1], wlo = c.weeks[0], whi = c.weeks[1];
    var items = [];
    if (c.base[1] > 0) items.push(['Base build: ' + c.name, c.base[0], c.base[1]]);
    c.qs.forEach(function (q) {
      var i = state.ans[q.id] || 0, o = q.opts[i];
      lo += o[1]; hi += o[2]; wlo += o[3]; whi += o[4];
      if (o[1] > 0) items.push([q.label + ': ' + o[0], o[1], o[2]]);
    });
    if (c.multi) c.multi.opts.forEach(function (o, i) {
      if (state.mods.indexOf(i) > -1) { lo += o[1]; hi += o[2]; wlo += o[3]; whi += o[4]; items.push([o[0], o[1], o[2]]); }
    });
    if (state.speed === 'fast') { items.push(['Compressed timeline: parallel staffing', Math.round(lo * .12), Math.round(hi * .12)]); lo *= 1.12; hi *= 1.12; wlo = Math.max(2, Math.round(wlo * .75)); whi = Math.max(3, Math.round(whi * .75)); }
    var mid = (lo + hi) / 2, pod;
    if (mid < 60) pod = ['1 senior engineer', '1 lead (fractional)', 'Designer (fractional)'];
    else if (mid < 150) pod = ['2 to 3 senior engineers', '1 engineering lead', '1 designer'];
    else if (mid < 300) pod = ['3 to 4 senior engineers', '1 engineering lead', '1 designer', 'QA engineer'];
    else pod = ['5 to 6 senior engineers', '1 engineering lead', '1 designer', 'QA engineer', 'Delivery manager'];
    if (state.type === 'contracts' || state.type === 'token') pod[0] = pod[0].replace('senior engineer', 'protocol engineer') + ' plus security reviewer';
    if (state.type === 'servicenow') pod = pod.map(function (x) { return x.replace('engineer', 'certified consultant'); });
    return { lo: lo, hi: hi, wlo: wlo, whi: whi, items: items, pod: pod };
  }

  function seg(label, opts, sel, onpick, hint) {
    var h = '<div class="est-q"><div class="est-l">' + label + (hint ? ' <em>' + hint + '</em>' : '') + '</div><div class="segs-btn">';
    opts.forEach(function (o, i) {
      h += '<button type="button" class="segb' + (sel === i || (Array.isArray(sel) && sel.indexOf(i) > -1) ? ' on' : '') + '" data-k="' + onpick + '" data-i="' + i + '">' + o[0] +
        (o[1] > 0 ? '<span>+' + K(o[1]) + ' to ' + K(o[2]) + '</span>' : '<span>included</span>') + '</button>';
    });
    return h + '</div></div>';
  }

  function render() {
    var h = '<div class="est-prog mono">STEP 0' + (state.step + 1) + ' / 04' +
      (state.step > 0 ? ' · ' + CFG[state.type].name.toUpperCase() : '') + '</div>';
    if (state.step === 0) {
      h += '<h3 class="est-h">What are we scoping?</h3><div class="est-types">';
      TYPE_LABELS.forEach(function (t) {
        h += '<button type="button" class="est-type' + (state.type === t[0] ? ' on' : '') + '" data-type="' + t[0] + '">' +
          '<span class="mono">' + t[2] + '</span><b>' + t[1] + '</b></button>';
      });
      h += '</div>';
    } else if (state.step === 1) {
      var c = CFG[state.type];
      h += '<h3 class="est-h">Scope the build.</h3>';
      c.qs.forEach(function (q) { h += seg(q.label, q.opts, state.ans[q.id] || 0, 'q:' + q.id); });
      if (c.multi) h += seg(c.multi.label, c.multi.opts, state.mods, 'multi', null);
    } else if (state.step === 2) {
      h += '<h3 class="est-h">Delivery context.</h3>';
      h += '<div class="est-q"><div class="est-l">Engagement shape</div><div class="segs-btn">' +
        '<button type="button" class="segb' + (state.eng === 'fixed' ? ' on' : '') + '" data-k="eng" data-i="fixed">Fixed scope<span>spec, price, date in writing</span></button>' +
        '<button type="button" class="segb' + (state.eng === 'pod' ? ' on' : '') + '" data-k="eng" data-i="pod">Dedicated pod<span>monthly run rate, roadmap owned together</span></button></div></div>';
      h += '<div class="est-q"><div class="est-l">Timeline pressure</div><div class="segs-btn">' +
        '<button type="button" class="segb' + (state.speed === 'standard' ? ' on' : '') + '" data-k="speed" data-i="standard">Standard<span>included</span></button>' +
        '<button type="button" class="segb' + (state.speed === 'fast' ? ' on' : '') + '" data-k="speed" data-i="fast">Compressed<span>+12% for parallel staffing</span></button></div></div>';
    } else {
      var r = calc(), c2 = CFG[state.type];
      var run = state.eng === 'pod' ? '<div class="est-note mono">POD RUN RATE ≈ ' + K((r.lo + r.hi) / 2 / ((r.wlo + r.whi) / 2) * 4.33) + ' / MONTH AT MIDPOINT</div>' : '';
      h += '<div id="est-report"><div class="rep-head"><div><span class="mono rep-code">SYV-EST-2026</span>' +
        '<h3 class="est-h">' + c2.name + ' estimate.</h3></div>' +
        '<div class="est-big"><b>' + K(r.lo) + ' to ' + K(r.hi) + '</b><span class="mono">' + r.wlo + ' TO ' + r.whi + ' WEEKS</span></div></div>';
      h += '<table class="est-table"><thead><tr><th>Line item</th><th>Range</th></tr></thead><tbody>';
      r.items.forEach(function (it) { h += '<tr><td>' + it[0] + '</td><td class="mono">' + K(it[1]) + ' to ' + K(it[2]) + '</td></tr>'; });
      h += '</tbody></table>' + run;
      h += '<div class="est-cols"><div><div class="est-l">Suggested pod</div><ul class="est-pod">' +
        r.pod.map(function (p) { return '<li>' + p + '</li>'; }).join('') + '</ul></div>' +
        '<div><div class="est-l">AIgile phases</div><ul class="est-pod">' +
        '<li>Analyze · ' + Math.max(1, Math.round(r.wlo * .15)) + ' wk</li><li>Build · ' + Math.round(r.wlo * .55) + ' to ' + Math.round(r.whi * .55) + ' wk</li>' +
        '<li>Launch · ' + Math.max(1, Math.round(r.wlo * .15)) + ' wk</li><li>Optimize · ongoing</li></ul></div></div>';
      h += '<p class="est-fine">Indicative range for senior, production-grade delivery, consistent with our published cost guides' +
        (c2.guide ? ' (<a href="' + c2.guide + '">see the full guide</a>)' : '') + '. A written Syvora quote is specific to your scope and locked once specced.</p></div>';
      h += '<div class="est-actions no-print"><a class="btn primary" target="_blank" rel="noopener" href="https://calendly.com/majid-khan-syvora/30min"><span class="tick"></span>Book a call with this estimate</a>' +
        '<button type="button" class="btn" id="est-print"><span class="tick"></span>Download as PDF</button>' +
        '<button type="button" class="btn" id="est-copy"><span class="tick"></span>Copy summary</button></div>';
    }
    h += '<div class="est-nav no-print">' +
      (state.step > 0 ? '<button type="button" class="btn" id="est-back"><span class="tick"></span>Back</button>' : '<span></span>') +
      (state.step < 3 ? '<button type="button" class="btn primary" id="est-next"' + (state.step === 0 && !state.type ? ' disabled' : '') + '><span class="tick"></span>' + (state.step === 2 ? 'See estimate' : 'Continue') + '</button>' : '<button type="button" class="btn" id="est-reset"><span class="tick"></span>Start over</button>') + '</div>';
    root.innerHTML = h;
    save();
  }

  root.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.dataset.type) { state.type = b.dataset.type; state.ans = {}; state.mods = []; render(); return; }
    if (b.dataset.k) {
      var k = b.dataset.k;
      if (k === 'multi') { var i = +b.dataset.i, x = state.mods.indexOf(i); x > -1 ? state.mods.splice(x, 1) : state.mods.push(i); }
      else if (k === 'eng' || k === 'speed') state[k] = b.dataset.i;
      else state.ans[k.slice(2)] = +b.dataset.i;
      render(); return;
    }
    if (b.id === 'est-next') { state.step++; render(); window.scrollTo({ top: root.offsetTop - 90, behavior: 'smooth' }); }
    if (b.id === 'est-back') { state.step--; render(); }
    if (b.id === 'est-reset') { state = { step: 0, type: null, ans: {}, mods: [], eng: 'fixed', speed: 'standard' }; render(); }
    if (b.id === 'est-print') window.print();
    if (b.id === 'est-copy') {
      var r = calc(), c = CFG[state.type];
      var txt = 'Syvora estimate (SYV-EST-2026)\n' + c.name + ': ' + K(r.lo) + ' to ' + K(r.hi) + ', ' + r.wlo + ' to ' + r.whi + ' weeks\n' +
        r.items.map(function (i) { return '- ' + i[0] + ': ' + K(i[1]) + ' to ' + K(i[2]); }).join('\n') +
        '\nBook: https://calendly.com/majid-khan-syvora/30min';
      navigator.clipboard.writeText(txt).then(function () { b.querySelector('.tick').style.background = '#19c37d'; });
    }
  });
  render();
})();
