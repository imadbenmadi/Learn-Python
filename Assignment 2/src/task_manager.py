from flask import Blueprint, request, jsonify
from Task import Task, PersonalTask, WorkTask
from datetime import datetime
import sqlite3

task_routes = Blueprint("task_routes", __name__)

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    if data['type'] == 'personal':
        task = PersonalTask(data['title'], data['due_date'], data.get('priority', 'low'), data.get('description', ''))
    else:
        task = WorkTask(data['title'], data['due_date'], data.get('description', ''))
    task.save_to_db()
    return jsonify({"message": "Task created successfully"}), 201

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM tasks"
        filters = request.args.get('type')
        if filters:
            query += f" WHERE type='{filters}'"
        cursor.execute(query)
        tasks = cursor.fetchall()
    return jsonify(tasks), 200

@task_routes.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.load_from_db(task_id)
    if task:
        return jsonify(task.__dict__), 200
    return jsonify({"error": "Task not found"}), 404

@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = Task.load_from_db(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    task.title = data['title']
    task.due_date = data['due_date']
    task.description = data.get('description', '')
    task.priority = data.get('priority', 'low')
    task.update_in_db()
    return jsonify({"message": "Task updated successfully"}), 200

@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    Task.delete_from_db(task_id)
    return jsonify({"message": "Task deleted successfully"}), 200

@task_routes.route('/tasks/pending', methods=['GET'])
def get_pending_tasks():
    tasks = Task.get_pending_tasks()
    return jsonify(tasks), 200

@task_routes.route('/tasks/overdue', methods=['GET'])
def get_overdue_tasks():
    current_date = datetime.now().strftime('%Y-%m-%d')
    tasks = Task.get_overdue_tasks(current_date)
    return jsonify(tasks), 200
