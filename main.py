from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from handlers import user_handlerctrlcctrrlv
from aiogram.enums.parse_mode import ParseMode # Для смены режима парсинга
import asyncio
import logging
from logging import basicConfig
from keyboards import get_command_menu
from keyboards import set_main_menu
import dotenv
import os

from config_folder.config import load_config, Config

config:Config = load_config("C:\VSProjects\BOT\TGBOT\.env")
bot_token = config.bot.token
superadmin = config.bot.admin_ids

logger = logging.getLogger(__name__)
bot = Bot(bot_token, default = DefaultBotProperties(parse_mode = ParseMode.HTML)) # Согласно документации
# Все отправленные боту сообщения будут обработаны как html, поэтому не придется обрабатывать
# каждое сообщение по отдельности

async def main(): # Цикл входа
    logger.basicConfig(
        level = logging.DEBUG,
        format = '%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s'
    )
    logging.info("STARTING BOT")

    config: Config = load_config()
    bot_token = config.bot.token
    bot = Bot(token = bot_token, default = DefaultBotProperties(parse_mode = ParseMode.HTML))
    # Все обработанные запросы боту приходят в HTML, поэтому не надо прописывать каждый
    # случай
    disp = Dispatcher(bot)

    disp.workflow_data.update()
    await set_main_menu(bot)

    #Роутеры
    logger.info('А вот и роутеры')

    #Миддлвари
    logger.info('А ВОТ И МИДДЛ(т)ВАРИ')
    #Удаляем накопившиеся апдейты и запускаем пулинг
    await bot.delete_webhook(drop_pending_updates= True)
    await disp.start_polling(bot)

asyncio.run(main())

# dotenv.load_dotenv()

# #BOT_TOKEN = os.getenv('BOT_TOKEN')
# BOT_TOKEN = bot_token
# logger = logging.getLogger(__name__)
# bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# dp = Dispatcher()


# async def main():
#     logging.basicConfig(level=logging.DEBUG,
#                         format='[{asctime}] #{levelname:8} {filename}:{lineno} - {name} - {message}',
#                         style='{'
#                         )

#     logger.info('Starting Bot')
#     dp.include_routers(user_handlerctrlcctrrlv.router)

#     # Эта строчка по идее должна быть аналогом предыдущей, но почему то она не работает
#     await bot.set_my_commands(get_command_menu())
#     await set_main_menu(bot)
#     # Удаляем сообщения, которые пришли ранее
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())
