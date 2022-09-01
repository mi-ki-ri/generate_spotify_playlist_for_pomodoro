# Generate Spotify Playlist For Pomodoro

## Instalation

```sh
pip install -r requirements.txt

export SPOTIPY_CLIENT_ID=987654321
export SPOTIPY_CLIENT_SECRET=123456789
export SPOTIPY_REDIRECT_URI=http://127.0.0.1:9090

python app.py
```

## Custamization

Specify Artist ID, like

```python app.py
GEORGE = "7FIoB5PHdrMZVC3q2HE5MS"
JOHN = "4x1nvY2FN8jxqAFA0DA02H"
```

```python app.py
playlist_append(playlist_id, GEORGE, minutes_25, 0) # GEORGE Songs 25 minites
playlist_append(playlist_id, JOHN, minutes_5, 0) # JOHN Songs 5 minites
```
