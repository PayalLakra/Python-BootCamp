import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

# Find the article titles using the new structure
article_tags = soup.select(".titleline a")

article_texts = []
article_links = []

for tag in article_tags:
    article_texts.append(tag.getText())
    article_links.append(tag.get("href"))

# Check if anything was found before accessing by index
if article_texts:
    top_article_text = article_texts[0]
    top_article_link = article_links[0]

    # Upvotes (not directly linked to the title, so this is just the first one)
    article_upvotes = soup.find_all(name="span", class_="score")
    top_article_upvote = article_upvotes[0].getText() if article_upvotes else "No upvotes found"

    print(top_article_text)
    print(top_article_link)
    print(top_article_upvote)
else:
    print("No articles found. HTML structure may have changed.")