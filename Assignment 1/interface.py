from task_manager import TaskManager
from task import PersonalTask, WorkTask


def main():
    manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add a Personal Task")
        print("2. Add a Work Task")
        print("3. View All Tasks")
        print("4. Delete a Task")
        print("5. View Pending Tasks")
        print("6. View Overdue Tasks")
        print("7. Save Tasks to CSV")
        print("8. Load Tasks from CSV")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            # Add a Personal Task
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (low, medium, high): ")
            description = input("Enter description (optional): ")
            try:
                task = PersonalTask(title, due_date, priority, description)
                manager.add_task(task)
                print("Personal task added.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            # Add a Work Task
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            description = input("Enter description (optional): ")
            try:
                task = WorkTask(title, due_date, description)
                while True:
                    member = input("Add team member (leave blank to stop): ")
                    if member == "":
                        break
                    task.add_team_member(member)
                manager.add_task(task)
                print("Work task added.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            # View All Tasks or Filter by Type
            flag = input("Filter by type (personal/work/none): ").lower()
            if flag == "none":
                manager.list_tasks()
            else:
                manager.list_tasks(flag)

        elif choice == "4":
            # Delete a Task
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "5":
            # View Pending Tasks
            manager.get_pending_tasks()

        elif choice == "6":
            # View Overdue Tasks
            manager.get_overdue_tasks()

        elif choice == "7":
            # Save Tasks to CSV
            manager.save_tasks()

        elif choice == "8":
            # Load Tasks from CSV
            manager.load_tasks()

        elif choice == "0":
            # Exit Program
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
