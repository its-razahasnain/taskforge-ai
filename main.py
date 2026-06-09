from helper import (
    print_equalto_seperator,
    print_new_line,
    print_dash_seperator,
    task_len,
)


task_list = []


def add_task():
    while True:
        print_new_line()
        print_dash_seperator(30)
        print("Taskforge AI - Add Task:")
        print_dash_seperator(30)
        task = (
            input("What task would you like to schedule: ").strip().lower().capitalize()
        )
        if task:
            task_list.append(task)
            print_new_line()
            print_dash_seperator(task_len(task))
            print(f"{task} successfully added!")
            print_dash_seperator(task_len(task))
            print_new_line()
            break
        print_new_line()
        print_dash_seperator(26)
        print("Task name cannot be empty!")
        print_dash_seperator(26)
        print_new_line()


def view_task():
    print_new_line()
    print_dash_seperator(30)
    print("Taskforge AI - View Task:")
    print_equalto_seperator(30)
    if task_list:
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")
    else:
        print("No Task added yet.")
    print_equalto_seperator(30)
    print_new_line()


def delete_task():
    print_new_line()
    print_dash_seperator(30)
    print("Taskforge AI - Delete Task:")
    print_dash_seperator(30)
    task_to_delete = (
        input("Which task you want me to delete: ").strip().lower().capitalize()
    )
    if task_to_delete:
        if not task_to_delete.isdigit():
            if task_to_delete in task_list:
                task_list.remove(task_to_delete)
                print_new_line()
                print_dash_seperator(30)
                print(f"{task_to_delete} removed successfully!")
                print_dash_seperator(30)
                print_new_line()
            else:
                print_new_line()
                print_dash_seperator(30)
                print(f"No Task here named {task_to_delete}!")
                print_dash_seperator(30)
                print_new_line()
        else:
            task_index = int(task_to_delete) - 1
            try:
                if task_list:
                    if task_index < 0:
                        print_new_line()
                        print_dash_seperator(30)
                        print("Choose a number greater than 0!")
                        print_dash_seperator(30)
                        print_new_line()
                    else:
                        print_new_line()
                        print_dash_seperator(30)
                        print(f"{task_list[task_index]} removed successfully!")
                        task_list.pop(task_index)
                        print_dash_seperator(30)
                        print_new_line()
                else:
                    print_new_line()
                    print_dash_seperator(30)
                    print("Can't delete anything. Tasklist is empty!")
                    print_dash_seperator(30)
                    print_new_line()
            except IndexError:
                print_new_line()
                print_dash_seperator(30)
                print(f"Invalid task number. You can only choose upto {len(task_list)}")
                print_dash_seperator(30)
                print_new_line()
    else:
        print_new_line()
        print_dash_seperator(30)
        print("Please Enter a task name to delete.")
        print_dash_seperator(30)
        print_new_line()


def show_menu():
    menu_option = ["Add Task", "View Task", "Delete Task", "Exit"]
    print_dash_seperator(38)
    print("Welcome to Taskforge AI - Task Manager")
    print_dash_seperator(38)
    while True:
        print("Menu Options:")
        for i, option in enumerate(menu_option, start=1):
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
                print_new_line()
                print_dash_seperator(42)
                print("Thank you for using TaskForge AI. Goodbye!")
                print_dash_seperator(42)
                print_new_line()
                break
            else:
                print_new_line()
                print_dash_seperator(38)
                print("Invalid choice! Please select from options")
                print_dash_seperator(38)
                print_new_line()
        except ValueError:
            print_new_line()
            print_dash_seperator(51)
            print("Invalid input! Please enter a numerical option here.")
            print_dash_seperator(51)
            print_new_line()


def main():
    show_menu()


if __name__ == "__main__":
    main()
