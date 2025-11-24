"""
Step 2: Core Functions and Error Handling
"""

# -------------------------------------------------------
# 1. LOAD EXPENSES
# -------------------------------------------------------

FILENAME = r"D:\sejong_major\advanced-python (011300-010)\lab\assingments\tasks.txt"


def load_expenses(filename):
    """
    Read data from file and return a list of dictionaries.
    Format:
        category,amount
    """
    expenses = []

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 2:
                    continue
                category, amount_str = parts
                amount = float(amount_str)
                expenses.append({"category": category, "amount": amount})

    except FileNotFoundError:
        print("No previous records found.")

    return expenses


# -------------------------------------------------------
# 2. SAVE EXPENSES
# -------------------------------------------------------

def save_expenses(filename, expenses):
    """
    Save expenses to a file.
    Format per line:
        category,amount
    """
    try:
        with open(filename, "w") as f:
            for e in expenses:
                f.write(f"{e['category']},{e['amount']}\n")
    except Exception:
        print("Could not save data.")


# -------------------------------------------------------
# 3. ADD EXPENSE
# -------------------------------------------------------

def add_expense(expenses):
    """
    Add a new expense with error handling.
    """
    
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    try:
        amt = float(amount)
        expenses.append({"category": category, "amount": amt})
    except ValueError:
        print("Amount must be a valid number.")


# -------------------------------------------------------
# 4. VIEW EXPENSES
# -------------------------------------------------------

def view_expenses(expenses):
    """
    Print all expenses in a clean numbered format.
    """
    if not expenses:
        print("No expenses yet.")
        return

    print("\nYour Expenses:")
    print("-" * 40)

    for idx, e in enumerate(expenses, start=1):
        print(f"{idx}. {e['category']} - {e['amount']}$")

    print("-" * 40)


# -------------------------------------------------------
# 5. TOTAL EXPENSE
# -------------------------------------------------------

def total_expense(expenses):
    """
    Compute and display the total spending.
    """
    total = sum(e["amount"] for e in expenses)
    print(f"Total: {total}$")


# -------------------------------------------------------
# 6. REMOVE EXPENSE
# -------------------------------------------------------

def remove_expense(expenses, index):
    """
    Remove an expense using 1-based index.
    """
    try:
        idx = int(index) - 1
        del expenses[idx]

    except ValueError:
        print("Invalid number.")

    except IndexError:
        print("Invalid index.")


# -------------------------------------------------------
# 7. MANUAL TESTING (NO MENU YET)
# -------------------------------------------------------

if __name__ == "__main__":
    """
    Uncomment to test step-by-step.
    """

    data = load_expenses("data.txt")
    add_expense(data, "Food", "10")
    add_expense(data, "Books", 25)
    view_expenses(data)
    total_expense(data)
    remove_expense(data, "1")
    save_expenses("data.txt", data)
    
