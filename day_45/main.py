# check robots.txt     !!!

from bs4 import BeautifulSoup
import requests

# Live Website (will change over time)
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# head_tag = soup.head
# print(f"{head_tag = }")
    
article_tag = soup.find(name="span", class_ = "titleline")
# print(article_tag)
# article_text = article_tag.getText()
# article_link = article_tag.find(name="a").get("href")
article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(f"{article_link = }")
# print(article_upvote)

articles = soup.find_all(name="span", class_ = "titleline")
article_texts = []
article_links = []
for article_tag in articles:
	text = article_tag.getText()
	article_texts.append(text)
	link = article_tag.find(name="a").get("href")
	article_links.append(link)

# print(f"{article_texts = }")
# print(f"{article_links = }")

scores = soup.find_all(class_="score")
# This uses a conditional expression to handle cases where there are no upvotes (span is None)
# article_upvotes = [int(line.getText().strip(" points")) if line else 0 for line in scores]
article_upvotes = [int(line.getText().strip(" points")) or 0 for line in scores]
# print(f"{article_upvotes = }")

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
# print(largest_number)
# print(largest_index)

print(
	f"Most upvoted article: {article_texts[largest_index]}\n"
	f"Number of upvotes: {article_upvotes[largest_index]} points\n"
	f"Available at: {article_links[largest_index]}."
	)

