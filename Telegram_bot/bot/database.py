import sqlite3
from typing import List, Dict

DATABASE_PATH = 'data/habits.db'

def init_db():
    """Инициализация базы данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
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

    conn.commit()
    conn.close()

def add_habit(name: str, description: str, target_date: str) -> None:
    """Добавление новой привычки в базу данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO habits (name, description, target_date) VALUES (?, ?, ?)', (name, description, target_date))
    conn.commit()
    conn.close()

def get_habits() -> List[Dict]:
    """Получение всех привычек из базы данных."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM habits')
    habits = cursor.fetchall()
    conn.close()
    return [{'id': habit[0], 'name': habit[1], 'description': habit[2], 'target_date': habit[3]} for habit in habits]

def delete_habit(name: str) -> bool:
    """Удаление привычки из базы данных по названию."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM habits WHERE name = ?', (name,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

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

