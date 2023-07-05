from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from pprint import pprint

ENDPOINT = "https://api.spotify.com"
clientId = "eb2f9df6f4ba4844807299161da13ff9"
secret = "5f9e503045284829a55926b3d947c08c"

date = input("Which year do you want to travel to? Date format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/" + date)
data = response.text

soup = BeautifulSoup(data, "html.parser")

rank = soup.select("li ul li h3")
song_titles = [i.text.strip() for i in rank if i.text.strip()]
print(song_titles)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=clientId,
        client_secret=secret,
        redirect_uri='http://example.com',
        scope='playlist-modify-private',
        cache_path='token.txt',
        username='alex nolla'

    )
)

user_id = sp.current_user()["id"]
# print(user_id)

# searching spotify for songs by the title generated from the list above
song_uri = []
year = date.split("-")[0]
for title in song_titles:
    result = sp.search(q=f"track:{title} year:{year}", type='track')
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        pprint(f"{title}:  does not exist in Spotify. Skippeds.")

# create the playList

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding each song found into a new playlist

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
