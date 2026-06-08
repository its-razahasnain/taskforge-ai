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
        task = input("What task would you like to schedule: ").strip().capitalize()
        if task:
            task_list.append(task)
            print_new_line()
            print_dash_seperator(task_len(task))
            print(f"{task} successfully added to your manager!")
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


def show_menu():
    menu_option = ["Add Task", "View Task", "Exit"]
    print_dash_seperator(38)
    print("Welcome to Taskforge AI - Task Manager")
    print_dash_seperator(38)
    while True:
        print("Menu Options:")
        for i, option in enumerate(menu_option, start=1):
            print(f"{i}. {option}")
        try:
            user_option = int(
                input("Please select an action from the menu to proceed: ")
            )
            if user_option == 1:
                add_task()
            elif user_option == 2:
                view_task()
            elif user_option == 3:
                print_new_line()
                print_dash_seperator(42)
                print("Thank you for using TaskForge AI. Goodbye!")
                print_dash_seperator(42)
                print_new_line()
                break
            else:
                print_new_line()
                print_dash_seperator(38)
                print("Invalid choice! Please select 1, 2, or 3")
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
