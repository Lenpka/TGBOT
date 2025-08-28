#rint("Hello  World")

import asyncio
import time

# async def send_message(num):
#     print(f' Сообщение типо отправлено {num}')
#     await asyncio.sleep(1)
#     print (f'Сообщение отправлено {num}')

# async def main():
#     for i in range(10):
#         await send_message(i)
# 10 секунд

async def send_messages(num):
    print (f'Сообщение отправлено : {num}')
    await asyncio.sleep(1)
    print(f"Доставлено {num}")

async def main ():
    lls = [send_messages(i) for i in range(10)]
    await asyncio.gather(*lls)


timeSt = time.time()

asyncio.run(main())
print(time.time() - timeSt)