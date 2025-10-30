import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import random

# Load environment variables
load_dotenv()

# ✅ Full Spotify scope
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

def get_spotify_client():
    """
    Create a Spotify client that works both locally and on Render.
    - On Render: uses cache (no input, no browser)
    - Locally: first-time auth opens browser and caches token
    """
    try:
        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                scope=scope,
                open_browser=False,        # 🔥 prevents EOF error on Render
                cache_path=".spotipyoauthcache"
            )
        )
    except Exception as e:
        print(f"⚠️ Spotify Auth Error: {e}")
        return None


def get_mood_tracks(query, limit=10):
    """
    Fetch random Spotify tracks for the detected mood.
    """
    sp = get_spotify_client()
    if sp is None:
        return ["Error: Unable to authenticate with Spotify."]

    try:
        offset = random.randint(0, 900)
        results = sp.search(q=query, type='track', limit=limit, offset=offset)
        return [
            f"{t['name']} - {t['artists'][0]['name']}"
            for t in results['tracks']['items']
        ]
    except Exception as e:
        return [f"Error fetching tracks: {str(e)}"]
