import requests
import time

BOT_URL = "https://api.telegram.org/bot"


chat_id:int
text = "Something"
timesToStop = 10
offset = -2


while True:
    wait_for_response = time.time()#0
    startTime = time.time()
    while (abs(wait_for_response - startTime)) <= timesToStop:
        #0
        updates = requests.get(f'{BOT_URL}{BOT_TOKEN}/getUpdates?offset={offset +1}').json()
       
        if updates['result']:
            for reques in updates['result']:
                offset = reques['update_id']
                chat_id = reques['message']['from']['id']
                wait_for_response = time.time()
                requests.get(f'{BOT_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
                
                print ('БЫЛО ОБНОВЛЕНИЕ')
        time.sleep(1)
        print(f"Время = {wait_for_response- time.time()}")
    wait_for_response = time.time()#0
    startTime = time.time()
