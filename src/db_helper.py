import sqlite3
from src import config as cfg


def create_table():
    with sqlite3.connect(cfg.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        ''')
        connection.commit()


def add_data_to_db(first_name, last_name):
    with sqlite3.connect(cfg.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
        connection.commit()
    return True