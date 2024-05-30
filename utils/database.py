import sqlite3


def init_database():
    # Создаем подключение к базе данных
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    # Запрос для создания таблицы для хранения id и chat_id
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL
    )
    ''')

    # Запрос для создания таблицы для хранения информации о фильмах
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video BLOB NOT NULL,
        genre TEXT NOT NULL,
        release_year INTEGER NOT NULL,
        duration INTEGER NOT NULL,
        description TEXT
    )
    ''')

    # Запрос для создания таблицы для хранения ссылок на каналы с текстовым сообщением
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link TEXT NOT NULL,
        message TEXT
    )
    ''')

    # Запрос для создания таблицы для хранения рассылки с отложенной публикацией
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scheduled_posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content_type TEXT NOT NULL,
        content BLOB,
        text_message TEXT,
        scheduled_date_time DATETIME NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
