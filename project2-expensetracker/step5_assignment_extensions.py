"""
Step 5: Assignment — Extend the Personal Expense Tracker.

You now have:
- Core functions implemented in step2_functions_core.py.
- Practice with map() and filter() in step3_map_filter_practice.py.
- A working menu (from step4_menu_program.py).

Your task in THIS file:
1. Add a menu option to filter expenses by category    (use filter()).
2. Add a menu option to show expenses with 10% change (discount or tax, use map()).
3. Keep the original data unchanged when showing discounted values.
4. Use the TODOs below as a precise guide.

You should submit this file as your final project code.
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


def filter_by_category(expenses):
    """
    Ask the user for a category and print only matching expenses.

    Requirements:
    - Ask: category = input("Enter category to view: ")
    - Use filter() to select only expenses where e["category"] == category.
    - Convert the filter object to a list so you can reuse it.
    - If the list is empty: print "No expenses in this category."
    - Otherwise: print each expense similar to view_expenses().
    """
    # TODO: implement this function using filter()
    pass


def show_discounted(expenses, rate=0.1):
    """
    Show all expenses after applying a discount (or tax) to the amounts.

    rate: fraction between 0 and 1. Example: 0.1 means 10%.

    Requirements:
    - Use map() to build NEW dictionaries, do not modify 'expenses'.
      For each e in expenses, create:
        {
            "category": e["category"],
            "amount": e["amount"] * (1 - rate)
        }
      (Use 1 + rate if you want to interpret it as tax instead of discount.)
    - Convert the map object to a list.
    - Print the result in a neat format:
         "Food (after discount) = 9.0$"
    """
    # TODO: implement this function using map()
    pass


def print_menu():
    """
    Menu for the extended version of the program.

    TODO:
    - Show options 1–7:
        1. Add Expense
        2. View Expenses
        3. Total Expenses
        4. Remove Expense
        5. Filter by Category          (NEW)
        6. Show Discounted Expenses    (NEW)
        7. Save and Exit
    """
    pass


def main():
    """
    Main loop for the extended version.

    TODO:
    - Load expenses from FILENAME.
    - Loop forever:
        * print_menu()
        * read choice
        * implement behavior:

          "1" -> add_expense(expenses)
          "2" -> view_expenses(expenses)
          "3" -> total_expense(expenses)
          "4" -> remove_expense(expenses)
          "5" -> call filter_by_category(expenses)
          "6" -> call show_discounted(expenses)
          "7" -> save_expenses(FILENAME, expenses), print goodbye, break
          otherwise -> print "Invalid choice. Try again."
    """
    pass


if __name__ == "__main__":
    main()
