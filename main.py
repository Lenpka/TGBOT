import requests
import time

api_url = 'https://api.telegram.org/bot'
BOT_TOKEN = '7392036746:AAHQQ1PS27ZxY1NvsfPMPR0h0oy6R4Y2fBQ'

offset = -2
updates: dict

def do_something()->None:
    print("Был апдейт")

while (True):
    start_time = time.time()
    updates = requests.get(f'{api_url}{BOT_TOKEN}/getUpdates&offset={offset+1}').json()

    if (updates['result']):
        for res in updates['result']:
            offset = res['update_id']
            do_something()
    time.sleep(3)
    end_time = time.time()
    print(f"Время между запросами: {end_time-start_time}")