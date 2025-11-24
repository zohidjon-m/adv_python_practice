"""
Step 3: Practice using map() and filter() with expenses.

Goal:
- Extract data (amounts, categories) using map().
- Select data (only some expenses) using filter().
- Produce NEW lists without changing the original data.

Use the sample_expenses list to test your functions.
"""

sample_expenses = [
    {"category": "Food", "amount": 10},
    {"category": "Transport", "amount": 25},
    {"category": "Food", "amount": 5},
    {"category": "Books", "amount": 30},
]


def get_amounts(expenses):
    """
    Return a list of only the amounts from the expenses.

    Example:
    >>> get_amounts(sample_expenses)
    [10, 25, 5, 30]

    TODO:
    - Use map() with a lambda to pick e["amount"] from each expense.
    - Convert the result of map() to a list.
    """
    pass


def get_categories(expenses):
    """
    Return a list of only the categories.

    Example:
    >>> get_categories(sample_expenses)
    ["Food", "Transport", "Food", "Books"]

    TODO:
    - Similar to get_amounts, but pick e["category"].
    """
    pass


def filter_by_category(expenses, category):
    """
    Return a new list containing only expenses with the given category.

    Example:
    >>> filter_by_category(sample_expenses, "Food")
    [{"category": "Food", "amount": 10}, {"category": "Food", "amount": 5}]

    TODO:
    - Use filter() with a lambda checking e["category"] == category.
    - Wrap the filter object with list() before returning.
    """
    pass


def discounted_expenses(expenses, rate):
    """
    Return a NEW list with a discount applied to each expense.

    rate: fraction between 0 and 1.
          Example: rate = 0.1  means 10% discount.

    Each new dict should look like:
        {"category": same_category, "amount": original_amount * (1 - rate)}

    TODO:
    - Use map() with a lambda that builds a new dictionary.
    - Convert the result of map() to a list.
    - DO NOT modify the original expense dictionaries.
    """
    pass


if __name__ == "__main__":
    # TODO: uncomment these lines one by one after implementation
    #       and run the file to check your understanding.

    # print("Amounts:", get_amounts(sample_expenses))
    # print("Categories:", get_categories(sample_expenses))
    # print("Only Food:", filter_by_category(sample_expenses, "Food"))
    # print("After 10% discount:", discounted_expenses(sample_expenses, 0.1))
    pass
