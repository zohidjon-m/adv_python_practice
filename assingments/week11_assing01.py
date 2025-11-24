import datetime

tasks = []

def welcome():
    print("\n====== TO-DO LIST MANAGER ======")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Remove task")
    print("5. Edit task")
    print("6. Save tasks to file")
    print("7. Exit")
    print("================================")

def add_task():
    text = input("Enter task: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"text": text, "created": timestamp, "completed": False})
    print("Task added successfully.")

def viewing_task():
    if not tasks:
        print("No tasks available.")
        return
    print("\nCurrent Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✔ completed" if t["completed"] else "❌ not completed"
        print(f"{i}. {t['text']} | Created: {t['created']} | {status}")

def mark():
    viewing_task()
  
    num = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete():
    viewing_task()
   
    num = int(input("Enter task number to delete: ")) - 1
    if 0 <= num < len(tasks):
        tasks.pop(num)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")
   

def edit_task():
    viewing_task()
   
    num = int(input("Task number to edit: ")) - 1
    if 0 <= num < len(tasks):
        new_text = input("Enter new task text: ")
        tasks[num]["text"] = new_text
        print("Task updated!")
    else:
        print("Invalid task number.")
 

def save_to_file():
    with open("tasks.txt", "w") as f:
        for t in tasks:
            line = f"{t['text']} | Created: {t['created']} | Completed: {t['completed']}\n"
            f.write(line)
    print("Tasks saved to tasks.txt")

def main():
    while True:
        welcome()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            viewing_task()
        elif choice == "3":
            mark()
        elif choice == "4":
            delete()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            print("Exiting... Goodbye!")
            return
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
