# foodmap

Single-page Leaflet map of Amex Platinum Gourmet Club Hong Kong restaurants.

**2026 edition** — refreshed annually around Jan/Feb with the new Amex statement. Live at GitHub Pages.

## Build inputs (for next year's refresh)

- `claude.md` — goal spec for the build
- `download_pdf.py` — one-shot fetcher for the Amex PDF
- `pdf_text.txt` — extracted text from the 2026 PDF (intermediate)
- `index.html` — final shipped artifact (hardcoded restaurant table + UI)

The raw `AmexGourmetClub2026.pdf` is intentionally **not** committed (financial-data hygiene). Re-fetch via `download_pdf.py` or the Amex link in `claude.md`.
