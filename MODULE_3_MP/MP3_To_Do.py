import os
os.system('cls' if os.name =='nt' else 'clear')

tasks = []

def menu():
    print("=== To Do List ===")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks.")
        else:
            print("Tasks:")
            for all_task in tasks:
                print("-", all_task)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")