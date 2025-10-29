import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
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


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')
# for art in results['items']:
#     print(f"{art['name']}: {art['popularity']}")

def get_mood_tracks(query, limit=10):
    offset = random.randint(0, 900)
    results = sp.search(q=query, type='track', limit=limit, offset=offset)
    return [t['name'] + " - " + t['artists'][0]['name'] for t in results['tracks']['items']]

# print(get_mood_tracks("energetic"))
