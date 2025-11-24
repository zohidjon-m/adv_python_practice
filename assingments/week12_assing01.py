"""
Step 5: Assignment — Extend the Personal Expense Tracker.

Completed version.
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
    Filter expenses by user-chosen category using filter().
    """
    category = input("Enter category to view: ")

    filtered = list(filter(lambda e: e["category"] == category, expenses))

    if not filtered:
        print("No expenses in this category.")
        return

    print(f"\nExpenses in category: {category}")
    print("-" * 40)
    for e in filtered:
        print(f"{e['category']} = {e['amount']}$")
    print("-" * 40)


def show_discounted(expenses, rate=0.1):
    """
    Show expenses after 10% discount (or tax if negative).
    Uses map(), does NOT modify original list.
    """
    updated = list(
        map(
            lambda e: {
                "category": e["category"],
                "amount": round(e["amount"] * (1 - rate), 2),
            },
            expenses,
        )
    )

    print("\nExpenses After Discount:")
    print("-" * 40)
    for e in updated:
        print(f"{e['category']} (after discount) = {e['amount']}$")
    print("-" * 40)


def print_menu():
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Remove Expense")
    print("5. Filter by Category")
    print("6. Show Discounted Expenses (10%)")
    print("7. Save and Exit")
    print("===================================")


def main():
    expenses = load_expenses(FILENAME)

    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            remove_expense(expenses)

        elif choice == "5":
            filter_by_category(expenses)

        elif choice == "6":
            show_discounted(expenses)

        elif choice == "7":
            save_expenses(FILENAME, expenses)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()