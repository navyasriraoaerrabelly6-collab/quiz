# ==============================
# TO-DO LIST PROJECT
# DecodeLabs Project 1
# ==============================

# List to store all tasks
tasks = []

# Task ID counter
task_id = 1


# Function to add a task
def add_task():
    global task_id

    title = input("Enter task title: ")

    task = {
        "id": task_id,
        "title": title
    }

    tasks.append(task)

    print("✅ Task Added Successfully!")

    task_id += 1


# Function to view tasks
def view_tasks():

    if len(tasks) == 0:
        print("📂 No tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        print(f"ID: {task['id']} | Task: {task['title']}")


# Function to search task
def search_task():

    keyword = input("Enter keyword to search: ")

    found = False

    for task in tasks:

        if keyword.lower() in task['title'].lower():

            print(f"✅ Found -> ID: {task['id']} | Task: {task['title']}")
            found = True

    if not found:
        print("❌ No matching task found.")


# Function to remove task
def remove_task():

    if len(tasks) == 0:
        print("📂 No tasks to remove.")
        return

    try:
        remove_id = int(input("Enter Task ID to remove: "))

        for task in tasks:

            if task['id'] == remove_id:
                tasks.remove(task)

                print("🗑 Task Removed Successfully!")
                return

        print("❌ Task ID not found.")

    except ValueError:
        print("⚠ Please enter a valid number.")


# Main Program Loop
while True:

    print("\n======================")
    print("   TO-DO LIST MENU")
    print("======================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ADD TASK
    if choice == "1":
        add_task()

    # VIEW TASKS
    elif choice == "2":
        view_tasks()

    # SEARCH TASK
    elif choice == "3":
        search_task()

    # REMOVE TASK
    elif choice == "4":
        remove_task()

    # EXIT
    elif choice == "5":
        print("👋 Exiting Program...")
        break

    # INVALID CHOICE
    else:
        print("⚠ Invalid choice. Please try again.")