from aiogram import Bot, Dispatcher # API и маршрутизация апдейтов
from aiogram.filters import Command # Хэндлер команд, то есть обработка начинающихся с / команд
from aiogram.types import Message, ContentType
import os
from dotenv import load_dotenv
#add photo handler
from aiogram import F # Магический фильтр


BOT_TOKEN = os.getenv("BOT_TOKEN") # Важно локально указать переменную

bot = Bot(token = BOT_TOKEN)
dispatcher = Dispatcher()


async def message_send(message: Message):
    print("Сообщение получил")
    await message.answer("Привет, это воскрешение телеграм бота")


async def help_info(message:Message):
    await message.answer(text = "Выбери опцию ниже по навигации: \n если их мало, пиши сюда:")

async def photo_get(message:Message ):
    await message.answer("Классная фотка, держи обратно! \n")
    await message.reply_photo(message.photo[0].file_id)



# Если не start и не help

async def if_not_list(message:Message):
    await message.answer("Извини не понимаю")
    await message.answer_photo(photo = "https://opencartsuppliers.com/ru/bl-content/uploads/media/product-photo9.png")

#Регистрация методов
dispatcher.message.register(message_send, Command(commands = "start"))
dispatcher.message.register(help_info, Command(commands = "help"))
dispatcher.message.register(photo_get, F.photo)
dispatcher.message.register(if_not_list)
if __name__ == "__main__": # ЕСЛИ ИСПОЛНЯЕМЫЙ
    dispatcher.run_polling(bot)