from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from loader import bot
from app.googlemodel import Model

with open('bot_tg/tg_bot_recognition_food/app/proxy.txt') as f:
    proxy = f.read()

with open('bot_tg/tg_bot_recognition_food/app/api_key_google.txt') as f:
    api_key = f.read()

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('привет /start')

@router.message(Command('help'))
async def cmd_help(message):
    await message.answer('Вы нажали на кнопку помощи /help')

@router.message(F.photo)
async def photo(message):
    image_id = message.photo[-1].file_id
    image_file = await bot.download(image_id)
    image_bytes = image_file.read()

    model = Model(proxy=proxy, api_key=api_key)
    predict = model.predict(image_bytes = image_bytes, to_bytes=False)
    if predict['food'] == 'YES':
        predict_text = f"Название: {predict['name']}\nКБЖУ на 100гр.:\nКилокалории: {predict['kilocalories']}\nБелок: {predict['proteins']}\nУглеводы: {predict['carbohydrates']}\nЖиры: {predict['fats']}"
        await message.answer_photo(image_id, caption=str(predict_text))
    else:
        await message.answer(image_id, caption='На фото не найдена еда, попробуйте присласть фото с другого ракурса')