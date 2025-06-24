import json


def load_tasks():
    """Read and load JSON file, return empty template if file doesn't exist or is invalid."""
    try:
        with open("to_do_list.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"to_do_list": []}


def save_tasks(data):
    """Save tasks to JSON file."""
    with open("to_do_list.json", "w") as f:
        json.dump(data, f, indent=4)


def is_duplicate_name(data, name, exclude_task=None):
    """Check if task name exists, optionally excluding a specific task."""
    return any(task["name"] == name for task in data["to_do_list"] if task != exclude_task)


def add_task():
    """Add a task to the to-do list."""
    task_name = input("Enter a name for the task: ").lower().strip()
    if not task_name:
        print("Task name cannot be empty.")
        return

    data = load_tasks()
    if is_duplicate_name(data, task_name):
        print("Task name already exists.")
        return

    task_to_add = input("Enter a task description: ").strip()
    if not task_to_add:
        print("Task description cannot be empty.")
        return

    add_dict = {
        "name": task_name,
        "task": task_to_add,
        "status": "in_progress"
    }
    data["to_do_list"].append(add_dict)
    save_tasks(data)
    print(f"The task '{task_name}' has been successfully added.")


def view_task():
    """View all tasks or a specific task by name."""
    data = load_tasks()
    if not data["to_do_list"]:
        print("No tasks to view.")
        return

    input_task_name = input("Enter task name or 'all' to view all tasks: ").lower().strip()
    if input_task_name == "all":
        print(json.dumps(data, indent=4))
    else:
        found = False
        for task in data["to_do_list"]:
            if task["name"] == input_task_name:
                print(json.dumps(task, indent=4))
                found = True
                break
        if not found:
            print("Task not found.")


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
            if new_name and new_name != task_to_update:
                if is_duplicate_name(data, new_name, exclude_task=task):
                    print("New task name already exists.")
                    return
                task["name"] = new_name

            new_task = input("Enter new task description (press Enter to keep current): ").strip()
            new_status = input("Enter new task status (in_progress, completed, on_hold, or press Enter): ").lower().strip()

            if new_task:
                task["task"] = new_task
            if new_status in ["in_progress", "completed", "on_hold"]:
                task["status"] = new_status
            elif new_status:
                print("Invalid status. Use in_progress, completed, or on_hold.")
                return

            save_tasks(data)
            print("Task updated successfully.")
            return
    print("Task not found.")


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


while True:
    try:
        user_input = input("Welcome to the To-Do List Manager\n"
                           "Select an option (1-5):\n"
                           "1. Add a task\n"
                           "2. View a task\n"
                           "3. Update a task\n"
                           "4. Delete a task\n"
                           "5. Quit\n")
        if not user_input:
            print("Input was empty. Select an option (1-5).")
            continue
        user_input = int(user_input)
        if user_input == 1:
            add_task()
        elif user_input == 2:
            view_task()
        elif user_input == 3:
            update_task()
        elif user_input == 4:
            delete_task()
        elif user_input == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please select a number between 1 and 5.")
    except (ValueError, EOFError):
        print("Invalid input. Please enter a number between 1 and 5.")
    except KeyboardInterrupt:
        break