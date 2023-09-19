import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")

all_titles = soup.select(".article-title-description__text .title")


with open("movie.txt", "w") as file:
    for title in reversed(all_titles):
        file.write(f'{title.getText()}\n')