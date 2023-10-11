from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import requests
import spotipy
import os

CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

date = input("Which year do you want to travel to?"
             " Type the date in this format YYYY-MM-DD: ")

r = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
r.raise_for_status()

top_100 = r.text
soup = BeautifulSoup(top_100, "html.parser")
songs = soup.select(selector="li ul li h3")
artists = soup.find_all(name="span", class_="a-no-trucate")
top_list = [text.getText().strip() for text in songs]
artist_list = [text.getText().strip() for text in artists]
# print(top_list)
# print(artist_list)

# formatted_list = [f"{top_list[i]} - {artist_list[i]}"
#                   for i in range(0, len(top_list))]
# print(formatted_list)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://www.example.com/",
    show_dialog=True,
    cache_path="token.txt",
    username=""))

user_id = sp.current_user()["id"]
# print(user_id)

year = date.split("-")[0]

uri_list = []
for song in top_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri_list.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify and has been skipped")
# print(uri_list)

playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False,
                                   description="Top 100 songs per "
                                               "specified date.")

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
