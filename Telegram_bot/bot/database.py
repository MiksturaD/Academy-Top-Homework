import sqlite3
from datetime import datetime
from typing import List, Dict

DATABASE_PATH = 'data/habits.db'

def init_db():
    """Инициализация базы данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            metric TEXT,
            target_date TEXT
        )
    ''')

    # Создание таблицы для хранения прогресса выполнения привычек
    cursor.execute('''CREATE TABLE IF NOT EXISTS habit_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id INTEGER NOT NULL,
        progress_date TEXT NOT NULL,
        progress TEXT NOT NULL,
        FOREIGN KEY (habit_id) REFERENCES habits (id)
    )''')

    #Создание таблицы для хранения данных о пользователе
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_state(
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    last_message_time TEXT
    )''')


    conn.commit()
    conn.close()

def add_habit(user_id: int, name: str, description: str, metric: str, target_date: str) -> None:
    """Добавление новой привычки в базу данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO habits (user_id, name, description, metric, target_date) VALUES (?, ?, ?, ?, ?)',
                   (user_id, name, description, metric, target_date))
    conn.commit()
    conn.close()

def get_habits(user_id: int) -> List[Dict]:
    """Получение всех привычек из базы данных для конкретного пользователя."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM habits WHERE user_id = ?', (user_id,))
    habits = cursor.fetchall()
    conn.close()
    return [{'id': habit[0], 'user_id': habit[1], 'name': habit[2], 'description': habit[3], 'metric': habit[4], 'target_date': habit[5]} for habit in habits]

def delete_habit(user_id: int, habit_id: int) -> bool:
    """Удаление привычки из базы данных по ID."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM habits WHERE user_id = ? AND id = ?', (user_id, habit_id))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
    except sqlite3.Error as e:
        print(f"Ошибка при удалении привычки: {e}")
        return False

def add_habit_progress(habit_id: int, progress_date: str, progress: str) -> None:
    """Добавление прогресса выполнения привычки."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO habit_progress (habit_id, progress_date, progress) VALUES (?, ?, ?)', (habit_id, progress_date, progress))
    conn.commit()
    conn.close()

def get_habit_progress(habit_id: int) -> List[Dict]:
    """Получение прогресса выполнения привычки по ID."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM habit_progress WHERE habit_id = ?', (habit_id,))
    progress = cursor.fetchall()
    conn.close()
    return [{'id': p[0], 'habit_id': p[1], 'progress_date': p[2], 'progress': p[3]} for p in progress]

def update_user_username(user_id: int, username: str) -> None:
    """Обновление имени пользователя в базе данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_state (user_id, username) VALUES (?, ?) ON CONFLICT(user_id) '
                   'DO UPDATE SET username = excluded.username', (user_id, username))
    conn.commit()
    conn.close()

def get_user_username(user_id: int) -> str:
    """Получение имени пользователя из базы данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM user_state WHERE user_id = ? LIMIT 1', (user_id,))
    username = cursor.fetchone()
    conn.close()
    return username[0] if username else None

def get_last_message_time(user_id: int) -> str:
    """Получение времени последнего сообщения пользователя из базы данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT last_message_time FROM user_state WHERE user_id = ? LIMIT 1', (user_id,))
    last_message_time = cursor.fetchone()
    conn.close()
    return last_message_time[0] if last_message_time else None

def update_last_message_time(user_id: int) -> None:
    """Обновление времени последнего сообщения пользователя в базе данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    last_message_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    cursor.execute('INSERT INTO user_state (user_id, last_message_time) VALUES (?, ?) ON CONFLICT(user_id) DO UPDATE SET last_message_time = excluded.last_message_time', (user_id, last_message_time))
    conn.commit()
    conn.close()

# Tortise или tortoice sql библиотеки ORM