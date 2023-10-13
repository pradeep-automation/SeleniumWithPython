import requests
from jsonpath_ng import jsonpath, parse

p = {"page": 2}
# resp = requests.get("https://reqres.in/api/users?page=2")
resp = requests.get("https://reqres.in/api/users", params=p)
json_resp = resp.json()
user_email = json_resp["data"][0]["email"]
print(user_email)
print(resp.url)
assert user_email.endswith("reqres.in"), "Email does not end with reqres.in"
