#!/usr/bin/env python3
# Syvora static site generator. Output: dist/. No em dashes anywhere.
import os, json, shutil
from data import SITE, SERVICES, PRACTICES, TECHNOLOGIES, ENGAGEMENT, PROCESS, DELTA, STATS, PAINS

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
DOMAIN = SITE["domain"]
P_ORDER = sorted(PRACTICES.keys(), key=lambda k: PRACTICES[k]["order"])
URLS = []

def practice_services(pslug):
    return [(s, SERVICES[s]) for s in SERVICES if SERVICES[s]["practice"] == pslug]

def tech_by_cat():
    out = {}
    for slug, t in TECHNOLOGIES.items():
        out.setdefault(t["cat"], []).append((slug, t))
    return out

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, separators=(",", ":")) + '</script>'

def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u}
            for i, (n, u) in enumerate(items)]}

NOSCRIPT = ('<noscript><style>.gauge i[data-on]{background:var(--arc)}'
    '.gauge i[data-on].s2{background:var(--porc)}.gauge i[data-on].s3{background:var(--arc2)}'
    '.gauge i[data-on].s4{background:#5A6273}.gauge.lightbg i[data-on].s2{background:var(--ink)}'
    '.gauge.lightbg i[data-on].s4{background:#B4B8AE}.rv{opacity:1;transform:none}</style></noscript>')

def head(title, desc, path, extra_ld=None):
    lds = "".join(jsonld(x) for x in (extra_ld or []))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="theme-color" content="#0F1319">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Syvora">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{path}">
<meta property="og:image" content="{DOMAIN}/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@thesyvora">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/archivo-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/archivo-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css">
{NOSCRIPT}
{lds}
</head>
<body>"""

def mega_services_cols():
    cols = ""
    for p in P_ORDER:
        pd = PRACTICES[p]
        links = "".join(f'<li><a class="mega-link" href="/services/{s}/">{sd["name"]}</a></li>'
                        for s, sd in practice_services(p))
        cols += (f'<div><div class="mega-h">{pd["name"].upper()}'
                 f'<a href="/practices/{p}/">{pd["code"]}</a></div><ul>{links}</ul></div>')
    return cols

def mega_tech_cols():
    byc = tech_by_cat()
    groups = [("Chains", "Languages"), ("Frontend", "Backend"), ("Cloud", "Platforms", "Mobile"), ("ServiceNow",)]
    cols = ""
    for grp in groups:
        inner = ""
        for cat in grp:
            links = "".join(f'<li><a class="mega-link" href="/technologies/{s}/">{t["name"]}</a></li>'
                            for s, t in byc.get(cat, []))
            mt = "18px" if inner else "0"
            inner += f'<div class="mega-h" style="margin-top:{mt}">{cat.upper()}</div><ul>{links}</ul>'
        cols += f"<div>{inner}</div>"
    return cols

def header():
    prac_links = "".join(
        f'<li><a class="mega-link" href="/practices/{p}/">{PRACTICES[p]["name"]}'
        f'<small>{PRACTICES[p]["short"]}</small></a></li>' for p in P_ORDER)
    m_prac = "".join(f'<li><a href="/practices/{p}/">{PRACTICES[p]["name"]}</a></li>' for p in P_ORDER)
    m_serv = ""
    for p in P_ORDER:
        m_serv += f'<li class="m-sub">{PRACTICES[p]["name"].upper()}</li>'
        m_serv += "".join(f'<li><a href="/services/{s}/">{sd["name"]}</a></li>' for s, sd in practice_services(p))
    m_tech = "".join(f'<li><a href="/technologies/{t}/">{TECHNOLOGIES[t]["name"]}</a></li>' for t in TECHNOLOGIES)
    return f"""
<header>
<div class="hd"><div class="wrap hd-in">
  <a class="brand" href="/"><span class="mk"></span>SYVORA</a>
  <ul class="nav">
    <li data-mega><button class="nav-btn" type="button">Practices <span class="chev"></span></button>
      <div class="mega"><div class="mega-in mega-3">
        <div class="mega-feat"><div class="kicker dim">THE BENCH</div><div class="n">64 engineers</div>
          <p>Four practices, one delivery system. Capacity matched to your stack in days, not months.</p>
          <a class="btn ghost-l" href="/practices/"><span class="tick"></span>Explore practices</a></div>
        <ul style="grid-column:span 2;columns:2;column-gap:36px">{prac_links}</ul>
      </div></div></li>
    <li data-mega><button class="nav-btn" type="button">Services <span class="chev"></span></button>
      <div class="mega"><div class="mega-in mega-4">
        <div class="mega-search"><input type="text" placeholder="Search 30 services and 28 technologies..." aria-label="Search services"><span class="hint">TYPE TO FILTER</span></div>
        <div class="sr"></div>
        {mega_services_cols()}
      </div></div></li>
    <li data-mega><button class="nav-btn" type="button">Technologies <span class="chev"></span></button>
      <div class="mega"><div class="mega-in mega-4">{mega_tech_cols()}</div></div></li>
    <li data-mega><button class="nav-btn" type="button">Company <span class="chev"></span></button>
      <div class="mega"><div class="mega-in mega-3">
        <div class="mega-feat"><div class="kicker dim">AIGILE</div><div class="n">First demo by week 3</div>
          <p>Analyze, build, launch, optimize. The delivery system every practice runs on.</p>
          <a class="btn ghost-l" href="/process/"><span class="tick"></span>See the process</a></div>
        <div><div class="mega-h">COMPANY</div><ul>
          <li><a class="mega-link" href="/about/">About Syvora<small>The studio, the values, the bench</small></a></li>
          <li><a class="mega-link" href="/process/">Process<small>The AIgile delivery system</small></a></li>
        </ul></div>
        <div><div class="mega-h">WORK WITH US</div><ul>
          <li><a class="mega-link" href="/engagement-models/">Engagement Models<small>Pods, staff aug, fixed scope, managed</small></a></li>
          <li><a class="mega-link" href="/contact/">Contact<small>Book a 30 minute discovery call</small></a></li>
        </ul></div>
      </div></div></li>
  </ul>
  <div class="hd-cta">
    <a class="btn primary hide-m" href="{SITE['calendly']}" target="_blank" rel="noopener"><span class="tick"></span>Book a call</a>
    <button class="burger" aria-label="Menu" type="button"><span></span><span></span><span></span></button>
  </div>
