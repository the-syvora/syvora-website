# Syvora Website (SYV-WEB-2026)

Static site, 70 pages, zero dependencies at runtime. Built by `build.py` from structured data.

## Deploy (fastest): Cloudflare Pages direct upload
1. Cloudflare dashboard > Workers & Pages > Create > Pages > Upload assets
2. Drag the `dist/` folder. Done. `_headers`, `404.html`, and clean URLs work out of the box.

## Deploy (recommended): GitHub + Cloudflare Pages
1. Push this whole folder as a repo.
2. Cloudflare Pages > Connect to Git > select repo.
3. Build command: (leave empty). Build output directory: `dist`.
   The built site is committed, so no build step is needed on Cloudflare.
4. Add the custom domain (syvora.com) in Pages > Custom domains.

## Editing content
- Copy lives in `data.py` (practices, technologies, engagement, process, values)
  and `services_a.py` / `services_b.py` (30 service pages).
- Rebuild: `python3 build.py` (pure stdlib; `pip install fonttools brotli pillow` only if you want og.png regenerated).
- Canonical domain is `SITE["domain"]` in `data.py`.

## Structure
- `/` home, `/practices/` + 4, `/services/` + 30, `/technologies/` + 28,
  `/process/`, `/engagement-models/`, `/about/`, `/contact/`, `404.html`
- SEO: sitemap.xml, robots.txt, llms.txt, canonical + OG on every page,
  JSON-LD (Organization, Service, FAQPage, BreadcrumbList), og.png share image.
- `_headers`: security headers + long-cache fonts/css/js.
