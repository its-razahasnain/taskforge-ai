import json
from pathlib import Path
from helper import (
    print_equalto_seperator,
    print_new_line,
    print_dash_seperator,
    print_message,
    get_status_emoji,
)

JSONFILE_PATH = Path("tasks.json")
tasks = []


def get_task_status():
    while True:
        user_input = (
            input("Is your task completed (Answer in Yes or No): ").strip().lower()
        )

        if user_input == "yes":
            return True
        elif user_input == "no":
            return False

        print_message("Task Status is invalid! Please enter 'Yes' or 'No'.")


def add_task():
    while True:
        print_message("Taskforge AI - Add Task:")
        task_name = (
            input("What task would you like to schedule: ").strip().lower().capitalize()
        )
        if not task_name:
            print_message("Task name can't be empty!")
            return
        task_status = get_task_status()
        task_to_save = {"title": task_name, "completed": task_status}
        tasks.append(task_to_save)
        save_to_json_file()
        print_message(f"{task_name} successfully added")
        break


def task_statistics():
    total_tasks = len(tasks)
    completed_task = sum(task["completed"] for task in tasks)
    pending_tasks = total_tasks - completed_task
    if total_tasks == 0:
        completion_percentage = 0
    else:
        completion_percentage = round((completed_task / total_tasks) * 100, 2)
    return total_tasks, completed_task, pending_tasks, completion_percentage


def view_task():
    print_new_line()
    print_dash_seperator(30)
    print("Taskforge AI - View Task:")
    print_equalto_seperator(30)
    print("ID\tStatus\tTask")
    print_dash_seperator(30)
    if tasks:
        for i, task in enumerate(tasks, start=1):
            status = get_status_emoji(task)
            print(f"{i}\t{status}\t{task['title']}")
        total_task, completed_tasks, pending_tasks, completion_percentage = (
            task_statistics()
        )
        print_dash_seperator(30)
        print(f"Total Tasks: {total_task}")
        print(f"Completed Task: {completed_tasks}")
        print(f"Pending Task: {pending_tasks}")
        print(f"Percentage: {completion_percentage}%")
        print_equalto_seperator(30)
    else:
        print("No Task added yet.")
        print_equalto_seperator(30)
    print_new_line()


def delete_by_name(task_to_delete):
    for task in tasks:
        if task.get("title") == task_to_delete:
            tasks.remove(task)
            save_to_json_file()
            print_message(f"{task_to_delete} removed successfully!")
            return

    print_message(f"No Task here named {task_to_delete}!")


def delete_by_index(task_to_delete):
    task_index = int(task_to_delete) - 1
    if not tasks:
        print_message("Can't delete anything. Tasklist is empty!")
        return
    if task_index < 0:
        print_message("Choose a number greater than 0!")
        return
    try:
        deleted_task = tasks.pop(task_index)
        save_to_json_file()
        print_message(f"{deleted_task['title']} removed successfully!")
    except IndexError:
        print_message(f"Invalid task number. You can only choose upto {len(tasks)}")


def delete_task():
    print_message("Taskforge AI - Delete Task:")
    task_to_delete = (
        input("Which task you want me to delete: ").strip().lower().capitalize()
    )
    if task_to_delete:
        if not task_to_delete.isdigit():
            delete_by_name(task_to_delete=task_to_delete)
        else:
            delete_by_index(task_to_delete=task_to_delete)
    else:
        print_message("Please Enter a task name to delete.")
        return


def mark_as_complete():
    print_new_line()
    print_dash_seperator(35)
    print("Taskforge AI - Mark as Complete: ")
    print_equalto_seperator(35)
    print("ID\tStatus\tTasks")
    print_dash_seperator(35)
    for i, task in enumerate(tasks, start=1):
        status = get_status_emoji(task)
        print(f"{i}\t{status}\t{task['title']}")
    if tasks:
        print_dash_seperator(35)
        print_new_line()
        task_to_mark = (
            int(input("Which Task from the following you want to marks as complete: "))
            - 1
        )
        if task_to_mark >= 0 and task_to_mark <= len(tasks):
            task_status = tasks[task_to_mark]
            if not task_status["completed"]:
                task_status["completed"] = True
                save_to_json_file()
                print_message("Task has been marked as completed!")
            else:
                print_message("The Task is already completed!")
                return

        else:
            print_message(f"You can only select task from 1 to {len(tasks)}!")
            return
    else:
        print("There are no tasks to show!")
        print_dash_seperator(35)
        print_new_line()
        return


def save_to_json_file():
    with open(JSONFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def load_from_json_file():
    if not JSONFILE_PATH.exists():
        return []
    with open(JSONFILE_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if not data:
                return []
            return data
        except json.JSONDecodeError:
            return []


def show_menu():
    menu_options = [
        "Add Task",
        "View Task",
        "Mark Task Complete",
        "Delete Task",
        "Exit",
    ]
    print_dash_seperator(38)
    print("Welcome to Taskforge AI - Task Manager")
    print_dash_seperator(38)
    while True:
        print("Menu Options:")
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")
        try:
            user_option = int(
                input("Please select an action from the menu to proceed: ").strip()
            )
            if user_option == 1:
                add_task()
            elif user_option == 2:
                view_task()
            elif user_option == 3:
                mark_as_complete()
            elif user_option == 4:
                delete_task()
            elif user_option == 5:
                print_message("Thank you for using TaskForge AI. Goodbye!")
                break
            else:
                print_message("Invalid choice! Please select from options")
        except ValueError:
            print_message("Invalid input! Please enter a numerical option here.")


def main():
    tasks.extend(load_from_json_file())
    show_menu()


if __name__ == "__main__":
    main()
