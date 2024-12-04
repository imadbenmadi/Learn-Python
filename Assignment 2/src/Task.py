import sqlite3
from database import DB_PATH

class Task:
    def __init__(self, title, due_date, description=None, flag="general", priority=None, task_id=None):
        self.id = task_id
        self.title = title
        self.due_date = due_date
        self.description = description if description is not None else ""
        self.flag = flag
        self.priority = priority
        self.status = "pending"

    def save_to_db(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tasks (type, title, due_date, description, priority, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.flag, self.title, self.due_date, self.description, self.priority, self.status))
            conn.commit()

    @staticmethod
    def get_all_tasks():
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM tasks"
            cursor.execute(query)
            tasks = cursor.fetchall()
            return tasks
                
        
    @staticmethod
    def load_from_db(task_id):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            if row:
                return Task(row[2], row[3], row[4], row[1], row[5], row[0])

    def update_in_db(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE tasks SET title=?, due_date=?, description=?, priority=?, status=?
                WHERE id=?
            ''', (self.title, self.due_date, self.description, self.priority, self.status, self.id))
            conn.commit()

    @staticmethod
    def delete_from_db(task_id):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()

    @staticmethod
    def get_pending_tasks():
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE status = 'pending'")
            return cursor.fetchall()

    @staticmethod
    def get_overdue_tasks(current_date):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE due_date < ? AND status = 'pending'", (current_date,))
            return cursor.fetchall()


class PersonalTask(Task):
    def __init__(self, title, due_date, priority="low", description=None, task_id=None):
        super().__init__(title, due_date, description, "personal", priority, task_id)


class WorkTask(Task):
    def __init__(self, title, due_date, description=None, task_id=None):
        super().__init__(title, due_date, description, "work", task_id=task_id)
        self.team_members = []

    def add_team_member(self, member):
        self.team_members.append(member)
