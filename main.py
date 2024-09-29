from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from decouple import config
redis_url = config('REDIS_URL')
from handlers import user_handlerctrlcctrrlv
from aiogram.filters import Command, CommandStart, StateFilter
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
dotenv.load_dotenv()
from aiogram.fsm.storage.redis import RedisStorage
r = redis.Redis(host=os.getenv('REDIS_URL'), port=6379, db=0, username='default', password=os.getenv('PASSWORD'))
#admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]

redis_url = config('REDIS_URL')

from aiogram.fsm.storage.redis import RedisStorage
BOT_TOKEN = os.getenv('BOT_TOKEN')
logger = logging.getLogger(__name__)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = RedisStorage(config('REDIS_URL'))
dp = Dispatcher(storage=storage)
@dp.callback_query(StateFilter(FSMFillForm.fill_wish_news),
                   F.data.in_(['yes_news', 'no_news']))
async def process_wish_news_press(callback: CallbackQuery, state: FSMContext):
    # Cохраняем данные о получении новостей по ключу "wish_news"
    await state.update_data(wish_news=callback.data == 'yes_news')
    # Добавляем в "базу данных" анкету пользователя
    # по ключу id пользователя
    user_dict[callback.from_user.id] = await state.get_data()
    # Завершаем машину состояний
    await state.clear()
    # Отправляем в чат сообщение о выходе из машины состояний
    await callback.message.edit_text(
        text='Спасибо! Ваши данные сохранены!\n\n'
             'Вы вышли из машины состояний'
    )
    # Отправляем в чат сообщение с предложением посмотреть свою анкету
    await callback.message.answer(
        text='Чтобы посмотреть данные вашей '
             'анкеты - отправьте команду /showdata'
    )



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
if message.from_user.id in user_handlerctrlcctrrlv.user_dict:
    print({user_handlerctrlcctrrlv.user_dict[message.from_user.id]["name"]})
if __name__ == '__main__':
    asyncio.run(main())
