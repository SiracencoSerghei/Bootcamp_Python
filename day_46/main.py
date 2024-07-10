from bs4 import BeautifulSoup
import os
import time
import json
from dotenv import load_dotenv
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()
APP_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
REDIRECT_URI = "http://localhost:3002"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=APP_CLIENT_ID,
 client_secret=APP_CLIENT_SECRET))

# date = input("What year you would like to travel to? (in YYYY-MM-DD) ")
date = "2024-07-13"
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

songs = soup.select("li ul li h3")
songs_names = [song.getText().strip() for song in songs]

song = songs_names[0]
results = sp.search(q=song, limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

# # ===========================
CACHE_PATH = ".cache"

# Function to read the .cache file and extract the access token
def get_access_token_from_cache(cache_path):
    with open(cache_path, 'r') as cache_file:
        token_info = json.load(cache_file)
        return token_info
token_info = ''
time.sleep(4)
# Check if the .cache file exists
if os.path.exists(CACHE_PATH):
    token_info = get_access_token_from_cache(CACHE_PATH)
    
token = token_info['access_token']
print(token)




# ======================


headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

def fetch_web_api(endpoint, method='GET', body=None):
    url = f'https://api.spotify.com/{endpoint}'
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, data=json.dumps(body))
    return response.json()

def get_top_tracks():
    # Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    endpoint = 'v1/me/top/tracks?time_range=long_term&limit=5'
    return fetch_web_api(endpoint).get('items', [])

top_tracks = get_top_tracks()
for track in top_tracks:
    track_name = track['name']
    artist_names = ', '.join(artist['name'] for artist in track['artists'])
    print(f'{track_name} by {artist_names}')

top_tracks_ids = [
    '52pSzZti2oeVCWwDSklMpH', '5sPBW4qTxwda6espyNqOIH',
    '5WcwIdG66MeOQzTfFAoRT7', '7ELgXEWwuVbUFVeXdZMK5c', '0bzIxZJNst6iypVZpZt6GR'
]

def get_recommendations():
    # Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-recommendations
    endpoint = f'v1/recommendations?limit=5&seed_tracks={",".join(top_tracks_ids)}'
    return fetch_web_api(endpoint).get('tracks', [])

recommended_tracks = get_recommendations()
for track in recommended_tracks:
    track_name = track['name']
    artist_names = ', '.join(artist['name'] for artist in track['artists'])
    print(f'{track_name} by {artist_names}')