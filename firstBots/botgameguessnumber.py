from aiogram.types import Message
import time
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import F
import os
BOT_TOKEN:str
BOT_TOKEN = os.getenv("BOT_TOKEN") # Важно локально указать переменную

bot = Bot(token=BOT_TOKEN)
disp = Dispatcher()


user_state = {
    "Is_Active": 0,
    "Count":0,
    "attempts" : 0


}

def getRandom() ->int:
    value = random.randint(1, 100)
    return value
value = getRandom()
@disp.message(Command(commands="startgame"))
async def startmessage(message:Message) -> int:
    print(f'ТССССССССССССС, ТИХО, СЕКРЕТНОЕ ЗНАЧЕНИЕ VALUE = {value}')
    await message.answer("ДАВАЙ ИГРАТЬ, ДАВАЙ натуральное ЧИСЛО ОТ 1 до 100 угадаем")
    user_state["Is_Active"] = 1
print(user_state["Is_Active"])

@disp.message(lambda x: x.text and x.text.isdigit() and int(x.text) == value)
async def youGuess(message:Message):
    await message.answer ("МОИ ПОЗДРАВЛЕНИЕ, В ТОЧКУ, ЕЩЕ РАЗ? Я ЗАГАДАЛ!")
    global value
    value = getRandom()
    if user_state["Is_Active"] == 1:

        user_state["Count"] += 1

@disp.message (lambda x: x.text and x.text.isdigit() and int(x.text) < value)
async def someBigger(message:Message):
    await message.answer("НЕМНОГО НЕДОБОР")
    if user_state["Is_Active"] == 1:
        user_state['attempts']+=1 


@disp.message (lambda x: x.text and x.text.isdigit() and int(x.text) > value)
async def someBigger(message:Message):
    await message.answer("НЕМНОГО ПЕРЕБОР")
    if user_state["Is_Active"] == 1:
        user_state['attempts'] += 1

@disp.message(Command(commands = ("help")))
async def sendHelp(message:Message):
    await message.answer("Чтобы поиграть напиши /start \n чтобы закончить - /end")
@disp.message(Command(commands = ("end")))
async def sendHelp(message:Message):
    await message.answer("Было приятно играть!")
    user_state["attempts"] = 0
    user_state["Count"] = 0
    user_state["Is_Active"]= 0
@disp.message(Command(commands = ("stat")))
async def sendHelp(message:Message):
    await message.answer(f"Твоя точность = {user_state['Count']/user_state['attempts']}")

@disp.message()
async def iDontUnderstand(message:Message):
    await message.answer("Честно я ничего не понял( Мне нужна чиселка или стоп")

if __name__ == "__main__":
    disp.run_polling(bot)