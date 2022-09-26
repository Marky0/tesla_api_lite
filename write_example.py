import requests
import json
import time

LOCAL_TOKEN_FILENAME = "tesla_token.json"

# Load current token stored in local file
with open(LOCAL_TOKEN_FILENAME, 'r') as f:
    token = json.load(f)
access_token = token["access_token"]

# Get list of current vehicles from Tesla API
# https://tesla-api.timdorr.com/api-basics/vehicles#get-api-1-vehicles

url = 'https://owner-api.teslamotors.com/api/1/vehicles'
headers = {"content-type": "application/json; charset=UTF-8", 'Authorization': 'Bearer {}'.format(access_token)}

response = requests.get(url, headers=headers).json()
print("\nVehicle request response")
print(response)
id = response["response"][0]["id"]          # Extract car ID - If you have more than one car this needs modification

# Wake car before you can write any data
# https://tesla-api.timdorr.com/vehicle/commands/wake#post-api-1-vehicles-id-wake_up

url = "https://owner-api.teslamotors.com/api/1/vehicles/" + str(id) + "/wake_up"
for x in range(10):
    response = requests.post(url, headers=headers).json()
    state = response["response"]["state"]               # get car state
    print(state)
    if state == 'online':
        break
    time.sleep(5)

# Set Charging Amps for car
# https://tesla-api.timdorr.com/vehicle/commands/charging#post-api-1-vehicles-id-command-set_charging_amps

url = "https://owner-api.teslamotors.com/api/1/vehicles/" + str(id) + "/command/set_charging_amps"
params = {"charging_amps": 10}                                      # set charging to 10amps
response = requests.post(url, data=json.dumps(params), headers=headers).json()
print("\nCar request response")
print(response)


