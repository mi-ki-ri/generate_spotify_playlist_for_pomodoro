import datetime
from pprint import pprint
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random


def appendWhile(playlist_id, tracks, duration, current_duration):
    while (True):
        time.sleep(0.1)
        print("TRACK")
        sptracks = sp.playlist(playlist_id=playlist_id, fields=[
            "tracks"])["tracks"]

        randomChoice = random.choice(tracks)
        print(randomChoice["duration_ms"])

        if (current_duration + randomChoice["duration_ms"] - minutes_5 > duration):
            break
        else:
            flg = False
            for pl_track in sptracks["items"]:
                # pprint("Pl_track")
                # pprint.pprint(pl_track)
                if (pl_track["track"]["id"] == randomChoice["id"]):
                    flg = True
            if flg == False:
                current_duration += randomChoice["duration_ms"]
                sp.playlist_add_items(
                    playlist_id=playlist_id, items=[randomChoice["id"]])


def playlist_append(playlist_id, artist_id, duration, current_duration):
    artist_all_tracks = []
    albums = sp.artist_albums(artist_id=artist_id)
    for album in albums["items"]:
        time.sleep(0.1)
        print("ALBUM")
        album_tracks = sp.album_tracks(album_id=album["id"])
        for track in album_tracks["items"]:
            artist_all_tracks.append(track)

    appendWhile(playlist_id=playlist_id,
                tracks=artist_all_tracks, duration=duration, current_duration=current_duration)


scopes = ["playlist-modify-private", "user-top-read"]


minutes_25 = 1500000
minutes_5 = 300000

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

user_id = sp.me()['id']

artists = sp.current_user_top_artists(limit=50, offset=0)
print(artists)

artist = random.choice(artists["items"])
aid = artist["id"]


playlist = sp.user_playlist_create(
    user_id, name=f"Pomodoro 1 Session {datetime.date.today()} playlist of {artist['name']}", public=False, collaborative=False, description=f"Generated {datetime.date.today()}")

print(playlist["id"])
playlist_id = playlist["id"]

playlist_append(playlist_id, aid, minutes_25, 0)
# playlist_append(playlist_id, JOHN, minutes_5, 0)