</div></div>
<nav class="m-nav">
  <div class="m-group"><button type="button">Practices<span>+</span></button><ul>{m_prac}</ul></div>
  <div class="m-group"><button type="button">Services<span>+</span></button><ul>{m_serv}</ul></div>
  <div class="m-group"><button type="button">Technologies<span>+</span></button><ul>{m_tech}</ul></div>
  <div class="m-group"><button type="button">Company<span>+</span></button><ul>
    <li><a href="/about/">About</a></li><li><a href="/process/">Process</a></li>
    <li><a href="/engagement-models/">Engagement Models</a></li><li><a href="/contact/">Contact</a></li></ul></div>
  <a class="btn primary" style="margin-top:26px" href="{SITE['calendly']}"><span class="tick"></span>Book a call</a>
</nav>
</header>"""

def footer():
    cols = ""
    for p in P_ORDER:
        pd = PRACTICES[p]
        links = "".join(f'<li><a href="/services/{s}/">{sd["name"]}</a></li>' for s, sd in practice_services(p))
        cols += f'<div><h4><a href="/practices/{p}/">{pd["name"].upper()}</a></h4><ul>{links}</ul></div>'
    return f"""
<footer class="ft"><div class="wrap">
<div class="ft-grid">
  <div class="ft-brand">
    <a class="brand" href="/"><span class="mk"></span>SYVORA</a>
    <p>A product studio combining strategy, design, and engineering. 64 engineers, four practices, one delivery system.</p>
    <ul>
      <li><a href="/about/">About</a></li>
      <li><a href="/process/">Process</a></li>
      <li><a href="/engagement-models/">Engagement Models</a></li>
      <li><a href="/technologies/">Technologies</a></li>
      <li><a href="/contact/">Contact</a></li>
      <li><a href="{SITE['linkedin']}" rel="noopener" target="_blank">LinkedIn</a></li>
      <li><a href="{SITE['x']}" rel="noopener" target="_blank">X / Twitter</a></li>
    </ul>
  </div>
  {cols}
</div>
<div class="ft-bot"><span>© 2026 SYVORA SERVICES · {SITE['tagline'].upper()}</span><span>SYV-WEB-2026</span></div>
</div></footer>
<script src="/js/search-index.js" defer></script>
<script src="/js/site.js" defer></script>
</body></html>"""

def gauge_html(animate=True, light=False):
    ticks = ""
    for p in P_ORDER:
        seg = "s" + str(PRACTICES[p]["order"])
        for _ in range(PRACTICES[p]["n"]):
            ticks += f'<i class="{seg}" data-on></i>'
    return (f'<div class="gauge{" lightbg" if light else ""}" style="height:64px"'
            f'{" data-animate" if animate else ""}>{ticks}</div>')

def gauge_practice(pslug, h="34px"):
    ticks = ""
    for p in P_ORDER:
        lit = " data-on" if p == pslug else ""
        for _ in range(PRACTICES[p]["n"]):
            ticks += f"<i{lit}></i>"
    return f'<div class="gauge lightbg" style="height:{h}" data-animate>{ticks}</div>'

def seg_labels(light=False):
    segs = "".join(
        f'<div class="seg" style="flex:{PRACTICES[p]["n"]}"><b>{PRACTICES[p]["n"]}</b>'
        f'<span>{PRACTICES[p]["name"].upper()}</span></div>' for p in P_ORDER)
    return f'<div class="seg-row{" lightbg-labels" if light else ""}">{segs}</div>'

def cta_band(h="Ready when your roadmap is.",
             sub="Book a 30 minute discovery call. Goals, constraints, and fit. A written proposal follows within a week."):
    return f"""<section class="cta-band"><div class="wrap cta-in">
  <div><div class="kicker dim">START A CONVERSATION</div><h2 class="h-lg" style="margin-top:14px">{h}</h2>
  <p class="lede" style="margin-top:16px">{sub}</p></div>
  <div style="display:flex;gap:14px;flex-wrap:wrap">
    <a class="btn primary" href="{SITE['calendly']}" target="_blank" rel="noopener"><span class="tick"></span>Book a call</a>
    <a class="btn ghost-l" href="/contact/"><span class="tick"></span>Contact</a>
  </div>
