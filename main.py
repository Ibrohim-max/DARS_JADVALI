import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandStart
from aiogram.types import FSInputFile, URLInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.utils.media_group import MediaGroupBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7622983219:AAGH4MkT9WzSlARmHm7LU840go5rJhjIfCQ")
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = [[types.KeyboardButton(text="Dushanba"),
           types.KeyboardButton(text="Sechanba")],
          [types.KeyboardButton(text="Chorchanba"),
           types.KeyboardButton(text="Paychanba")],
          [types.KeyboardButton(text="Juma"),
           types.KeyboardButton(text="To'garaklar")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="HAFTA KUNINI TANLANG...")
    await message.answer("Hafta kunini tanlang", reply_markup=keyboard)
    
@dp.message(F.text == "Dushanba")
async def cmd_film(message: types.Message):
    await message.answer('''1. Geometriya/Fizika 8:30- 9:15
2. Algebra 	                 9:20-10:05
3. Adabiyot	                10:10-10:55
4. Tarix	                      11:15-12:00
5. Robototexnika      12:20-13:05
6. Kimyo	                    13:10-13:55
7. Ona tili	                   14:00-14:45''')
    
@dp.message(F.text == "Sechanba")
async def cmd_film(message: types.Message):
    await message.answer('''1. Kimyo	                     8:30- 9:15
2. Fizika/geometriya  9:20-10:05
3. Geometriya/Fizika  10:10-10:55
4. Jismoniy     	            11:15-12:00
5. Ingliz tili                   12:20-13:05
6. Algebra	                   13:10-13:55
7. O'zbekiston tarixi    14:00-14:45''')
    
@dp.message(F.text == "Chorchanba")
async def cmd_film(message: types.Message):
    await message.answer('''1. Rus tili	                     8:30- 9:15
2. Algebra                     9:20-10:05
3. San'at ART               10:10-10:55
4. Ona tili                     11:15-12:00
5. Geometriya/Fizika   12:20-13:05
6. Biologiya	                13:10-13:55
7. Ingliz tili                  14:00-14:45
8. Geografiya              14:50-15:35''')
    

@dp.message(F.text == "Paychanba")
async def cmd_film(message: types.Message):
    await message.answer('''1. Informatika	          8:30- 9:15
2. Ingliz tili                 9:20-10:05
3. Fizka/geometriya  10:10-10:55
4. Rus tili                    11:15-12:00
5. Robototexnika      12:20-13:05
6. Adabiyot	                13:10-13:55
7. O'zbekiston tarixi 14:00-14:45
8. Biyologiya              14:50-15:35''')
    
@dp.message(F.text == "Juma")
async def cmd_film(message: types.Message):
    await message.answer('''1. Sinf soati	               8:30- 9:15
2. San'at ART             9:20-10:05
3. Ingliz tili                 10:10-10:55
4. Fizika/geometriya 11:15-12:00
5. Informatika             12:20-13:05
6. Tarbiya	                  13:10-13:55
7. Algebra                   14:00-14:45''')
    

@dp.message(F.text == "To'garaklar")
async def cmd_film(message: types.Message):
    await message.answer('''Dushanba - Matemtika 1-2 guruh
Sechanba - Ingliz tili 1-2 guruh
Chorchanba - 1-guruh Ona tili 2-guruh Matematika
Juma -Matematika 1-2 guruh
Shanba-Fizika 1-2 guruh 10:30-12:00''')


if __name__=="__main__":
    asyncio.run(main())
