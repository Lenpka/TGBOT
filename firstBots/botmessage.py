from aiogram import Bot, Dispatcher # API и маршрутизация апдейтов
from aiogram.filters import Command # Хэндлер команд, то есть обработка начинающихся с / команд
from aiogram.types import Message
import os
from dotenv import load_dotenv

BOT_TOKEN = os.getenv("BOT_TOKEN") # Важно локально указать переменную

bot = Bot(token = BOT_TOKEN)
dispatcher = Dispatcher()

@dispatcher.message(Command(commands="start"))
async def message_send(message: Message):
    print("Сообщение получил")
    await message.answer("Привет, это воскрешение телеграм бота")

@dispatcher.message(Command(commands="help"))
async def help_info(message:Message):
    await message.answer(text = "Выбери опцию ниже по навигации: \n если их мало, пиши сюда:")
# Если не start и не help
@dispatcher.message()
async def if_not_list(message:Message):
    await message.answer("Извини не понимаю")
    await message.answer_photo(photo = "https://opencartsuppliers.com/ru/bl-content/uploads/media/product-photo9.png")

if __name__ == "__main__": # ЕСЛИ ИСПОЛНЯЕМЫЙ
    dispatcher.run_polling(bot)