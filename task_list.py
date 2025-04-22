tasks = []

while True:
    print("\n1. Add 2. Remove 3. Update 4. View 5. Sort 6. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        task = input("Enter task: ")
        tasks.append(task)
    elif ch == '2':
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
    elif ch == '3':
        idx = int(input("Index to update: "))
        new_task = input("New task: ")
        tasks[idx] = new_task
    elif ch == '4':
        print("Tasks:", tasks)
    elif ch == '5':
        tasks.sort()
    elif ch == '6':
        break
