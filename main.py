from helper import (
    print_equalto_seperator,
    print_new_line,
    print_dash_seperator,
    print_message,
)


tasks = []


def add_task():
    while True:
        print_message("Taskforge AI - Add Task:")
        task_name = (
            input("What task would you like to schedule: ").strip().lower().capitalize()
        )
        if task_name:
            tasks.append(task_name)
            print_message(f"{task_name} successfully added")
            break
        print_message("Task name cannot be empty!")


def view_task():
    print_new_line()
    print_dash_seperator(30)
    print("Taskforge AI - View Task:")
    print_equalto_seperator(30)
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No Task added yet.")
    print_equalto_seperator(30)
    print_new_line()


def delete_by_name(task_to_delete):
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        print_message(f"{task_to_delete} removed successfully!")
    else:
        print_message(f"No Task here named {task_to_delete}!")
        return


def delete_by_index(task_to_delete):
    task_index = int(task_to_delete) - 1
    if not tasks:
        print_message("Can't delete anything. Tasklist is empty!")
        return
    if task_index < 0:
        print_message("Choose a number greater than 0!")
    try:
        deleted_task = tasks.pop(task_index)
        print_message(f"{deleted_task} removed successfully!")
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


def show_menu():
    menu_options = ["Add Task", "View Task", "Delete Task", "Exit"]
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
                delete_task()
            elif user_option == 4:
                print_message("Thank you for using TaskForge AI. Goodbye!")
                break
            else:
                print_message("Invalid choice! Please select from options")
        except ValueError:
            print_message("Invalid input! Please enter a numerical option here.")


def main():
    show_menu()


if __name__ == "__main__":
    main()
