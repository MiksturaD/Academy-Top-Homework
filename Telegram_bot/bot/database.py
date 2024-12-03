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
