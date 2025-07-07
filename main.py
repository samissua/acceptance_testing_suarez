import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

# Task class
class Task:
    def __init__(self, title, description, date=None, is_done=False):
        self.title = title
        self.description = description
        self.date = date if date else datetime.today().strftime("%Y-%m-%d")
        self.is_done = is_done

    def complete(self):
        self.is_done = True

    def undo(self):
        self.is_done = False

    def update(self, new_title, new_description):
        self.title = new_title
        self.description = new_description

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "is_done": self.is_done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["description"], data["date"], data["is_done"])


# ToDoList class
class ToDoList:
    def __init__(self, filename=TASKS_FILE):
        self.filename = filename
        self.tasks = []
        self.load()

    def add_task(self, title, description):
        self.tasks.append(Task(title, description))
        self.save()

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return
        print("\nTasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✅ Done" if task.is_done else "❌ Not Done"
            print(f"{i}. {task.title} - {task.description} - Created on: {task.date} [{status}]")

    def complete_task(self, task_num):
        self.tasks[task_num - 1].complete()
        self.save()

    def undo_task(self, task_num):
        self.tasks[task_num - 1].undo()
        self.save()

    def update_task(self, task_num, title, description):
        self.tasks[task_num - 1].update(title, description)
        self.save()

    def clear_tasks(self):
        self.tasks.clear()
        self.save()

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in data]


# Console menu interface
def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Mark Task as Undone")
        print("5. Update Task")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description: ")
            todo.add_task(title, description)
            print("Task added.")

        elif choice == "2":
            todo.list_tasks()

        elif choice == "3":
            num = int(input("Enter task number to mark as done: "))
            todo.complete_task(num)
            print("Task marked as done.")

        elif choice == "4":
            num = int(input("Enter task number to mark as undone: "))
            todo.undo_task(num)
            print("Task marked as undone.")

        elif choice == "5":
            num = int(input("Enter task number to update: "))
            new_title = input("New Title: ")
            new_description = input("New Description: ")
            todo.update_task(num, new_title, new_description)
            print("Task updated.")

        elif choice == "6":
            todo.clear_tasks()
            print("All tasks cleared.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
