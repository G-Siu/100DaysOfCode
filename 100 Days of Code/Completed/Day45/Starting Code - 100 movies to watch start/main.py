import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
r = requests.get(URL)
website_html = r.content

soup = BeautifulSoup(website_html, "html.parser")
h3 = soup.find_all(name="h3", class_="title")
all_movies = [text.getText() for text in h3]
movies = all_movies[::-1]
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
