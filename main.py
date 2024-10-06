from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from decouple import config
redis_url = config('REDIS_URL')
from handlers import user_handlerctrlcctrrlv
from aiogram.filters import StateFilter
from aiogram.enums.parse_mode import ParseMode
import asyncio
import logging
from keyboards import get_command_menu
from keyboards import set_main_menu
from aiogram.types import Message
import dotenv
import os
from aiogram.types import CallbackQuery
from decouple import config
import redis
from aiogram.fsm.storage.memory import MemoryStorage
dotenv.load_dotenv()
from aiogram.fsm.storage.redis import RedisStorage, Redis
add = os.getenv('REDIS_URL')
r = Redis(host=add, port=6379, db=0, username='default', password=os.getenv('PASSWORD'))
#admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]

redis_url = config('REDIS_URL')

from aiogram.fsm.storage.redis import RedisStorage
BOT_TOKEN = os.getenv('BOT_TOKEN')
logger = logging.getLogger(__name__)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = RedisStorage(redis = r)
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
# if message.from_user.id in user_handlerctrlcctrrlv.user_dict:
#     print({user_handlerctrlcctrrlv.user_dict[message.from_user.id]["name"]})
if __name__ == '__main__':
    asyncio.run(main())
