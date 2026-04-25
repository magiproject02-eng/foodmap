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
