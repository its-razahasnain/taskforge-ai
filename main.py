import json
from pathlib import Path
from helper import (
    print_equalto_seperator,
    print_new_line,
    print_dash_seperator,
    print_message,
    get_status_emoji,
)


class TaskForgeAI:
    def __init__(self):
        self.tasks = []
        self.json_file_path = Path("tasks.json")

    def add_task(self):
        while True:
            print_message("Taskforge AI - Add Task:")
            task_name = (
                input("What task would you like to schedule: ")
                .strip()
                .lower()
                .capitalize()
            )
            if not task_name:
                print_message("Task name can't be empty!")
                return
            task_status = False
            task_id = max((task["unique_id"] for task in self.tasks), default=0) + 1
            task_to_save = {
                "unique_id": task_id,
                "title": task_name,
                "completed": task_status,
            }
            self.tasks.append(task_to_save)
            self.save_to_json_file()
            print_message(f"{task_name} successfully added")
            break

    def task_statistics(self):
        total_tasks = len(self.tasks)
        completed_task = sum(task["completed"] for task in self.tasks)
        pending_tasks = total_tasks - completed_task
        if total_tasks == 0:
            completion_percentage = 0
        else:
            completion_percentage = round((completed_task / total_tasks) * 100, 2)
        return total_tasks, completed_task, pending_tasks, completion_percentage

    def display_task(self):
        for task in self.tasks:
            status = get_status_emoji(task)
            task_id = task["unique_id"]
            print(f"{task_id}\t{status}\t{task['title']}")

    def view_task(self):
        print_new_line()
        print_dash_seperator(30)
        print("Taskforge AI - View Task:")
        print_equalto_seperator(30)
        print("ID\tStatus\tTask")
        print_dash_seperator(30)
        if self.tasks:
            self.display_task()
            total_task, completed_tasks, pending_tasks, completion_percentage = (
                self.task_statistics()
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

    def delete_by_name(self, task_to_delete):
        for index, task in enumerate(self.tasks):
            if task.get("title") == task_to_delete:
                del self.tasks[index]
                self.save_to_json_file()
                print_message(f"{task_to_delete} removed successfully!")
                return

        print_message(f"No Task here named {task_to_delete}!")

    def delete_by_id(self, task_to_delete):
        task_id = int(task_to_delete)
        if task_id < 0:
            print_message("Choose a number greater than 0!")
            return
        found = False

        for task in self.tasks:
            if task["unique_id"] == task_id:
                self.tasks.remove(task)
                self.save_to_json_file()
                print_message(f"{task['title']} removed successfully!")
                found = True
                break

        if not found:
            print_message("No task found with this ID!")

    def delete_task(self):
        print_message("Taskforge AI - Delete Task:")
        self.display_task()
        if not self.tasks:
            print_message("Can't delete anything. Tasklist is empty!")
            return
        task_to_delete = (
            input("Which task you want me to delete: ").strip().lower().capitalize()
        )
        if task_to_delete:
            if not task_to_delete.isdigit():
                self.delete_by_name(task_to_delete=task_to_delete)
            else:
                self.delete_by_id(task_to_delete=task_to_delete)
        else:
            print_message("Please Enter a task name to delete.")
            return

    def mark_as_complete(self):
        print_new_line()
        print_dash_seperator(35)
        print("Taskforge AI - Mark as Complete: ")
        print_equalto_seperator(35)
        print("ID\tStatus\tTasks")
        print_dash_seperator(35)
        self.display_task()
        if self.tasks:
            print_dash_seperator(35)
            print_new_line()
            try:
                task_to_mark = int(
                    input(
                        "Which Task from the following you want to marks as complete: "
                    )
                )
            except ValueError:
                print_message("only numerical IDs are accepted!")
            for task in self.tasks:
                if task["unique_id"] == task_to_mark:
                    if task["completed"]:
                        print_message("Task is already completed!")
                        return

                    task["completed"] = True
                    self.save_to_json_file()
                    print_message("Task marked as completed!")
                    return

            print_message("No task found with this ID!")

        else:
            print("There are no tasks to show!")
            print_dash_seperator(35)
            print_new_line()
            return

    def save_to_json_file(self):
        with open(self.json_file_path, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)

    def load_from_json_file(self):
        if not self.json_file_path.exists():
            return []
        with open(self.json_file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    return []
            except json.JSONDecodeError:
                return []

    def show_menu(self):
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
                    self.add_task()
                elif user_option == 2:
                    self.view_task()
                elif user_option == 3:
                    self.mark_as_complete()
                elif user_option == 4:
                    self.delete_task()
                elif user_option == 5:
                    print_message("Thank you for using TaskForge AI. Goodbye!")
                    break
                else:
                    print_message("Invalid choice! Please select from options")
            except ValueError:
                print_message("Invalid input! Please enter a numerical option here.")

    def main(self):
        self.tasks.extend(self.load_from_json_file())
        self.tasks.sort(key=lambda task: task["unique_id"])
        self.show_menu()


if __name__ == "__main__":
    TaskForgeAI().main()
