from datetime import datetime

class Task:
    task_id_counter = 1  # Auto-incremented unique identifier

    def __init__(self, title, due_date, description=None, flag=None):
        if type(title) != str or title.strip() == "":
            raise Exception("Title must be a non-empty string.")
        if type(due_date) != str or not self._is_valid_date(due_date):
            raise Exception("Due date must be correct and in the format YYYY-MM-DD.")
        if description and len(description) > 15:
            raise Exception("Description cannot exceed 15 characters.")

        self._task_id = Task.task_id_counter
        Task.task_id_counter += 1
        self.title = title
        self.due_date = due_date
        self.status = "pending"
        self.description = description if description is not None else ""
        self.flag = flag if flag else "general"

    def _is_valid_date(self, date_str):  # Now it takes 'self' as an argument
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def mark_completed(self):
        self.status = "completed"

    def __str__(self):
        return f"ID: {self.get_task_id()}, Title: {self.title}, Due: {self.due_date}, Status: {self.status}, Description: {self.getdescription()}"

    def display(self):
        return self.__str__()

    # Getters and setters for task_id
    def get_task_id(self):
        return self._task_id

    def settask_id(self, task_id):
        self._task_id = task_id

    # Getters and setters for description
    def getdescription(self):
        return self.description

    def setdescription(self, description):
        if len(description) > 15:
            raise Exception("Description cannot exceed 15 characters.")
        self.description = description


class PersonalTask(Task):
    def __init__(self, title, due_date, priority="low", description=None):
        super().__init__(title, due_date, description=description, flag="personal")
        if priority not in ["low", "medium", "high"]:
            raise Exception("Priority must be 'low', 'medium', or 'high'.")
        self.priority = priority

    def is_high_priority(self):
        return self.priority == "high"
    
    def set_priority(self, priority):
        if priority in ["high", "medium", "low"]:
            self.priority = priority
        else:
            print("Invalid priority. Choose 'high', 'medium', or 'low'.")

    def __str__(self):
        return super().__str__() + f", Priority: {self.priority}"


class WorkTask(Task):
    def __init__(self, title, due_date, description=None):
        super().__init__(title, due_date, description=description, flag="work")
        self.team_members = []

    def add_team_member(self, member):
        if type(member) != str or member.strip() == "":
            raise Exception("Team member name must be a non-empty string.")
        else:
            self.team_members.append(member)

    def __str__(self):
        members = ", ".join(self.team_members) if self.team_members else "None"
        return super().__str__() + f", Team Members: {members}"
