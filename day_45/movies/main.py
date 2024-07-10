import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

movies = soup.find_all(name="h3", class_="title")
movies_texts = [movie.getText() for movie in movies][::-1]

with open("movies.txt", "w") as file:
	for movie in movies_texts:
		file.write(f"{movie}\n")
	