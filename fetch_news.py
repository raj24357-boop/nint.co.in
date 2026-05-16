import requests
import xml.etree.ElementTree as ET
import re

# Google News Telugu Trending & National RSS Feeds
feeds = {
    "దేశం - విదేశం (Top Stories)": "https://news.google.com/rss?hl=te&gl=IN&ceid=IN:te",
    "బిజినెస్ & స్టాక్స్ (Business)": "https://news.google.com/rss/sections/ certain/CAAqBwgKMJyvCwgwv6gD?hl=te&gl=IN&ceid=IN:te",
    "సినిమా & స్పోర్ట్స్ (Entertainment)": "https://news.google.com/rss/sections/ certain/CAAqBwgKMMq9Cwgw76gD?hl=te&gl=IN&ceid=IN:te"
}

articles_html = ""
count = 0

for category, url in feeds.items():
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        root = ET.fromstring(response.content)
        items = root.findall('.//item')
        
        # Taking top 5 burning topics from each category (Total 15)
        for item in items[:5]:
            title = item.find('title').text if item.find('title') is not None else "బ్రేకింగ్ న్యూస్ అప్‌డేట్"
            link = item.find('link').text if item.find('link') is not None else "#"
            desc = item.find('description').text if item.find('description') is not None else "పూర్తి వార్త చదవడానికి లింక్ క్లిక్ చేయండి."
            
            # Cleaning source tags from Google titles (e.g., "- Eenadu")
            title = re.sub(r'\s-\s.*$', '', title)
            if desc and "<" in desc:
                desc = desc.split('<')[0]
            if len(desc.strip()) < 5:
                desc = "దేశంలో జరుగుతున్న ఈ లేటెస్ట్ ట్రెండింగ్ టాపిక్ కి సంబంధించిన పూర్తి వివరాలు నెట్‌వర్క్ లో అందుబాటులో ఉన్నాయి..."

            # Premium Category-based Thumbnails for high CTR clicks
            img_url = "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=600" # Default
            if "CAAqBwgKMJyvCwgwv6gD" in url:
                img_url = "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600" # Business/Stocks
            elif "CAAqBwgKMMq9Cwgw76gD" in url:
                img_url = "https://images.unsplash.com/photo-1478720143033-6a972678aa30?w=600" # Movies/Cinema
            elif "news" in category:
                img_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600" # Tech/National

            articles_html += f"""
            <div class="card">
                <div class="thumbnail-wrapper">
                    <img src="{img_url}" alt="NINT News">
                </div>
                <div class="card-content">
                    <span class="date">{category.upper()} • లైవ్ అప్‌డేట్</span>
                    <h2><a href="{link}" target="_blank">{title}</a></h2>
                    <p>{desc[:180]}...</p>
                    <a href="{link}" target="_blank" class="read-btn">పూర్తిగా చదవండి →</a>
                </div>
            </div>
            """
            count += 1
    except Exception as e:
        print(f"Error fetching data: {e}")

# High-converting Telugu UI Layout
full_html = f"""<!DOCTYPE html>
<html lang="te">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NINT - లైవ్ తెలుగు న్యూస్ పోర్టల్</title>
    <style>
        body {{ font-family: 'Inter', 'Segoe UI', sans-serif; margin: 0; padding: 0; background-color: #f4f6f9; color: #222; }}
        header {{ background-color: #111111; color: white; padding: 30px 0; text-align: center; border-bottom: 5px solid #d32f2f; }}
        header h1 {{ margin: 0; font-size: 3em; letter-spacing: 2px; font-weight: 900; }}
        header p {{ color: #ccc; font-size: 1.1em; margin-top: 5px; }}
        .nav {{ background-color: #ffffff; overflow: hidden; display: flex; justify-content: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 1000; }}
        .nav a {{ color: #333; text-align: center; padding: 18px 25px; text-decoration: none; font-weight: bold; font-size: 1em; transition: 0.2s; }}
        .nav a:hover {{ color: #d32f2f; background-color: #fcfcfc; }}
        .container {{ max-width: 1150px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: 2.4fr 1fr; gap: 35px; }}
        .card {{ background: white; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); margin-bottom: 30px; overflow: hidden; transition: 0.3s; border: 1px solid #eef2f6; }}
        .card:hover {{ transform: translateY(-4px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); }}
        .thumbnail-wrapper {{ width: 100%; max-height: 260px; overflow: hidden; }}
        .thumbnail-wrapper img {{ width: 100%; height: 260px; object-fit: cover; transition: transform 0.5s ease; }}
        .card:hover .thumbnail-wrapper img {{ transform: scale(1.03); }}
        .card-content {{ padding: 25px; }}
        .card h2 {{ color: #111; margin: 0 0 12px 0; font-size: 1.6em; line-height: 1.4; font-weight: 800; }}
        .card h2 a {{ color: #111; text-decoration: none; transition: 0.2s; }}
        .card h2 a:hover {{ color: #d32f2f; }}
        .card p {{ line-height: 1.6; font-size: 1.05em; color: #555; margin-bottom: 20px; }}
        .date {{ color: #d32f2f; font-size: 0.85em; font-weight: 800; letter-spacing: 1px; display: block; margin-bottom: 10px; }}
        .read-btn {{ display: inline-block; background-color: #111; color: white; padding: 10px 20px; text-decoration: none; font-weight: bold; font-size: 0.9em; border-radius: 6px; transition: 0.2s; }}
        .read-btn:hover {{ background-color: #d32f2f; }}
        .sidebar .card {{ border-top: 4px solid #111; padding: 25px; }}
        .sidebar h3 {{ margin-top: 0; color: #111; font-size: 1.3em; font-weight: 800; border-bottom: 2px solid #111; padding-bottom: 10px; }}
        .sidebar ul {{ list-style-type: none; padding: 0; margin: 15px 0 0 0; }}
        .sidebar li {{ padding: 12px 0; border-bottom: 1px solid #edf2f7; font-size: 0.95em; font-weight: 600; color: #444; }}
        footer {{ background-color: #111; color: #999; text-align: center; padding: 25px 0; margin-top: 50px; }}
        @media (max-width: 768px) {{ .container {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>

<header>
    <h1>NINT.CO.IN</h1>
    <p>లైవ్ ఆటోమేటెడ్ తెలుగు వార్తలు • క్లీన్ రీడర్ ఎక్స్ పీరియన్స్</p>
</header>

<div class="nav">
    <a href="#">హోమ్</a>
    <a href="#">రాజకీయాలు</a>
    <a href="#">వ్యాపారం & స్టాక్స్</a>
    <a href="#">సినిమాలు</a>
    <a href="#">క్రీడలు</a>
</div>

<div class="container">
    <div class="main-content">
        {articles_html}
    </div>
    
    <div class="sidebar">
        <div class="card">
            <h3>లైవ్ సిస్టమ్ నెట్‌వర్క్</h3>
            <ul>
                <li>• మూలాలు: గూగుల్ న్యూస్ తెలుగు, ఈనాడు ఫీడ్స్</li>
                <li>• ఆటోమేషన్ లూప్: యాక్టివ్</li>
                <li>• రీఫ్రెష్ రేట్: బ్రేకింగ్ అప్‌డేట్స్</li>
                <li>• ప్రస్తుత వార్తలు: {count} టాపిక్స్</li>
            </ul>
        </div>
    </div>
</div>

<footer>
    <p>&copy; 2026 NINT Live News Engine.</p>
</footer>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Telugu automated engine is successfully set up!")
