from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def admin_main_keyboard():
    keyboard = [
        [InlineKeyboardButton("Добавить рассылку", callback_data='add_announcement'),
         InlineKeyboardButton("Удалить рассылку", callback_data='remove_announcement')],
        [InlineKeyboardButton("Добавить фильм", callback_data='add_movie'),
         InlineKeyboardButton("Удалить фильм", callback_data='remove_movie')],
        [InlineKeyboardButton("Добавить канал", callback_data='add_channel'),
         InlineKeyboardButton("Удалить канал", callback_data='remove_channel')],
        [InlineKeyboardButton("Изменить приветственное сообщение", callback_data='change_welcome_message')],
        [InlineKeyboardButton("Статистика", callback_data='statistics')],
        [InlineKeyboardButton("Добавить администратора", callback_data='add_administrator')]
    ]
    return InlineKeyboardMarkup(keyboard)

