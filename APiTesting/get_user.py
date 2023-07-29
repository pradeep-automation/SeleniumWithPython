import requests
from jsonpath_ng import jsonpath, parse

res = requests.get("https://reqres.in/api/users?page=2")

code = res.status_code
# assert code == 201, f"Code is {code}"
print(res.text)
print("*"*20)
print(res.content)
print("*"*20)
print(res.json())
print("*"*200)
print("Headers in the response are ---------> ", res.headers)
print("*"*200)
print("Cookies are---> ", res.cookies)
print("*"*200)
print(res.encoding)
print("*"*200)
print(res.url)
