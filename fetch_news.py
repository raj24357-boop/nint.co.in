import requests
import xml.etree.ElementTree as ET
import re
from datetime import datetime

# Telangana Regional & Hyper-Local Targeted Feeds
feeds = {
    "రాజకీయాలు": "https://news.google.com/rss/search?q=Telangana+Politics+OR+TRS+OR+BRS+OR+Congress+Congress+Telangana&hl=te&gl=IN&ceid=IN:te",
    "జిల్లా వార్తలు": "https://news.google.com/rss/search?q=Telangana+Districts+OR+Warangal+OR+Bhupalpally+OR+Karimnagar&hl=te&gl=IN&ceid=IN:te",
    "రైతు లోకం & క్రైమ్": "https://news.google.com/rss/search?q=Telangana+Crime+OR+Telangana+Farmers+OR+Agriculture&hl=te&gl=IN&ceid=IN:te",
    "బిజినెస్ & మార్కెట్": "https://news.google.com/rss/search?q=Hyderabad+Business+OR+Telangana+Market+Prices&hl=te&gl=IN&ceid=IN:te"
}

hero_html = ""
grid_html = ""
count = 0
current_date = datetime.now().strftime("%d-%m-%Y")

# Common Telangana Locations for fallback tagging
districts = ["భూపాలపల్లి", "కటారం", "వరంగల్", "కరీంనగర్", "హైదరాబాద్", "ఖమ్మం", "నల్గొండ", "నిజామాబాద్", "మెదక్", "ఆదిలాబాద్"]

for category, url in feeds.items():
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        root = ET.fromstring(response.content)
        items = root.findall('.//item')
        
        for index, item in enumerate(items[:4]):
            title = item.find('title').text if item.find('title') is not None else ""
            link = item.find('link').text if item.find('link') is not None else "#"
            desc = item.find('description').text if item.find('description') is not None else ""
            
            title = re.sub(r'\s-\s.*$', '', title)
            if desc and "<" in desc:
                desc = desc.split('<')[0]
            
            # Extract or assign a local area/district dynamically
            area_tag = "తెలంగాణ"
            for dist in districts:
                if dist in title or dist in desc:
                    area_tag = dist
                    break
            if area_tag == "తెలంగాణ" and category == "జిల్లా వార్తలు":
                area_tag = "జయశంకర్ భూపాలపల్లి"

            # Premium Graphic Assets matching local content
            img_url = "https://images.unsplash.com/photo-1541535650810-10d26f5c2ab3?w=600" # Default
            if category == "రాజకీయాలు":
                img_url = "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?w=600"
            elif category == "రైతు లోకం & క్రైమ్":
                img_url = "https://images.unsplash.com/photo-1593113598332-cd288d649433?w=600" if "Crime" in url else "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=600"
            elif category == "బిజినెస్ & మార్కెట్":
                img_url = "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600"

            # Top 2 Stories go into the Massive High-Impact Hero Section
            if count < 2 and category == "రాజకీయాలు":
                hero_html += f"""
                <div class="hero-card">
                    <img src="{img_url}" alt="NINT Live">
                    <div class="hero-overlay">
                        <span class="location-badge">📍 {area_tag} • {current_date}</span>
                        <h2><a href="{link}" target="_blank">{title}</a></h2>
                        <p>{desc[:150]}...</p>
                        <a href="{link}" target="_blank" class="tg-btn">ఇప్పుడే చదవండి →</a>
                    </div>
                </div>
                """
            else:
                # Other stories go into a clean, professional news grid
                grid_html += f"""
                <div class="news-grid-card" data-cat="{category}">
                    <img src="{img_url}" alt="News">
                    <div class="grid-card-body">
                        <span class="grid-meta">📍 {area_tag} | {current_date} | <span class="cat-tag">{category}</span></span>
                        <h3><a href="{link}" target="_blank">{title}</a></h3>
                        <p>{desc[:120]}...</p>
                    </div>
                </div>
                """
            count += 1
    except Exception as e:
        print(f"Error compilation: {e}")

