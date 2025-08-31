from aiogram.types import Message
import time
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram import F
import os
import requests

BOT_TOKEN:str
BOT_TOKEN = os.getenv("BOT_TOKEN") # Важно локально указать переменную

bot = Bot(token=BOT_TOKEN)
disp = Dispatcher()
users = {}



def getRandom() ->int:
    value = random.randint(1, 100)
    return value
value = getRandom()
@disp.message(Command(commands="startgame"))
async def startmessage(message:Message) -> int:
    print(f'ТССССССССССССС, ТИХО, СЕКРЕТНОЕ ЗНАЧЕНИЕ VALUE = {value}')
    await message.answer("ДАВАЙ ИГРАТЬ, ДАВАЙ натуральное ЧИСЛО ОТ 1 до 100 угадаем")
    if message.from_user.id not in users:
      
        users[message.from_user.id] ={
    "Is_Active": 0,
    "Count":0,
    "attempts" : 0
}
    users[message.from_user.id]["Is_Active"] = 1
    print(users[message.from_user.id]["Is_Active"])

@disp.message(lambda x: x.text and x.text.isdigit() and int(x.text) == value)
async def youGuess(message:Message):
    if users[message.from_user.id]["Is_Active"] == 1:
        await message.answer ("МОИ ПОЗДРАВЛЕНИЕ, В ТОЧКУ, ЕЩЕ РАЗ? Я ЗАГАДАЛ!")
        users[message.from_user.id]["Count"] += 1
        global value
        value = getRandom()

@disp.message(Command(commands="update"))
async def getUpdate(message:Message):
    update = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates').json()
    print(update)
    print(message.model_dump_json(indent=4, exclude_none=True))
    if update['result']:
        await message.answer(f"{update}")

        

@disp.message (lambda x: x.text and x.text.isdigit() and int(x.text) < value)
async def someBigger(message:Message):
    await message.answer("НЕМНОГО НЕДОБОР")
    if users[message.from_user.id]["Is_Active"] == 1:
        users[message.from_user.id]['attempts']+=1 


@disp.message (lambda x: x.text and x.text.isdigit() and int(x.text) > value)
async def someBigger(message:Message):
    await message.answer("НЕМНОГО ПЕРЕБОР")
    if users[message.from_user.id]["Is_Active"] == 1:
        users[message.from_user.id]['attempts'] += 1

@disp.message(Command(commands = ("help")))
async def sendHelp(message:Message):
    await message.answer("Чтобы поиграть напиши /start \n чтобы закончить - /end")
@disp.message(Command(commands = ("end")))
async def sendHelp(message:Message):
    await message.answer("Было приятно играть!")
    users[message.from_user.id]["attempts"] = 0
    users[message.from_user.id]["Count"] = 0
    users[message.from_user.id]["Is_Active"]= 0
@disp.message(Command(commands = ("stat")))
async def sendHelp(message:Message):
    if users[message.from_user.id]['Count'] > 0:
        await message.answer(f"Твоя точность = {users[message.from_user.id]['Count']*100/(users[message.from_user.id]['attempts']+users[message.from_user.id]['Count'])}%")
    else:
        await message.answer ("Угадай хоть 1 число)")

@disp.message()
async def iDontUnderstand(message:Message):
    await message.answer("Честно я ничего не понял( Мне нужна чиселка или стоп")

if __name__ == "__main__":
    disp.run_polling(bot)