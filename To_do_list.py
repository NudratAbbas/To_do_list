import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks in your list!\n")
    else:
        print("\n📝 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "✘"
            print(f"{idx}. [{status}] {task['title']}")
        print()

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("✅ Task added.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        print("✔ Task marked as done.")
    except (ValueError, IndexError):
        print("⚠ Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"🗑 Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("⚠ Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid option. Try again.")

if __name__ == "__main__":
    main()
