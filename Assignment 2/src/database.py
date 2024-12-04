import sqlite3

DB_PATH = "tasks.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                title TEXT NOT NULL,
                due_date TEXT NOT NULL,
                description TEXT,
                priority TEXT,
                status TEXT DEFAULT 'pending'
            )
        ''')
        conn.commit()
