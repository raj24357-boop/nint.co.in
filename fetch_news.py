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
        
        # Taking top 4 breaking stories from each category to fetch around 15+ live items
        for item in items[:4]:
            title = item.find('title').text if item.find('title') is not None else "Breaking News Update"
            link = item.find('link').text if item.find('link') is not None else "#"
            desc = item.find('description').text if item.find('description') is not None else "Click the title link to read full coverage on the network."
            
            if desc and "<" in desc:
                desc = desc.split('<')[0] # Clean any raw HTML tags inside RSS feed
            
            # Premium Unsplash Stock Images perfectly matching the specific news category
            img_url = "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=600" # Default
            if "markets" in url:
                img_url = "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=600" # Stocks
            elif "entertainment" in url:
                img_url = "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=600" # Movies
            elif "sports" in url:
                img_url = "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=600" # Sports
            elif "india-news" in url:
                img_url = "https://images.unsplash.com/photo-1541535650810-10d26f5c2ab3?w=600" # Politics

            articles_html += f"""
            <div class="card">
                <img src="{img_url}" alt="News Image" style="width:100%; max-height:280px; object-fit:cover; border-radius:6px; margin-bottom:15px;">
                <h2><a href="{link}" target="_blank" style="text-decoration:none; color:#1a1a1a;">{title}</a></h2>
                <span class="date">{category.upper()} • LIVE SYNC UPDATE</span>
                <p>{desc[:250]}...</p>
            </div>
            """
            count += 1
    except Exception as e:
        print(f"Error fetching data from {category}: {e}")

# Generating full updated index.html layout design
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NINT - Live Automated Premium News Portal</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f4f4f9; color: #333; }}
        header {{ background-color: #1a1a1a; color: white; padding: 30px 0; text-align: center; }}
        header h1 {{ margin: 0; font-size: 2.8em; letter-spacing: 2px; text-transform: uppercase; }}
        header p {{ color: #ccc; font-size: 1.1em; }}
        .nav {{ background-color: #d32f2f; overflow: hidden; display: flex; justify-content: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .nav a {{ color: white; text-align: center; padding: 15px 25px; text-decoration: none; font-weight: bold; transition: 0.3s; }}
        .nav a:hover {{ background-color: #b71c1c; }}
        .container {{ max-width: 1100px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: 2.5fr 1fr; gap: 30px; }}
        .card {{ background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 25px; border-top: 4px solid #d32f2f; }}
        .card h2 {{ color: #1a1a1a; margin-top: 0; font-size: 1.8em; line-height: 1.3; }}
        .date {{ color: #d32f2f; font-size: 0.9em; font-weight: bold; margin-bottom: 15px; display: block; }}
        .card p {{ line-height: 1.6; font-size: 1.05em; color: #444; }}
        .sidebar .card {{ border-top: 4px solid #333; }}
        .sidebar h3 {{ margin-top: 0; color: #1a1a1a; }}
        .sidebar ul {{ list-style-type: none; padding: 0; }}
        .sidebar li {{ padding: 12px 0; border-bottom: 1px solid #eee; font-size: 0.95em; line-height: 1.4; }}
        footer {{ background-color: #1a1a1a; color: white; text-align: center; padding: 20px 0; margin-top: 40px; }}
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
    <p>&copy; 2026 NINT Live News Engine. Built for growth.</p>
</footer>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Successfully auto-updated index.html with live media assets!")
