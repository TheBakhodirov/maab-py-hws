"""
Homework 1. ToDo List Application

Define Task Class:
Create a Task class with attributes such as task title, description, due date, and status.
Define ToDoList Class:
Create a ToDoList class that manages a list of tasks.
Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
Create Main Program:
Develop a simple CLI to interact with the ToDoList.
Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
Test the Application:
Create instances of tasks and test the functionality of your ToDoList.
"""
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_complete = False
        
    def mark_as_complete(self):
        self.is_complete = True
        
    def __str__(self):
        status = "Complete" if self.is_complete else "Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}"
    
class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' has been added.")
    
    def mark_task_complete(self, title):
        for task in self.tasks:
            if title == task.title: 
                task.mark_as_complete()
                print(f"Task '{title}' has been marked as complete.")
                return
        print(f"Task '{title}' not found.")
        
    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available")
        else:
            print("All tasks: ")
            for task in self.tasks:
                print(task)
                
    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task.is_complete]
        if not incomplete_tasks:
            print("No incomplete tasks available.")
        else:
            print("Incomplete Tasks:")
            for task in incomplete_tasks:
                print(task)

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                task = Task(title, description, due_date)
                todo_list.add_task(task)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)
        elif choice == "3":
            todo_list.list_all_tasks()
        elif choice == "4":
            todo_list.list_incomplete_tasks()
        elif choice == "5":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
