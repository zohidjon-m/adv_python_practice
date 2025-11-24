"""
Time: 20 minutes
Step 1: Lists, dictionaries, and simple file I/O.

Goal:
- Represent one expense as a dictionary.
- Store many expenses in a list.
- Save/load that list from a text file.

Run this file and complete the TODOs.
"""

# An empty list that will hold expense dictionaries.
expenses = []

# Every expense should look like this:
# {"category": "Food", "amount": 15.0}


def add_expense(expenses, category, amount):
    """
    Create a new expense dictionary and append it to the list.

    TODO:
    - Make a dict with keys "category" and "amount".
    - Append it to the expenses list.
    """
    # Hint: use float(amount) to ensure it is numeric.
    expense = {"category":category,"amount":  float(amount)}
    expenses.append(expense)



def print_expenses(expenses):
    """
    Print each expense as: "1. Food - 15.0$"

    TODO:
    - Use enumerate(expenses, start=1).
    - Inside the loop, access e["category"] and e["amount"].
    """
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - {expense['amount']}")
    


def save_to_file(filename, expenses):
    """
    Save expenses into a text file.

    File format (one line per expense):
        category,amount

    TODO:
    - Use: with open(filename, "w") as f:
    - For each expense, write: f.write(f"{category},{amount}\\n")
    """
    with open(filename, "w") as f:
        for i, expense in enumerate(expenses):
            f.write(f"{expense['category'], {expense['amount']}}\n")


def load_from_file(filename):
    """
    Load expenses from a text file and return a list of dicts.

    TODO:
    - Start with an empty list.
    - Use: with open(filename, "r") as f:
    - For each line:
        * line = line.strip()
        * category, amount_str = line.split(",")
        * amount = float(amount_str)
        * append {"category": category, "amount": amount}
    - Return the list.
    """
    expenses01 = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            category, amount_str = line.split(",")
            amount = float(amount_str)
            expenses.append({"category":{category},"amount":{amount}})
    
    return expenses01  


if __name__ == "__main__":
    # TODO (manual test for yourself):
    # 1. Call add_expense(expenses, "Food", 10)
    #    and a few more categories.
    # 2. Call print_expenses(expenses).
    # 3. Call save_to_file("step1_test.txt", expenses).
    # 4. Call load_from_file("step1_test.txt") into a new variable
    #    and print it to see that it matches.
    
    add_expense(expenses, "Food", 10)
    print_expenses(expenses)
    save_to_file("step1_test.txt", expenses)
    load_from_file("step1_test.txt")
    
