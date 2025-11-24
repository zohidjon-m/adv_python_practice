"""
Project Step 1 – Practice using a list for tasks (20 minutes).

Goal:
- Use a Python list to store multiple tasks.
- Add tasks with append().
- Access tasks with indexing.
"""

def step1_list_practice():
    """
    TODO:
    1. Create an empty list called `tasks`.
    2. Use input() to ask the user for at least TWO task descriptions.
    3. Append each task to the list.
    4. Print the first task (index 0).
    5. Print the last task (index -1).
    6. Ask the user for an index number.
    7. Remove the task at that index using pop().
    8. Print the updated list after removal.
    """
    # TODO: write your code here
    tasks = []
    
    print("Add at least 2 tasks: \n")
    i=0
    while(True):
        if (i==2):
            break 
        task = str(input("\nTask: "))
        tasks.append(task)
        i+=1
    print_tasks(tasks)
    rmi = int(input("Task to remove: "))
    remove_task(tasks, rmi)
    print_tasks(tasks)
        
def print_tasks(tasks):
    i =0
    for a in tasks:
        print(f"Task {i}: {a}")
        i+=1

def remove_task(tasks, i):
    tasks.pop(i)

# if __name__ == "__main__":
#     step1_list_practice()
