import requests
import xml.etree.ElementTree as ET

# News sources (Hindustan Times, Mint, Deccan, etc RSS Feeds)
feeds = {
    "Tech & Business": "https://www.livemint.com/rss/news",
    "Global & Politics": "https://www.hindustantimes.com/rss/world-news",
    "Sports & Entertainment": "https://www.hindustantimes.com/rss/sports"
}

news_html = ""

for category, url in feeds.items():
    try:
        response = requests.get(url, timeout=10)
        root = ET.fromstring(response.content)
        
        # Top 5 stories from each channel to make total 15 news items
        for item in root.findall('.//item')[:5]:
            title = item.find('title').text
            link = item.find('link').text
            desc = item.find('description').text if item.find('description') is not None else "Click to read full story."
            
            # Placeholder premium news images matching the topics
            image_url = "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=500" # Default News Image
            if "sport" in url:
                image_url = "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=500"
            elif "mint" in url:
                image_url = "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=500"

            news_html += f'''
            <div class="card">
                <img src="{image_url}" alt="News Image" style="width:100%; max-height:250px; object-fit:cover; border-radius:6px; margin-bottom:15px;">
                <h2><a href="{link}" target="_blank" style="text-decoration:none; color:#1a1a1a;">{title}</a></h2>
                <span class="date">{category.upper()} • JUST NOW</span>
                <p>{desc[:200]}...</p>
            </div>
            '''
    except Exception as e:
        print(f"Error fetching {category}: {e}")

# Base HTML Template update cheyadam
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Dynamic content block update cheyadam
# (Make sure your index.html has a placeholder comment or we rewrite the content container)
