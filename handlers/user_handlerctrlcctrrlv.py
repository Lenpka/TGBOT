from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon_ru import LEXICON_COMMAND_RU
from keyboards import get_command_menu
from handlers.schedule import FNM_first_course
import datetime

router = Router()


@router.message(Command(commands=['scheduletoday']))
async def process_start_command(message: Message):
    today = datetime.datetime.now()
    day = today.strftime("%A")
    lectures = FNM_first_course[day]
    res = '\n'.join([str(lecture) for lecture in lectures])
    await message.answer(res)
    await message.answer(text=LEXICON_COMMAND_RU['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_COMMAND_RU['/help'])


@router.message(Command(commands=['scheduletommorow']))
async def tommorow_command(message: Message):
    tommorow = datetime.datetime.now()
    day = tommorow.strftime("%A")
    lectures = FNM_first_course[day + 1]
    res = '\n'.join([str(lecture) for lecture in lectures])
    await message.answer(res)

@router.message(Command(commands=['homework']))
async def process_setmenu_command(message: Message, bot: Bot):
    await bot.set_my_commands(get_command_menu())
    await message.answer(text=LEXICON_COMMAND_RU['/homework'])