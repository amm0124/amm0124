import feedparser, time

URL = "https://amm0124.github.io/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

# Read the existing file and remove the last 8 lines
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Save all but the last 8 lines
lines = lines[:-8]

# Write the updated content back to the file
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)

markdown_text = """
## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        print(feed_date, markdown_text)
     
        
f = open("README.md", mode="a", encoding="utf-8")
f.write(markdown_text)
f.close()
