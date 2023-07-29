import requests

payload = {
    "name": "Anku",
    "job": "Arch"
            }

resp = requests.put("https://reqres.in/api/users/2", data=payload)

print(resp)
print(resp.json())