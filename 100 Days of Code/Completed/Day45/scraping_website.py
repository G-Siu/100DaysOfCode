from bs4 import BeautifulSoup
import requests

r = requests.get("https://news.ycombinator.com/")
yc_webpage = r.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# article_tag = soup.select_one(selector=".titleline a")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.select_one(selector=".score").getText()

article_texts = []
article_links = []
articles = soup.select(selector=".titleline")
for article_tag in articles:
    text = article_tag.find(name="a").getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)

highest_upvote = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_upvote])
print(article_links[highest_upvote])

#  /robots.txt to see what's allowed to be scraped