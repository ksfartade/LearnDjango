import requests
import json
import redis

c_id = "SzFBaWhWQjd4NlFueGhhM0FBSGY6MTpjaQ"
r_uri = "https://dev-app-new.famepilot.com/redirect/uri/"

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


# with open("code_verifier.json", "r") as f:
#     data = json.load(f)
#     cv = data["code_verifier"]

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
cv = r.get('code_verifier')
authorization_code = input("enter the code: ")
print(f"Auth code:{authorization_code}")
# cv = 'QtfTf1jik6nzDxNvf-yqlm0YWI1qtcFW5BTdNTQbezA'
access_token_response = get_access_token(
    client_id=c_id,
    code=authorization_code,
    code_verifier=cv,
    redirect_uri=r_uri
)

print(access_token_response)