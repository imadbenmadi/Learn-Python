Task Management System with Flask API and SQLite3

github Link : https://github.com/imadbenmadi/Learn-Python/tree/main/Assignment%202

This project is a Flask-based Task Management System using SQLite3 for persistent storage. It supports creating, updating, retrieving, and deleting tasks via RESTful API endpoints.

API Documentation:

1. POST /tasks

    - Description: Create a new task (PersonalTask or WorkTask).
    - Request format:  
      {
      "type": "personal",  
       "title": "Task Title",  
       "due_date": "YYYY-MM-DD",  
       "description": "Short description",  
       "priority": "low"  
      }
    - Example Response:  
      {"message": "Task created successfully"}

2. GET /tasks

    - Description: Retrieve all tasks or filter by type using the query parameter ?type=personal or ?type=work.
    - Example Response:  
      [
      {"id": 1, "type": "personal", "title": "Example Task", "due_date": "2024-12-01", "description": "", "priority": "low", "status": "pending"}
      ]

3. GET /tasks/<int:task_id>

    - Description: Retrieve a specific task by its ID.
    - Example Response:  
      {"id": 1, "type": "personal", "title": "Example Task", "due_date": "2024-12-01", "description": "", "priority": "low", "status": "pending"}

4. PUT /tasks/<int:task_id>

    - Description: Update task details (e.g., status, priority).
    - Request format:  
      {
      "title": "Updated Task Title",  
       "due_date": "YYYY-MM-DD",  
       "description": "Updated description",  
       "priority": "medium"  
      }
    - Example Response:  
      {"message": "Task updated successfully"}

5. DELETE /tasks/<int:task_id>

    - Description: Delete a task by its ID.
    - Example Response:  
      {"message": "Task deleted successfully"}

6. GET /tasks/pending

    - Description: Fetch all tasks marked as "pending."
    - Example Response:  
      [{"id": 2, "type": "work", "title": "Work Task", "due_date": "2024-11-30", "description": "", "priority": "low", "status": "pending"}]

7. GET /tasks/overdue
    - Description: Fetch all overdue tasks based on the current date.
    - Example Response:  
      [{"id": 3, "type": "personal", "title": "Overdue Task", "due_date": "2024-11-01", "description": "", "priority": "low", "status": "pending"}]

Database Schema:

-   Table: tasks
    -   id (INTEGER, Primary Key, Auto Increment)
    -   type (TEXT, Task type: personal or work)
    -   title (TEXT, Task title)
    -   due_date (TEXT, Task due date in YYYY-MM-DD format)
    -   description (TEXT, Optional task description)
    -   priority (TEXT, Task priority: low, medium, high)
    -   status (TEXT, Task status: pending, completed)

Setup Instructions:

1. Create a virtual environment:
   python -m venv venv

2. Activate the virtual environment:

    - On Windows:  
      venv\Scripts\activate

3. Install dependencies:  
   pip install -r requirements.txt

4. Initialize the database by running the application. This will create the necessary SQLite database file if it doesn't exist.

5. Run the Flask application:  
   python src/app.py

Example Usage:

1. Create a new task (PersonalTask):  
   curl -X POST -H "Content-Type: application/json" -d "{\"type\":\"personal\",\"title\":\"Test Task\",\"due_date\":\"2024-12-01\",\"priority\":\"low\"}" http://127.0.0.1:5000/tasks

2. Retrieve all tasks:  
   curl -X GET http://127.0.0.1:5000/tasks

3. Retrieve a task by ID:  
   curl -X GET http://127.0.0.1:5000/tasks/1

4. Update a task:  
   curl -X PUT -H "Content-Type: application/json" -d "{\"title\":\"Updated Task\",\"due_date\":\"2024-12-02\",\"priority\":\"medium\"}" http://127.0.0.1:5000/tasks/1

5. Delete a task:  
   curl -X DELETE http://127.0.0.1:5000/tasks/1

6. Retrieve pending tasks:  
   curl -X GET http://127.0.0.1:5000/tasks/pending

7. Retrieve overdue tasks:  
   curl -X GET http://127.0.0.1:5000/tasks/overdue
