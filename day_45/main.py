from bs4 import BeautifulSoup
# import lxml
# import html5lib

with open("website.html") as html_file:
	content = html_file.read()

# soup = BeautifulSoup(content, "lxml")
# soup = BeautifulSoup(content, "html5lib")
soup = BeautifulSoup(content, "html.parser") # html.parser  is buil-in
# print(soup.title)    # <title>Angela's Personal Site</title>
# print(soup.title.name)    # title
# print(soup.title.string)  # Angela's Personal Site
# print(soup.p)
# print(soup.find_all(name="p"))
# print(soup.a)
# print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
# 	print(tag.getText())
# 	print(tag.get("href"))
	
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_ = "heading")  # class will be error, need class_
# print(section_heading)
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)
#
# heading = soup.select(".heading")
# print(heading)


