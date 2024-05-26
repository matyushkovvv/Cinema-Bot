import sqlite3
def init_db():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        chat_id INTEGER NOT NULL UNIQUE
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS films (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        video BLOB NOT NULL,
                        description TEXT NOT NULL,
                        categories TEXT NOT NULL
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS channels (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        link TEXT NOT NULL UNIQUE
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS schedules (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        chat_id INTEGER NOT NULL,
                        content_type TEXT NOT NULL,
                        content BLOB NOT NULL,
                        text TEXT,
                        scheduled_time TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

def add_user(chat_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (chat_id) VALUES (?)', (chat_id,))
    conn.commit()
    conn.close()

def get_all_users(admin_chat_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT chat_id FROM users WHERE chat_id != ?', (admin_chat_id,))
    users = cursor.fetchall()
    conn.close()
    return [user[0] for user in users]

def add_film(video, description, categories):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO films (video, description, categories) VALUES (?, ?, ?)', (video, description, categories))
    conn.commit()
    conn.close()

def delete_film(film_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM films WHERE id = ?', (film_id,))
    conn.commit()
    conn.close()

def add_channel(link):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO channels (link) VALUES (?)', (link,))
    conn.commit()
    conn.close()

def get_all_channels():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, link FROM channels')
    channels = cursor.fetchall()
    conn.close()
    return channels

def delete_channel(channel_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM channels WHERE id = ?', (channel_id,))
    conn.commit()
    conn.close()

def schedule_message(chat_id, content_type, content, text, scheduled_time):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO schedules (chat_id, content_type, content, text, scheduled_time) VALUES (?, ?, ?, ?, ?)',
                   (chat_id, content_type, content, text, scheduled_time))
    conn.commit()
    conn.close()

def get_scheduled_messages():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, chat_id, content_type, content, text, scheduled_time FROM schedules')
    messages = cursor.fetchall()
    conn.close()
    return messages

def delete_scheduled_message(schedule_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM schedules WHERE id = ?', (schedule_id,))
    conn.commit()
    conn.close()
