import requests
from requests.auth import HTTPBasicAuth

resp = requests.get('https://httpbin.org/basic-auth/user/pass', auth=HTTPBasicAuth('user', 'pass'))
print(resp.status_code)
print(resp.json())
