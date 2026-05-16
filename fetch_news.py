import requests
import xml.etree.ElementTree as ET
import re
from datetime import datetime

# Hyperlocal Target: Google News Telugu - Regional Feeds
feeds = {
    "రాజకీయాలు": "https://news.google.com/rss/search?q=Telangana+TRS+BRS+Congress+Revanth+KCR+Telangana+Politics&hl=te&gl=IN&ceid=IN:te",
    "జిల్లా వార్తలు": "https://news.google.com/rss/search?q=Telangana+Local+News+OR+Peddapalli+OR+Kataram+OR+Bhupalpally+OR+Warangal&hl=te&gl=IN&ceid=IN:te",
    "క్రైమ్ & రైతు": "https://news.google.com/rss/search?q=Telangana+Crime+OR+Telangana+Farmers+OR+Agriculture&hl=te&gl=IN&ceid=IN:te",
    "మార్కెట్": "https://news.google.com/rss/search?q=Hyderabad+Market+Prices+Gold+OR+Telangana+Crop+Rates&hl=te&gl=IN&ceid=IN:te"
}

grid_html = ""
count = 0
current_date = datetime.now().strftime("%d-%m-%Y")
locations = ["పెద్దపల్లి", "కటారం", "భూపాలపల్లి", "వరంగల్", "హైదరాబాద్", "కరీంనగర్", "ఖమ్మం", "నల్గొండ"]

for category, url in feeds.items():
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
        root = ET.fromstring(response.content)
        items = root.findall('.//item')
        
        # Take top 5 unique hot items per category to build a 20-news dashboard
        for item in items[:5]:
            title = item.find('title').text if item.find('title') is not None else ""
            link = item.find('link').text if item.find('link') is not None else "#"
            desc = item.find('description').text if item.find('description') is not None else ""
            
            # Clean headline and create an engaging 'no sodhi' Telugu Summary
            title = re.sub(r'\s-\s.*$', '', title) # Remove source name like "- Eenadu"
            
            # Use RegEx to parse actual description from messy Google News HTML
            match = re.search(r'>([^<]+)</a>', desc)
            if match:
                desc = match.group(1).strip()
            
            if len(desc) < 10 or "&nbsp;" in desc:
                desc = "తెలంగాణలో సంచలనం సృష్టిస్తున్న ఈ లేటెస్ట్ బ్రేకింగ్ టాపిక్ కి సంబంధించిన పూర్తి వివరాలు మరియు విశ్లేషణ నెట్‌వర్క్ లో అందుబాటులోకి వచ్చాయి..."

            # 1. Hyperlocal Area Tagging Logic
            area_tag = "తెలంగాణ"
            for loc in locations:
                if loc in title or loc in desc:
                    area_tag = loc
                    break
            
            # 2. Live Image Fetching Logic (Simplified for GitHub Actions)
            # Fetch generic high-quality assets matching category as primary image,
            # (Fetching live-time thumbnails needs more complex scraping/time in Actions)
            img_url = "https://images.unsplash.com/photo-1541535650810-10d26f5c2ab3?w=600" # Default
            if category == "రాజకీయాలు":
                img_url = "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?w=600"
            elif category == "క్రైమ్ & రైతు":
                if "Crime" in url or "Murder" in title:
                    img_url = "https://images.unsplash.com/photo-1610473187211-137b0d7715ec?w=600"
                else:
                    img_url = "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=600"
            elif category == "మార్కెట్":
                img_url = "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600"

            grid_html += f"""
            <div class="news-card">
                <img src="{img_url}" alt="NINT Local">
                <div class="news-body">
                    <span class="news-meta">📍 {area_tag} | {current_date}</span>
                    <h2>{title}</h2>
                    <p>{desc[:180]}...</p>
                    <a href="{link}" target="_blank" class="read-more-btn">పూర్తిగా చదవండి (Source) →</a>
                </div>
            </div>
            """
            count += 1
    except Exception as e:
        print(f"Update compilation failed: {e}")

