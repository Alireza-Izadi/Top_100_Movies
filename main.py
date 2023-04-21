import requests

from bs4 import BeautifulSoup

URL = "https://variety.com/lists/best-movies-of-all-time/"

response = requests.get(URL)
variery_website = response.text

soup = BeautifulSoup(variery_website, "html.parser")
best_movies_tag = soup.find_all(name="h2")

best_movies = []
for movie in best_movies_tag:
    best_movies.append(movie.getText())

best_movies.pop()
best_movies.reverse()

for i, movie in enumerate(best_movies):
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(f"{i+1}) {movie}\n")
