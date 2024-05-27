import numpy as np
import onnxruntime as rt

from PIL import Image

from config import MODEL_TO_USE_PATH, SNEAKERS_THRESHOLD, REVERSE_CLASS_MAPPING
from db_api.body_formulator import RequestBodyFormulator
from db_api.database_api import perform_request
from keyboards.utils.output_formulator import format_message
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class PhotoState(StatesGroup):
    photo = State()


@dp.message_handler(commands="model_by_photo")
async def get_photo(message: types.Message):
    await message.reply("Download image of the model you want to find...")
    await PhotoState.photo.set()


def preprocess_input_custom(downloaded_image):
    # Convert BytesIO to PIL Image
    input_image = Image.open(downloaded_image)

    # Resize the image to match the model input size
    resized_image = input_image.resize((240, 240))

    # Convert PIL Image to NumPy array
    img_array = np.array(resized_image)

    # Normalize pixels into range [0, 1]
    normalized_image = img_array / 255.0
    return normalized_image


def predict_class_probabilities(downloaded_image):
    sess = rt.InferenceSession(MODEL_TO_USE_PATH)
    input_name = sess.get_inputs()[0].name

    img = preprocess_input_custom(downloaded_image)
    img = np.expand_dims(img, axis=0)
    predicted_class_probabilities = sess.run(None, {input_name: img.astype(np.float32)})[0]
    return predicted_class_probabilities


def predict_top3_classes(downloaded_image):
    proba_predicts = predict_class_probabilities(downloaded_image).flatten()
    top_3_classes = np.argsort(proba_predicts)[-3:][::-1]
    top_3_probabilities = proba_predicts[top_3_classes]
    print(top_3_probabilities)
    print("Sum: ", sum(top_3_probabilities))
    # case: photo does not have sneakers in it or does not exist in database
    if sum(top_3_probabilities) < SNEAKERS_THRESHOLD: # or top_3_classes[0] < SNEAKERS_THRESHOLD:
        return []
    return top_3_classes


@dp.message_handler(content_types=types.ContentType.PHOTO, state=PhotoState.photo)
async def get_model_availability_by_photo(message: types.Message, state: FSMContext):
    # print("Second function for by photo: ", message)
    print("File id: ", message.photo[-1].file_id)
    downloaded_image = await message.bot.download_file_by_id(message.photo[-1].file_id)
    top3_classes = predict_top3_classes(downloaded_image)
    top3_sneaker_articles = [REVERSE_CLASS_MAPPING[predicted_class] for predicted_class in top3_classes]
    if not list(top3_classes):
        await message.answer("Photo may not contain sneakers from our storage😢 or does not contain any sneakers")
    else:
        something_went_wrong = 0  # problems of obsolete model / updated storage
        for article in top3_sneaker_articles:
            body_by_article_request = RequestBodyFormulator.form_by_article(article)
            response = perform_request(body_by_article_request)
            if not response:
                something_went_wrong += 1
                continue

            found_model = response[0]
            caption = format_message(found_model)

            await message.answer_photo(found_model["image"], caption=caption, parse_mode="Markdown")
            await state.finish()

        if something_went_wrong == 3:
            await message.answer("Well, something might be wrong from our side😢. "
                                 "Please, reach out to us through @oleh_nulp, so that we can investigate the issue.")
    await state.finish()
