"""
Expense Tracker and Monthly Report
A beginner-friendly command-line personal expense tracker.
"""

from datetime import datetime


# All expenses are stored as dictionaries inside this list.
expenses = []

# Monthly budgets are stored using a YYYY-MM key, for example: {"2026-09": 5000.0}
budgets = {}

CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Education",
    "Health",
    "Other",
]
DATE_FORMAT = "%Y-%m-%d"
MONTH_FORMAT = "%Y-%m"


def get_valid_date():
    """Read and validate a date in YYYY-MM-DD format."""
    while True:
        date_text = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_text, DATE_FORMAT)
            return date_text
        except ValueError:
            print("Error: enter a valid date, such as 2026-09-23.")


def get_valid_month(prompt="Enter month and year (YYYY-MM): "):
    """Read and validate a month in YYYY-MM format."""
    while True:
        month_text = input(prompt).strip()
        try:
            datetime.strptime(month_text, MONTH_FORMAT)
            return month_text
        except ValueError:
            print("Error: enter a valid month, such as 2026-09.")


def get_valid_category():
    """Read a category and accept it regardless of letter case."""
    print("Available categories:")
    print(", ".join(CATEGORIES))

    while True:
        category_text = input("Enter category: ").strip().lower()
        for category in CATEGORIES:
            if category.lower() == category_text:
                return category
        print("Error: invalid category. Choose a category from the list.")


def get_valid_description():
    """Read a description that is not empty or only spaces."""
    while True:
        description = input("Enter description: ").strip()
        if description:
            return description
        print("Error: description cannot be empty.")


def get_valid_amount(prompt="Enter amount: "):
    """Read a positive numeric amount."""
    while True:
        amount_text = input(prompt).strip()
        try:
            amount = float(amount_text)
            if amount <= 0:
                print("Error: amount must be greater than zero.")
            else:
                return round(amount, 2)
        except ValueError:
            print("Error: amount must be a number, such as 250 or 250.50.")


def add_expense():
    """Collect expense details and add one dictionary to the expenses list."""
    print("\n--- Add Expense ---")
    expense = {
        "date": get_valid_date(),
        "category": get_valid_category(),
        "description": get_valid_description(),
        "amount": get_valid_amount(),
    }
    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses(expense_list=None):
    """Display expenses in a simple table."""
    if expense_list is None:
        expense_list = expenses

    print("\n--- Expenses ---")
    if not expense_list:
        print("No expenses recorded.")
        return

    print(f"{'No.':<5}{'Date':<13}{'Category':<16}{'Description':<28}{'Amount':>12}")
    print("-" * 74)
    for number, expense in enumerate(expense_list, start=1):
        print(
            f"{number:<5}{expense['date']:<13}{expense['category']:<16}"
            f"{expense['description'][:27]:<28}{expense['amount']:>12.2f}"
        )


def calculate_total(expense_list=None):
    """Calculate and display the total expenditure."""
    if expense_list is None:
        expense_list = expenses

    print("\n--- Total Expenditure ---")
    if not expense_list:
        print("No expenses recorded.")
        return 0.0

    total = round(sum(expense["amount"] for expense in expense_list), 2)
    print(f"Total expenditure: {total:.2f}")
    return total


def highest_expense(expense_list=None, display=True):
    """Return and optionally display the expense with the greatest amount."""
    if expense_list is None:
        expense_list = expenses

    if not expense_list:
        if display:
            print("\nNo expenses recorded.")
        return None

    highest = max(expense_list, key=lambda expense: expense["amount"])
    if display:
        print("\n--- Highest Expense ---")
        print(f"Date: {highest['date']}")
        print(f"Category: {highest['category']}")
        print(f"Description: {highest['description']}")
        print(f"Amount: {highest['amount']:.2f}")
    return highest


def category_wise_spending(expense_list=None, display=True):
    """Calculate totals for categories used in the supplied expense list."""
    if expense_list is None:
        expense_list = expenses

    if not expense_list:
        if display:
            print("\nNo expenses recorded.")
        return {}

    totals = {category: 0.0 for category in CATEGORIES}
    for expense in expense_list:
        totals[expense["category"]] += expense["amount"]

    totals = {category: round(amount, 2) for category, amount in totals.items()}
    if display:
        print("\n--- Category-Wise Spending ---")
        for category in CATEGORIES:
            if totals[category] > 0:
                print(f"{category:<18} {totals[category]:.2f}")
    return totals


def monthly_report():
    """Display a complete report for a selected month."""
    print("\n--- Monthly Spending Report ---")
    month = get_valid_month()
    monthly_expenses = [expense for expense in expenses if expense["date"].startswith(month)]

    if not monthly_expenses:
        print(f"No expenses found for {month}.")
        return

    print(f"\nReport for {month}")
    view_expenses(monthly_expenses)
    total = calculate_total(monthly_expenses)
    category_wise_spending(monthly_expenses)
    highest = highest_expense(monthly_expenses, display=False)

    print(f"Number of expenses: {len(monthly_expenses)}")
    print("Highest expense of the month:")
    print(f"{highest['description']} - {highest['amount']:.2f}")

    if month in budgets:
        print(f"Monthly budget: {budgets[month]:.2f}")
        print(f"Remaining budget: {budgets[month] - total:.2f}")
        show_budget_warning(total, budgets[month])


def set_budget():
    """Set or replace a positive budget for a selected month."""
    print("\n--- Set Monthly Budget ---")
    month = get_valid_month()
    amount = get_valid_amount("Enter monthly budget: ")
    budgets[month] = amount
    print(f"Budget for {month} set to {amount:.2f}.")


def show_budget_warning(spending, budget):
    """Print the required 80% and over-budget warnings."""
    if spending > budget:
        print("WARNING: Spending exceeds the monthly budget.")
    elif spending >= budget * 0.80:
        print("WARNING: Spending has reached at least 80% of the budget.")


def check_budget():
    """Show spending, budget, remaining amount, and warning for a month."""
    print("\n--- Check Budget ---")
    month = get_valid_month()

    if month not in budgets:
        print(f"No budget has been set for {month}.")
        return

    spending = sum(expense["amount"] for expense in expenses if expense["date"].startswith(month))
    budget = budgets[month]
    remaining = round(budget - spending, 2)

    print(f"Month: {month}")
    print(f"Budget: {budget:.2f}")
    print(f"Total spending: {spending:.2f}")
    print(f"Remaining budget: {remaining:.2f}")
    show_budget_warning(spending, budget)


def display_menu():
    print(
        """
========== EXPENSE TRACKER ==========
1. Add Expense
2. View All Expenses
3. Total Expenditure
4. Highest Expense
5. Category-wise Spending
6. Monthly Spending Report
7. Set Monthly Budget
8. Check Budget
9. Exit
======================================
"""
    )


def main():
    """Run the menu until the user chooses Exit."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("\n--- Highest Expense ---")
            highest_expense()
        elif choice == "5":
            print("\n--- Category-Wise Spending ---")
            category_wise_spending()
        elif choice == "6":
            monthly_report()
        elif choice == "7":
            set_budget()
        elif choice == "8":
            check_budget()
        elif choice == "9":
            print("Thank you for using Expense Tracker.")
            break
        else:
            print("Error: choose a number from 1 to 9.")


if __name__ == "__main__":
    main()
