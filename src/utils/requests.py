import sqlite3
from datetime import datetime

from telegram.ext import Application


# Извлечь всех подписанных пользователей
def get_all_users():
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("SELECT chat_id FROM users")
    users = cursor.fetchall()
    conn.close()

    return [user[0] for user in users]


# Добавить нового пользователя в системе
def add_user(chat_id):
    users = get_all_users()
    if chat_id in users:
        return

    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (chat_id) VALUES (?)", (chat_id,))
    conn.commit()
    conn.close()


# Добавить фильм
def add_film(video, genre, release_year, duration, description):
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO movies (video, genre, release_year, duration, description) VALUES (?, ?, ?, ?, ?)",
                   (video, genre, release_year, duration, description,))
    conn.commit()
    conn.close()


# Извлечь фильм по id
def get_film_by_id(id):
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("SELECT video, genre, release_year, duration, description FROM movies WHERE id = ?",
                   (id,))
    film_card = cursor.fetchall()
    conn.close()

    return film_card


# Удалить фильм по id
def delete_film_by_id(id):
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM movies WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# Добавить канал для подписывания
def add_channel(link, description):
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO channels (link, message) VALUES (?, ?)", (link, description,))
    conn.commit()
    conn.close()


# Извлечь все каналы для подписок
def get_all_channels():
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, link, message FROM channels")
    channels = cursor.fetchall()
    conn.close()

    # Возвращает лист list[i][j][k], i - id, j - ая ссылка на i канал, k - описание канала в j строке
    return channels


# Удалить канал по его id
def delete_channel_by_id(id):
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM channels WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# Добавить рассылку
def add_scheduled_post(content_type, content, text_message, scheduled_date_time):
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO scheduled_posts (content_type, content, text_message, scheduled_date_time) VALUES (?, ?, ?, ?)",
                   (content_type, content, text_message, scheduled_date_time,))
    conn.commit()
    conn.close()


# Получить список всех рассылок
def get_scheduled_posts():
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scheduled_posts")
    scheduled_post = cursor.fetchall()
    conn.close()

    return scheduled_post


# Удалить рассылку по id
def delete_scheduled_post_by_id(id):
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM scheduled_posts WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# Функция для отправки сообщений
async def send_scheduled_post(application: Application, chat_id: int, content_type: str, content: str,
                              text_message: str):
    if content_type == 'photo':
        await application.bot.send_photo(chat_id, content, caption=text_message)
    elif content_type == 'video':
        await application.bot.send_video(chat_id, content, caption=text_message)
    elif text_message:
        await application.bot.send_message(chat_id, text_message)


# Проверка базы данных и отправка запланированных сообщений
async def check_and_send_scheduled_posts(application: Application) -> None:
    conn = sqlite3.connect('./resources/cinema.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, content_type, content, text_message, scheduled_date_time FROM scheduled_posts WHERE scheduled_date_time <= ?",
        (datetime.now(),))
    posts = cursor.fetchall()

    for post in posts:
        post_id, content_type, content, text_message, scheduled_date_time = post

        for chat_id in get_all_users():
            await send_scheduled_post(application, chat_id, content_type, content, text_message)

        cursor.execute("DELETE FROM scheduled_posts WHERE id = ?", (post_id,))

    conn.commit()
    conn.close()
