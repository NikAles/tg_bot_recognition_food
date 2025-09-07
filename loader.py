from aiogram import Bot, Dispatcher

with open('bot_tg/tg_bot_recognition_food/api_key.txt') as f:
    API_KEY = f.read()

bot = Bot(token=API_KEY)
dp = Dispatcher()