full_html = f"""<!DOCTYPE html>
<html lang="te">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NINT - తెలంగాణ హైపర్-లోకల్ లైవ్ ఫీడ్</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;700;900&family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Noto Sans Telugu', 'Inter', sans-serif; background-color: #f0f2f5; color: #1c1e21; line-height: 1.5; }}
        
        /* Premium Enterprise Slate Header */
        header {{ background: linear-gradient(135deg, #18191a, #242526); text-align: center; padding: 40px 20px; border-bottom: 5px solid #dc2626; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }}
        header h1 {{ font-size: 3.5em; font-weight: 900; letter-spacing: 3px; color: #ffffff; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }}
        header p {{ color: #a0aab4; font-size: 1.1em; margin-top: 8px; font-weight: bold; letter-spacing: 1px; }}
        
        .container {{ max-width: 1300px; margin: 40px auto; padding: 0 20px; }}
        
        /* Futuristic Category Labels Bar */
        .section-nav {{ display: flex; justify-content: center; gap: 15px; margin-bottom: 40px; flex-wrap: wrap; }}
        .cat-pill {{ background-color: #ffffff; color: #4b5563; border: 2px solid #e5e7eb; padding: 12px 24px; border-radius: 30px; font-weight: bold; font-size: 1em; cursor: pointer; transition: 0.2s; }}
        .cat-pill.active {{ background-color: #dc2626; color: #ffffff; border-color: #dc2626; box-shadow: 0 4px 10px rgba(220, 38, 38, 0.3); }}
        
        /* Grid Layout */
        .news-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; }}
        .news-card {{ background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; transition: all 0.3s ease; display: flex; flex-direction: column; }}
        .news-card:hover {{ transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); border-color: #d1d5db; }}
        
        .news-card img {{ width: 100%; height: 200px; object-fit: cover; transition: 0.5s; }}
        .news-card:hover img {{ transform: scale(1.02); }}
        
        .news-body {{ padding: 25px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; }}
        .news-meta {{ font-size: 0.85em; color: #dc2626; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; display: block; }}
        
        .news-card h2 {{ color: #1c1e21; font-size: 1.5em; font-weight: 800; line-height: 1.35; margin-bottom: 12px; }}
        .news-card h2 a {{ color: #1c1e21; text-decoration: none; transition: 0.2s; }}
        .news-card h2 a:hover {{ color: #dc2626; }}
        
        .news-card p {{ color: #4b5563; font-size: 1.05em; line-height: 1.6; margin-bottom: 20px; }}
        
        .read-more-btn {{ display: inline-block; background-color: #1c1e21; color: white; padding: 10px 20px; text-decoration: none; font-weight: 700; font-size: 0.9em; border-radius: 8px; transition: 0.2s; align-self: flex-start; }}
        .read-more-btn:hover {{ background-color: #dc2626; }}
        
        footer {{ background-color: #18191a; color: #a0aab4; text-align: center; padding: 30px 0; margin-top: 60px; font-weight: bold; border-top: 5px solid #dc2626; }}
        
        @media (max-width: 600px) {{
            header h1 {{ font-size: 2.2em; }}
            .news-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>

<header>
    <h1>NINT NEWS</h1>
    <p>⚡ తెలంగాణ హైపర్-లోకల్ ఆటోమేటెడ్ న్యూస్ డ్యాష్‌బోర్డ్</p>
</header>

<div class="container">
    <div class="section-nav">
        <button class="cat-pill active">🔥 అంతా ఒకేచోట</button>
        <button class="cat-pill">🏛️ రాజకీయాలు</button>
        <button class="cat-pill">📍 జిల్లా వార్తలు</button>
        <button class="cat-pill">🚜 క్రైమ్ & రైతు</button>
        <button class="cat-pill">📈 మార్కెట్ రేట్లు</button>
    </div>

    <div class="news-grid">
        {grid_html}
    </div>
</div>

<footer>
    <p>&copy; 2026 NINT NEWS NETWORK • తెలంగాణ ಬ್ರೀಫಿಂಗ್ ఇಂజిన్</p>
</footer>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Telangana Professional Dashoard v2.0 Successfully Synced!")
