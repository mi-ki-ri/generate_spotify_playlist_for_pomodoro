import datetime
from locale import locale_encoding_alias
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
        print(randomChoice["name"], f"{randomChoice['duration_ms']}ms")

        if (current_duration + randomChoice["duration_ms"] > duration):
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


def playlist_append(playlist_id, user_id, duration, current_duration):
    user_all_tracks = []
    tracks = []

    short_terms = sp.current_user_top_tracks(
        limit=50, offset=0, time_range="short_term")["items"]
    mid_terms = sp.current_user_top_tracks(
        limit=50, offset=0, time_range="medium_term")["items"]
    long_terms = sp.current_user_top_tracks(
        limit=50, offset=0, time_range="long_term")["items"]

    user_all_tracks.extend(short_terms)
    user_all_tracks.extend(mid_terms)
    user_all_tracks.extend(long_terms)

    appendWhile(playlist_id=playlist_id,
                tracks=user_all_tracks, duration=duration, current_duration=current_duration)


scopes = ["playlist-modify-private", "user-top-read"]


minutes_25 = 1500000
minutes_5 = 300000

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

user_id = sp.me()['id']

dt_now = datetime.datetime.now()
timestr = dt_now.strftime('%Y-%m-%d %H:%M:%S')

playlist = sp.user_playlist_create(
    user_id, name=f"Pomodoro Session @{timestr}", public=False, collaborative=False, description=f"")

print(playlist["id"])
playlist_id = playlist["id"]

playlist_append(playlist_id, user_id, minutes_25, 0)
