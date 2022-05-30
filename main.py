import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5412186458:AAFSC8kCpaI-IbGf4KjyCL5g7Nje61Garq0")
dp = Dispatcher(bot)

@dp.message_handler()
async def on_message(message: types.Message):
    await message.answer(message.text)
