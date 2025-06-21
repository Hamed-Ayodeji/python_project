import json


# Functions for the to-do-list-manager
## Function to add task
def add_task():
    # Prompt the user for the task name and task and store them into variables
    task_name = input("Enter a name for the task: \n").lower()
    task_to_add = input("Enter a task: \n")

    # Use the variable to build dictionary
    add_dict = {
            "name": task_name,
            "task": task_to_add,
            "status": "in_progress"
    }

    # Template for the to-do-list JSON file
    template = {
        "to_do_list": [
            add_dict
        ]
    }

    try:
        # JSON file exists, append new task
        with open("to_do_lists.json", "r") as f:
            data = json.load(f)
            data["to_do_list"].append(add_dict)
        with open("to_do_lists.json", "w") as f:
            json.dump(data, f, indent=4)

    except FileNotFoundError:
        # JSON file does not exist, create new file, and append new task
        with open("to_do_lists.json", "w") as f:
            json.dump(template, f, indent=4)

## Function to view tasks
def view_task():
    # Prompt user for name of task
    input_task_name = input("Enter the name for the specific task you want to view, or enter 'all' to view all tasks: \n").lower()

    # To view all the tasks
    if input_task_name == "all":
        try:
            with open("to_do_lists.json", "r") as f:
                data = json.load(f)
                print(json.dumps(data, indent=4))

        # If no JSON file exist
        except FileNotFoundError:
            print("No tasks to view")

    elif input_task_name != "all":

        # I didn't use the try except here to prevent redundancy
        with open("to_do_lists.json", "r") as f:
            data = json.load(f)
            for task in data["to_do_list"]:
                if task["name"] == input_task_name:
                    print(json.dumps(task, indent=4))
                else:
                    print("Task not found")

## Function to update a task
def update_task():
    # Prompt user for input to identify task
    task_to_update = input("Enter a task to update: \n").lower()
    # Variable for updated values
    new_name = input("Enter the new name for the task: \n").lower()
    new_task = input("Enter a task to update: \n")
    new_status = input("Enter new task status: \n")

    try:
        with open("to_do_lists.json", "r") as f:
            data = json.load(f)
            for task in data["to_do_list"]:
                if task["name"] == task_to_update:
                    # Checks if the input is an empty string
                    if new_name != "":
                        task["name"] = new_name
                    if new_task != "":
                        task["task"] = new_task
                    if new_status != "":
                        task["status"] = new_status
        with open("to_do_lists.json", "w") as f:
            json.dump(data, f, indent=4)

    except FileNotFoundError and ValueError:
        print("No tasks to update")

## Function to delete a task or all tasks
def delete_task():
    #  Prompt the user for the task or tasks to delete
    task_to_delete = input("Enter the specific name of the task to delete or enter 'all' to delete all tasks: \n").lower()
    if task_to_delete == "all":
        try:
            with open("to_do_lists.json", "r") as f:
                data = json.load(f)
                data["to_do_list"][:] = []
                # data["to_do_list"].clear()

            with open("to_do_lists.json", "w") as f:
                json.dump(data, f, indent=4)

        except FileNotFoundError and ValueError:
            print("No tasks to delete")

    elif task_to_delete != "all":
        try:
            with open("to_do_lists.json", "r") as f:
                data = json.load(f)
                # Delete specific task
                for task in data["to_do_list"]:
                    if task["name"] == task_to_delete:
                        data["to_do_list"].remove(task)

            with open("to_do_lists.json", "w") as f:
                json.dump(data, f, indent=4)

        except FileNotFoundError and ValueError:
            print("No tasks to delete")

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
            print("Quit")
            break

    except ValueError:
        print("Invalid input. Please Select a valid option.")