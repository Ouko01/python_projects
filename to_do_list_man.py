import json

def display_menu():
    print("Welcome to the To-Do List Manager!")
    print("1. Add task")
    print("2. View task")
    print("3. Remove a task")
    print("4. Mark task as completed")
    print("5. Save and Exit")

tasks = [] # List to store tasks

# Function to add a task
def add_task():
    tasks_input = input("Enter tasks separated by commas: ")
    task_list = [task.strip() for task in tasks_input.split(",") if task.strip()]
    for task in task_list:
        tasks.append({"task": task, "completed": False})
    print(f"Added {len(task_list)} tasks successfully!")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} - {status}")
    else:
        print("No tasks in your list.")

# Fuction to remove a task
def remove_task():
    view_tasks()
    task_nums = input("Enter task numbers to remove (separated by commas): ")
    try:
        task_indexes = sorted([int(num.strip()) - 1 for num in task_nums.split(",") if num.strip()], reverse=True)
        for index in task_indexes:
            if 0 <= index < len(tasks):
                tasks.pop(index)
            print(f"Removed {len(task_indexes)} task(s) successfully!")
    except ValueError:
        print("Invalid input. Please enter valid task numbers.")       

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    task_nums = (input("Enter the task number to mark as completed: "))
    try:
        task_indexes = [
            int(num.strip()) - 1 for num in task_nums.split(",") if num.strip()
        ]
        for index in task_indexes:
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
        print(f"Marked {len(task_indexes)} task(s) as completed.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def save_tasks_to_file(filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f)
    print("Tasks saved successfully!.")

# Function to load tasks from a file
def load_tasks_from_file(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Return an empty list if the file does not exist
        return []
    except json.JSONDecodeError:
        # Handle the cases where the file is corrupted or empty
        print("Error: Could not load tasks. Starting with an empty list.")
        return []

def main():
    global tasks
    tasks = load_tasks_from_file()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            save_tasks_to_file() # Save tasks beforre exiting
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the program
if __name__ == "__main__":
    main()