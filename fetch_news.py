import requests
import xml.etree.ElementTree as ET
import re

# Premium Feeds for High-CTR Content
feeds = {
    "politics": "https://news.google.com/rss?hl=te&gl=IN&ceid=IN:te",
    "business": "https://news.google.com/rss/sections/ certain/CAAqBwgKMJyvCwgwv6gD?hl=te&gl=IN&ceid=IN:te",
    "movies": "https://news.google.com/rss/sections/ certain/CAAqBwgKMMq9Cwgw76gD?hl=te&gl=IN&ceid=IN:te",
    "sports": "https://news.google.com/rss/sections/ certain/CAAqBwgKMK29Cwgw76gD?hl=te&gl=IN&ceid=IN:te"
}

articles_html = ""
count = 0

for category, url in feeds.items():
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        root = ET.fromstring(response.content)
        items = root.findall('.//item')
        
        # Category wise 5 high-quality breaking items
        for item in items[:5]:
            title = item.find('title').text if item.find('title') is not None else "బ్రేకింగ్ అప్‌డేట్"
            link = item.find('link').text if item.find('link') is not None else "#"
            desc = item.find('description').text if item.find('description') is not None else ""
            
            # Cleaning title & creating a no-sodhi crisp short summary
            title = re.sub(r'\s-\s.*$', '', title)
            if desc and "<" in desc:
                desc = desc.split('<')[0]
            
            if len(desc.strip()) < 10:
                desc = "దేశంలో సంచలనం సృష్టిస్తున్న ఈ ట్రెండింగ్ టాపిక్ కి సంబంధించిన పూర్తి లైవ్ అప్‌డేట్స్ మరియు విశ్లేషణ నెట్‌వర్క్ లో అందుబాటులోకి వచ్చాయి."

            # Premium UI Graphics Assets (Category wise high engaging background tags)
            img_url = "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=600"
            if category == "business":
                img_url = "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600"
            elif category == "movies":
                img_url = "https://images.unsplash.com/photo-1478720143033-6a972678aa30?w=600"
            elif category == "sports":
                img_url = "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=600"
            elif category == "politics":
                img_url = "https://images.unsplash.com/photo-1541535650810-10d26f5c2ab3?w=600"

            articles_html += f"""
            <div class="news-card active-card" data-cat="{category}">
                <div class="thumbnail-box">
                    <img src="{img_url}" alt="NINT News">
                    <span class="badge {category}">{category.upper()}</span>
                </div>
                <div class="news-body">
                    <h2>{title}</h2>
                    <p class="summary-text">⚡ {desc[:150]}...</p>
                    <div class="card-footer">
                        <span class="live-pulse">🔴 LIVE</span>
                        <a href="{link}" target="_blank" class="action-link">పూర్తిగా చదవండి →</a>
                    </div>
                </div>
            </div>
            """
            count += 1
    except Exception as e:
        print(f"Error compiling {category}: {e}")

