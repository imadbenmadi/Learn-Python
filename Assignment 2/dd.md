Got it! Since you need both front-end (HTML pages) and back-end (Flask API with SQLite3), here's a comprehensive project structure with an example of how to integrate HTML pages with Flask routes. This will help you build a Task Management System with Flask and SQLite3.

### **1. Project Structure**

Here's how you can organize your project directory:

```
task_management_system/
│
├── src/
│   ├── __init__.py            # Flask app initialization
│   ├── app.py                 # Main app file (Flask routes)
│   ├── task_manager.py        # Task management logic (Task and TaskManager classes)
│   ├── static/                # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css      # Styling for the HTML pages
│   │   └── js/
│   │       └── app.js         # JavaScript for handling dynamic content
│   ├── templates/             # HTML templates
│   │   ├── index.html         # Home page (display tasks)
│   │   ├── create_task.html   # Page for creating tasks
│   │   └── update_task.html   # Page for updating tasks
│   └── requirements.txt       # List of required Python packages
│
├── venv/                      # Virtual environment (generated after running `python -m venv venv`)
├── tasks.db                   # SQLite database file
└── README.md                  # Documentation for your project
```

### **2. Back-End (Flask App with SQLite3)**

#### `src/app.py`

This file sets up the Flask application and handles routing:

```python
from flask import Flask, render_template, request, redirect, url_for, jsonify
from task_manager import TaskManager, Task

app = Flask(__name__)

@app.route('/')
def index():
    tasks = TaskManager.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/tasks/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        task_data = request.form.to_dict()
        task = TaskManager.create_task(task_data)
        return redirect(url_for('index'))
    return render_template('create_task.html')

@app.route('/tasks/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = TaskManager.get_task(task_id)
    if not task:
        return "Task not found", 404

    if request.method == 'POST':
        task_data = request.form.to_dict()
        TaskManager.update_task(task_id, task_data)
        return redirect(url_for('index'))

    return render_template('update_task.html', task=task)

@app.route('/tasks/delete/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    success = TaskManager.delete_task(task_id)
    if success:
        return redirect(url_for('index'))
    return "Task not found", 404

@app.route('/api/tasks', methods=['GET', 'POST'])
def api_tasks():
    if request.method == 'POST':
        task_data = request.get_json()
        task = TaskManager.create_task(task_data)
        return jsonify(task.__dict__), 201
    else:
        tasks = [task.__dict__ for task in TaskManager.get_all_tasks()]
        return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
```

#### `src/task_manager.py`

The task management logic interacts with the SQLite3 database:

```python
import sqlite3

class Task:
    def __init__(self, task_id, task_type, title, due_date, description, priority, status):
        self.id = task_id
        self.type = task_type
        self.title = title
        self.due_date = due_date
        self.description = description
        self.priority = priority
        self.status = status

    def save_to_db(self):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute('''INSERT INTO tasks (type, title, due_date, description, priority, status)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (self.type, self.title, self.due_date, self.description, self.priority, self.status))
        conn.commit()
        conn.close()

    @classmethod
    def load_from_db(cls, task_id):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return cls(*row)
        return None

    def update_in_db(self):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute('''UPDATE tasks
                     SET type = ?, title = ?, due_date = ?, description = ?, priority = ?, status = ?
                     WHERE id = ?''',
                  (self.type, self.title, self.due_date, self.description, self.priority, self.status, self.id))
        conn.commit()
        conn.close()

    def delete_from_db(self):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute('DELETE FROM tasks WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()

class TaskManager:
    @staticmethod
    def get_all_tasks():
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute('SELECT * FROM tasks')
        rows = c.fetchall()
        conn.close()
        return [Task(*row) for row in rows]

    @staticmethod
    def create_task(task_data):
        task = Task(
            task_id=None,  # ID will be autogenerated by SQLite
            task_type=task_data['type'],
            title=task_data['title'],
            due_date=task_data['due_date'],
            description=task_data['description'],
            priority=task_data['priority'],
            status='pending'  # default status
        )
        task.save_to_db()
        return task

    @staticmethod
    def get_task(task_id):
        return Task.load_from_db(task_id)

    @staticmethod
    def update_task(task_id, task_data):
        task = Task.load_from_db(task_id)
        if task:
            task.title = task_data.get('title', task.title)
            task.due_date = task_data.get('due_date', task.due_date)
            task.description = task_data.get('description', task.description)
            task.priority = task_data.get('priority', task.priority)
            task.status = task_data.get('status', task.status)
            task.update_in_db()
            return task
        return None

    @staticmethod
    def delete_task(task_id):
        task = Task.load_from_db(task_id)
        if task:
            task.delete_from_db()
            return True
        return False
```

### **3. Front-End (HTML + CSS + JS)**

#### `src/templates/index.html`

This is the home page that lists all tasks:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Task Management</title>
        <link
            rel="stylesheet"
            href="{{ url_for('static', filename='css/style.css') }}"
        />
    </head>
    <body>
        <h1>Task Management System</h1>
        <a href="{{ url_for('create_task') }}">Create New Task</a>
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Due Date</th>
                    <th>Status</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for task in tasks %}
                <tr>
                    <td>{{ task.title }}</td>
                    <td>{{ task.due_date }}</td>
                    <td>{{ task.status }}</td>
                    <td>
                        <a href="{{ url_for('update_task', task_id=task.id) }}"
                            >Edit</a
                        >
                        <a href="{{ url_for('delete_task', task_id=task.id) }}"
                            >Delete</a
                        >
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
</html>
```

#### `src/templates/create_task.html`

This page is for creating new tasks:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Create Task</title>
        <link
            rel="stylesheet"
            href="{{ url_for('static', filename='css/style.css') }}"
        />
    </head>
    <body>
        <h1>Create a New Task</h1>
        <form method="POST">
            <label for="type">Task Type:</label>
            <select name="type" id="type">
                <option value="personal">Personal</option>
                <option value="work">Work</option>
            </select>
            <br />

            <label for="title">Title:</label>
            <input type="text" id="title" name="title" required />
            <br />

            <label for="due_date">Due Date:</label>
            <input type="date" id="due_date" name="due_date" required />
            <br />

            <label for="description">Description:</label>
            <textarea id="description" name="description" required></textarea>
            <br />

            <label for="priority">Priority:</label>
            <select name="priority" id="priority">
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
            </select>
            <br />

            <button type="submit">Create Task</button>
        </form>
    </body>
</html>
```

#### `src/static/css/style.css`

A basic CSS file to style the HTML pages:

```css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    font-size: 24px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

table,
th,
td {
    border: 1px solid black;
}

th,
td {
    padding: 8px;
    text-align: left;
}

a {
    text-decoration: none;
    color: blue;
}

form {
    max-width: 400px;
    margin: 20px auto;
}

label {
    display: block;
    margin-bottom: 5px;
}

input,
select,
textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
}
```

### **4. Running the Project**

1. **Set Up the Virtual Environment:**
    - `python -m venv venv`
    - Activate the virtual environment:
        - **Windows**: `venv\Scripts\activate`
        - **macOS/Linux**: `source venv/bin/activate`
2. **Install Dependencies**:
    - `pip install flask sqlite3`
3. **Run the Flask App**:
    - `python src/app.py`

This structure will give you a fully functional back-end and front-end for the Task Management System, using Flask and SQLite3. You can extend it further by adding additional features such as user authentication or advanced filtering. Let me know if you need further clarification!
