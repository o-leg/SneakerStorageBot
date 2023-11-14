"""

"""
import random

from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from ..constants import available_models


class ArticleState(StatesGroup):
    article = State()


@dp.message_handler(commands="model_by_article")
async def get_article(message: types.Message):
    await message.reply("Type in the article of the model you want to find...")
    await ArticleState.article.set()


@dp.message_handler(state=ArticleState.article)
async def get_model_availability_by_article(message: types.Message, state: FSMContext):
    message_text = ' '.join(message.text.split())
    available_models_metadata = available_models["article"].get(message_text, "No model found😢")
    if isinstance(available_models_metadata, str):
        await message.answer(available_models_metadata)
    if isinstance(available_models_metadata, dict):
        availability_by_size = available_models_metadata.get('availability_by_size')
        sizes = '\t|\t'.join([str(curr[0]) for curr in availability_by_size])
        size_availability = ' | '.join(["✅" if curr[1] else "❌" for curr in availability_by_size])

        await message.answer(f"Model name: {available_models_metadata.get('name')} \n\n "
                             f"Available sizes: \n "
                             f"{sizes} \n"
                             f"{size_availability} \n\n"
                             f"Article: {message_text}")
    await state.finish()