import requests
import xml.etree.ElementTree as ET

# News sources (Hindustan Times, Livemint public RSS feeds)
feeds = {
    "Politics & National": "https://www.hindustantimes.com/rss/india-news",
    "Stocks & Business": "https://www.livemint.com/rss/markets",
    "Movies & Cinema": "https://www.hindustantimes.com/rss/entertainment",
    "Sports & Games": "https://www.hindustantimes.com/rss/sports"
}

articles_html = ""
count = 0

for category, url in feeds.items():
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        root = ET.fromstring(response.content)
        items = root.findall('.//item')
        
        for item in items[:4]:
            title = item.find('title').text if item.find('title') is not None else "Breaking News Update"
            link = item.find('link').text if item.find('link') is not None else "#"
            desc = item.find('description').text if item.find('description') is not None else "Click the title link to read full coverage on the network."
            
            if desc and "<" in desc:
                desc = desc.split('<')[0]
            
            # Premium Matching Thumbnails
            img_url = "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=600"
            if "markets" in url:
                img_url = "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=600"
            elif "entertainment" in url:
                img_url = "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=600"
            elif "sports" in url:
                img_url = "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=600"
            elif "india-news" in url:
                img_url = "https://images.unsplash.com/photo-1541535650810-10d26f5c2ab3?w=600"

            articles_html += f"""
            <div class="card">
                <div class="thumbnail-wrapper">
                    <img src="{img_url}" alt="News Image" class="news-img">
                </div>
                <span class="date">{category.upper()} • LIVE SYNC</span>
                <h2><a href="{link}" target="_blank">{title}</a></h2>
                <p>{desc[:220]}...</p>
                <a href="{link}" target="_blank" class="read-btn">Read Full Story →</a>
            </div>
            """
            count += 1
    except Exception as e:
        print(f"Error fetching data from {category}: {e}")

# High-converting UI Layout
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NINT - Premium Automated News Portal</title>
    <style>
        body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; background-color: #f7f9fc; color: #222; }}
        header {{ background-color: #111111; color: white; padding: 35px 0; text-align: center; border-bottom: 5px solid #d32f2f; }}
        header h1 {{ margin: 0; font-size: 3em; letter-spacing: 3px; font-weight: 900; text-transform: uppercase; }}
        header p {{ color: #bbb; font-size: 1.1em; margin-top: 5px; font-weight: 400; }}
        .nav {{ background-color: #ffffff; overflow: hidden; display: flex; justify-content: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 1000; }}
        .nav a {{ color: #333; text-align: center; padding: 18px 25px; text-decoration: none; font-weight: 700; font-size: 0.95em; text-transform: uppercase; transition: 0.2s; }}
        .nav a:hover {{ color: #d32f2f; background-color: #fcfcfc; }}
        .container {{ max-width: 1150px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: 2.4fr 1fr; gap: 35px; }}
        .card {{ background: white; padding: 0; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); margin-bottom: 30px; overflow: hidden; transition: 0.3s; border: 1px solid #eef2f6; }}
        .card:hover {{ transform: translateY(-4px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); }}
        .thumbnail-wrapper {{ width: 100%; max-height: 280px; overflow: hidden; background-color: #eee; }}
        .news-img {{ width: 100%; height: 280px; object-fit: cover; transition: transform 0.5s ease; }}
        .card:hover .news-img {{ transform: scale(1.04); }}
        .card h2 {{ color: #111; margin: 0 0 12px 0; font-size: 1.7em; line-height: 1.3; font-weight: 800; }}
        .card h2 a {{ color: #111; text-decoration: none; transition: 0.2s; }}
        .card h2 a:hover {{ color: #d32f2f; }}
        .card p {{ line-height: 1.6; font-size: 1.05em; color: #555; margin-bottom: 20px; }}
        .date {{ color: #d32f2f; font-size: 0.85em; font-weight: 800; letter-spacing: 1px; display: block; margin-bottom: 10px; text-transform: uppercase; }}
        .card-content {{ padding: 25px; }}
        /* Adjust padding since layout has no inner container in string builder */
        .card h2, .card p, .card .date, .card .read-btn {{ margin-left: 25px; margin-right: 25px; }}
        .card h2 {{ margin-top: 15px; }}
        .read-btn {{ display: inline-block; background-color: #111; color: white; padding: 10px 20px; text-decoration: none; font-weight: 700; font-size: 0.9em; border-radius: 6px; margin-bottom: 25px; transition: 0.2s; }}
        .read-btn:hover {{ background-color: #d32f2f; }}
        .sidebar .card {{ border-top: 4px solid #111; padding: 25px; }}
        .sidebar h3 {{ margin-top: 0; color: #111; font-size: 1.3em; font-weight: 800; border-bottom: 2px solid #111; padding-bottom: 10px; }}
        .sidebar ul {{ list-style-type: none; padding: 0; margin: 15px 0 0 0; }}
        .sidebar li {{ padding: 12px 0; border-bottom: 1px solid #edf2f7; font-size: 0.95em; line-weight: 1.4; font-weight: 600; color: #444; }}
        footer {{ background-color: #111; color: #999; text-align: center; padding: 25px 0; margin-top: 50px; font-size: 0.9em; }}
        @media (max-width: 768px) {{ .container {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>

<header>
    <h1>NINT.CO.IN</h1>
    <p>Live AI Automated News Feed • No Ads • Clean Experience</p>
</header>

<div class="nav">
    <a href="#">Home</a>
    <a href="#">Politics</a>
    <a href="#">Business & Stocks</a>
    <a href="#">Movies</a>
    <a href="#">Sports</a>
</div>

<div class="container">
    <div class="main-content">
        {articles_html}
    </div>
    
    <div class="sidebar">
        <div class="card">
            <h3>Live Engine Network</h3>
            <ul>
                <li>• Sources: Hindustan Times, Livemint</li>
                <li>• Automation Loop: Active</li>
                <li>• Refresh Rate: Every 15 Minutes</li>
                <li>• Clean Growth Phase: Active (No Ads)</li>
                <li>• Total Feeds: {count} Active Stories</li>
            </ul>
        </div>
    </div>
</div>

<footer>
    <p>&copy; 2026 NINT Live News Engine. Premium Reader Mode.</p>
</footer>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Successfully optimized UI for high user retention!")
