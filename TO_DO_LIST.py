todo_list = []

def task_add(task):
    todo_list.append(task)  
    print(f"The '{task}' task you entered has been added to your TO-DO LIST.")

def task_remove(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' has been removed from your to-do list.")

def list_display():
    if not todo_list:
        print("TO-DO LIST is empty.")
    else:
        print("TO-DO LIST:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

while True:
    print("-------------------- Welcome to the TO-DO LIST application --------------------")
    print("1: Add a task")
    print("2: Remove a task")
    print("3: Display to-do list")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task you want to add:")
        task_add(task)

    elif choice == "2":
        task = input("Enter the task you want to remove:")
        task_remove(task)

    elif choice == "3":
        list_display()

    elif choice == "4":
        print("Thank you for using our application.")
        break
    else:
        print("Invalid choice")
