from telegram import Update
from telegram.ext import ContextTypes

from utils.requests import add_user

from config import ADMIN_IDs

from keyboards.admin import admin_main_keyboard
from keyboards.user import user_main_keyboard


# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.chat_id
    add_user(user_id)

    # Проверка id на соответствие администратору
    if user_id in ADMIN_IDs:
        await update.message.reply_text('Панель администратора', reply_markup=admin_main_keyboard())
    else:
        await update.message.reply_text('В разработке', reply_markup=user_main_keyboard())

