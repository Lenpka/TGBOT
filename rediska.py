from main import bot
import hashlib
import dotenv
import redis
import os
dotenv.load_dotenv()
from aiogram.fsm.storage.redis import RedisStorage
r = redis.Redis(host=os.getenv('REDIS_URL'), port=6379, db=0, username='default', password=os.getenv('PASSWORD'))
# password = 'starwars'
# password_hash = hashlib.sha256(password.encode()).hexdigest()
# print(password_hash)
#storage = RedisStorage.from_url('redis://127.0.0.1:6379/0')
try:
    info = r.info()
    print(info['redis_version'])
    response = r.ping()
    if response:
         print("Подключение успешно!")
    else:
         print("Не удалось подключиться к Redis.")
except redis.exceptions.RedisError as e:
    print(f"Ошибка: {e}")
