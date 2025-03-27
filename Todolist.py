from datetime import datetime

from datetime import timedelta

def add_task(todo_list_ong,task, deadline,):
    #add task to todolist but also a deadline
    try:
        deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        todo_list_ong.append({"task": task, "deadline": deadline, "completed": False})
    except ValueError:
        print("Invalid deadline format! Use: YYYY-MM-DD HH:MM")

def remove_task(todo_list_ong,):
        if not todo_list_ong:
            print("No tasks to remove!")
            return

        print("--Current Tasks--")
        for index, task in enumerate(todo_list_ong):
            print(f"{index + 1}. {task['task']} (Deadline: {task['deadline']})")

        try:
            task_num = int(input("\nEnter the task number to remove (or 0 to cancel): "))
            if task_num == 0:
                print("Cancelled.")
            elif 1 <= task_num <= len(todo_list_ong):
                removed_task = todo_list_ong.pop(task_num - 1)
                print(f"Removed: {removed_task['task']}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def mark_task_complete(todo_list_ong, todo_list_com):
    if not todo_list_ong:
        print("No ongoing tasks!")
        return

    print("--Current Tasks--")
    for index, task in enumerate(todo_list_ong):
        print(f"{index + 1}. {task['task']} (Deadline: {task['deadline']})")

    try:
        task_num = int(input("\nEnter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(todo_list_ong):
            task = todo_list_ong.pop(task_num)
            task["completed"] = True
            todo_list_com.append(task)
            print(f"Completed: {task['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def view_task_list(todo_list_ong, todo_list_com,):
    #i want it to be able to not only view task but categorize them in completed and work in progress and the deadline
    print("--Ongoing Task--")
    if not todo_list_ong:
        print("You currently have no ongoing task!")
    else:
        for index, task in enumerate(todo_list_ong):
            if isinstance(task, dict):
                print(f"{index + 1}. {task['task']} (Deadline: {task['deadline']})")
            else:
                print(f"{index + 1 }. {task}")

    print("--Completed Task--")
    if not todo_list_com:
        print("You currently have no completed task!")
    else:
        for index, task in enumerate(todo_list_com):
            if isinstance(task, dict):
                print(f"{index + 1}. {task['task']} (Deadline: {task['deadline']})")
            else:
                print(f"{index + 1 }. {task}")

def alert_task(todo_list_ong):


    now = datetime.now()
    print("\n--- Deadline Alerts ---")
    alerts_found = False

    for task in todo_list_ong:
        if task["completed"]:
            continue

        time_left = task["deadline"] - now
        if timedelta(0) < time_left <= timedelta(days=1):
            print(f"⚠️ '{task['task']}' is due in {time_left}!")
            alerts_found = True

    if not alerts_found:
        print("No urgent deadlines.")


def main():
    todo_list_ong = []
    todo_list_com = []

    while True:
        print("--Task Menu--")
        print("1. Add Tasks? ")
        print("2. Remove Tasks? ")
        print("3. View Tasks? ")
        print("4. Mark Task as Completed? ")
        print("5. Check Task Deadlines")
        print("6. Exit Program? ")

        choice = input("Enter your number choice: ")

        if choice == "1":
            task = input("Enter task to add: ")
            deadline = input('When does this need to be completed?(Format: Year-Month-Date Hour:Minutes)')
            add_task(todo_list_ong, task, deadline)
        elif choice == "2":
            remove_task(todo_list_ong,)
        elif choice == "3":
             view_task_list(todo_list_ong, todo_list_com,)
        elif choice =="4":
            mark_task_complete(todo_list_ong, todo_list_com,)
        elif choice == "5":
             alert_task(todo_list_ong)
        elif choice =="6":
            print("Goodbye!")
            break
        else:
            print("Invalide Choice. Please try again.")

if __name__ == "__main__":
    main()
