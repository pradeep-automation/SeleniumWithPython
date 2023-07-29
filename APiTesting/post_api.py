import requests

url = "https://reqres.in/api/users"
payload = {
    "name": "Pradeep",
    "job": "Ramola"
}

# resp = requests.post(url,data=payload)
resp = requests.post(url,data=payload)
print(resp.json())
assert resp.json()["name"] == "Praeep", "Name doesn't match"
