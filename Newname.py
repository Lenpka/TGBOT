import requests

response = requests.get('http://numbersapi.com/43')
if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)