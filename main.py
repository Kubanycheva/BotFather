import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


TOKEN = '7858920138:AAFpB3fkPZ3ZgZqpAASL6qGGis1zOATPgdA'

bot = Bot(token=TOKEN)
dp = Dispatcher()


# secret_number = random.randint(1, 100)
# count = 0


@dp.message(Command('start'))
async def send_message(message: Message):
    await message.answer(f'Hello, {message.from_user.username}😊, Соз жаз')


# @dp.message()
# async def check_number(message: Message):
#     word = message.text.lower()
#     if word == word[::-1]:
#         await message.answer('Palindrom')
#     else:
#         await message.answer('Palindrom emes')






# @dp.message()
# async def check_number(message: Message):
#     global count
#     number = int(message.text)
#     count += 1
#
#     if number > secret_number:
#         await message.answer('Сиз жазган сан чон')
#     elif number < secret_number:
#         await message.answer('Сиз жазган сан кичине')
#     else:
#         await message.answer(f'Куттуктайбыз сиз {secret_number} санын {count} иретте таптыныз')
#




@dp.message()
async def check_number(message: Message):
    number_one = int(message.text)
    number_two = int(message.text)
    znak = await message.answer('+ - * / : ')

    if znak == '+':
        await message.answer(number_one + number_two)
    elif znak == '-':
        await message.answer(number_one - number_two)
    elif znak == '*':
        await message.answer(number_one * number_two)
    elif znak == '/':
        await message.answer(number_one / number_two)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())