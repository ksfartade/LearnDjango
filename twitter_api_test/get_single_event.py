import requests
import tweepy

# Replace with your Bearer token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOxq%2FwAAAAAAmQO8HmXaM2DAuelqq4NBCmaPURk%3D45sqyAmcb3iVx3ZjwpAlM5O01O75qcVypRNYX28q3ZPNu22GJn"
from requests_oauthlib import OAuth1
import json

# Replace with your actual credentials
CONSUMER_KEY = 'jz5lFWSwq77GULHNkqgdvWFMM'
CONSUMER_SECRET = 'fw2LL4FdI73mRtEXsPmx3yqQzFXTRz2vUOwVxsw2VDqITPrWJz'
ACCESS_TOKEN = '1025827801952407552-sVtseYNhx3heKzT4yaHsHZPtkg0E5O'
ACCESS_SECRET = 'sDzKbrnpgt5Y5O2GhF4nYLeH82Pf3ufTkelWsfNJCSTox'

import base64
import hashlib
import os
import re
import json
import requests
from requests_oauthlib import OAuth2Session

# This example is set up to retrieve Direct Message events of the authenticating user. This supports both
# one-to-one and group conversations.
GET_DM_EVENTS_URL = "https://api.twitter.com/2/dm_events/{}"

#-----------------------------------------------------------------------------------------------------------------------
# These variables need to be updated to the setting that match how your Twitter App is set-up at
# https://developer.twitter.com/en/portal/dashboard. These will not change from run-by-run.
client_id = "LXI0WVN2MS16SERzN09JTGtJVE46MTpjaQ"
#This must match *exactly* the redirect URL specified in the Developer Portal.
redirect_uri = "https://dev-app-new.famepilot.com/redirect/uri/"
#-----------------------------------------------------------------------------------------------------------------------

# new twitter creds:
client_id = "SzFBaWhWQjd4NlFueGhhM0FBSGY6MTpjaQ"
# redirect_uri = "https://dev-app.famepilot.com/redirect/uri/"
# scopes = ['dm.read', 'tweet.read', 'users.read', 'offline.access']
def handle_oauth():

    # Set the scopes needed to be granted by the authenticating user.
    scopes = ["dm.read", "tweet.read", "users.read", "offline.access"]

    # Create a code verifier.
    code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
    code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)
    print("Code verifier: ", code_verifier)

    # Create a code challenge.
    code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
    code_challenge = code_challenge.replace("=", "")

    # Start an OAuth 2.0 session.
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)

    # Create an authorize URL.
    auth_url = "https://twitter.com/i/oauth2/authorize"
    authorization_url, state = oauth.authorization_url(
        auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    )

    # Visit the URL to authorize your App to make requests on behalf of a user.
    print(
        "Visit the following URL to authorize your App on behalf of your Twitter handle in a browser:"
    )
    print(authorization_url)

    # Paste in your authorize URL to complete the request.
    authorization_response = input(
        "Paste in the full URL after you've authorized your App:\n"
    )

    # Fetch your access token.
    token_url = "https://api.twitter.com/2/oauth2/token"

    # The following line of code will only work if you are using a type of App that is a public client.
    auth = False
    oauth2 = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)
    token = oauth2.fetch_token(
        token_url=token_url,
        authorization_response=authorization_response,
        auth=auth,
        client_id=client_id,
        include_client_id=True,
        code_verifier=code_verifier,
    )

    # The access token.
    access = token["access_token"]
    print("Token: ", token)

    return access

def get_user_conversation_events():

    access = handle_oauth()
    headers = {
        "Authorization": "Bearer {}".format(access),
        "Content-Type": "application/json",
        "User-Agent": "TwitterDevSampleCode",
        "X-TFE-Experiment-environment": "staging1",
        "Dtab-Local": "/s/gizmoduck/test-users-temporary => /s/gizmoduck/gizmoduck"
    }

    event_id = "1815656885007401261"

    request_url = GET_DM_EVENTS_URL.format(event_id)
    print("Request url: ", request_url)

    response = requests.request("GET", request_url, headers=headers)

    if response.status_code != 200:
        print("Request returned an error: {} {}".format(response.status_code))
    else:
        print(f"Response code: {response.status_code}")
    return response


def main():
    # response = get_user_conversation_events()
    response = handle_oauth()
    print("Response: ", response)
    # print('data: ', response.text)
    # print(json.dumps(json.loads(response.text), indent=4, sort_keys=True))

if __name__ == "__main__":
    main()


# fartadek@
# old app token: {'token_type': 'bearer', 'expires_in': 7200, 'access_token': 'dDhCNEJHU3Bpck9RckplYkpwRTFmNVNlU2ZwNEl0VGhWc3hLR1EzT3hVcFd0OjE3MjIzOTc5MDg1NDQ6MTowOmF0OjE', 'scope': ['users.read', 'tweet.read', 'offline.access', 'dm.read'], 'refresh_token': 'YWFCRTBhM1pvWUFUcEdWd09xSVpMOTBZa280XzhheThaWFRxWHRsSjB0cjVZOjE3MjIzOTc5MDg1NDQ6MToxOnJ0OjE', 'expires_at': 1722405109.2633672}