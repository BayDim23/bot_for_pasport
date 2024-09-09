import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from datetime import datetime, timedelta
from dadata import Dadata
import json

from config import TOKEN2

bot = Bot(token=TOKEN2)
dp = Dispatcher()

token = "55c4eb40824e5dc3c3d23e7a93ce370d69277f18"
secret = "83f31577a90e2efe7b25b325a08c047490e8b28f"

@dp.message(Command("start"))
async def start_command(message: Message):
   await message.answer(f"Напиши паспортные двнные в формате /passport 0000 000000 которые нужно проверить")

@dp.message(Command("passport"))
async def send_info(message: Message):
   dadata = Dadata(token, secret)
   result = dadata.clean("passport", message.text)

   qc_result = result.get("qc")
   if qc_result == 1:
       await message.answer("Неправильный формат серии или номера")
   elif qc_result == 0:
       await message.answer("Действующий паспорт")
   elif qc_result == 2:
       await message.answer("Исходное значение пустое")
   else:
       await message.answer("Недействительный паспорт")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())