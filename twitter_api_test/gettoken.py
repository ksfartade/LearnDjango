import requests
import base64
import hashlib
import os
import secrets
import json
import redis

client_id = "SzFBaWhWQjd4NlFueGhhM0FBSGY6MTpjaQ"
redirect_uri = "https://dev-app-new.famepilot.com/redirect/uri/"

def get_token():
    def generate_code_verifier():
        return base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8').rstrip('=')

    def generate_code_challenge(code_verifier):
        sha256 = hashlib.sha256()
        sha256.update(code_verifier.encode('utf-8'))
        digest = sha256.digest()
        return base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')

    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)

    # with open("code_verifier.json", "w") as f:
    #     json.dump({"code_verifier": code_verifier}, f)
    # r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # r.set("code_verifier", code_verifier)

    print(f"Code Verifier: {code_verifier}")
    print(f"type Code Verifier: {type(code_verifier)}")
    print(f"Code Challenge: {code_challenge}")

    state = secrets.token_urlsafe(16)  # Generate a random 16-character URL-safe string

    authorization_url = (
        "https://twitter.com/i/oauth2/authorize"
        "?response_type=code"
        f"&client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        "&scope=tweet.read users.read follows.read follows.write dm.read dm.write offline.access"
        f"&state={state}"
        f"&code_challenge={code_challenge}"
        "&code_challenge_method=S256"
    )

    print("Authorization URL:", authorization_url)


    # Assuming you have the authorization code from the callback URL
    authorization_code = input("AUTHORIZATION_CODE_FROM_CALLBACK")

    def get_access_token(client_id, code, code_verifier, redirect_uri):
        token_url = "https://api.twitter.com/2/oauth2/token"
        
        payload = {
            "client_id": client_id,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "code_verifier": code_verifier,
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(token_url, data=payload, headers=headers)
        return response.json()


    auth_tokens = get_access_token(
        client_id=client_id,
        code=authorization_code,
        code_verifier=code_verifier,
        redirect_uri=redirect_uri
    )
    return auth_tokens

auth_tokens = get_token()
print("Auth token", auth_tokens)

def send_dm():
    SEND_DM_TO_CONVERSATION = "https://api.twitter.com/2/dm_conversations/{}/messages"

    dm_conversation_id = "1459536043116412936-1815353842252627968"
    url = SEND_DM_TO_CONVERSATION.format(dm_conversation_id)

    headers = {
        "Authorization": "Bearer {}".format(auth_tokens.get('access_token')),
        "Content-Type": "application/json",
    }

    body = {
        "text" : "testing send message"
    }

    body = json.dumps(body)
    response = requests.post(
        url=url,
        headers=headers,
        json=json.loads(body),
    )

    print("Response: ", response.status_code, "Respone text: ", response.text)

# access_token = access_token_response["access_token"]

# headers = {
#     "Authorization": f"Bearer {access_token}",
# }

# response = requests.get("https://api.twitter.com/2/users/me", headers=headers)
# print("Response: ", response)
# print(response.json())


# old: dDhCNEJHU3Bpck9RckplYkpwRTFmNVNlU2ZwNEl0VGhWc3hLR1EzT3hVcFd0OjE3MjIzOTc5MDg1NDQ6MTowOmF0OjE
# new: dUR1QmtvOFFiOWVwbEpKbXIyMjdFWFkwd2hFeU0zaDl1VHdVQWxLMWduM3JhOjE3MjI0MDAwNzI4OTE6MToxOmF0OjE