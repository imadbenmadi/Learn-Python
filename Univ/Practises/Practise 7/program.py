from datetime import datetime

class Employee:
    def __init__(self, name, emp_id, department, join_date):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.join_date = datetime.strptime(join_date, "%Y-%m-%d")
    
    def __str__(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}, Department: {self.department}, Joined: {self.join_date.strftime('%Y-%m-%d')}"
    
    def work_duration(self):
        today = datetime.now()
        duration = today - self.join_date
        return f"{duration.days} days"


class Manager(Employee):
    def __init__(self, name, emp_id, department, join_date, team_size):
        super().__init__(name, emp_id, department, join_date)
        self.team_size = team_size

    def __str__(self):
        return f"{super().__str__()}, Team Size: {self.team_size}"


class Developer(Employee):
    def __init__(self, name, emp_id, department, join_date, programming_languages):
        super().__init__(name, emp_id, department, join_date)
        self.programming_languages = programming_languages

    def __str__(self):
        languages = ', '.join(self.programming_languages)
        return f"{super().__str__()}, Programming Languages: {languages}"


class InvalidDepartmentError(Exception):
    def __init__(self, department):
        self.department = department
        self.message = f"Invalid department: {self.department}. Please enter a valid department."
        super().__init__(self.message)


try:
    valid_departments = ['HR', 'IT', 'Finance', 'Marketing']
    
    dev = Developer("Alice", 101, "IT", "2020-06-15", ["Python", "JavaScript"])
    
    #department = "Operations"
    department = "HR"
    if department not in valid_departments:
        raise InvalidDepartmentError(department)
    
    manager = Manager("Bob", 102, department, "2018-04-01", 10)

except InvalidDepartmentError as e:
    print(e)

print(dev)
print(dev.work_duration())
