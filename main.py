import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext

from keyboards.admin import admin_keyboard
from keyboards.user import user_keyboard

from utils.database import add_user, init_db

from config import ADMIN_IDs, TOKEN


# Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.chat_id
    add_user(user_id)

    # Проверка id на соответствие администратору
    if user_id in ADMIN_IDs:
        update.message.reply_text('Панель администратора', reply_markup=admin_keyboard())
    else:
        update.message.reply_text('В разработке', reply_markup=user_keyboard())


# Функция основного запуска бота
def main() -> None:

    init_db()

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
