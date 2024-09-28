from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType
#from main import admins

def main_kb(user_id: int):
    kb_list = [
        [KeyboardButton(text="Расписание"), KeyboardButton(text="График дежурств")],
        [KeyboardButton(text="Домашние работы"), KeyboardButton(text="Рейтинг")],

    ]
    #if user_id in admins:
        #kb_list.append([KeyboardButton(text="Администрирование")])
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Используй меню')
    return keyboard

def spec_kb():
    kom_list = [
    [KeyboardButton(text="Поделиться номером", request_contact=True)],
    [KeyboardButton(text="Отправить викторину/опрос", request_poll=KeyboardButtonPollType())]
    ]
    keyboard_spec = ReplyKeyboardMarkup(keyboard = kom_list, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Используй специальное меню')
    return keyboard_spec