from aiogram import Bot, Dispatcher
from config_folder.config import Config, load_config

config:Config = load_config("C:\VSProjects\BOT\TGBOT\.env")

bot = Bot(token = config.bot.token)
bot_token = config.bot.token
superadmin = config.bot.admin_ids
print(bot_token, '\n', superadmin)