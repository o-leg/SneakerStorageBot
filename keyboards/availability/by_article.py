"""

"""
from db_api.body_formulator import RequestBodyFormulator
from db_api.database_api import perform_request
from keyboards.utils.output_formulator import format_sizes, format_message
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class ArticleState(StatesGroup):
    article = State()


@dp.message_handler(commands="model_by_article")
async def get_article(message: types.Message):
    await message.reply("Type in the article of the model you want to find...")
    await ArticleState.article.set()


@dp.message_handler(state=ArticleState.article)
async def get_model_availability_by_article(message: types.Message, state: FSMContext):
    message_text = ' '.join(message.text.split())
    body_by_article_request = RequestBodyFormulator.form_by_article(message_text)
    print("Body for request by article: ", body_by_article_request)
    response = perform_request(body_by_article_request)
    print("Response be article: ", response)
    if not response:
        await message.answer("No model found😢")
    else:
        found_model = response[0]
        print(found_model['sizes'])
        caption = format_message(found_model)

        await message.answer_photo(found_model["image"], caption=caption, parse_mode="Markdown")
        print("Response: ", found_model)
    await state.finish()
