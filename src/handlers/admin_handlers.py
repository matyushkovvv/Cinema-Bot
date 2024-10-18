from datetime import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

from utils.requests import add_scheduled_post


# Хранение временных данных между шагами
user_data = {}

# Обработчик для добавления рассылки
async def add_announcement(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Отправьте текст и/или фото для рассылки.")
    return "WAITING_FOR_CONTENT"


# Обработчик для получения контента
async def receive_content(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    user = update.message.from_user.id
    user_data[user] = {'content_type': None, 'content': None, 'text_message': None}

    if update.message.photo:
        user_data[user]['content_type'] = 'photo'
        user_data[user]['content'] = update.message.photo[-1].file_id
    elif update.message.video:
        user_data[user]['content_type'] = 'video'
        user_data[user]['content'] = update.message.video.file_id
    elif update.message.text:
        user_data[user]['text_message'] = update.message.text

    await update.message.reply_text("Теперь отправьте дату и время для отложенной отправки в формате YYYY-MM-DD HH:MM")
    return "WAITING_FOR_DATETIME"


# Обработчик для получения даты и времени
async def receive_datetime(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user.id
    scheduled_date_time = update.message.text

    try:
        datetime.strptime(scheduled_date_time, "%Y-%m-%d %H:%M")
        user_data[user]['scheduled_date_time'] = scheduled_date_time

        # Сохранение в базу данных
        add_scheduled_post(user_data[user]['content_type'], user_data[user]['content'], user_data[user]['text_message'],
                           user_data[user]['scheduled_date_time'])

        await update.message.reply_text("Сообщение успешно сохранено и будет отправлено в указанное время.")
    except ValueError:
        await update.message.reply_text(
            "Неверный формат даты и времени. Пожалуйста, попробуйте снова в формате YYYY-MM-DD HH:MM")


async def remove_announcement(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Удаление рассылки")
    # Здесь реализуйте функционал удаления рассылки


async def add_movie(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Добавление фильма")
    # Здесь реализуйте функционал добавления фильма


async def remove_movie(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Удаление фильма")
    # Здесь реализуйте функционал удаления фильма


async def add_channel(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Добавление канала")
    # Здесь реализуйте функционал добавления канала


async def remove_channel(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Удаление канала")
    # Здесь реализуйте функционал удаления канала


async def change_welcome_message(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Изменить приветственное сообщение")
    # Здесь реализуйте функционал изменения приветственного сообщения


async def statistics(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Просмотр статистики")
    # Здесь реализуйте функционал просмотра статистики


async def add_administrator(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Добавления администратора")
    # Здесь реализуйте функционал добавления администратора
