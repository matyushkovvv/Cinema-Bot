from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def category_keyboard():
    categories = ['Комедия', 'Драма', 'Триллер', 'Детектив', 'Мистика', 'Аниме', 'Боевик', 'Ужасы', 'Фантастика', 'Приключения']
    keyboard = [[InlineKeyboardButton(category, callback_data=f'category_{category}')] for category in categories]
    return InlineKeyboardMarkup(keyboard)