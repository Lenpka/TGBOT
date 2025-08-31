from aiogram.types import Message
import time
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart # = Command(commands = "start")
from aiogram import F
import os
from environs import Env
env:Env = Env()
BOT_TOKEN:str
BOT_TOKEN = os.getenv("BOT_TOKEN") # Важно локально указать переменную
#MY_ENV = os.getenv("MY_ENV")
MY_ENV = env("ADMIN_IDS")
bot = Bot(token=BOT_TOKEN)
disp = Dispatcher()
users = {}



@disp.message(CommandStart)
async def startmessage(message:Message) -> int:
    print(f'ТССССССССССССС, ТИХО, СЕКРЕТНОЕ ЗНАЧЕНИЕ ID = {message.message_id}, ')
    await message.answer("ДАВАЙ ИГРАТЬ, ДАВАЙ натуральное ЧИСЛО ОТ 1 до 100 угадаем")
    if message.from_user.id not in users:
      
        users[message.from_user.id] ={
    "Is_Active": 0,
    "Count":0,
    "attempts" : 0
}
    users[message.from_user.id]["Is_Active"] = 1
    print(users[message.from_user.id]["Is_Active"])


@disp.message(lambda message: message.from_user.id == MY_ENV)
async def printstatus(message:Message):
    await message.answer("ТЫ АДМИН")
    print(message.answer(message.from_user.id))

if __name__ == "__main__":
    disp.run_polling(bot)
