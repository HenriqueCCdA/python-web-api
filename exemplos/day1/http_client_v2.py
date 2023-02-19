from urllib import request


import requests
from urllib.request import urlopen

result = urlopen("http://example.com/index.html")
print(result.read())

result = requests.get("http://example.com/index.html")
print(result)
