import requests

response = requests.get("http://google.com")
if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)