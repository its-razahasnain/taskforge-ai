from helper import print_equalto_seperator, print_new_line, print_dash_seperator


task_list = []


def add_task():
    while True:
        print_new_line()
        task = input("What task would you like to schedule: ").strip()
        if task:
            task_list.append(task)
            print_new_line()
            print_dash_seperator(40)
            print(f"{task} successfully added to your manager!")
            print_dash_seperator(40)
            break
        print_new_line()
        print_dash_seperator(26)
        print("Task name cannot be empty!")
        print_dash_seperator(26)


def show_menu():
    menu_option = ["Add Task", "View Task", "Exit"]
    print_dash_seperator(39)
    print("Welcome to Taskforge AI - Task Manager")
    print_dash_seperator(39)
    print("Menu Options:")
    for i, option in enumerate(menu_option, start=1):
        print(f"{i}. {option}")


def main():
    show_menu()
    add_task()


if __name__ == "__main__":
    main()
