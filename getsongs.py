import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import random

load_dotenv()

scope = (
    "ugc-image-upload "
    "user-read-playback-state "
    "user-modify-playback-state "
    "user-read-currently-playing "
    "app-remote-control "
    "streaming "
    "playlist-read-private "
    "playlist-read-collaborative "
    "playlist-modify-private "
    "playlist-modify-public "
    "user-follow-modify "
    "user-follow-read "
    "user-library-modify "
    "user-library-read "
    "user-read-email "
    "user-read-private "
    "user-top-read "
    "user-read-recently-played "
    "user-read-playback-position"
)

# ✅ Explicitly pull credentials from environment
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        open_browser=False,  # prevents trying to open a browser
        cache_path=".spotipyoauthcache"  # reuse token once authorized
    )
)

def get_mood_tracks(query, limit=10):
    offset = random.randint(0, 900)
    results = sp.search(q=query, type='track', limit=limit, offset=offset)
    return [t['name'] + " - " + t['artists'][0]['name'] for t in results['tracks']['items']]
