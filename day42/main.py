from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

data = response.text

soup = BeautifulSoup(data, "html.parser")

rank = soup.find_all('h3', class_='title')

movie_title = [i.getText() for i in rank]

# we can use any of the method below to reverse the array

# movie_title.reverse()
#
# for i in range(len(movie_title) - 1, -1, -1):
#     print(movie_title[i])

movies = movie_title[::-1]
print(movies)

with open("movie.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")








