import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from app.handlers import router
from loader import bot, dp

async def main():

    dp.include_router(router=router)
    await dp.start_polling(bot)

print(1)

if __name__ == '__main__':

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот Выключен')

