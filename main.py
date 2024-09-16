from aiogram.types import ContentType
from aiogram import F, B
from aiogram import types
from aiogram.types import Audio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
import os
import dotenv
dotenv.load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
from classes import English, Seminar_Chemistry, Lunch, Practice
from keyboards import set_main_menu_button


async def main():
    bot = Bot(token = BOT_TOKEN, parse_mode = "HTML")
    dp = Dispatcher()
    await set_main_menu_button(bot)
# Создаем объекты бота и диспетчера
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
# async def set_main_menu(bot:Bot):
#     main_commands = [
#         BotCommand(command = "/help",
#                    description= "Помощь с ботом"),
#         BotCommand(command = "/start",
#                    description= " Начнем")
#         BotCommand(command = "/help",
#                    description= "Помощь с ботом")
#         BotCommand(command = "/help",
#                    description= "Помощь с ботом")
#     ]

# Этот хэндлер будет срабатывать на команду "/start"
# @dp.message(lambda msg: msg.text == '/start')
# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

# dp.message(F.voice)
# async def sent_voice(message: Message):
#     print(Message)
#     await message.answer(text = 'вы прислали голосовое')

# # Этот хэндлер будет срабатывать на команду "/help"
# async def process_help_command(message: Message):
#     await message.answer(
#         'Напиши мне что-нибудь и в ответ '
#         'я пришлю тебе твое сообщение'
#     )

# async def send_photo_echo(message: Message):
#     print(message)
#     await message.reply_photo(message.photo[0].file_id)
# # Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# # кроме команд "/start" и "/help"
# dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#         await message.reply(text="Прости, не понимаю")
#     except TypeError:
#         await message.reply(text="Данный тип не поддерживается")


# # Регистрируем хэндлеры
# dp.message.register(process_start_command, Command(commands='start'))
# dp.message.register(process_help_command, Command(commands='help'))

# dp.message.register(send_photo_echo, F.photo)
# dp.message.register(send_echo)

# if __name__ == '__main__':
#     dp.run_polling(bot)

# # ...

# # Этот хэндлер будет срабатывать на отправку боту фото
