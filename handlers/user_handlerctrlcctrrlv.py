from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from handlers.schedule_get import schedule_test_get_data, homework_get_data
from lexicon_ru import LEXICON_COMMAND_RU
from keyboards import get_command_menu
import datetime
# from handlers.schedule_get import schedule_test_get_data

router = Router()
schedule = schedule_test_get_data()
homework = homework_get_data()

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