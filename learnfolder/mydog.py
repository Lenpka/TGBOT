import requests
import time
print("Я РАБОТАЮ")
#Переменные бота
API_SERVER_DOGS = "https://random.dog/woof.json"
TOKEN_BOT = "6145670952:AAGJ2DV-KnAi6ZxV3hCrIHjuBOtGGDCnly4"
API_SERVER_CATS = "https://api.thecatapi.com/v1/images/search"
API_BOT = 'https://api.telegram.org/bot'
TEXT = "ВОТ СОБАКА"
COUNT_ANIMALS = 100

#Переменные среды
offset = -2
counter = 0
chat_id :int

def getImage(url:str):
    response = requests.get(url)
    FromJson = response.json()["url"]
    return FromJson



while counter <= COUNT_ANIMALS:
    #Запрос кошки и собаки
    updates = requests.get(f"{API_BOT}{TOKEN_BOT}/getUpdates?offset={offset+1}").json()

    #ИЗОБРАЖЕНИЕ
    if updates['result']:

        for reqs in updates['result']:

            offset =reqs['update_id']
            chat_id= reqs['message']['from']['id']
            requests.get(f"{API_BOT}{TOKEN_BOT}/sendPhoto?chat_id={chat_id}&photo={getImage(API_SERVER_CATS)}")
            requests.get(f"{API_BOT}{TOKEN_BOT}/sendPhoto?chat_id={chat_id}&photo={getImage(API_SERVER_DOGS)}")
    #Time
    time.sleep(1)
    counter +=1



