
task_list = []

def add_task():
    while True:
        task = input("What task would you like to schedule?").strip()
        if task:
            task_list.append(task)
            print("Task successfully added to your manager!")
            break
        print("Task name cannot be empty!")

def main():
    print("Welcome to Taskforge AI")
    add_task()


if __name__ == "__main__":
    main()
