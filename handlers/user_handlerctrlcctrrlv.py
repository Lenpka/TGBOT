from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart, CallbackQuery
from aiogram.types import Message

from handlers.schedule_get import schedule_test_get_data, homework_get_data
from lexicon_ru import LEXICON_COMMAND_RU
from keyboards import get_command_menu
import datetime
# from handlers.schedule_get import schedule_test_get_data
from keyboard.all_kb import main_kb
router = Router()
schedule = schedule_test_get_data()
homework = homework_get_data()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск по команде /start', reply_markup=main_kb(message.from_user.id))

# class DB:
#     answer_data = {}


# @dp.message_handler(commands='start', state=None)
# async def start(message: types.Message):
#     await RegisterMessages.step1.set()
#     await bot.send_message(message.from_user.id, text='Здравствуйте! Введите имя:')


# @dp.message_handler(content_types='text', state=RegisterMessages.step1)
# async def reg_step1(message: types.Message):
#     async with lock:
#         DB.answer_data['name'] = message.text
#     await bot.send_message(message.from_user.id, text='Принято! Введите фамилию:')
#     await RegisterMessages.next()


# @dp.message_handler(content_types='text', state=RegisterMessages.step2)
# async def reg_step2(message: types.Message, state: FSMContext):
#     async with lock:
#         DB.answer_data['surname'] = message.text
#     await bot.send_message(message.from_user.id, text='Принято! Чтобы посмотреть данные введите команду /check')
#     await state.finish()


# @dp.message_handler(commands='check')
# async def get_reg_data(message: types.Message):
#     answer = ''
#     answer += f'Имя: {DB.answer_data["name"]}\n\n'
#     answer += f'Фамилия: {DB.answer_data["surname"]}'
#     await bot.send_message(message.from_user.id, text=answer)


# @router.callback_query(F.data == 'get_person')
# async def send_random_person(call: CallbackQuery):
#     # await call.answer('Генерирую случайного пользователя')
#     formatted_message = (
#         f"👤 <b>Имя:</b> {user['name']}\n"
#         f"🏠 <b>Адрес:</b> {user['address']}\n"
#         f"📧 <b>Email:</b> {user['email']}\n"
#         f"📞 <b>Телефон:</b> {user['phone_number']}\n"
#         f"🎂 <b>Дата рождения:</b> {user['birth_date']}\n"
#         f"🏢 <b>Компания:</b> {user['company']}\n"
#         f"💼 <b>Должность:</b> {user['job']}\n"
#     )
#     await call.message.answer(formatted_message)
def getDay(day: datetime.datetime) -> str:
    day = day.strftime("%A")
    lectures = schedule[day]
    return '\n'.join([str(lecture) for lecture in lectures])
def getWork(day: datetime.datetime) -> str:
    day = day.strftime("%A")
    work = homework[day]
    return '\n'.join([str(ork) for ork in work])
@router.message(Command(commands=['scheduletoday']))
async def process_start_command(message: Message):
    today = datetime.datetime.now()
    res = getDay(today)
    await message.answer(res)
    await message.answer(text=LEXICON_COMMAND_RU['/start'])

@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_COMMAND_RU['/help'])
@router.message(Command(commands=['/start']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_COMMAND_RU['/start'])


@router.message(Command(commands=['scheduletommorow']))
async def tommorow_command(message: Message):
    tommorow = datetime.datetime.now() + datetime.timedelta(days=1)
    res = getDay(tommorow)
    await message.answer(res)
@router.message(Command(commands=['scheduleaftertommorow']))
async def tommorow_command(message: Message):
    tommorow = datetime.datetime.now() + datetime.timedelta(days=2)
    res = getDay(tommorow)
    await message.answer(res)

@router.message(Command(commands=['homework']))
async def process_setmenu_command(message: Message, bot: Bot):
    tommorow = datetime.datetime.now() + datetime.timedelta(days=1)
    res = getWork(tommorow)
    await message.answer(res)

@router.message(Command(commands=['homeworknotnow']))
async def process_setmenu_command(message: Message, bot: Bot):
    tommorow = datetime.datetime.now() + datetime.timedelta(days=2)
    res = getWork(tommorow)
    await message.answer(res)