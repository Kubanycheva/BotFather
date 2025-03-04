import asyncio

import aiogram
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


TOKEN = '7858920138:AAFpB3fkPZ3ZgZqpAASL6qGGis1zOATPgdA'

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def send_message(message: Message):
    await message.answer(f'Hello, {message.from_user.username}😊, Соз жаз')


@dp.message()
async def check_palindrom(message: Message):
    word = message.text.lower()
    if word == word[::-1]:
        await message.answer('Palindrom')
    else:
        await message.answer('Palindrom emes')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())