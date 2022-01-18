import requests

resp = requests.get("https://www.baidu.com/")
print(type(resp))
a = resp.content
print(a)