import urllib.request
import os
import ssl

os.makedirs('C:/Users/david/projects_c/foodmap', exist_ok=True)

url = 'https://www.americanexpress.com/content/dam/amex/hk/benefits/pdf/TnCs_AmexGourmetClub2026.pdf'
output = 'C:/Users/david/projects_c/foodmap/AmexGourmetClub2026.pdf'

ctx = ssl.create_default_context()
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as response:
    data = response.read()
    with open(output, 'wb') as f:
        f.write(data)
    print(f'Downloaded {len(data)} bytes to {output}')
