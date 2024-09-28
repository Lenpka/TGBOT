from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from handlers import user_handlerctrlcctrrlv
from aiogram.enums.parse_mode import ParseMode
import asyncio
import logging
from keyboards import get_command_menu
from keyboards import set_main_menu
import dotenv
import os
from decouple import config
#admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]
dotenv.load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
logger = logging.getLogger(__name__)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='[{asctime}] #{levelname:8} {filename}:{lineno} - {name} - {message}',
                        style='{'
                        )

    logger.info('Starting Bot')
    dp.include_routers(user_handlerctrlcctrrlv.router)

    # Эта строчка по идее должна быть аналогом предыдущей, но почему то она не работает
    await bot.set_my_commands(get_command_menu())
    await set_main_menu(bot)
    # Удаляем сообщения, которые пришли ранее
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
