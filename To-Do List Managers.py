# To-Do List Manager

# Create an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your task list is empty.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Deleted task: {deleted_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
while True:
    print("\n-- To-Do List Manager --")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
