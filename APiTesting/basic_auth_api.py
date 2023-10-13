import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
resp = requests.get('https://httpbin.org/basic-auth/user/pass', auth=HTTPBasicAuth('user', 'pass'))
print(resp.status_code)
print(resp.json())

oauth = OAuth1()

