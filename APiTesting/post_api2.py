import json

import requests



url = "https://reqres.in/api/users"
with open("data.json", "r") as f:
    payload = f.read()
    # print(json.loads(payload))
    resp = requests.post(url, json.loads(payload))
    print(resp.json()['name'])





