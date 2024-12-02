import csv
from datetime import datetime
from task import Task

class TaskManager:
    def __init__(self, task_list_file_name="task_list.csv"):
        self.tasks = []
        self.task_list_file_name = task_list_file_name

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self, flag=None):
        filtered_tasks = (
            [task for task in self.tasks if task.flag == flag]
            if flag
            else self.tasks
        )
        for task in filtered_tasks:
            print(task.display())

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.get_task_id() == task_id:  # Use getter
                self.tasks.remove(task)
                print("Task deleted.")
                return
        print("Task not found.")

    def save_tasks(self):
        with open(self.task_list_file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "task_id",
                    "title",
                    "due_date",
                    "status",
                    "description",
                    "flag",
                ]
            )
            for task in self.tasks:
                writer.writerow(
                    [
                        task.get_task_id(),  # Use getter
                        task.title,
                        task.due_date,
                        task.status,
                        task.getdescription(),  # Use getter
                        task.flag,
                    ]
                )
        print("Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open(self.task_list_file_name, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if not row["title"] or not self._is_valid_date(row["due_date"]):
                        print(f"Skipping invalid task row: {row}")
                        continue
                    task = Task(
                        title=row["title"],
                        due_date=row["due_date"],
                        description=row.get("description", ""),
                        flag=row["flag"],
                    )
                    task.settask_id(int(row["task_id"]))  # Use setter
                    task.status = row["status"]
                    self.tasks.append(task)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No task file found. Starting with an empty list.")

    def get_pending_tasks(self):
        pending_tasks = filter(lambda task: task.status == "pending", self.tasks)
        for task in pending_tasks:
            print(task.display())

    def get_overdue_tasks(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        overdue_tasks = [
            task for task in self.tasks if task.due_date < current_date
        ]
        for task in overdue_tasks:
            print(task.display())
