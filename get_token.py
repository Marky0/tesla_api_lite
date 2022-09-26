import base64
import os
import hashlib
import requests
import json
from urllib import parse

LOCAL_TOKEN_FILENAME = "tesla_token.json"               # Filename that we will store a copy of tesla token to

# This script follows the three steps for authentication through the tesla api as described here
#https://tesla-api.timdorr.com/api-basics/authentication

# STEP 1 : Obtain TESLA login page to enter your authentication details into
# https://tesla-api.timdorr.com/api-basics/authentication#step-1-obtain-the-login-page

codeVerifier = base64.urlsafe_b64encode(os.urandom(32)).rstrip(b'=')
print("This is a random secret code known as a code_verifier : " + codeVerifier.decode('ascii'))

hashVerifier = hashlib.sha256(codeVerifier).digest()                    # hash code verifier
codeChallenge = base64.urlsafe_b64encode(hashVerifier).rstrip(b'=').decode('ascii')     # encoded in URL-safe base64
print("This is a public key known as a code_challenge :" + codeChallenge)

# Generate random state to track response requests
state = base64.urlsafe_b64encode(os.urandom(16)).rstrip(b'=').decode('ascii')

loginURL = ("https://auth.tesla.com/oauth2/v3/authorize?" +
            "client_id=ownerapi&" +
            "code_challenge=" + codeChallenge + "&" +
            "code_challenge_method=S256&" +
            "redirect_uri=https%3A%2F%2Fauth.tesla.com%2Fvoid%2Fcallback&" +
            "response_type=code&" +
            "scope=openid+email+offline_access&" +
            "state=" + state)

# STEP 2 : Obtain an authorization code : It is difficult to programatically login to the TESLA API to authenticate
# Tesla has firewall checks for bots, and are constantly changing the login process so script longetivity is poor
# Better to use Tesla's own human authentication webpage so it always remains current.
# This can be done through a web-browser and then the response is manually processed to get the access code.
# This procedure is only needed once

print("Copy this URL into a web-browser and login to your tesla account : Note you can check this is a bonafide tesla URL\n")
print(loginURL)
print("\nAfter login ""Page Not Found"" is displayed : copy the resulting URL below :\n")
url = input("Tesla URL : ")
params = dict(parse.parse_qsl(parse.urlsplit(url).query))
code = params["code"]
print("\nState Sent : " + state + "   State Received : " + params["state"] + "   These should match !!")

# STEP 3 : Exchange code for access token
# https://tesla-api.timdorr.com/api-basics/authentication#step-3-exchange-authorization-code-for-bearer-token

print(code)
url = "https://auth.tesla.com/oauth2/v3/token"
requestTolken = {
        "grant_type": "authorization_code",
        "client_id": "ownerapi",
        "code": code,
        "code_verifier": codeVerifier.decode("ascii"),
        "redirect_uri": "https://auth.tesla.com/void/callback"
}
token = requests.post(url, json=requestTolken)

# Save refreshed token to local text file
with open(LOCAL_TOKEN_FILENAME, 'w', encoding='utf-8') as f:
    json.dump(token.json(), f, ensure_ascii=False, indent=4)

print("\nToken success and saved to local file : " + LOCAL_TOKEN_FILENAME)
print(token.text)