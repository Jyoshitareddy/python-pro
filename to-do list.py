def add_task(todo_list, task):
    if task not in todo_list:
        todo_list[task] = False
        print(f"Task '{task}' added.")
    else:
        print(f"Task '{task}' already exists.")

def complete_task(todo_list, task):
    if task in todo_list:
        todo_list[task] = True
        print(f"Task '{task}' marked as complete.")
    else:
        print(f"Task '{task}' not found.")

def delete_task(todo_list, task):
    if task in todo_list:
        del todo_list[task]
        print(f"Task '{task}' deleted.")
    else:
        print(f"Task '{task}' not found.")

def display_tasks(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
        return

    print("\nTo-Do List:")
    for task, is_complete in todo_list.items():
        status = "[ ]"  # Incomplete
        if is_complete:
            status = "[x]"  # Complete
        print(f"- {status} {task}")
    print()


def main():
    todo_list = {}

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Complete task")
        print("3. Delete task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            add_task(todo_list, task)
        elif choice == '2':
            task = input("Enter task to complete: ")
            complete_task(todo_list, task)
        elif choice == '3':
            task = input("Enter task to delete: ")
            delete_task(todo_list, task)
        elif choice == '4':
            display_tasks(todo_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()