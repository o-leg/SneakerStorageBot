"""
In telegram ```/start``` is used to start conversation with the bot.

This file defines how ```/start``` works.
"""
from aiogram import types
from loader import dp


@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    await message.answer(
        f"Hi, {message.from_user.full_name} Hi🤚, I am your personal sneakers sales assistant."
        f"Type /help command and get to know what I can do for you😎.")