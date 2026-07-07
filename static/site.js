/* Syvora site JS. Vanilla, no dependencies. */
(function () {
  var d = document;

  /* sticky header */
  var hd = d.querySelector('.hd');
  function onScroll() { hd.classList.toggle('solid', window.scrollY > 24); }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  /* mega menus */
  var items = [].slice.call(d.querySelectorAll('.nav > li[data-mega]'));
  function closeAll(except) {
    items.forEach(function (li) { if (li !== except) li.classList.remove('on'); });
    hd.classList.toggle('open', !!except);
  }
  items.forEach(function (li) {
    var btn = li.querySelector('.nav-btn');
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var was = li.classList.contains('on');
      closeAll(null); if (!was) { li.classList.add('on'); hd.classList.add('open'); }
    });
    li.addEventListener('mouseenter', function () { closeAll(li); li.classList.add('on'); });
  });
  d.addEventListener('click', function () { closeAll(null); });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(null); });
  var headerEl = d.querySelector('header');
  if (headerEl) headerEl.addEventListener('mouseleave', function () { closeAll(null); });

  /* mobile nav */
  var burger = d.querySelector('.burger'), mnav = d.querySelector('.m-nav');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      var on = mnav.classList.toggle('on');
      burger.classList.toggle('on', on);
      hd.classList.toggle('open', on);
      d.body.classList.toggle('locked', on);
    });
    [].forEach.call(mnav.querySelectorAll('a'), function (a) {
      a.addEventListener('click', function () {
        mnav.classList.remove('on'); burger.classList.remove('on');
        d.body.classList.remove('locked'); hd.classList.remove('open');
      });
    });
    [].forEach.call(mnav.querySelectorAll('.m-group > button'), function (b) {
      b.addEventListener('click', function () { b.parentElement.classList.toggle('on'); });
    });
  }

  /* reveal on scroll */
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  [].forEach.call(d.querySelectorAll('.rv'), function (el) { io.observe(el); });

  /* gauge fill animation */
  function animateGauge(g) {
    var ticks = [].slice.call(g.querySelectorAll('i'));
    ticks.forEach(function (t, i) {
      if (t.hasAttribute('data-on')) setTimeout(function () { t.classList.add('on'); }, 260 + i * 14);
    });
  }
  var gio = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { animateGauge(e.target); gio.unobserve(e.target); } });
  }, { threshold: 0.4 });
  [].forEach.call(d.querySelectorAll('.gauge[data-animate]'), function (g) { gio.observe(g); });

  /* count-up stats */
  function countUp(el) {
    var raw = el.getAttribute('data-count'); var suffix = el.getAttribute('data-suffix') || '';
    var target = parseFloat(raw); var dur = 1100; var t0 = null;
    function step(ts) {
      if (!t0) t0 = ts; var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString('en-US') + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var cio = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { countUp(e.target); cio.unobserve(e.target); } });
  }, { threshold: 0.5 });
  [].forEach.call(d.querySelectorAll('[data-count]'), function (el) { cio.observe(el); });

  /* practice explorer tabs */
  var px = d.querySelector('.px');
  if (px) {
    var tabs = [].slice.call(px.querySelectorAll('.px-tab'));
    var panels = [].slice.call(px.querySelectorAll('.px-panel'));
    tabs.forEach(function (t) {
      t.addEventListener('click', function () {
        tabs.forEach(function (x) { x.classList.remove('on'); });
        panels.forEach(function (p) { p.style.display = 'none'; });
        t.classList.add('on');
        var p = px.querySelector('.px-panel[data-p="' + t.getAttribute('data-p') + '"]');
        if (p) {
          p.style.display = 'block';
          var g = p.querySelector('.gauge');
          if (g) { [].forEach.call(g.querySelectorAll('i'), function (i) { i.classList.remove('on'); }); animateGauge(g); }
        }
      });
    });
  }

  /* process stepper */
  var proc = d.querySelector('.proc');
  if (proc) {
    var steps = [].slice.call(proc.querySelectorAll('.proc-step'));
    var detail = d.querySelector('.proc-detail p');
    function setStep(s) {
      steps.forEach(function (x) { x.classList.remove('on'); });
      s.classList.add('on');
      if (detail) detail.textContent = s.getAttribute('data-detail');
    }
    var auto = null;
    steps.forEach(function (s) {
      s.addEventListener('click', function () { setStep(s); if (auto) { clearInterval(auto); auto = null; } });
      s.addEventListener('mouseenter', function () { setStep(s); if (auto) { clearInterval(auto); auto = null; } });
    });
    var idx = 0;
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      auto = setInterval(function () { idx = (idx + 1) % steps.length; setStep(steps[idx]); }, 5600);
    }
  }

  /* FAQ accordions */
  [].forEach.call(d.querySelectorAll('.faq-item'), function (item) {
    var q = item.querySelector('.faq-q'), a = item.querySelector('.faq-a');
    q.addEventListener('click', function () {
      var open = item.classList.toggle('on');
      a.style.maxHeight = open ? a.scrollHeight + 'px' : '0px';
    });
  });

  /* mega menu service search */
  var input = d.querySelector('.mega-search input');
  var results = d.querySelector('.sr');
  if (input && results && window.SYVORA_INDEX) {
    input.addEventListener('click', function (e) { e.stopPropagation(); });
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      if (q.length < 2) { results.classList.remove('on'); results.innerHTML = ''; return; }
      var hits = window.SYVORA_INDEX.filter(function (it) {
        return it.t.toLowerCase().indexOf(q) > -1 || it.k.indexOf(q) > -1;
      }).slice(0, 6);
      results.innerHTML = hits.map(function (h) {
        return '<a href="' + h.u + '">' + h.t + '<small>' + h.c + '</small></a>';
      }).join('') || '<a href="/contact/">No direct match. Talk to us instead.<small>CONTACT</small></a>';
      results.classList.add('on');
    });
  }
})();
