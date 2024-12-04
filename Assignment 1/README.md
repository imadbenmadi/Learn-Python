Task Management System

1. Overview  
   The Task Management System is a Python-based console application designed to assist in managing and organizing tasks. It allows users to create, view, delete, and filter tasks by type (Personal or Work). The system supports saving tasks to a CSV file and loading tasks from a CSV file. Users can also view pending and overdue tasks.

Features:

-   Add, view, and delete tasks.
-   Personal tasks with priority levels (low, medium, high).
-   Work tasks with team member management.
-   Save and load tasks to/from a CSV file.
-   View pending tasks and overdue tasks.

2. Setup Instructions  
   Steps to Run:
1. Ensure Python 3 is installed on your system.
1. Download and save the files `task.py`, `task_manager.py`, and `interface.py` in the same folder.
1. Install dependencies if required (e.g., pandas). You can install them using `pip install -r requirements.txt` (if a requirements file is included).
1. Run the program by executing the following command:  
   `python interface.py`

1. Class and Method Descriptions

task.py

1. Task Class

    - Attributes:
        - `_task_id`: Auto-incremented unique identifier.
        - `title`: Name of the task.
        - `due_date`: Due date for task completion.
        - `status`: Status of the task, defaulting to "pending."
        - `description`: Short optional description (max 15 characters).
        - `flag`: Indicates if the task is "personal" or "work."
    - Methods:
        - `mark_completed()`: Marks the task as completed.
        - `display()`: Returns task details as a formatted string.
        - Getter and setter methods for `_task_id` and `description`.

2. PersonalTask Class (inherits from Task)

    - Attributes: Adds `priority` (low, medium, high).
    - Methods:
        - `set_priority(priority)`: Updates priority with validation.
        - `display()`: Extends Task's display with priority.

3. WorkTask Class (inherits from Task)
    - Attributes: Adds `team_members` (list of names).
    - Methods:
        - `add_team_member(member)`: Adds a team member with validation.
        - `display()`: Extends Task's display with team members.

task_manager.py

1. TaskManager Class
    - Attributes:
        - `tasks`: A list of all tasks.
        - `task_list_file_name`: Name of the CSV file for saving/loading tasks.
    - Methods:
        - `add_task(task)`: Adds a task to the list.
        - `list_tasks(flag=None)`: Lists all tasks or filters by type.
        - `delete_task(_task_id)`: Deletes a task by ID; prints an error message if not found.
        - `save_task()`: Saves tasks to a CSV file.
        - `load_task()`: Loads tasks from a CSV file.
        - `get_pending_tasks()`: Uses a lambda function to list pending tasks.
        - `get_overdue_tasks()`: Lists overdue tasks based on the current date.

interface.py  
Provides a user-friendly menu-driven interface to interact with the system.

-   Options include:
    -   Adding Personal or Work tasks.
    -   Viewing tasks (all, filtered by type, pending, or overdue).
    -   Deleting tasks by ID.
    -   Saving and loading tasks from CSV.
    -   Exiting the program.

4. Error Handling  
   The program ensures robust error handling:

-   Validates inputs such as `title`, `due_date`, and priority.
-   Prevents invalid team member entries.
-   Provides feedback if an invalid `_task_id` is entered for deletion.
-   Handles missing or incorrectly formatted data when loading from CSV.
-   Warns users of invalid or incomplete input during task creation.
