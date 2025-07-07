task_list = []

options = """
    1. Add task
    2. View tasks
    3. Mark task as done
    4. Exit
"""

def add_task():
    task = input("Type a task: ")
    dic = {
        "task": task,
        "done": False
    }
    task_list.append(dic)
    print("Task added!\n")

def view_task():
    if len(task_list) == 0:
        print("No task yet.\n")
    else:
        print("Your tasks:")
        for index, task in enumerate(task_list, start=1):
            status = "[Done]" if task["done"] else "[Pending]"
            print(f"{index}. {task['task']} {status}")
        print()

def mark_done():
    if len(task_list) == 0:
        print("No task to mark as done.\n")
        return

    view_task()
    userIndex = input("Enter the task number to mark as done: ")

    if userIndex.isdigit():
        y = int(userIndex) - 1
        if 0 <= y < len(task_list):
            task_list[y]["done"] = True
            print("Marked as Done!\n")
        else:
            print("Task number is out of range.\n")
    else:
        print("Invalid input. Please enter a number.\n")

while True:
    print(options)
    userInput = input("Enter your option: ")

    if userInput == "1":
        add_task()
    elif userInput == "2":
        view_task()
    elif userInput == "3":
        mark_done()
    elif userInput == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid option. Please select from 1 to 4.\n")
