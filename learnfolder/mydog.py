import requests
import time
print("Я РАБОТАЮ")
#Переменные бота
API_SERVER_DOGS = "https://random.dog/woof.json"
TOKEN_BOT = "YOURS"
API_SERVER_CATS = "https://api.thecatapi.com/v1/images/search"
API_BOT = 'https://api.telegram.org/bot'
TEXT = "ВОТ СОБАКА"
COUNT_ANIMALS = 100

#Переменные среды
offset = -2
counter = 0
chat_id :int
# cat_response : requests.Response
# dog_response : requests.Request



def getImage(url:str, animal = "CAT") -> str:
    animal_response = requests.get(url).status_code
    if animal_response == 200:
        if animal == "CAT":
            response = requests.get(url).json()
            linkToPhoto = response[0]['url']
        if animal == "DOG":
            response = requests.get(url).json()
            linkToPhoto = response['url']
        return linkToPhoto



while counter <= COUNT_ANIMALS:
    #Запрос кошки и собаки
    updates = requests.get(f"{API_BOT}{TOKEN_BOT}/getUpdates?offset={offset+1}").json()
    print(f"Выполнено {counter}")
    #ИЗОБРАЖЕНИЕ
    if updates['result']:

        for reqs in updates['result']:

            offset =reqs['update_id']
            chat_id= reqs['message']['from']['id']
            link_to_CATS = getImage(API_SERVER_CATS)
            requests.get(f"{API_BOT}{TOKEN_BOT}/sendPhoto?chat_id={chat_id}&photo={link_to_CATS}")

            link_to_DOGS = getImage(API_SERVER_DOGS, animal="DOG")
            requests.get(f"{API_BOT}{TOKEN_BOT}/sendPhoto?chat_id={chat_id}&photo={link_to_DOGS}")
    #Time
    time.sleep(1)
    counter +=1



