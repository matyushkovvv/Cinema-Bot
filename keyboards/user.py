from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Функция для создания пользовательской клавиатуры
def user_keyboard():
    keyboard = [
        [InlineKeyboardButton("Категории", callback_data='categories')],
        [InlineKeyboardButton("Поиск по номеру", callback_data='search_by_number')],
        [InlineKeyboardButton("Поиск по названию", callback_data='search_by_title')],
        [InlineKeyboardButton("Обратная связь", callback_data='feedback')]
    ]
    return InlineKeyboardMarkup(keyboard)
