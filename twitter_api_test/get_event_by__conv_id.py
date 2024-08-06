import base64
import hashlib
import os
import re
import json
import requests
from requests_oauthlib import OAuth2Session

# This example is set up to retrieve Direct Message events by conversation ID. This supports both
# one-to-one and group conversations.
GET_DMS_EVENTS_URL = "https://api.twitter.com/2/dm_conversations/:dm_conversation_id/dm_events"

#-----------------------------------------------------------------------------------------------------------------------
# These variables need to be updated to the setting that match how your Twitter App is set-up at
# https://developer.twitter.com/en/portal/dashboard. These will not change from run-by-run.
client_id = os.getenv('client_id')
#This must match *exactly* the redirect URL specified in the Developer Portal.
redirect_uri = os.getenv('redirect_uri')
#-----------------------------------------------------------------------------------------------------------------------
# This variable specifies the conversation to retrieve. A more ready-to-be used example would
# have this passed in from some calling code.
# What is the ID of the conversatikon to retrieve?
dm_conversation_id = "1025827801952407552-1815403461946875904"
#-----------------------------------------------------------------------------------------------------------------------

print('cliend id: ', client_id)
print('redirect_uri: ', redirect_uri)
def handle_oauth():

    # Set the scopes needed to be granted by the authenticating user.
    scopes = ["dm.read", "tweet.read", "users.read", "offline.access"]

    # Create a code verifier
    code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
    code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

    # Create a code challenge
    code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
    code_challenge = code_challenge.replace("=", "")

    # Start and OAuth 2.0 session
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

def get_events_by_conservation_id(dm_conversation_id):

    access = handle_oauth()

    headers = {
        "Authorization": "Bearer {}".format(access),
        "Content-Type": "application/json",
        "User-Agent": "TwitterDevSampleCode",
        "X-TFE-Experiment-environment": "staging1",
        "Dtab-Local": "/s/gizmoduck/test-users-temporary => /s/gizmoduck/gizmoduck"
    }

    request_url = GET_DMS_EVENTS_URL.replace(':dm_conversation_id', str(dm_conversation_id))

    response = requests.request("GET", request_url, headers=headers)

    if response.status_code != 200:
        print("Request returned an error: {} {}".format(response.status_code, response.text))
    else:
        print(f"Response code: {response.status_code}")
        return response

def main():
    # response = get_events_by_conservation_id(dm_conversation_id)
    # print(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
    handle_oauth()

if __name__ == "__main__":
    main()


# response: 
# Token:  {'token_type': 'bearer', 'expires_in': 7200, 'access_token': 'WF9PcmI2Z1N6UmpUblhsLUFJMUxkY0l5N05Bd05USEh5bVFIZml0dTdlZmM4OjE3MjE4MTYwMjY4NDM6MToxOmF0OjE', 'scope': ['users.read', 'tweet.read', 'offline.access', 'dm.read'], 'refresh_token': 'bXpTRExQcGpqQ19sTDBSa2Myd1BqdWJOSVFNeVc4dTdVZlpmbTZmdFB5Z2c5OjE3MjE4MTYwMjY4NDM6MToxOnJ0OjE', 'expires_at': 1721823224.157445}
# Response code: 200
# {
#     "data": [
#         {
#             "event_type": "MessageCreate",
#             "id": "1816051747883999617",
#             "participant_ids": [
#                 "1025827801952407552",
#                 "1815403461946875904"
#             ],
#             "text": "Hi, I am DMing you using the v2 DM one-to-one endpoint."
#         }
#     ],
#     "meta": {
#         "next_token": "18LAA69JT5OLSMJ1G400ZZZZ",
#         "previous_token": "1BLC469JT5OLSMJ1G400ZZZZ",
#         "result_count": 1
#     }
# }