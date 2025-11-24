"""
Project Step 2 – Functions for each operation (no menu loop yet) (20 minutes).

Goal:
- Keep the global `tasks` list.
- Implement functions:
    - add_task()
    - viewing_task()
    - mark()
    - delete()
Students will call these functions manually from the Python shell
(or from a temporary test block) to test them.
"""

# Global list that will store all tasks as strings.
tasks = []  # Start with an empty list of tasks.


def add_task():
    """
    Add a new task to the global tasks list.

    TODO:
    1. Ask the user for a task description with input().
    2. Append the new task to `tasks`.
    3. Print a confirmation message, e.g. "Task added successfully!".
    """
    # TODO: implement this function
    
    task = str(input("\nTasks to add: "))
    tasks.append(task)
    print(f"Task {task} is successfully added,")
    


def viewing_task():
    """
    Print all tasks with dynamic numbering starting from 1.

    TODO:
    1. If there are no tasks, print a message and return.
    2. Use a for-loop and a counter variable i (start from 1).
    3. For each task, print: "Task i: <task>".
    """
    # TODO: implement this function
    if len(tasks)==0:
        print("\nthere is no any tasks")
    else:
        i =1
        for a in tasks:
            print(f"Task {i}: <{a}>")
            i+=1


def mark():
    """
    Mark a task as completed.

    TODO:
    1. Ask the user for the task number (1-based index).
    2. Convert it to list index by subtracting 1.
    3. Check if the index is inside the valid range (0 <= index < len(tasks)).
    4. If valid:
        - Update that element in `tasks` to add " - completed" at the end.
        - Print "Task marked as complete".
       Else:
        - Print "Invalid task number".
    """
    # TODO: implement this function
    index = int(input("\nWhich task do you want to Complete? "))
    if 0<=index-1<len(tasks):
        tasks[index-1] +=" Completed"
        print(f"Task {index}: {tasks[index-1]}")

def delete():
    """
    Delete a task by its number.

    TODO:
    1. Ask the user for the task number (1-based index).
    2. Convert it to list index by subtracting 1.
    3. Check if the index is inside the valid range.
    4. If valid:
        - Remove the corresponding task from `tasks`.
        - Print "Task deleted successfully".
       Else:
        - Print "Invalid task number".
    """
    # TODO: implement this function
    i = int(input("Task to remove: "))
    if 0<=i-1<len(tasks):
        tasks.pop(i-1)
    else:
        print("invalid task number")



# if __name__ == "__main__":
#     # Temporary manual test area (You can modify this if you want).
#     # Example:
#     add_task()
#     viewing_task()
    
