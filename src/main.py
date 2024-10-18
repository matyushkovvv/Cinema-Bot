import logging

from aiogram import Bot, Dispatcher, types
import asyncio

from keyboards.admin import admin_main_keyboard
from keyboards.user import user_main_keyboard

from utils.database import init_database
from utils.requests import add_user

import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher()


# Логирование
logging.basicConfig(level=logging.INFO)


@dp.message(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    add_user(user_id)

    # Проверка id на соответствие администратору
    if user_id in config.ADMIN_IDs:
        await message.reply('Панель администратора', reply_markup=admin_main_keyboard())
    else:
        await message.reply('В разработке', reply_markup=user_main_keyboard())


# Функция основного запуска бота
if __name__ == '__main__':
    init_database()

    dp.start_polling(skip_updates=True)
