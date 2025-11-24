"""
Step 4: Build the menu-driven Personal Expense Tracker.

Goal:
- Import and use the functions from step2_functions_core.py.
- Implement main() with a while-loop menu.
- At this step, there is NO filter/map feature yet.

Make sure step2_functions_core.py is in the same folder and fully implemented.
"""

from step2_functions_core import (
    FILENAME,
    load_expenses,
    save_expenses,
    add_expense,
    view_expenses,
    total_expense,
    remove_expense,
)


def print_menu():
    """
    Print the main menu for the program.

    TODO:
    - Show options 1–5:
        1. Add Expense
        2. View Expenses
        3. Total Expenses
        4. Remove Expense
        5. Save and Exit
    """
    pass


def main():
    """
    Main loop of the program.

    TODO:
    - Step 1: load data using: expenses = load_expenses(FILENAME)
    - Step 2: in a while True loop:
        * call print_menu()
        * ask for user choice: choice = input("Choose an option: ")
        * if choice == "1": call add_expense(expenses)
        * if choice == "2": call view_expenses(expenses)
        * if choice == "3": call total_expense(expenses)
        * if choice == "4": call remove_expense(expenses)
        * if choice == "5":
              - call save_expenses(FILENAME, expenses)
              - print a goodbye message
              - break out of the loop
        * otherwise: print "Invalid choice. Try again."
    """
    pass


if __name__ == "__main__":
    main()
