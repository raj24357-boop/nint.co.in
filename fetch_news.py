import requests
import xml.etree.ElementTree as ET
import re
import os
from datetime import datetime

# Hyperlocal Telangana Feeds
feeds = {
    "రాజకీయాలు": "https://news.google.com/rss/search?q=Telangana+TRS+BRS+Congress+Revanth+KCR+Telangana+Politics&hl=te&gl=IN&ceid=IN:te",
    "జిల్లా వార్తలు": "https://news.google.com/rss/search?q=Telangana+Local+News+OR+Peddapalli+OR+Kataram+OR+Bhupalpally+OR+Warangal&hl=te&gl=IN&ceid=IN:te",
    "క్రైమ్ & రైతు": "https://news.google.com/rss/search?q=Telangana+Crime+OR+Telangana+Farmers+OR+Agriculture&hl=te&gl=IN&ceid=IN:te",
    "మార్కెట్": "https://news.google.com/rss/search?q=Hyderabad+Market+Prices+Gold+OR+Telangana+Crop+Rates&hl=te&gl=IN&ceid=IN:te"
}

# Read existing old news from index.html to push them down
old_html = ""
if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        old_html = f.read()

old_feeds_match = re.search(r'(.*?)', old_html, re.DOTALL)
old_feeds_content = old_feeds_match.group(1) if old_feeds_match else ""

new_articles_html = ""
current_date = datetime.now().strftime("%d-%m-%Y")
locations = ["పెద్దపల్లి", "కటారం", "భూపాలపల్లి", "వరంగల్", "హైదరాబాద్", "కరీంనగర్", "ఖమ్మం", "నల్గొండ"]

for category, url in feeds.items():
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
        root = ET.fromstring(response.content)
        items = root.findall('.//item')
        
        for item in items[:4]:
            title = item.find('title').text if item.find('title') is not None else ""
            link = item.find('link').text if item.find('link') is not None else "#"
            desc = item.find('description').text if item.find('description') is not None else ""
            
            title = re.sub(r'\s-\s.*$', '', title)
            
            # Anti-Duplicate Check
            if title in old_html or link in old_html:
                continue

            match = re.search(r'>([^<]+)</a>', desc)
            if match:
                desc = match.group(1).strip()
            if len(desc) < 10 or "&nbsp;" in desc:
                desc = "తెలంగాణలో సంచలనం సృష్టిస్తున్న ఈ లేటెస్ట్ బ్రేకింగ్ టాపిక్ కి సంబంధించిన పూర్తి వివరాలు నెట్‌వర్క్ లో అందుబాటులోకి వచ్చాయి..."

            area_tag = "తెలంగాణ"
            for loc in locations:
                if loc in title or loc in desc:
                    area_tag = loc
                    break
            
            img_url = "https://images.unsplash.com/photo-1541535650810-10d26f5c2ab3?w=600"
            if category == "రాజకీయాలు":
                img_url = "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?w=600"
            elif category == "క్రైమ్ & రైతు":
                img_url = "https://images.unsplash.com/photo-1610473187211-137b0d7715ec?w=600" if "Crime" in url else "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=600"
            elif category == "మార్కెట్":
                img_url = "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600"

            # Clean single quotes in title for JavaScript safety
            safe_title = title.replace("'", "\\'")

            # Build cards with separate action buttons
            new_articles_html += f"""
            <div class="news-card">
                <img src="{img_url}" alt="NINT Local">
                <div class="news-body">
                    <span class="news-meta">📍 {area_tag} | {current_date}</span>
                    <h2>{title}</h2>
                    <p>{desc[:180]}...</p>
                    <div class="card-actions">
                        <a href="{link}" target="_blank" class="read-more-btn">చదవండి →</a>
                        <button class="share-btn" onclick="shareNews('{safe_title}', '{link}')">📲 షేర్</button>
                    </div>
                </div>
            </div>
            """
    except Exception as e:
        print(f"Error compiling {category}: {e}")

# Combine: New News on Top + Old News at bottom
combined_feeds = new_articles_html + old_feeds_content

