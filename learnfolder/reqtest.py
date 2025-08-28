import requests

print (requests.get("http://numbersapi.com/43").status_code)
print (requests.get("http://numbersapi.com/43").content)
