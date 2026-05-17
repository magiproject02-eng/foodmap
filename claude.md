# FoodMap - Amex Gourmet Club Discount Map

## Goal
Build a webapp that visualises Amex discount restaurants on an interactive map, allowing users to search and browse deals.

## Data Source
- PDF: https://www.americanexpress.com/content/dam/amex/hk/benefits/pdf/TnCs_AmexGourmetClub2026.pdf
- Contains Amex Gourmet Club 2026 restaurant discounts in Hong Kong

## Steps
1. Download and parse the PDF to extract restaurant info (name, address, discount details)
2. Geocode restaurant addresses to get lat/lng coordinates
3. Build an interactive web app with:
   - Map view showing all restaurants as pins
   - Search/filter functionality (by name, area, discount type)
   - Click on a pin to see restaurant details and discount info

---

## Type

`web-app` — static HTML/JS + Leaflet map. Single `index.html` file
with restaurant data inlined (annual artifact). `download_pdf.py` is
a Python helper for the annual refresh.

## Deploy

- **Platform:** GitHub Pages on `main` branch (auto-builds).
- **Deploy command:** `git push origin main`
- **Deploy gate:** local preview at `http://localhost:8000/` confirms
  map renders + all pins clickable before push.

## Entry points

- **Local:** `python -m http.server 8000` then open
  `http://localhost:8000/`
- **Production:** the GitHub Pages URL for `magiproject02-eng/foodmap`
- **Smoke:** `curl -sf <prod-url> | grep -q "Leaflet" && echo OK`
- **Annual refresh script:** `python download_pdf.py`

## Rollback

- **Last-known-good:** prior commit on `main` (per `git log`).
- **Revert command:** `git revert <sha> && git push origin main` —
  GitHub Pages will rebuild on push.
- **Data reverse:** restaurant data is hard-coded in `index.html`;
  rollback is byte-clean.

## Upstream deps

- **Amex Gourmet Club PDF** — external annual artifact at
  `americanexpress.com/.../TnCs_AmexGourmetClub2026.pdf` (URL changes
  each year). Source of truth for restaurant list.
- **Leaflet.js** — included via CDN in `index.html`. No build step.
- **Python** (`pypdf` or equivalent) — for `download_pdf.py` annual
  refresh.

## Downstream consumers

End users (David + share-link recipients) browsing the deployed map.
No other projects depend on this one.

## Invariants

- Single-file webapp — keep all HTML/CSS/JS inline (no build step).
- No backend — pure static; never add server-side calls.
- Restaurant data lives IN `index.html` (not external); rebuild via
  `download_pdf.py` for annual updates.

---

## Operational state — 2026-05-17 (Layer 2 baseline)

Initial fill from persona's Layer 2 portfolio sweep (Claude Code direct
read, not a live recon dispatch). Sparse CLAUDE.md (this file pre-dates
the persona fit-standard); the standard sections aren't all present.

- Project consists of `index.html` (vanilla HTML/JS + Leaflet map) +
  `download_pdf.py` (Python PDF fetcher). Deployed to GitHub Pages
  per persona ECOLOGY §1 (annual artifact, 2026 edition).
- Annual lifecycle: when Amex publishes a new year's PDF, re-run
  `download_pdf.py` + re-process restaurant data + redeploy.
- No backend, no DB, no build step.

## Dispatch usage pattern (from claude.ai)

**Rare dispatch target** — annual artifact, mostly redeployed once a
year when Amex publishes the new gourmet club PDF.

Tool: `dispatch_to_claude_code(target_repo, plan_md, gate="human", exec_mode="focused")`
- `target_repo: "C:\\Users\\david\\projects_c\\foodmap"`
- `exec_mode: "focused"`

Common dispatch tasks (rare):

**1. Annual refresh — pull new Amex PDF + reprocess**
```
cd C:\Users\david\projects_c\foodmap
python download_pdf.py
# Re-parse + re-geocode + update index.html data
```

**2. Local preview**
```
cd C:\Users\david\projects_c\foodmap
python -m http.server 8000
# Open http://localhost:8000/
```

**3. Deploy to GitHub Pages**
```
cd C:\Users\david\projects_c\foodmap
git push origin main    # GitHub Pages auto-builds from main
```

Prerequisites: Python (for download_pdf.py); GitHub Pages enabled on
the repo's main branch.

Per ECOLOGY BI-35: Stella cites this section when dispatching here.
