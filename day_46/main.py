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
REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=APP_CLIENT_ID,
 client_secret=APP_CLIENT_SECRET))
scope = "user-top-read playlist-modify-private playlist-modify-public"
sp_oauth = SpotifyOAuth(
    client_id=APP_CLIENT_ID,
    client_secret=APP_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
)

# date = input("What year you would like to travel to? (in YYYY-MM-DD) ")
date = "2000-07-13"
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in songs]

song = song_names[0]
results = sp.search(q=song, limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

# ======================

def get_token():
    # Get the authorization URL
    auth_url = sp_oauth.get_authorize_url()
    print(f'Please navigate here: {auth_url}')
    
    # Prompt user to enter the URL they were redirected to
    redirected_url = input('Enter the URL you were redirected to: ')
    
    # Extract the authorization code from the redirected URL
    code = sp_oauth.parse_response_code(redirected_url)
    print(f'Authorization code: {code}')
    
    # Get the access token using the authorization code
    token_info = sp_oauth.get_access_token(code, as_dict=True)
    # token_info = sp_oauth.get_cached_token()

    # Save the access token
    access_token = token_info['access_token']
    print(f'Access token: {access_token}')
    return access_token

token = get_token()

print(f"{token = }")
headers = {
    'Authorization': f'Bearer {token}'
}

def fetch_web_api(endpoint, method='GET', body=None):
    url = f'https://api.spotify.com/{endpoint}'
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, data=json.dumps(body))
    return response.json()

top_tracks_ids = [
    '52pSzZti2oeVCWwDSklMpH', '5sPBW4qTxwda6espyNqOIH',
    '5WcwIdG66MeOQzTfFAoRT7', '7ELgXEWwuVbUFVeXdZMK5c', '0bzIxZJNst6iypVZpZt6GR'
]

def get_recommendations():
    # Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-recommendations
    endpoint = f'v1/recommendations?limit=5&seed_tracks={",".join(top_tracks_ids)}'
    return fetch_web_api(endpoint).get('tracks', [])
print("\n")
recommended_tracks = get_recommendations()
for track in recommended_tracks:
    track_name = track['name']
    artist_names = ', '.join(artist['name'] for artist in track['artists'])
    print(f'{track_name} by {artist_names}')
print("=================")
def get_artist_spotify_url(song_name):
    results = sp.search(q=song_name, limit=1)  # Limit to 1 for simplicity
    if results['tracks']['items']:
        artist_info = results['tracks']['items'][0]['artists'][0]  # First artist of the first track
        artist_name = artist_info['name']
        artist_url = artist_info['external_urls']['spotify']
        return artist_name, artist_url
    else:
        return None, None
    
user_id = sp.current_user()["id"]

song_uris = []
song_urls = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        artist_name, artist_url = get_artist_spotify_url(song)
        if artist_name and artist_url:
            song_urls.append({artist_name: artist_url})
            # print(f'Song: {song}, Artist: {artist_name}, Spotify URL: {artist_url}')
        else:
            print(f'Song: {song} not found on Spotify')
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# print(song_uris)
# print(song_urls)

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
