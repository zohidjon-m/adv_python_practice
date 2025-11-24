"""
Project Step 3 – Menu-driven To-Do List program (25 minutes).

Goal:
- Reuse the same operations (add, view, mark, delete).
- Add a welcome() function that prints the menu.
- Implement a main() function with a while True loop to keep
  showing the menu until the user exits.
"""
import project_step2_functions

tasks = []  # Global list of tasks.


def welcome():
    """
   Print the menu for the To-Do List program.

    TODO:
    1. Print a welcome message (e.g., "Welcome to our To-Do List").
    2. Print the menu options exactly as in the slides:
       1. Add task
       2. View tasks
       3. Mark task as complete
       4. Remove task
       5. Exit
    """
    # TODO: implement this function
    print("Welcome to our To-Do List")
   
    print("\nOperations")
    print("\n1. Add task")
    print("\n2. View tasks")
    print("\n3. Mark task as complete")
    print("\n4. Remove task")
    print("\n5. Exit")
    
    op = (input("Operation: "))
    return op

def add_task():
    """
    Add a new task entered by the user.

    TODO:
    1. Ask the user for a task description.
    2. Append it to the global `tasks` list.
    3. Print a confirmation message.
    """
    # TODO: implement this function
    project_step2_functions.add_task()
    


def viewing_task():
    """
    Show all tasks with their numbers.

    TODO:
    1. If the list is empty, print something like "No tasks yet."
       and return.
    2. Use i = 1 and a for-loop: for task in tasks:
           print(f"Task {i}: {task}")
           i += 1
    """
    # TODO: implement this function
    project_step2_functions.viewing_task()


def mark():
    """
    Mark one task as completed.

    TODO:
    1. Ask the user: "Enter your task number: ".
    2. Convert to integer and subtract 1 to get the index.
    3. If index is between 0 and len(tasks) - 1:
         - Update tasks[index] = tasks[index] + " - completed"
         - Print "Task marked as complete"
       Else:
         - Print "Invalid task number"
    """
    # TODO: implement this function
    project_step2_functions.mark()


def delete():
    """
    Delete one task by its number.

    TODO:
    1. Ask the user: "Enter your task number: ".
    2. Convert to integer and subtract 1 to get the index.
    3. If index is valid:
         - Remove the task from the list.
         - Print "Task deleted successfully"
       Else:
         - Print "Invalid task number"
    """
    # TODO: implement this function
    project_step2_functions.delete()


def main():
    """
    Main loop for the menu-driven program.

    TODO:
    1. Call welcome() once at the beginning (to show the menu).
    2. Start an infinite loop: while True:
          - Ask the user for a choice: input("Enter your choice: ")
          - If "1": call add_task()
          - If "2": call viewing_task()
          - If "3": call mark()
          - If "4": call delete()
          - If "5":
                print a goodbye message like
                "Thank you for using the program!"
                break or return
          - Otherwise: print "Invalid input"
    3. (Optional) You may call welcome() again inside the loop so
       the menu is shown every time.
    """
    # TODO: implement this function
    op = welcome()
    
    while(True):
        if op == "1":
            add_task()
        elif op== "2":
            viewing_task()
        elif op == "3":
            mark()
        elif op =="4":
            delete()
        elif op =="5":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid input")
        welcome()

if __name__ == "__main__":
    main()
