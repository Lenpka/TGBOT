from dataclasses import dataclass
from environs import Env
@dataclass
class DataBaseConfig:
    name: str
    host: str
    user: str
    password: str

@dataclass
class TgBot:
    token: str
    admin_ids: int

@dataclass
class Config:
    bot: TgBot
    database:DataBaseConfig

env : Env = Env()
env.read_env()  



config = Config(
    bot = TgBot(
        token = env("BOT_TOKEN"),
        admin_ids = env("ADMIN_IDS")
    ),
    database = DataBaseConfig(
        name = env("DB_NAME"),
        host = str(env("DB_HOST")),
        user = env("DB_USER"),
        password = env("DB_PASSWORD")
    )
)

#Выведем - убедимся, что все доступно
print('BOT_TOKEN:', config.bot.token)
print('ADMIN_IDS:', config.bot.admin_ids)
print()
print('DB_NAME:', config.database.name)
print('DB_HOST:', config.database.host)
print('DB_USER:', config.database.user)
print('DB_PASSWORD:', config.database.password)
print('ТАК РАБОТАЕТ ВЫВОД')

def load_config(path:str | None = None) -> Config:
    env:Env = Env()
    env.read_env(path)

    return Config(
        bot = TgBot(
            token= env("BOT_TOKEN"),
            admin_ids= env("ADMIN_IDS")),
        database=
        DataBaseConfig(
            name = env("DB_NAME"),
            host = env("DB_HOST"),
            user = env("DB_USER"),
            password = env("DB_PASSWORD")
        )
    )