# Limit total history to top 45 cards
all_cards = re.findall(r'<div class="news-card">.*?</div>\s*</div>\s*</div>', combined_feeds, re.DOTALL)
if not all_cards:
    all_cards = re.findall(r'<div class="news-card">.*?</div>\s*</div>', combined_feeds, re.DOTALL)

final_grid_html = "\n".join(all_cards[:45])
total_count = len(all_cards[:45])

full_html = f"""<!DOCTYPE html>
<html lang="te">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NINT - తెలంగాణ లైవ్ ఫీడ్</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;700;900&family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Noto Sans Telugu', 'Inter', sans-serif; background-color: #f0f2f5; color: #1c1e21; line-height: 1.5; }}
        header {{ background: linear-gradient(135deg, #18191a, #242526); text-align: center; padding: 40px 20px; border-bottom: 5px solid #dc2626; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }}
        header h1 {{ font-size: 3.5em; font-weight: 900; letter-spacing: 3px; color: #ffffff; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }}
        header p {{ color: #a0aab4; font-size: 1.1em; margin-top: 8px; font-weight: bold; }}
        .container {{ max-width: 1300px; margin: 40px auto; padding: 0 20px; }}
        .news-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; }}
        .news-card {{ background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; transition: all 0.3s ease; display: flex; flex-direction: column; }}
        .news-card:hover {{ transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); border-color: #d1d5db; }}
        .news-card img {{ width: 100%; height: 200px; object-fit: cover; }}
        .news-body {{ padding: 25px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; }}
        .news-meta {{ font-size: 0.85em; color: #dc2626; font-weight: 800; text-transform: uppercase; margin-bottom: 10px; display: block; }}
        .news-card h2 {{ color: #1c1e21; font-size: 1.35em; font-weight: 800; line-height: 1.4; margin-bottom: 12px; min-height: 2.8em; }}
        .news-card p {{ color: #4b5563; font-size: 1.02em; line-height: 1.6; margin-bottom: 20px; }}
        
        /* Flexbox structure to keep buttons perfectly aligned */
        .card-actions {{ display: flex; gap: 12px; width: 100%; margin-top: auto; }}
        .read-more-btn {{ flex: 1; text-align: center; background-color: #1c1e21; color: white; padding: 12px 10px; text-decoration: none; font-weight: 700; font-size: 0.9em; border-radius: 8px; transition: 0.2s; }}
        .read-more-btn:hover {{ background-color: #dc2626; }}
        
        /* Share Button Design */
        .share-btn {{ flex: 1; background-color: #25d366; color: white; border: none; padding: 12px 10px; font-weight: 700; font-size: 0.9em; border-radius: 8px; cursor: pointer; transition: 0.2s; }}
        .share-btn:hover {{ background-color: #128c7e; box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3); }}
        
        footer {{ background-color: #18191a; color: #a0aab4; text-align: center; padding: 30px 0; margin-top: 60px; font-weight: bold; border-top: 5px solid #dc2626; }}
    </style>
</head>
<body>

<header>
    <h1>NINT NEWS</h1>
    <p>⚡ తెలంగాణ హైపర్-లోకల్ లైవ్ టైమ్-లైన్ డ్యాష్‌బోర్డ్</p>
</header>

<div class="container">
    <div class="news-grid">
        {final_grid_html}
        </div>
</div>

<footer>
    <p>&copy; 2026 NINT NEWS NETWORK • టోటల్ లైవ్ స్టోరీలు: {total_count}</p>
</footer>

<script>
function shareNews(title, link) {{
    const shareData = {{
        title: title,
        text: title + " \\n\\n👉 పూర్తి వివరాల కోసం NINT News చూడండి: \\n",
        url: link
    }};

    // If mobile device allows native sharing (WhatsApp, Insta, FB list)
    if (navigator.share) {{
        navigator.share(shareData)
            .then(() => console.log('Successfully Shared!'))
            .catch((error) => console.log('Error sharing:', error));
    }} else {{
        // Desktop Fallback: Directly open WhatsApp Web with pre-filled text
        const whatsappUrl = "https://api.whatsapp.com/send?text=" + encodeURIComponent(title + "\\n" + link);
        window.open(whatsappUrl, '_blank');
    }}
}}
</script>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Successfully injected universal social sharing engine!")
            
