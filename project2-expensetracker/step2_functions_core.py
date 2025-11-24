"""
Step 2: Core Functions and Error Handling

Goal:
- Create and test core project functions:
    load_expenses()
    save_expenses()
    add_expense()
    view_expenses()
    total_expense()
    remove_expense()
- Handle errors gracefully with try/except.
- Test interactively (no menu yet).
"""

# -------------------------------------------------------
# 1. LOAD EXPENSES
# -------------------------------------------------------

def load_expenses(filename):
    """
    Read data from file and return a list of dictionaries.

    File format (one per line):
        category,amount

    TODO:
    - Start with an empty list.
    - Use try/except to catch FileNotFoundError.
    - Inside try:
        * open file in "r"
        * loop over lines:
            - strip newline
            - split into category, amount_str
            - convert amount_str to float
            - append {"category": category, "amount": amount}
    - On FileNotFoundError: print "No previous records found."
    - Return the list.
    """
    expenses = []

    # HINT:
    # try:
    #     with open(...) as f:
    #         ...
    # except FileNotFoundError:
    #     print("No previous records found.")

    pass


# -------------------------------------------------------
# 2. SAVE EXPENSES
# -------------------------------------------------------

def save_expenses(filename, expenses):
    """
    Write the list of dictionaries to a file in the format:
        category,amount

    TODO:
    - Use with open(filename, "w")
    - Loop through expenses:
        * extract e["category"], e["amount"]
        * write f"{category},{amount}\n"
    - Wrap code in try/except to prevent crashing.
    - On any exception: print "Could not save data."
    """
    # HINT:
    # try:
    #     with open(filename, "w") as f:
    #         for e in expenses:
    #             ...
    # except Exception:
    #     print("Could not save data.")
    pass


# -------------------------------------------------------
# 3. ADD EXPENSE
# -------------------------------------------------------

def add_expense(expenses, category, amount):
    """
    Add a new expense dictionary to the list.

    TODO:
    - Convert amount to float inside try/except.
    - Append {"category": category, "amount": amount}
    - On ValueError (invalid number): print "Amount must be a valid number."
    """
    # HINT:
    # try:
    #     amt = float(amount)
    #     expenses.append({"category": category, "amount": amt})
    # except ValueError:
    #     print("Amount must be a valid number.")
    pass


# -------------------------------------------------------
# 4. VIEW EXPENSES
# -------------------------------------------------------

def view_expenses(expenses):
    """
    Print all expenses in a clean format.

    Example Output:
        1. Food - 10.0$
        2. Books - 30.0$

    TODO:
    - If list is empty: print "No expenses yet."
    - Use enumerate(expenses, start=1)
    - Print each: "<index>. <category> - <amount>$"
    """
    pass


# -------------------------------------------------------
# 5. TOTAL EXPENSE
# -------------------------------------------------------

def total_expense(expenses):
    """
    Compute and print the total of all amounts.

    TODO:
    - Loop through expenses and sum e["amount"]
    - Print the total as: "Total: <value>$"
    """
    pass


# -------------------------------------------------------
# 6. REMOVE EXPENSE
# -------------------------------------------------------

def remove_expense(expenses, index):
    """
    Remove an expense by index (1-based index).

    TODO:
    - Convert index to int inside try/except.
    - Delete expenses[index - 1]
    - Handle two errors:
        * ValueError → non-numeric index
        * IndexError → out-of-range index
    - Print appropriate error message.
    """
    # HINT:
    # try:
    #     idx = int(index) - 1
    #     del expenses[idx]
    # except ValueError:
    #     print("Invalid number.")
    # except IndexError:
    #     print("Invalid index.")
    pass


# -------------------------------------------------------
# 7. MANUAL TESTING (NO MENU YET)
# -------------------------------------------------------

if __name__ == "__main__":
    """
    TODO:
    - Uncomment tests one by one after implementing functions.

    Example sequence:
    1. data = load_expenses("data.txt")
    2. add_expense(data, "Food", "10")
    3. add_expense(data, "Books", 25)
    4. view_expenses(data)
    5. total_expense(data)
    6. remove_expense(data, "1")
    7. save_expenses("data.txt", data)
    """

    # data = load_expenses("data.txt")
    # add_expense(data, "Food", "10")
    # add_expense(data, "Books", 25)
    # view_expenses(data)
    # total_expense(data)
    # remove_expense(data, "1")
    # save_expenses("data.txt", data)

    pass
