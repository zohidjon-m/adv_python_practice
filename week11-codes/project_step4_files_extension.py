"""
Project Step 4 – Extension:
- Add Edit Task option.
- Save tasks to a text file.
- Add timestamps when tasks are created.

IMPORTANT:
- This file assumes you already understand Step 3.
- Students should implement each TODO using the file-handling
  techniques from the lecture (open, write, with, etc.).
"""

import datetime  # for timestamps (datetime.datetime.now())

tasks = []  # Each element could be a string like "Buy milk [2025-11-04 10:30]"


def add_task():
    """
    Add a new task with a timestamp.

    TODO:
    1. Ask the user for the task description.
    2. Get the current time: datetime.datetime.now().
    3. Combine description + timestamp into one string, e.g.
         "Finish homework [2025-11-04 10:30]".
    4. Append it to `tasks`.
    """
    # TODO: implement this function
    pass


def viewing_task():
    """
    Same idea as before: print tasks with numbers.

    TODO:
    1. If tasks is empty, print a message and return.
    2. Loop through tasks and print them with numbers.
    """
    # TODO: implement this function
    pass


def edit_task():
    """
    Edit an existing task.

    TODO:
    1. Ask the user for the task number (1-based).
    2. Convert to index and validate.
    3. If valid:
         - Ask the user for the new task description.
         - (Option A) Keep the old timestamp and only change the text.
         - (Option B) Create a new timestamp for the edit.
         - Replace the element in `tasks`.
         - Print "Task updated!".
       Else:
         - Print "Invalid task number".
    """
    # TODO: implement this function
    pass


def save_tasks_to_file(filename="tasks.txt"):
    """
    Save all tasks into a text file.

    TODO:
    1. Use a with-statement:
           with open(filename, "w") as f:
    2. For each task in tasks, write it to the file followed by "\n".
    3. Print a message when saving is complete.
    """
    # TODO: implement this function
    pass


def main():
    """
    Extended menu including Edit and Save.

    Suggested options:
      1. Add task
      2. View tasks
      3. Edit task
      4. Save tasks to file
      5. Exit

    TODO:
    1. Implement a while True loop similar to Step 3.
    2. Call the correct function for each choice.
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    main()
