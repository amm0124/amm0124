import feedparser, time

URL = "https://amm0124.github.io/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

# Read the existing file and remove the last 8 lines
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Save all but the last 8 lines
lines = lines[:-9]

# Write the updated content back to the file
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)

# Create a Markdown table header
markdown_text = """
## ✅ Latest Blog Posts

| Date       | Category | Title |
|------------|----------|-------|
"""  # Table header for blog posts

# Append the blog posts to the table
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        formatted_date = time.strftime('%Y/%m/%d', feed_date)
        title = feed['title']
        link = feed['link']
        # Extract category (if available)
        category = feed['tags'][0]['term'] if 'tags' in feed and len(feed['tags']) > 0 else 'Uncategorized'        
        # Add a row for each blog post
        markdown_text += f"| {formatted_date} | {category} | [{title}]({link}) |\n"

# Append the new content to the README.md file
with open("README.md", mode="a", encoding="utf-8") as f:
    f.write(markdown_text)