</div></section>"""

def write(path, html):
    full = os.path.join(DIST, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    if path.endswith("index.html"):
        URLS.append("/" + path[: -len("index.html")].lstrip("/"))

def faq_html(faqs):
    items = "".join(
        f'<div class="faq-item"><button class="faq-q" type="button">{q}<span class="pm">+</span></button>'
        f'<div class="faq-a"><p>{a}</p></div></div>' for q, a in faqs)
    return f'<div class="faq">{items}</div>'

# ------------------------------------------------------------------ HOME
def page_home():
    marq = "".join(f'<b>·</b> {TECHNOLOGIES[t]["name"]} ' for t in TECHNOLOGIES)
    marq_span = f"<span>{marq}</span>"
    stats = ""
    for v, l in STATS:
        if v == "64": b = '<b data-count="64">64</b>'
        elif v == "35+": b = '<b data-count="35" data-suffix="+">35+</b>'
        elif v == "6+": b = '<b data-count="6" data-suffix="+">6+</b>'
        elif v == "200K+": b = '<b data-count="200" data-suffix="K+">200K+</b>'
        else: b = f"<b>{v}</b>"
        stats += f'<div class="stat rv">{b}<span>{l}</span></div>'
    tabs, panels = "", ""
    for i, p in enumerate(P_ORDER):
        pd = PRACTICES[p]
        tabs += (f'<button class="px-tab{" on" if i == 0 else ""}" data-p="{p}" type="button">'
                 f'<span class="c">{pd["code"]}</span><span class="t">{pd["name"]}</span>'
                 f'<span class="n">{pd["n"]} ENG</span></button>')
        caps = "".join(f'<div class="px-cap">{SERVICES[s]["name"]}</div>' for s, _ in practice_services(p))
        meta = "".join(f'<div><b>{v}</b><span>{l}</span></div>' for v, l in pd["stats"][:3])
        disp = "block" if i == 0 else "none"
        panels += (f'<div class="px-panel" data-p="{p}" style="display:{disp}">'
                   f'<div class="kicker">{pd["code"]} · {pd["tag"]}</div>'
                   f'{gauge_practice(p)}<div class="bench-cap"><b>{pd["n"]}</b> of 64 studio engineers</div>'
                   f'<div class="px-caps">{caps}</div><div class="px-meta">{meta}</div>'
                   f'<a class="btn" href="/practices/{p}/"><span class="tick"></span>Explore {pd["name"]}</a></div>')
    steps = "".join(
        f'<div class="proc-step{" on" if i == 0 else ""}" data-detail="{d}">'
        f'<div class="i">{n} /</div><h3>{t}</h3><p>{s}</p></div>'
        for i, (n, t, s, d) in enumerate(PROCESS))
    featured = ["smart-contract-development", "web-application-development", "servicenow-itsm-implementation",
                "ai-agentic-automation", "defi-development", "shopify-commerce-engineering",
                "wallet-account-abstraction", "technical-seo-growth"]
    fcards = "".join(
        f'<a class="card rv" href="/services/{s}/"><div class="cc">{PRACTICES[SERVICES[s]["practice"]]["code"]}</div>'
        f'<h3>{SERVICES[s]["name"]}</h3><p>{SERVICES[s]["short"]}</p>'
        f'<span class="more">View service <span class="arrow">→</span></span></a>' for s in featured)
    pains = "".join(f'<div class="pain rv"><div class="pl">{l}</div><h3>{t}</h3><p>{d}</p></div>'
                    for l, t, d in PAINS)
    eng = "".join(
        f'<a class="card rv" href="/engagement-models/#{e["slug"]}"><div class="cc">MODEL 0{i+1}</div>'
        f'<h3>{e["name"]}</h3><p>{e["short"]}</p><span class="more">How it works <span class="arrow">→</span></span></a>'
        for i, e in enumerate(ENGAGEMENT))
    delta = "".join(f'<div class="rv"><b>{w}</b><p>{d}</p></div>' for w, d in DELTA)
    ld = [
        {"@context": "https://schema.org", "@type": "Organization", "name": "Syvora", "url": DOMAIN,
         "logo": DOMAIN + "/favicon.svg", "slogan": SITE["tagline"],
         "sameAs": [SITE["linkedin"], SITE["x"]],
         "description": "Product studio combining strategy, design, and engineering across blockchain, full stack, ServiceNow, and specialist capabilities."},
        {"@context": "https://schema.org", "@type": "WebSite", "name": "Syvora", "url": DOMAIN},
    ]
    html = head("Syvora: Product Studio for Blockchain, Full Stack & ServiceNow Engineering",
        "One studio, four practices, 64 engineers. Syvora ships blockchain protocols, full stack products, and ServiceNow platforms under one delivery system.",
        "/", ld) + header() + f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-rule"><span>SYVORA · PRODUCT STUDIO</span><span>SYV-WEB-2026</span></div>
    <div class="kicker dim">{SITE['tagline'].upper()}</div>
    <h1 class="h-xl">One studio.<br>Four practices.<br><span class="a">64 engineers.</span></h1>
    <p class="lede">Syvora combines strategy, design, and engineering in a single accountable team.
    From smart contract systems and full stack products to enterprise workflows on ServiceNow,
    one delivery system runs from first spec to measured adoption.</p>
    <div class="hero-cta">
      <a class="btn primary" href="{SITE['calendly']}" target="_blank" rel="noopener"><span class="tick"></span>Book a discovery call</a>
      <a class="btn ghost-l" href="/practices/"><span class="tick"></span>Explore practices</a>
    </div>
    <div class="hero-gauge">
      <div class="hero-meta"><span>STUDIO CAPACITY</span><span>64 ENGINEERS ACROSS FOUR PRACTICES</span></div>
      {gauge_html()}{seg_labels()}
    </div>
  </div>
</section>
<div class="marq"><div class="marq-track">{marq_span}{marq_span}</div></div>
<section class="stats"><div class="wrap stats-in">{stats}</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">PRACTICES</div><h2 class="h-lg">Four practices. One accountable bench.</h2></div>
  <p class="side">Every engineer sits in one of four practices and ships under one system. Select a practice to see where the bench sits.</p></div>
  <div class="px rv"><div class="px-tabs">{tabs}</div><div>{panels}</div></div>
</div></section>
<section class="sec dark"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">HOW WE BUILD · THE AIGILE PROCESS</div><h2 class="h-lg">Analyze. Build. Launch. Optimize.</h2></div>
  <p class="side">The same delivery system runs across every practice, so the second engagement is always faster than the first.</p></div>
  <div class="rv"><div class="proc">{steps}</div>
  <div class="proc-detail"><p>{PROCESS[0][3]}</p></div></div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">SERVICES</div><h2 class="h-lg">30 services, engineered the same way.</h2></div>
  <a class="btn" href="/services/"><span class="tick"></span>View all services</a></div>
  <div class="grid g4">{fcards}</div>
</div></section>
<section class="sec tint"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">PAIN POINTS WE REMOVE</div><h2 class="h-lg">The problems teams bring us.</h2></div></div>
  <div class="grid g2">{pains}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">ENGAGEMENT MODELS</div><h2 class="h-lg">Four ways to plug us in.</h2></div>
  <a class="btn" href="/engagement-models/"><span class="tick"></span>Compare models</a></div>
  <div class="grid g4">{eng}</div>
</div></section>
<section class="sec dark"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">VALUES · THE DELTA FRAMEWORK</div><h2 class="h-lg">How we behave when it matters.</h2></div></div>
  <div class="delta">{delta}</div>
</div></section>
{cta_band()}""" + footer()
    write("index.html", html)

