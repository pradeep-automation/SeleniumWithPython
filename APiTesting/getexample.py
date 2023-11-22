import json

import requests
# headers = {
#     "Authorization": f'Token special-key'
# }
resp = requests.get("https://petstore.swagger.io/v2/pet/findPetsByStatus", params={'status':'pending'})

print(resp.json())
url = "https://petstore.swagger.io/v2/pet"

with open("pet.json", 'r') as F:
    payload = F.read()

resp = requests.post(url, json= json.loads(payload))

print(resp.json())
