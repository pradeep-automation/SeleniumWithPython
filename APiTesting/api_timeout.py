import requests

# resp = requests.get("https://reqres.in/api/users?delay=3", timeout=5)
resp = requests.get("https://httpbin.org/delay/3", timeout=5)

print(resp)