import os
from dotenv import load_dotenv
import requests
import base64

# load environment variables
load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

credentials = f'{CLIENT_ID}:{CLIENT_SECRET}'
creds_b64 = base64.b64encode(credentials.encode('ascii')).decode('utf-8')

token_url = 'https://accounts.spotify.com/api/token'

headers = {
    'Authorization': f'Basic {creds_b64}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'grant_type': 'client_credentials'
}

response = requests.post(token_url, headers=headers, data=data)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print(f'Access token: {access_token}')
else:
    print(f"Error: {response.status_code}, {response.text}")
