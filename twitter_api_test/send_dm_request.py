import base64
import hashlib
import os
import re
import json
import requests
from requests_oauthlib import OAuth2Session

#This example is set up to add a new DM to a one-to-one conversation.
POST_DM_URL = "https://api.twitter.com/2/dm_conversations/with/:participant_id/messages"

#-----------------------------------------------------------------------------------------------------------------------
# These variables need to be updated to the setting that match how your Twitter App is set-up at
# https://developer.twitter.com/en/portal/dashboard. These will not change from run-by-run.
# client_id = 'LXI0WVN2MS16SERzN09JTGtJVE46MTpjaQ'
client_id = "SzFBaWhWQjd4NlFueGhhM0FBSGY6MTpjaQ"

#This must match *exactly* the redirect URL specified in the Developer Portal.
redirect_uri = "https://dev-app-new.famepilot.com/redirect/uri/"
#-----------------------------------------------------------------------------------------------------------------------
# These variables indicate the participant of the one-to-one conversation and the message to add. A more ready-to-be
# used example would have these passed in from some calling code.
#Who is this DM being sent to? Reference their User ID.
participant_id = "1815403461946875904"
#Set the text of the message to be sent.
text_message = "Hi hope you are doing well fartade_ki7144..."
#-----------------------------------------------------------------------------------------------------------------------

def handle_oauth():

    # Set the scopes needed to be granted by the authenticating user.
    scopes = ["dm.read", "dm.write", "tweet.read", "users.read", "offline.access"]

    # Create a code verifier
    code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
    code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

    # Create a code challenge
    code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
    code_challenge = code_challenge.replace("=", "")

    # Start an OAuth 2.0 session
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)

    # Create an authorize URL
    auth_url = "https://twitter.com/i/oauth2/authorize"
    authorization_url, state = oauth.authorization_url(
        auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    )
    

    # Visit the URL to authorize your App to make requests on behalf of a user
    print(
        "Visit the following URL to authorize your App on behalf of your Twitter handle in a browser:"
    )
    print(authorization_url)

    # Paste in your authorize URL to complete the request
    authorization_response = input(
        "Paste in the full URL after you've authorized your App:\n"
    )

    # Fetch your access token
    token_url = "https://api.twitter.com/2/oauth2/token"

    # The following line of code will only work if you are using a type of App that is a public client
    auth = False

    token = oauth.fetch_token(
        token_url=token_url,
        authorization_response=authorization_response,
        auth=auth,
        client_id=client_id,
        include_client_id=True,
        code_verifier=code_verifier,
    )

    # Your access token
    access = token["access_token"]

    print('Token: ', token)

    return access

def post_dm_to_one_to_one_conversation(participant_id):

    request_body = {}

    access = handle_oauth()
    # return
    # access = "MTF1RHB4X0NPZnNCdzBCa2xXVnhpS0pqS0RaWVNtamN3T2ZjWEpna29waUxpOjE3MjI0MDQ3NDA5NTk6MToxOmF0OjE"

    headers = {
        "Authorization": "Bearer {}".format(access),
        "Content-Type": "application/json",
        "User-Agent": "TwitterDevSampleCode",
        "X-TFE-Experiment-environment": "staging1",
        "Dtab-Local": "/s/gizmoduck/test-users-temporary => /s/gizmoduck/gizmoduck"
    }

    request_url = POST_DM_URL.replace(':participant_id', str(participant_id))
    request_body['text'] = text_message
    json_body = json.dumps(request_body)

    #Send DM
    response = requests.request("POST", request_url, headers=headers, json=json.loads(json_body))

    if response.status_code != 201:
        print("Request returned an error: {} {}".format(response.status_code, response.text))
    else:
        print(f"Response code: {response.status_code} Response data: {response.json()}")

    return response


response = post_dm_to_one_to_one_conversation(participant_id)
# print(json.dumps(json.loads(response.text), indent=4, sort_keys=True))


# response: 
# Token:  {'token_type': 'bearer', 'expires_in': 7200, 'access_token': 'ajh5Qi1ldEF4X2VPbHl4cHFELVJuci1sblY0U2RaLTEzQUtmakkxcE1tYVdXOjE3MjE4MTU0NTExNzQ6MToxOmF0OjE', 'scope': ['offline.access', 'dm.read', 'users.read', 'dm.write', 'tweet.read'], 'refresh_token': 'NGMzS1RFR1ppdGdHRnhsODJBMFpBUWx5QkdvdFVCaGktUmFtNS1OQXJ3aDVkOjE3MjE4MTU0NTExNzQ6MTowOnJ0OjE', 'expires_at': 1721822648.5327115}
# Response code: 201
# {
#     "data": {
#         "dm_conversation_id": "1025827801952407552-1815403461946875904",
#         "dm_event_id": "1816051747883999617"
#     }
# }
