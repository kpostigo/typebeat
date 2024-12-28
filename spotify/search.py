import os
from dotenv import load_dotenv
from auth import get_access_token
import requests

# load environment variables
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def search(query):
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    search_url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=10"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        results = response.json()["tracks"]["items"]
        return results 
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

print(search("Big L"))