# ------------------------------------------------------------------ PRACTICES
def page_practices_index():
    rows = ""
    for p in P_ORDER:
        pd = PRACTICES[p]
        rows += (f'<a class="row rv" href="/practices/{p}/"><span class="rc">{pd["code"]} · {pd["n"]} ENGINEERS</span>'
                 f'<div><h3>{pd["name"]}</h3><p>{pd["short"]}</p></div><span class="arrow">→</span></a>')
    ld = [breadcrumb([("Home", "/"), ("Practices", "/practices/")])]
    html = head("Engineering Practices | Syvora",
        "Four practices, 64 engineers: Blockchain & Web3, Full Stack Engineering, ServiceNow, and Extended Capabilities under one delivery system.",
        "/practices/", ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / PRACTICES</div>
  <div class="kicker dim">THE BENCH, MAPPED</div>
  <h1 class="h-xl">Four practices.<br>One delivery system.</h1>
  <p class="lede">Every Syvora engineer sits in one of four practices: live delivery capacity, not a resume pool.</p>
  <div class="hero-gauge">{gauge_html()}{seg_labels()}</div>
</div></section>
<section class="sec"><div class="wrap"><div class="rows">{rows}</div></div></section>
{cta_band()}""" + footer()
    write("practices/index.html", html)

def page_practice(pslug):
    pd = PRACTICES[pslug]
    chips = "".join(f'<span class="chip"><b>{n}</b>{name.upper()}</span>' for name, n in pd["comp"])
    bstats = "".join(f'<div><b>{v}</b><span>{l}</span></div>' for v, l in pd["stats"])
    cards = "".join(
        f'<a class="card rv" href="/services/{s}/"><div class="cc">{pd["code"]}</div>'
        f'<h3>{sd["name"]}</h3><p>{sd["short"]}</p>'
        f'<span class="more">View service <span class="arrow">→</span></span></a>'
        for s, sd in practice_services(pslug))
    tags = "".join(f'<a class="tag" href="/technologies/{t}/">{TECHNOLOGIES[t]["name"]}</a>'
                   for t in pd["tech"] if t in TECHNOLOGIES)
    path = f"/practices/{pslug}/"
    ld = [breadcrumb([("Home", "/"), ("Practices", "/practices/"), (pd["name"], path)]),
          {"@context": "https://schema.org", "@type": "Service", "name": pd["name"],
           "provider": {"@type": "Organization", "name": "Syvora", "url": DOMAIN},
           "description": pd["meta"], "url": DOMAIN + path}]
    html = head(f'{pd["name"]} Practice | Syvora', pd["meta"], path, ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / <a href="/practices/">PRACTICES</a> / {pd["name"].upper()}</div>
  <div class="kicker dim">{pd["code"]} · {pd["tag"]}</div>
  <h1 class="h-xl">{pd["name"]}</h1>
  <p class="lede">{pd["lede"]}</p>
</div></section>
<section class="sec"><div class="wrap">
  <div class="bench rv">
    <div><div class="kicker dim" style="color:var(--muted)">BENCH STRENGTH</div>
      {gauge_practice(pslug, "40px")}
      <div class="bench-cap"><b>{pd["n"]}</b> of 64 studio engineers · {pd["code"]}</div>
      <div class="kicker dim" style="color:var(--muted);margin-top:22px">BENCH COMPOSITION</div>
      <div class="chips">{chips}</div>
    </div>
    <div class="bench-stats">{bstats}</div>
  </div>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">SERVICES IN THIS PRACTICE</div>
  <h2 class="h-lg">What the {pd["name"]} bench ships.</h2></div></div>
  <div class="grid g3">{cards}</div>
  <div style="margin-top:44px" class="rv"><div class="kicker" style="margin-bottom:16px">CORE STACK</div>
  <div class="tags">{tags}</div></div>
</div></section>
{cta_band(f'Need {pd["name"].lower()} capacity?', 'Talent matched to your stack in days. Kickoff inside two weeks, first demo by week three.')}""" + footer()
    write(f"practices/{pslug}/index.html", html)

# ------------------------------------------------------------------ SERVICES
def page_services_index():
    secs = ""
    for p in P_ORDER:
        pd = PRACTICES[p]
        rows = "".join(
            f'<a class="row rv" href="/services/{s}/"><span class="rc">{pd["code"]}</span>'
            f'<div><h3>{sd["name"]}</h3><p>{sd["short"]}</p></div><span class="arrow">→</span></a>'
            for s, sd in practice_services(p))
        secs += (f'<section class="sec" style="padding:56px 0"><div class="wrap">'
                 f'<div class="sec-hd rv"><div><div class="kicker">{pd["code"]} · {pd["n"]} ENGINEERS</div>'
                 f'<h2 class="h-md">{pd["name"]}</h2></div>'
                 f'<a class="btn" href="/practices/{p}/"><span class="tick"></span>Practice overview</a></div>'
                 f'<div class="rows">{rows}</div></div></section>')
    ld = [breadcrumb([("Home", "/"), ("Services", "/services/")])]
    html = head("Engineering Services | Syvora",
        "30 engineering services across blockchain, full stack, ServiceNow, and specialist capabilities, delivered under one accountable system.",
        "/services/", ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / SERVICES</div>
  <div class="kicker dim">FULL SERVICE INDEX</div>
  <h1 class="h-xl">30 services.<br>One standard.</h1>
  <p class="lede">Every service below runs on the same AIgile delivery system: senior-led, weekly demos, and instrumented after go-live.</p>
</div></section>
{secs}
{cta_band()}""" + footer()
    write("services/index.html", html)

def page_service(slug):
    sd = SERVICES[slug]
    pd = PRACTICES[sd["practice"]]
    path = f"/services/{slug}/"
    scope = "".join(f'<li><span><b>{t}</b> {d}</span></li>' for t, d in sd["scope"])
    deliv = "".join(f"<span>{x}</span>" for x in sd["deliverables"])
    rel = "".join(
        f'<li><a href="/services/{r}/">{SERVICES[r]["name"]}<span class="arrow">→</span></a></li>'
        for r in sd["related"] if r in SERVICES)
    tags = "".join(f'<a class="tag" href="/technologies/{t}/">{TECHNOLOGIES[t]["name"]}</a>'
                   for t in sd["tech"] if t in TECHNOLOGIES)
    paras = "".join(f"<p>{x}</p>" for x in sd["body"])
    ld = [
        breadcrumb([("Home", "/"), ("Services", "/services/"), (sd["name"], path)]),
        {"@context": "https://schema.org", "@type": "Service", "name": sd["name"],
         "serviceType": sd["name"], "url": DOMAIN + path, "description": sd["meta"],
         "provider": {"@type": "Organization", "name": "Syvora", "url": DOMAIN},
         "areaServed": "Worldwide"},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in sd["faqs"]]},
    ]
    html = head(f'{sd["name"]} Services | Syvora', sd["meta"], path, ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / <a href="/services/">SERVICES</a> / <a href="/practices/{sd["practice"]}/">{pd["name"].upper()}</a></div>
  <div class="kicker dim">{pd["code"]} · {pd["name"].upper()}</div>
  <h1 class="h-lg" style="font-size:clamp(34px,4.6vw,58px)">{sd["name"]}</h1>
  <p class="lede">{sd["hero"]}</p>
</div></section>
<section class="sec"><div class="wrap body-cols">
  <div class="prose rv">
    {paras}
    <h2>What this covers</h2>
    <ul class="scope">{scope}</ul>
    <h2>What you get</h2>
    <div class="deliv">{deliv}</div>
    <h2>Frequently asked</h2>
    {faq_html(sd["faqs"])}
  </div>
  <aside class="aside">
    <div class="aside-card cta rv">
      <h3 style="color:var(--porc-dim)">START HERE</h3>
      <p>Scope this in a 30 minute discovery call. A written proposal with price and date follows within a week.</p>
      <a class="btn primary" href="{SITE['calendly']}" target="_blank" rel="noopener" style="width:100%;justify-content:center"><span class="tick"></span>Book a call</a>
    </div>
    <div class="aside-card rv"><h3>RELATED SERVICES</h3><ul>{rel}</ul></div>
    <div class="aside-card rv"><h3>TECHNOLOGIES</h3><div class="tags">{tags}</div></div>
    <div class="aside-card rv"><h3>PRACTICE</h3><ul>
      <li><a href="/practices/{sd["practice"]}/">{pd["name"]}<span class="arrow">→</span></a></li>
      <li><a href="/services/">All 30 services<span class="arrow">→</span></a></li></ul></div>
  </aside>
</div></section>
{cta_band(f'Scope your {sd["name"].lower()} build.', 'Thirty minutes on goals, constraints, and fit. Named engineers inside two weeks if we proceed.')}""" + footer()
    write(f"services/{slug}/index.html", html)

# ------------------------------------------------------------------ TECHNOLOGIES
def page_tech_index():
    byc = tech_by_cat()
    secs = ""
    for cat in ["Chains", "Languages", "Frontend", "Backend", "Cloud", "Platforms", "Mobile", "ServiceNow"]:
        if cat not in byc: continue
        cards = "".join(
            f'<a class="card rv" href="/technologies/{s}/"><div class="cc">{cat.upper()}</div>'
            f'<h3>{t["name"]}</h3><p>{t["blurb"].split(". ")[0]}.</p>'
            f'<span class="more">How we use it <span class="arrow">→</span></span></a>'
            for s, t in byc[cat])
        secs += (f'<div class="rv" style="margin-bottom:52px"><div class="kicker" style="margin-bottom:18px">{cat.upper()}</div>'
                 f'<div class="grid g3">{cards}</div></div>')
    ld = [breadcrumb([("Home", "/"), ("Technologies", "/technologies/")])]
    html = head("Technology Stack | Syvora",
        "The technologies Syvora ships on: Ethereum, Solana, TypeScript, React, Next.js, PostgreSQL, AWS, Cloudflare, Kubernetes, Shopify, and the ServiceNow platform.",
        "/technologies/", ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / TECHNOLOGIES</div>
  <div class="kicker dim">THE STACK</div>
  <h1 class="h-xl">Chosen per workload,<br>not per fashion.</h1>
  <p class="lede">Every technology below is one we run in production today. Each page explains what we build with it and which services it powers.</p>
</div></section>
<section class="sec"><div class="wrap">{secs}</div></section>
{cta_band()}""" + footer()
    write("technologies/index.html", html)

def page_tech(slug):
    t = TECHNOLOGIES[slug]
    path = f"/technologies/{slug}/"
    points = "".join(f"<li><span>{p}</span></li>" for p in t["points"])
    rows = "".join(
        f'<a class="row rv" href="/services/{s}/"><span class="rc">{PRACTICES[SERVICES[s]["practice"]]["code"]}</span>'
        f'<div><h3>{SERVICES[s]["name"]}</h3><p>{SERVICES[s]["short"]}</p></div><span class="arrow">→</span></a>'
        for s in t["services"] if s in SERVICES)
    others = "".join(
        f'<a class="tag" href="/technologies/{s}/">{TECHNOLOGIES[s]["name"]}</a>'
        for s, x in TECHNOLOGIES.items() if x["cat"] == t["cat"] and s != slug)
    ld = [breadcrumb([("Home", "/"), ("Technologies", "/technologies/"), (t["name"], path)])]
    title = f'{t["name"]} Development Services | Syvora'
    desc = f'{t["name"]} engineering at Syvora: {t["blurb"].split(". ")[0]}. See what we build with {t["name"]} and the services it powers.'
    html = head(title, desc, path, ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / <a href="/technologies/">TECHNOLOGIES</a> / {t["name"].upper()}</div>
  <div class="kicker dim">{t["cat"].upper()}</div>
  <h1 class="h-xl">{t["name"]}</h1>
  <p class="lede">{t["blurb"]}</p>
</div></section>
<section class="sec"><div class="wrap body-cols">
  <div class="prose rv">
    <h2 style="margin-top:0">What we build with {t["name"]}</h2>
    <ul class="scope">{points}</ul>
    <h2>Services powered by {t["name"]}</h2>
    <div class="rows">{rows}</div>
  </div>
  <aside class="aside">
    <div class="aside-card cta rv"><h3 style="color:var(--porc-dim)">START HERE</h3>
      <p>Tell us what you are building on {t["name"]}. Thirty minutes, honest fit assessment, written follow-up.</p>
      <a class="btn primary" href="{SITE['calendly']}" target="_blank" rel="noopener" style="width:100%;justify-content:center"><span class="tick"></span>Book a call</a></div>
    <div class="aside-card rv"><h3>MORE IN {t["cat"].upper()}</h3><div class="tags">{others}</div></div>
  </aside>
</div></section>
{cta_band()}""" + footer()
    write(f"technologies/{slug}/index.html", html)

# ------------------------------------------------------------------ COMPANY PAGES
def page_process():
    blocks = ""
    for n, t, s, d in PROCESS:
        blocks += (f'<div class="rv" style="border-top:1px solid var(--line);padding:44px 0;display:grid;'
                   f'grid-template-columns:180px 1fr;gap:40px">'
                   f'<div class="kicker">{n} / {t.upper()}</div>'
                   f'<div><h2 class="h-md" style="margin-bottom:14px">{t}</h2>'
                   f'<p style="color:var(--graphite);font-size:16.5px;max-width:70ch">{d}</p></div></div>')
    steps = "".join(
        f'<div class="proc-step{" on" if i == 0 else ""}" data-detail="{d}">'
        f'<div class="i">{n} /</div><h3>{t}</h3><p>{s}</p></div>'
        for i, (n, t, s, d) in enumerate(PROCESS))
    path_row = "".join(
        f'<div class="card rv"><div class="cc">WEEK {w}</div><h3>{t}</h3><p>{d}</p></div>'
        for w, t, d in [("0","Discovery call","Thirty minutes on goals, constraints, and fit."),
                        ("1","Scope & proposal","A written spec with price, plan, and team shape."),
                        ("2","Pod assembled","Named engineers, kickoff, environments live."),
                        ("3","First demo","Working software on screen. Weekly from here.")])
    ld = [breadcrumb([("Home", "/"), ("Process", "/process/")])]
    html = head("The AIgile Process | Syvora",
        "How Syvora delivers: Analyze, Build, Launch, Optimize. One delivery system across every practice, with first demo by week three.",
        "/process/", ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / PROCESS</div>
  <div class="kicker dim">HOW WE BUILD · THE AIGILE PROCESS</div>
  <h1 class="h-xl">Analyze. Build.<br>Launch. Optimize.</h1>
  <p class="lede">One delivery system runs across every practice. It is why the second engagement is always faster than the first.</p>
</div></section>
<section class="sec dark" style="padding-top:56px"><div class="wrap rv">
  <div class="proc">{steps}</div><div class="proc-detail"><p>{PROCESS[0][3]}</p></div>
</div></section>
<section class="sec"><div class="wrap">{blocks}</div></section>
<section class="sec tint"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">FROM FIRST CALL TO FIRST DEMO</div>
  <h2 class="h-lg">Three weeks to working software.</h2></div></div>
  <div class="grid g4">{path_row}</div>
</div></section>
{cta_band()}""" + footer()
    write("process/index.html", html)

def page_engagement():
    blocks = ""
    for i, e in enumerate(ENGAGEMENT):
        blocks += (f'<div class="rv" id="{e["slug"]}" style="border:1px solid var(--line);background:var(--card);'
                   f'padding:40px;margin-bottom:22px;display:grid;grid-template-columns:1fr 1fr;gap:44px">'
                   f'<div><div class="kicker">MODEL 0{i+1}</div><h2 class="h-md" style="margin:12px 0 14px">{e["name"]}</h2>'
                   f'<p style="color:var(--graphite)">{e["detail"]}</p></div>'
                   f'<div style="border-left:1px solid var(--line);padding-left:40px;align-self:center">'
                   f'<div class="kicker dim" style="color:var(--muted)">BEST FIT FOR</div>'
                   f'<p style="margin-top:12px;color:var(--graphite)">{e["fits"]}</p>'
                   f'<a class="btn" style="margin-top:22px" href="{SITE["calendly"]}" target="_blank" rel="noopener">'
                   f'<span class="tick"></span>Discuss this model</a></div></div>')
    ld = [breadcrumb([("Home", "/"), ("Engagement Models", "/engagement-models/")])]
    html = head("Engagement Models | Syvora",
        "Four ways to work with Syvora: dedicated product pods, staff augmentation, fixed-scope delivery, and SLA-backed managed services.",
        "/engagement-models/", ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / ENGAGEMENT MODELS</div>
  <div class="kicker dim">HOW WE ENGAGE</div>
  <h1 class="h-xl">Four ways to<br>plug us in.</h1>
  <p class="lede">Same bench, same delivery system, four commercial shapes. Pick by how you want to own the roadmap.</p>
</div></section>
<section class="sec"><div class="wrap">{blocks}</div></section>
{cta_band('Not sure which model fits?', 'That is what the discovery call is for. We will recommend one, with reasons, in writing.')}""" + footer()
    write("engagement-models/index.html", html)

def page_about():
    stats = "".join(f'<div class="stat rv"><b>{v}</b><span>{l}</span></div>' for v, l in STATS)
    delta = "".join(f'<div class="rv"><b>{w}</b><p>{d}</p></div>' for w, d in DELTA)
    rows = "".join(
        f'<a class="row rv" href="/practices/{p}/"><span class="rc">{PRACTICES[p]["code"]} · {PRACTICES[p]["n"]} ENGINEERS</span>'
        f'<div><h3>{PRACTICES[p]["name"]}</h3><p>{PRACTICES[p]["short"]}</p></div><span class="arrow">→</span></a>'
        for p in P_ORDER)
    ld = [breadcrumb([("Home", "/"), ("About", "/about/")]),
          {"@context": "https://schema.org", "@type": "AboutPage", "url": DOMAIN + "/about/",
           "name": "About Syvora"}]
    html = head("About Syvora | The Engine Behind Real Adoption",
        "Syvora is a product studio built by engineers behind some of the most used blockchain projects in the world: 64 engineers, four practices, one system.",
        "/about/", ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / ABOUT</div>
  <div class="kicker dim">THE STUDIO</div>
  <h1 class="h-xl">Built by engineers.<br>Run like a product.</h1>
  <p class="lede">{SITE["tagline"]}: not a slogan, a delivery standard measured after go-live.</p>
</div></section>
<section class="sec"><div class="wrap body-cols">
  <div class="prose rv">
    <p>Syvora is a product studio built by engineers and designers behind some of the most used blockchain projects in the world. We build our own ventures and partner with startups and enterprises to take products from first spec to real adoption.</p>
    <p>The studio runs four practices from one bench: Blockchain & Web3, where we started; Full Stack Engineering, the product layer around every system we ship; ServiceNow, our enterprise workflow practice run by certified consultants; and Extended Capabilities, the specialist capacity that gives every engagement more surface area.</p>
    <p>The same playbooks, code libraries, and AIgile delivery process run across every practice, so a client gets one accountable studio whether the work is a DeFi protocol, a SaaS platform, or an enterprise ServiceNow rollout.</p>
    <p>We keep the bench senior on purpose: 6+ years average experience, every pod run by an engineer with shipped products, and weekly demos as the default reporting unit. Discretion is the first letter of our values framework, which is why you will find delivery standards on this site rather than client logos.</p>
  </div>
  <aside class="aside">
    <div class="aside-card cta rv"><h3 style="color:var(--porc-dim)">TALK TO THE STUDIO</h3>
      <p>Thirty minutes with an engineer, not a salesperson.</p>
      <a class="btn primary" href="{SITE['calendly']}" target="_blank" rel="noopener" style="width:100%;justify-content:center"><span class="tick"></span>Book a call</a></div>
    <div class="aside-card rv"><h3>ELSEWHERE</h3><ul>
      <li><a href="{SITE['linkedin']}" target="_blank" rel="noopener">LinkedIn<span class="arrow">→</span></a></li>
      <li><a href="{SITE['x']}" target="_blank" rel="noopener">X / Twitter<span class="arrow">→</span></a></li></ul></div>
  </aside>
</div></section>
<section class="stats"><div class="wrap stats-in">{stats}</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">THE BENCH</div><h2 class="h-lg">Where the 64 sit.</h2></div></div>
  <div class="rows">{rows}</div>
</div></section>
<section class="sec dark"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">VALUES · THE DELTA FRAMEWORK</div><h2 class="h-lg">How we behave when it matters.</h2></div></div>
  <div class="delta">{delta}</div>
</div></section>
{cta_band()}""" + footer()
    write("about/index.html", html)

def page_contact():
    path_row = "".join(
        f'<div class="card rv"><div class="cc">WEEK {w}</div><h3>{t}</h3><p>{d}</p></div>'
        for w, t, d in [("0","Discovery call","Thirty minutes on goals, constraints, and fit."),
                        ("1","Scope & proposal","A written spec with price, plan, and team shape."),
                        ("2","Pod assembled","Named engineers, kickoff, environments live."),
                        ("3","First demo","Working software on screen. Weekly from here.")])
    ld = [breadcrumb([("Home", "/"), ("Contact", "/contact/")]),
          {"@context": "https://schema.org", "@type": "ContactPage", "url": DOMAIN + "/contact/",
           "name": "Contact Syvora"}]
    html = head("Contact Syvora | Book a Discovery Call",
        "Book a 30 minute discovery call with Syvora. Goals, constraints, and fit, with a written proposal within a week.",
        "/contact/", ld) + header() + f"""
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="/">HOME</a> / CONTACT</div>
  <div class="kicker dim">START A CONVERSATION</div>
  <h1 class="h-xl">Thirty minutes.<br>Zero slideware.</h1>
  <p class="lede">You talk to an engineer, not a salesperson. We map goals and constraints, then follow up with a written recommendation whether or not we work together.</p>
  <div class="hero-cta" style="margin-top:34px;padding-bottom:56px">
    <a class="btn primary" href="{SITE['calendly']}" target="_blank" rel="noopener"><span class="tick"></span>Book on Calendly</a>
    <a class="btn ghost-l" href="{SITE['linkedin']}" target="_blank" rel="noopener"><span class="tick"></span>Message on LinkedIn</a>
    <a class="btn ghost-l" href="{SITE['x']}" target="_blank" rel="noopener"><span class="tick"></span>DM on X</a>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-hd rv"><div><div class="kicker">WHAT HAPPENS NEXT</div>
  <h2 class="h-lg">From first call to first demo.</h2></div></div>
  <div class="grid g4">{path_row}</div>
</div></section>
{cta_band('Prefer async?', 'Send context on LinkedIn or X and we will reply with questions worth a call, or an honest no.')}""" + footer()
    write("contact/index.html", html)

def page_404():
    html = head("Page Not Found | Syvora", "This page does not exist. The rest of the studio does.", "/404.html") + header() + f"""
<section class="page-hero" style="min-height:70vh"><div class="wrap">
  <div class="kicker dim">HTTP 404</div>
  <h1 class="h-xl">This tick is<br>not on the gauge.</h1>
  <p class="lede">The page you wanted does not exist. The bench does.</p>
  <div class="hero-cta" style="padding-bottom:56px">
    <a class="btn primary" href="/"><span class="tick"></span>Back to home</a>
    <a class="btn ghost-l" href="/services/"><span class="tick"></span>Browse services</a>
  </div>
</div></section>""" + footer()
    with open(os.path.join(DIST, "404.html"), "w") as f:
        f.write(html)

# ------------------------------------------------------------------ ASSETS
def build_search_index():
    idx = []
    for s, sd in SERVICES.items():
        idx.append({"t": sd["name"], "u": f"/services/{s}/",
                    "c": PRACTICES[sd["practice"]]["name"].upper(),
                    "k": (sd["short"] + " " + s.replace("-", " ")).lower()})
    for t, td in TECHNOLOGIES.items():
        idx.append({"t": td["name"], "u": f"/technologies/{t}/", "c": "TECHNOLOGY · " + td["cat"].upper(),
                    "k": (td["blurb"] + " " + t.replace("-", " ")).lower()})
    for p in P_ORDER:
        idx.append({"t": PRACTICES[p]["name"], "u": f"/practices/{p}/", "c": "PRACTICE",
                    "k": PRACTICES[p]["short"].lower()})
    os.makedirs(os.path.join(DIST, "js"), exist_ok=True)
    with open(os.path.join(DIST, "js", "search-index.js"), "w") as f:
        f.write("window.SYVORA_INDEX=" + json.dumps(idx, separators=(",", ":")) + ";")

def build_meta_files():
    with open(os.path.join(DIST, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    urls = "".join(
        f"<url><loc>{DOMAIN}{u}</loc><changefreq>monthly</changefreq>"
        f"<priority>{'1.0' if u == '/' else '0.8' if u.count('/') == 2 else '0.7'}</priority></url>"
        for u in sorted(set(URLS)))
    with open(os.path.join(DIST, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>")
    with open(os.path.join(DIST, "_headers"), "w") as f:
        f.write("""/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/css/*
  Cache-Control: public, max-age=604800
/js/*
  Cache-Control: public, max-age=604800
""")
    with open(os.path.join(DIST, "favicon.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
                '<rect width="32" height="32" fill="#0F1319"/>'
                '<rect x="7" y="7" width="18" height="18" fill="#2B49F5"/></svg>')
    lines = ["# Syvora", "", "> Product studio: strategy, design, and engineering. 64 engineers across "
             "Blockchain & Web3, Full Stack Engineering, ServiceNow, and Extended Capabilities.", "", "## Practices"]
    lines += [f"- [{PRACTICES[p]['name']}]({DOMAIN}/practices/{p}/): {PRACTICES[p]['short']}" for p in P_ORDER]
    lines += ["", "## Services"]
    lines += [f"- [{SERVICES[s]['name']}]({DOMAIN}/services/{s}/): {SERVICES[s]['short']}" for s in SERVICES]
    with open(os.path.join(DIST, "llms.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")

def build_og():
    try:
        from fontTools.ttLib import TTFont
        from PIL import Image, ImageDraw, ImageFont
        conv = {}
        for w in ("900", "500"):
            src = os.path.join(ROOT, "static", "fonts", f"archivo-latin-{w}-normal.woff2")
            dst = f"/tmp/archivo-{w}.ttf"
            f = TTFont(src); f.flavor = None; f.save(dst); conv[w] = dst
        msrc = os.path.join(ROOT, "static", "fonts", "ibm-plex-mono-latin-500-normal.woff2")
        f = TTFont(msrc); f.flavor = None; f.save("/tmp/plex-500.ttf")
        im = Image.new("RGB", (1200, 630), "#0F1319")
        dr = ImageDraw.Draw(im)
        big = ImageFont.truetype(conv["900"], 118)
        mono = ImageFont.truetype("/tmp/plex-500.ttf", 26)
        mono_s = ImageFont.truetype("/tmp/plex-500.ttf", 20)
        dr.rectangle([70, 74, 98, 102], fill="#2B49F5")
        dr.text((116, 62), "SYVORA", font=ImageFont.truetype(conv["900"], 40), fill="#F1F2ED")
        dr.text((70, 200), "One studio.", font=big, fill="#FFFFFF")
        dr.text((70, 330), "64 engineers.", font=big, fill="#2B49F5")
        counts = [(22, "#2B49F5"), (24, "#F1F2ED"), (8, "#5F79FF"), (10, "#5A6273")]
        x, y, tw, gap, th = 70, 500, 12.5, 5.2, 46
        for n, c in counts:
            for _ in range(n):
                dr.rectangle([x, y, x + tw, y + th], fill=c); x += tw + gap
        dr.text((70, 570), "BLOCKCHAIN · FULL STACK · SERVICENOW · EXTENDED", font=mono_s, fill="#9AA3B2")
        dr.text((836, 78), "SYV-WEB-2026", font=mono_s, fill="#9AA3B2")
        im.save(os.path.join(DIST, "og.png"), optimize=True)
        print("og.png written")
    except Exception as e:
        print("og skipped:", e)

def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(ROOT, "static", "fonts"), os.path.join(DIST, "fonts"))
    os.makedirs(os.path.join(DIST, "css")); os.makedirs(os.path.join(DIST, "js"))
    shutil.copy(os.path.join(ROOT, "static", "site.css"), os.path.join(DIST, "css", "site.css"))
    shutil.copy(os.path.join(ROOT, "static", "site.js"), os.path.join(DIST, "js", "site.js"))
    page_home(); page_practices_index()
    for p in P_ORDER: page_practice(p)
    page_services_index()
    for s in SERVICES: page_service(s)
    page_tech_index()
    for t in TECHNOLOGIES: page_tech(t)
    page_process(); page_engagement(); page_about(); page_contact(); page_404()
    build_search_index(); build_meta_files(); build_og()
    n = sum(len(fs) for _, _, fs in os.walk(DIST))
    print(f"built {len(URLS)} pages, {n} files total")

if __name__ == "__main__":
    main()
