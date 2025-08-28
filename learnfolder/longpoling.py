import requests
import time

BOT_URL = "https://api.telegram.org/bot"
BOT_TOKEN  = "7392036746:AAHofH1Aexm8azr9oCmgtXbVm-qZ593Jpno"

chat_id:int
text = "Something"
timesToStop = 30
offset = -2


while True:
    wait_for_response = time.time()#0

        #0
    updates = requests.get(f'{BOT_URL}{BOT_TOKEN}/getUpdates?offset={offset +1}&timeout={timesToStop}').json()
       
    if updates['result']:
        for reques in updates['result']:
            offset = reques['update_id']
            chat_id = reques['message']['from']['id']

            requests.get(f'{BOT_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
            
            print ('БЫЛО ОБНОВЛЕНИЕ')
    time.sleep(1)
    endTime = time.time()
    print(f"Время = {wait_for_response- endTime}")#0