# High-Level Professional Enterprise UI Layout
full_html = f"""<!DOCTYPE html>
<html lang="te">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NINT - తెలంగాణ లైవ్ న్యూస్ పోర్టల్</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;700;900&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Noto Sans Telugu', 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; line-height: 1.5; }}
        
        /* Corporate Slate Header */
        header {{ background-color: #0f172a; color: white; padding: 25px 20px; text-align: center; border-bottom: 4px solid #dc2626; }}
        header h1 {{ font-size: 2.8em; font-weight: 900; letter-spacing: 2px; color: #ffffff; }}
        header p {{ color: #94a3b8; font-size: 1.1em; margin-top: 5px; font-weight: bold; }}
        
        .container {{ max-width: 1250px; margin: 30px auto; padding: 0 20px; }}
        
        /* Massive Highlight Headline Section */
        .breaking-hero-container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-bottom: 40px; }}
        .hero-card {{ position: relative; border-radius: 14px; overflow: hidden; height: 420px; box-shadow: 0 10px 25px rgba(0,0,0,0.15); }}
        .hero-card img {{ width: 100%; height: 100%; object-fit: cover; }}
        .hero-overlay {{ position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(15,23,42,0.95), rgba(15,23,42,0.4), transparent); padding: 30px; color: white; }}
        .hero-overlay h2 {{ font-size: 1.8em; font-weight: 900; line-height: 1.4; margin: 10px 0; }}
        .hero-overlay h2 a {{ color: white; text-decoration: none; }}
        .hero-overlay p {{ color: #cbd5e1; font-size: 1.05em; margin-bottom: 15px; }}
        .location-badge {{ background-color: #dc2626; color: white; padding: 5px 12px; border-radius: 6px; font-size: 0.85em; font-weight: bold; display: inline-block; }}
        
        .tg-btn {{ display: inline-block; background-color: white; color: #0f172a; padding: 8px 18px; text-decoration: none; font-weight: bold; border-radius: 6px; font-size: 0.9em; }}
        
        /* Category Navigation Bar */
        .section-title {{ font-size: 1.6em; font-weight: 900; color: #0f172a; margin-bottom: 20px; padding-left: 10px; border-left: 5px solid #dc2626; text-transform: uppercase; }}
        
        /* Professional Compact Grid Grid Layout */
        .news-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 25px; }}
        .news-grid-card {{ background: white; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); display: flex; flex-direction: column; transition: 0.3s; }}
        .news-grid-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 20px -3px rgba(0,0,0,0.1); }}
        .news-grid-card img {{ width: 100%; height: 180px; object-fit: cover; }}
        
        .grid-card-body {{ padding: 20px; display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between; }}
        .grid-meta {{ font-size: 0.8em; color: #64748b; font-weight: bold; margin-bottom: 8px; display: block; }}
        .cat-tag {{ color: #dc2626; }}
        .news-grid-card h3 {{ font-size: 1.2em; font-weight: 800; color: #0f172a; line-height: 1.4; margin-bottom: 10px; }}
        .news-grid-card h3 a {{ color: #0f172a; text-decoration: none; }}
        .news-grid-card h3 a:hover {{ color: #dc2626; }}
        .news-grid-card p {{ color: #475569; font-size: 0.95em; line-height: 1.5; }}
        
        footer {{ background-color: #0f172a; color: #94a3b8; text-align: center; padding: 25px 0; margin-top: 60px; font-weight: bold; border-top: 4px solid #dc2626; }}
        
        @media (max-width: 850px) {{
            .breaking-hero-container {{ grid-template-columns: 1fr; }}
            .hero-card {{ height: 350px; }}
            .hero-overlay h2 {{ font-size: 1.4em; }}
        }}
    </style>
</head>
<body>

<header>
    <h1>NINT NEWS NETWORK</h1>
    <p>తెలంగాణ హైపర్-లోకల్ ఆటోమేటెడ్ న్యూస్ డ్యాష్‌బోర్డ్</p>
</header>

<div class="container">
    <div class="section-title">🔥 ముఖ్యమైన వార్తలు (Top Highlights)</div>
    <div class="breaking-hero-container">
        {hero_html}
    </div>

    <div class="section-title">📰 తాజా సమాచారం (Latest Local Updates)</div>
    <div class="news-grid">
        {grid_html}
    </div>
</div>

<footer>
    <p>&copy; 2026 NINT News Network • తెలంగాణ బ్రీఫింగ్ ఇంజిన్</p>
</footer>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Telangana Hyperlocal Professional Layout Successfully Synced!")
