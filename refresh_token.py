import requests
import json

LOCAL_TOKEN_FILENAME = "tesla_token.json"

# Load current token stored in local text file
with open(LOCAL_TOKEN_FILENAME, 'r') as f:
    token = json.load(f)
refresh_token = token["refresh_token"]
print("Old Token : " + str(token))

# Refresh token through tesla api
# https://tesla-api.timdorr.com/api-basics/authentication#post-https-auth.tesla.com-oauth2-v3-token-1

url = 'https://auth.tesla.com/oauth2/v3/token'
refresh_json = {
             "grant_type": "refresh_token",
             "client_id": "ownerapi",
             "refresh_token": refresh_token,
             "scope": "openid email offline_access"
}

token = requests.post(url, json=refresh_json)
print("New Token : " + token.text)

# Save refreshed token to local text file
with open(LOCAL_TOKEN_FILENAME, 'w', encoding='utf-8') as f:
    json.dump(token.json(), f, ensure_ascii=False, indent=4)
