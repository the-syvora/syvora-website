/* Syvora Audit Readiness Scorecard. Pure client-side. */
(function () {
  var d = document, root = d.getElementById('ars');
  if (!root) return;
  var CATS = [
    ['Specification & Docs', [
      ['A written technical spec exists and matches the current code', 'Write or update the spec before outreach; auditors bill orientation hours otherwise.'],
      ['Every external and public function has NatSpec documentation', 'Add NatSpec across the external surface; it is the map auditors read first.'],
      ['Trust assumptions and privileged roles are documented in one place', 'Create a TRUST.md listing roles, powers, and oracle assumptions.']]],
    ['Testing', [
      ['Unit test coverage exists for every state-changing function', 'Close the coverage gaps on state-changing paths before anything else.'],
      ['Fork tests run against mainnet state for integrations', 'Add fork tests for every external protocol you touch.'],
      ['CI runs the full suite on every commit', 'Wire the suite into CI; green-on-main is table stakes for firms.']]],
    ['Fuzzing & Invariants', [
      ['Invariant tests assert conservation and accounting properties', 'Write invariants for fund conservation and share accounting; this is where deep bugs die.'],
      ['Fuzz campaigns run with meaningful runs and depth', 'Stand up Foundry fuzzing with configured depth, not defaults.'],
      ['Known past findings have regression tests', 'Convert every past finding into a permanent regression test.']]],
    ['Access Control & Upgrades', [
      ['Privileged functions are behind multisig, not EOAs', 'Move admin powers to a multisig before the audit, not after.'],
      ['Timelocks cover user-affecting parameter changes', 'Add timelocks so users can react to changes; firms flag its absence.'],
      ['Upgradeability is deliberate, documented, and tested', 'Decide and document the upgrade story; test the upgrade path itself.']]],
    ['Deployment & Ops', [
      ['Deploy scripts are deterministic and reviewed', 'Script deployments end to end; manual deploys are findings waiting to happen.'],
      ['Source is verified on explorers for existing deployments', 'Verify all deployed source; unverified contracts stall reviews.'],
      ['Monitoring and alerting exist for critical invariants', 'Stand up invariant monitors before mainnet, not after the incident.']]],
    ['Process', [
      ['An internal security review happened in the last quarter', 'Run an internal pass first; it converts paid audit hours into depth.'],
      ['A known-issues log exists for auditors', 'Keep a running known-issues log; it prevents duplicate findings and awkward calls.'],
      ['Scope for the audit is written and frozen', 'Freeze scope in writing; scope drift is the main cause of budget overruns.']]]
  ];
  var state = load() || { a: {} };
  function load() { try { return JSON.parse(localStorage.getItem('syv-ars-v1')); } catch (e) { return null; } }
  function save() { try { localStorage.setItem('syv-ars-v1', JSON.stringify(state)); } catch (e) {} }
  function render() {
    var total = 0, max = 0, done = 0, count = 0, catScores = [], gaps = [];
    var qh = '';
    CATS.forEach(function (cat, ci) {
      var cs = 0, cm = cat[1].length * 2;
      qh += '<div class="ars-cat"><div class="est-l">' + cat[0] + '</div>';
      cat[1].forEach(function (q, qi) {
        var k = ci + '-' + qi, v = state.a[k];
        count++;
        if (v !== undefined) { done++; cs += v; if (v < 2) gaps.push([v, cat[0], q[0], q[1]]); }
        qh += '<div class="ars-q"><p>' + q[0] + '</p><div class="segs-btn sm">' +
          [['No', 0], ['Partial', 1], ['Yes', 2]].map(function (o) {
            return '<button type="button" class="segb' + (v === o[1] ? ' on' : '') + '" data-k="' + k + '" data-v="' + o[1] + '">' + o[0] + '</button>';
          }).join('') + '</div></div>';
      });
      qh += '</div>';
      total += cs; max += cm; catScores.push([cat[0], cs, cm]);
    });
    var pct = max ? Math.round(total / max * 100) : 0;
    var grade = pct >= 85 ? 'A' : pct >= 70 ? 'B' : pct >= 55 ? 'C' : pct >= 40 ? 'D' : 'F';
    var costNote = pct >= 85 ? 'Prepared codebases at this level routinely cut 20 to 35 percent off firm hours and skip a remediation round.'
      : pct >= 55 ? 'Expect the audit to surface prep gaps; closing the items below first typically saves a five-figure amount.'
      : 'Booking a firm at this readiness level buys expensive orientation. Close the top gaps first; the audit will be cheaper and deeper.';
    gaps.sort(function (a, b) { return a[0] - b[0]; });
    var rep = '';
    if (done === count) {
      rep = '<div id="ars-report"><div class="rep-head"><div><span class="mono rep-code">SYV-ARS-2026</span>' +
        '<h3 class="est-h">Audit readiness: grade ' + grade + '.</h3></div>' +
        '<div class="est-big"><b>' + pct + '/100</b><span class="mono">READINESS SCORE</span></div></div>' +
        '<div class="ars-bars">' + catScores.map(function (c) {
          var p = Math.round(c[1] / c[2] * 100);
          return '<div class="ars-bar"><span>' + c[0] + '</span><i><b style="width:' + p + '%"></b></i><em class="mono">' + p + '%</em></div>';
        }).join('') + '</div>' +
        '<p class="est-fine" style="margin-top:22px">' + costNote + '</p>' +
        (gaps.length ? '<div class="est-l" style="margin-top:26px">Fix first, in this order</div><ol class="ars-fixes">' +
          gaps.slice(0, 5).map(function (g) { return '<li><b>' + g[2] + '</b><span>' + g[3] + '</span></li>'; }).join('') + '</ol>' : '') +
        '</div><div class="est-actions no-print">' +
        '<a class="btn primary" target="_blank" rel="noopener" href="https://calendly.com/majid-khan-syvora/30min"><span class="tick"></span>Close the gaps with us</a>' +
        '<button type="button" class="btn" id="ars-print"><span class="tick"></span>Download report</button>' +
        '<a class="btn" href="/services/smart-contract-audit-readiness/"><span class="tick"></span>Audit readiness service</a></div>';
    } else {
      rep = '<div class="est-note mono no-print">' + done + ' / ' + count + ' ANSWERED · REPORT UNLOCKS AT ' + count + '</div>';
    }
    root.innerHTML = '<div class="no-print">' + qh + '</div>' + rep;
    save();
  }
  root.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.dataset.k) { state.a[b.dataset.k] = +b.dataset.v; render(); return; }
    if (b.id === 'ars-print') window.print();
  });
  render();
})();
