import tweepy
import json

# Replace these values with your own credentials
client_id = "LXI0WVN2MS16SERzN09JTGtJVE46MTpjaQ"
client_secret = "sDzKbrnpgt5Y5O2GhF4nYLeH82Pf3ufTkelWsfNJCSTox"
redirect_uri = "https://dev-app.famepilot.com/redirect/uri/"


import base64
import hashlib
import os
import re
import requests
import json
from requests_oauthlib import OAuth2Session
# OAuth2 scopes
scopes = ["dm.read", "tweet.read", "users.read", "offline.access"]

def get_oauth2_token():
    # Create a code verifier
    code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
    code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

    # Create a code challenge
    code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8").replace("=", "")

    # Start OAuth 2.0 session
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)

    # Create authorization URL
    auth_url = "https://twitter.com/i/oauth2/authorize"
    authorization_url, state = oauth.authorization_url(
        auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    )

    # Redirect user to authorization URL
    print("Visit the following URL to authorize your App:")
    print(authorization_url)

    # Get authorization response from user
    authorization_response = input("Paste the full redirect URL after authorization:\n")

    # Fetch access token
    token_url = "https://api.twitter.com/2/oauth2/token"
    token = oauth.fetch_token(
        token_url=token_url,
        authorization_response=authorization_response,
        client_id=client_id,
        client_secret=client_secret,
        code_verifier=code_verifier,
    )

    return token["access_token"]

def get_dm_events(access_token):
    client = tweepy.Client(bearer_token=access_token)

    try:
        # response = client.get_dm_events()
        response = client.create_direct_message()
        print(json.dumps(response.data, indent=4))
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

def main():
    access_token = get_oauth2_token()
    print("Acess token: ", access_token)
    get_dm_events(access_token)

if __name__ == "__main__":
    main()