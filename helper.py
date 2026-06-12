def print_equalto_seperator(n):
    print("=" * n)


def print_dash_seperator(n):
    print("-" * n)


def print_new_line():
    print("\n")


def task_len(task):
    return len(task) + 20


def print_message(message):
    message_length = len(message)
    print_new_line()
    print_dash_seperator(message_length)
    print(message)
    print_dash_seperator(message_length)
    print_new_line()


def get_status_emoji(task):
    if task["completed"]:
        return "✅"

    return "❌"
