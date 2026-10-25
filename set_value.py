from category import choose_category
from logs import logs_tracker
from monthly import CATEGORIES, read_monthly, get_budget_and_expense
from monthly import add_budget, add_expense, get_remaining
from rich import print
from rich.markup import escape
from table_view import print_table, peso


def add_value():
    logs = logs_tracker()
    category = choose_category()

    try:
        added_value = float(input("Please Enter Your Amount: "))
        if added_value <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    month = add_budget(category, added_value)

    logs(f"Budget: +₱ {added_value:.2f} | {category}")

    print("\n---Amount is Successfully Added to the Budget---")
    show_budget_table(month, category)


def show_budget_table(month, changed_category):
    records = read_monthly()

    rows = []
    styles = {}
    total_budget = 0.0
    total_expense = 0.0

    for category in CATEGORIES:
        budget, expense = get_budget_and_expense(records, month, category)
        remaining = budget - expense

        total_budget += budget
        total_expense += expense

        # The changed category is highlighted. Categories with nothing in them are dimmed.
        if category == changed_category:
            styles[len(rows)] = "bold cyan"
        elif budget == 0 and expense == 0:
            styles[len(rows)] = "dim"

        rows.append([category, peso(budget), peso(expense), peso(remaining)])

    print_table(
        f"MONTHLY BUDGET ({month})",
        ["Category", "Budget", "Expense", "Remaining"],
        rows,
        ["<", ">", ">", ">"],
        total=["Total", peso(total_budget), peso(total_expense), peso(total_budget - total_expense)],
        styles=styles,
    )


def deduct_value():
    logs = logs_tracker()
    category = choose_category()

    balance = get_remaining(category)

    try:
        deducted_value = float(
            input("Please Enter Your Expense Amount: ")
        )
        if deducted_value <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    if deducted_value > balance:
        print("---[!] Insufficient Budget ---")
        return

    desc = expense_description()

    month = add_expense(category, deducted_value)

    logs(
        f"[red bold]Expense: -₱ {deducted_value:.2f}"
        f"[/red bold] | {category} | {escape(desc)}"
    )

    print("\n---Amount is Successfully Deducted to the Budget---")
    show_budget_table(month, category)


def expense_description():
    return input("Please Enter Your Expense Description: ").replace("|", "/").strip()