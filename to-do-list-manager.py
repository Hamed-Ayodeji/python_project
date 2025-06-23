import json

# Functions for the to-do-list-manager

## Function to read JSON file
def load_tasks():
    """This function reads and loads JSON file and handles FileNotFoundError and json.JSONDecodeError,
    by creating a new empty to_do_list list as template in the JSON file"""
    try:
        with open("to_do_list.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"to_do_list": []}

## Function to save JSON file
def save_tasks(data):
    """This function saves content into the JSON file"""
    with open("to_do_list.json", "w") as f:
        json.dump(data, f, indent=4)

## Function to add task
def add_task():
    """Adds a task to the to_do_list list"""
    # Prompts user for input, converts input to lower case and removes leading and trailing spaces
    task_name = input("Enter a name for the task: \n").lower().strip()

    # Checks if task_name input field is empty
    if not task_name:
        print("Task name cannot be empty.")
        return

    data = load_tasks()
    # Checks if task_name already exists
    if any(task["name"] == task_name for task in data["to_do_list"]):
        print("Task name already exists.")
        return

    task_to_add = input("Enter a task: \n")

    # Use the variable to build dictionary
    add_dict = {
            "name": task_name,
            "task": task_to_add,
            "status": "in_progress"
    }

    data["to_do_list"].append(add_dict)
    save_tasks(data)
    print(f"the task called {task_name} has been successfully added.")

## Function to view tasks
def view_task():
    """View all tasks or a specific task by name."""

    # Checks if there are no task in the to-do-list manager
    data = load_tasks()
    if not data["to_do_list"]:
        print("No tasks to view.")
        return

    input_task_name = input("Enter the name for the specific task you want to view, or enter 'all' to view all tasks: \n").lower().strip()
    # To view all the tasks
    if input_task_name == "all":
        print(json.dumps(data, indent=4))
    else:
        # To view specific task
        found = False
        for task in data["to_do_list"]:
            if task["name"] == input_task_name:
                print(json.dumps(task, indent=4))
                found = True
                break
        if not found:
            print("Task not found.")

## Function to update a task
def update_task():
    """Update a task's name, description, or status."""
    data = load_tasks()
    if not data["to_do_list"]:
        print("No tasks to update.")
        return

    task_to_update = input("Enter the task name to update: ").lower().strip()
    for task in data["to_do_list"]:
        if task["name"] == task_to_update:
            new_name = input("Enter new task name (press Enter to keep current): ").lower().strip()
            # Checks if the new name already exist before proceeding with the update
            if new_name and new_name != task_to_update:
                if any(t["name"] == new_name for t in data["to_do_list"]):
                    print("New task name already exists.")
                    return
                task["name"] = new_name

            new_task = input("Enter new task description (press Enter to keep current): ")
            new_status = input("Enter new task status (press Enter to keep current): ")

            if new_task:
                task["task"] = new_task
            if new_status:
                task["status"] = new_status
            save_tasks(data)
            print("Task updated successfully.")
            return
    print("Task not found.")

## Function to delete a task or all tasks
def delete_task():
    """Delete a specific task or all tasks."""
    data = load_tasks()
    if not data["to_do_list"]:
        print("No tasks to delete.")
        return

    task_to_delete = input("Enter task name or 'all' to delete all tasks: ").lower().strip()
    if task_to_delete == "all":
        data["to_do_list"] = []
        save_tasks(data)
        print("All tasks deleted.")
    else:
        original_len = len(data["to_do_list"])
        data["to_do_list"] = [task for task in data["to_do_list"] if task["name"] != task_to_delete]
        if len(data["to_do_list"]) < original_len:
            save_tasks(data)
            print("Task deleted successfully.")
        else:
            print("Task not found.")

# Prompt user for input
while True:
    try:
        user_input = int(input("Welcome to the To-do List Manager\n"
                           "Select an option below\n"
                           "1. Add a task\n"
                           "2. View a task\n"
                           "3. Update a task\n"
                           "4. Delete a task\n"
                           "5. Quit\n"))

        if user_input == 1:
            print("Add a task")
            add_task()

        elif user_input == 2:
            print("View a task")
            view_task()

        elif user_input == 3:
            print("Update a task")
            update_task()

        elif user_input == 4:
            print("Delete a task")
            delete_task()

        elif user_input == 5:
            print("Goodbye")
            break

    except ValueError:
        print("Invalid input. Please Select a valid option between 1 and 5.")