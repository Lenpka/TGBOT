from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon_ru import LEXICON_COMMANDS_RU
from keyboards import get_command_menu

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_COMMANDS_RU['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_COMMANDS_RU['/help'])


@router.message(Command(commands=['deletemenu']))
async def process_deletemenu_command(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text=LEXICON_COMMANDS_RU['/deletemenu'])


@router.message(Command(commands=['setmenu']))
async def process_setmenu_command(message: Message, bot: Bot):
    await bot.set_my_commands(get_command_menu())
    await message.answer(text=LEXICON_COMMANDS_RU['/setmenu'])