# High-Retention SPA UI/UX Engine Design
full_html = f"""<!DOCTYPE html>
<html lang="te">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NINT - Premium Live Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }}
        body {{ background-color: #0b0f19; color: #f3f4f6; padding-bottom: 50px; }}
        
        /* Modern Premium Header */
        header {{ background: linear-gradient(135deg, #111827, #1f2937); text-align: center; padding: 40px 20px; border-bottom: 4px solid #ef4444; }}
        header h1 {{ font-size: 3.5em; font-weight: 900; letter-spacing: 4px; color: #ffffff; text-shadow: 0 4px 10px rgba(0,0,0,0.5); }}
        header p {{ color: #9ca3af; font-size: 1.1em; margin-top: 8px; font-weight: 600; letter-spacing: 1px; }}
        
        /* Futuristic Category Filter Pills */
        .filter-navigation {{ display: flex; justify-content: center; gap: 12px; margin: 30px auto; max-width: 800px; padding: 0 20px; flex-wrap: wrap; }}
        .pill-btn {{ background-color: #1f2937; color: #9ca3af; border: 2px solid #374151; padding: 12px 24px; border-radius: 30px; font-weight: 800; cursor: pointer; font-size: 0.95em; transition: all 0.25s ease; text-transform: uppercase; }}
        .pill-btn:hover {{ background-color: #374151; color: #ffffff; }}
        .pill-btn.active-pill {{ background-color: #ef4444; color: #ffffff; border-color: #ef4444; box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4); }}
        
        /* Layout Container */
        .main-layout {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; display: grid; grid-template-columns: 2.5fr 1fr; gap: 35px; }}
        
        /* Grid Cards Interface */
        .news-feed {{ display: grid; grid-template-columns: 1fr; gap: 25px; }}
        .news-card {{ background-color: #111827; border-radius: 16px; overflow: hidden; border: 1px solid #1f2937; display: flex; flex-direction: row; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }}
        .news-card:hover {{ transform: translateY(-5px); border-color: #4b5563; box-shadow: 0 15px 30px rgba(0,0,0,0.4); }}
        
        .thumbnail-box {{ width: 35%; position: relative; overflow: hidden; background-color: #1f2937; }}
        .thumbnail-box img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }}
        .news-card:hover .thumbnail-box img {{ transform: scale(1.05); }}
        
        /* Badges */
        .badge {{ position: absolute; top: 15px; left: 15px; padding: 6px 12px; border-radius: 6px; font-size: 0.75em; font-weight: 900; color: white; letter-spacing: 1px; }}
        .politics {{ background-color: #3b82f6; }}
        .business {{ background-color: #10b981; }}
        .movies {{ background-color: #8b5cf6; }}
        .sports {{ background-color: #f59e0b; }}
        
        /* Content Body */
        .news-body {{ width: 65%; padding: 25px; display: flex; flex-direction: column; justify-content: space-between; }}
        .news-body h2 {{ color: #ffffff; font-size: 1.45em; font-weight: 800; line-height: 1.4; margin-bottom: 12px; }}
        .summary-text {{ color: #9ca3af; font-size: 1.05em; line-height: 1.6; margin-bottom: 15px; font-weight: 500; }}
        
        .card-footer {{ display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #1f2937; padding-top: 15px; }}
        .live-pulse {{ font-size: 0.85em; font-weight: 900; color: #ef4444; letter-spacing: 1px; display: flex; align-items: center; gap: 5px; }}
        .action-link {{ color: #ef4444; text-decoration: none; font-weight: 800; font-size: 0.95em; transition: 0.2s; }}
        .action-link:hover {{ color: #ffffff; }}
        
        /* Sidebar Dynamic Widget */
        .sidebar-panel {{ background-color: #111827; border-radius: 16px; padding: 25px; border: 1px solid #1f2937; height: fit-content; }}
        .sidebar-panel h3 {{ color: #ffffff; font-size: 1.25em; font-weight: 900; border-bottom: 2px solid #ef4444; padding-bottom: 10px; margin-bottom: 15px; }}
        .sidebar-panel ul {{ list-style: none; }}
        .sidebar-panel li {{ padding: 12px 0; border-bottom: 1px solid #1f2937; color: #9ca3af; font-size: 0.95em; font-weight: 600; }}
        
        /* Active/Inactive state classes for SPA mechanism */
        .news-card {{ display: flex !important; }}
        .news-card.hidden-card {{ display: none !important; }}
        
        @media (max-width: 900px) {{
            .main-layout {{ grid-template-columns: 1fr; }}
            .news-card {{ flex-direction: column; }}
            .thumbnail-box {{ width: 100%; height: 200px; }}
            .news-body {{ width: 100%; }}
        }}
    </style>
</head>
<body>

<header>
    <h1>NINT.CO.IN</h1>
    <p>⚡ FAST • CRISP • AUTOMATED TELEGU INSIGHTS</p>
</header>

<div class="filter-navigation">
    <button class="pill-btn active-pill" onclick="filterCat('all')">🔥 అంతా ఒకేచోట</button>
    <button class="pill-btn" onclick="filterCat('politics')">🏛️ రాజకీయాలు</button>
    <button class="pill-btn" onclick="filterCat('business')">📈 బిజినెస్ & స్టాక్స్</button>
    <button class="pill-btn" onclick="filterCat('movies')">🎬 సినిమా ముచ్చట్లు</button>
    <button class="pill-btn" onclick="filterCat('sports')">🏆 క్రీడలు</button>
</div>

<div class="main-layout">
    <div class="news-feed" id="feed-container">
        {articles_html}
    </div>
    
    <div class="sidebar-panel">
        <h3>⚡ లైవ్ ఆటోమేషన్ ఇంజిన్</h3>
        <ul>
            <li>• అప్‌డేట్ ఫ్రీక్వెన్సీ: సూపర్ ఫాస్ట్</li>
            <li>• యాడ్స్ స్థితి: 100% క్లీన్ (No Ads)</li>
            <li>• స్మార్ట్ ఫిల్టర్స్: యాక్టివ్</li>
            <li>• లోడింగ్ స్పీడ్: 0.2 సెకన్లు</li>
            <li>• మొత్తం లైవ్ స్టోరీలు: {count} ఫీడ్స్</li>
        </ul>
    </div>
</div>

<script>
function filterCat(cat) {{
    // Update active pill styling
    const buttons = document.querySelectorAll('.pill-btn');
    buttons.forEach(btn => btn.classList.remove('active-pill'));
    event.currentTarget.classList.add('active-pill');
    
    // Smooth SPA filter animation logic
    const cards = document.querySelectorAll('.news-card');
    cards.forEach(card => {{
        if(cat === 'all' || card.getAttribute('data-cat') === cat) {{
            card.classList.remove('hidden-card');
        }} else {{
            card.classList.add('hidden-card');
        }}
    }});
}}
</script>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Futuristic High-Retention Premium SPA UI Successfully Written!")
