from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup, default_state
from handlers.schedule_get import schedule_test_get_data, homework_get_data
from lexicon_ru import LEXICON_COMMAND_RU
from aiogram.filters import StateFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from keyboards import get_command_menu
import datetime

# from handlers.schedule_get import schedule_test_get_data
from keyboard.all_kb import main_kb
router = Router()
schedule = schedule_test_get_data()
homework = homework_get_data()
user_dict: dict[int, dict[str,str| int | bool]] = {}

# Начало и запрос данных
@router.message(CommandStart(), StateFilter(default_state))
async def cmd_start(message: Message):
    await message.answer('Запуск по команде /start и регистрация - /registration', reply_markup=main_kb(message.from_user.id))

@router.message(Command(commands = 'cancel'), StateFilter(default_state))
async def cancel_func(message: Message):
    await message.answer(
        text = 'Вы отменили регистрацию. Чтобы продолжить регистрацию - /registration',
    )

@router.message(Command(command = 'cancel'), ~StateFilter(default_state))
async def cancel_func(message: Message, state: FSMContext):
    await message.answer(
        text = 'Вы отменили регистрацию. Чтобы продолжить - /registration',
    )
    await state.clear()

@router.message(Command(commands=['registration']), StateFilter(default_state))
async def process_help_command(message: Message, state: FSMContext):
    await message.answer(text = "Введи, пожалуйста фамилию по образцу: КОНСТАНТИНОВ")
    await state.set_state(Reg.name)


#Данные студента
class Reg(StatesGroup):
    name = State()
    family = State()

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

@router.message(Command(commands=['start']))
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

@dp.callback_query()
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



from aiogram.filters import Command, CommandStart, StateFilter