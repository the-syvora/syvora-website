/* Syvora Vendor Due Diligence Scorecard. Pure client-side. */
(function () {
  var d = document, root = d.getElementById('vds');
  if (!root) return;
  var CRIT = [
    ['Delivery', ['Will show working software weekly, not status decks',
      'First demo committed within three weeks of kickoff',
      'Puts spec, price, and date in writing for scopeable work']],
    ['Team', ['Names the actual engineers before the contract is signed',
      'The people who pitched are the people who build',
      'Average engineer seniority is stated and verifiable']],
    ['Transparency', ['Reports scope and burn honestly every week',
      'Decisions and trade-offs are documented, not just made',
      'Will recommend against work that does not serve you']],
    ['Security & Ownership', ['You own all code and infrastructure from day one',
      'NDA-first and clean handling of credentials and access',
      'Security practices are described concretely, not as a badge wall']],
    ['Commercial', ['Pricing model is flat and predictable, not meter-based surprise',
      'Replacement or exit terms are defined and painless',
      'Post-launch support exists with real SLAs, not best effort']]
  ];
  var state = load() || { names: ['Vendor A', 'Syvora', ''], s: {} };
  function load() { try { return JSON.parse(localStorage.getItem('syv-vds-v1')); } catch (e) { return null; } }
  function save() { try { localStorage.setItem('syv-vds-v1', JSON.stringify(state)); } catch (e) {} }
  function active() { return state.names.map(function (n, i) { return [n, i]; }).filter(function (x) { return x[0].trim(); }); }
  function render() {
    var act = active(), MAX = 15 * 3;
    var h = '<div class="vds-names no-print"><div class="est-l">Vendors (leave a name blank to hide the column)</div><div class="vds-inputs">';
    state.names.forEach(function (n, i) {
      h += '<input type="text" maxlength="18" value="' + n.replace(/"/g, '') + '" data-n="' + i + '" placeholder="Vendor ' + (i + 1) + '">';
    });
    h += '</div></div>';
    h += '<div id="vds-report"><div class="rep-head"><div><span class="mono rep-code">SYV-VDS-2026</span>' +
      '<h3 class="est-h">Vendor due diligence.</h3></div></div>';
    h += '<table class="est-table vds-table"><thead><tr><th>Criterion · score 0 to 3</th>' +
      act.map(function (a) { return '<th>' + a[0] + '</th>'; }).join('') + '</tr></thead><tbody>';
    CRIT.forEach(function (cat, ci) {
      h += '<tr class="vds-cat"><td colspan="' + (act.length + 1) + '" class="mono">' + cat[0].toUpperCase() + '</td></tr>';
      cat[1].forEach(function (q, qi) {
        h += '<tr><td>' + q + '</td>' + act.map(function (a) {
          var k = ci + '-' + qi + '-' + a[1], v = state.s[k];
          return '<td class="vds-cell">' + [0, 1, 2, 3].map(function (n) {
            return '<button type="button" class="vds-dot' + (v === n ? ' on' : '') + '" data-k="' + k + '" data-v="' + n + '" aria-label="' + n + '">' + n + '</button>';
          }).join('') + '</td>';
        }).join('') + '</tr>';
      });
    });
    var totals = act.map(function (a) {
      var t = 0; CRIT.forEach(function (cat, ci) { cat[1].forEach(function (_, qi) { t += state.s[ci + '-' + qi + '-' + a[1]] || 0; }); });
      return t;
    });
    h += '<tr class="vds-total"><td class="mono">TOTAL / ' + MAX + '</td>' + totals.map(function (t) {
      return '<td class="mono"><b>' + t + '</b></td>';
    }).join('') + '</tr></tbody></table>';
    var best = Math.max.apply(null, totals.concat(0));
    if (best > 0) {
      var lead = act[totals.indexOf(best)][0];
      h += '<p class="est-fine">Leading: <b>' + lead + '</b> at ' + best + '/' + MAX +
        '. Anything under 2 on Delivery or Transparency is a future incident wearing a proposal. These fifteen criteria are the promises we make in writing; score us against them on a call.</p>';
    }
    h += '</div><div class="est-actions no-print">' +
      '<a class="btn primary" target="_blank" rel="noopener" href="https://calendly.com/majid-khan-syvora/30min"><span class="tick"></span>Score Syvora live</a>' +
      '<button type="button" class="btn" id="vds-print"><span class="tick"></span>Download comparison</button>' +
      '<button type="button" class="btn" id="vds-reset"><span class="tick"></span>Reset</button></div>';
    root.innerHTML = h;
    save();
  }
  root.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.dataset.k) { state.s[b.dataset.k] = +b.dataset.v; render(); return; }
    if (b.id === 'vds-print') window.print();
    if (b.id === 'vds-reset') { state = { names: ['Vendor A', 'Syvora', ''], s: {} }; render(); }
  });
  root.addEventListener('input', function (e) {
    if (e.target.dataset.n !== undefined) { state.names[+e.target.dataset.n] = e.target.value; save(); }
  });
  root.addEventListener('change', function (e) { if (e.target.dataset.n !== undefined) render(); });
  render();
})();
