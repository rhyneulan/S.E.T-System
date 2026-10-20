from monthly import CATEGORIES, get_current_month, get_month_label, read_monthly, get_budget_and_expense
from table_view import print_table, peso

NEAR_LIMIT = 70  # percentage where the "near limit" warning starts


def get_percent(spend, budget):
    if budget <= 0:
        return 0.0
    return (spend / budget) * 100


def get_highest_spending(records, month):
    # Returns the category with the highest expense in that month and the amount.
    highest_category = ""
    highest_amount = 0.0

    for category in CATEGORIES:
        budget, expense = get_budget_and_expense(records, month, category)
        if expense > highest_amount:
            highest_category = category
            highest_amount = expense

    return highest_category, highest_amount


def get_warnings(records, month):
    # Returns a list of warnings for that month. Each warning is [category, status, color].
    warnings = []

    for category in CATEGORIES:
        budget, expense = get_budget_and_expense(records, month, category)
        percent = get_percent(expense, budget)

        if budget == 0 and expense > 0:
            warnings.append([category, "Over budget (no budget set)", "red bold"])
        elif expense > budget:
            warnings.append([category, f"Over budget ({percent:.0f}% used)", "red bold"])
        elif budget > 0 and expense >= budget:
            warnings.append([category, f"Limit reached ({percent:.0f}% used)", "red bold"])
        elif percent >= NEAR_LIMIT:
            warnings.append([category, f"Near limit ({percent:.0f}% used)", "blue bold"])

    return warnings


def show_expense_vs_budget():
    records = read_monthly()
    month = get_current_month()
    label = get_month_label(month)

    # Table 1: budget vs. expense of every category this month
    rows = []
    styles = {}
    total_budget = 0.0
    total_expense = 0.0

    for category in CATEGORIES:
        budget, expense = get_budget_and_expense(records, month, category)

        if budget == 0 and expense == 0:
            continue  # nothing happened in this category

        remaining = budget - expense
        used = f"{get_percent(expense, budget):.0f}%" if budget > 0 else "-"

        if remaining < 0:
            styles[len(rows)] = "red"

        rows.append([category, peso(budget), peso(expense), peso(remaining), used])
        total_budget += budget
        total_expense += expense

    total = [
        "Total",
        peso(total_budget),
        peso(total_expense),
        peso(total_budget - total_expense),
        f"{get_percent(total_expense, total_budget):.0f}%" if total_budget > 0 else "-",
    ]

    print_table(
        f"EXPENSE VS. BUDGET ({label})",
        ["Category", "Budget", "Expense", "Remaining", "Used"],
        rows,
        ["<", ">", ">", ">", ">"],
        total=total,
        styles=styles,
        empty_message="No budget or expenses recorded this month.",
    )

    if len(rows) == 0:
        return

    # Table 2: highest spending category of this month
    highest_category, highest_amount = get_highest_spending(records, month)
    highest_rows = []
    if highest_category != "":
        highest_rows.append([highest_category, peso(highest_amount)])

    print_table(
        f"HIGHEST SPENDING CATEGORY ({label})",
        ["Category", "Amount Spent"],
        highest_rows,
        ["<", ">"],
        styles={0: "red bold"},
        empty_message="No expenses yet.",
    )

    # Table 3: warnings of this month
    warning_rows = []
    warning_styles = {}

    for number, (category, status, color) in enumerate(get_warnings(records, month), start=1):
        warning_rows.append([number, category, status])
        warning_styles[number - 1] = color

    print_table(
        f"WARNING ({label})",
        ["No.", "Category", "Warning"],
        warning_rows,
        styles=warning_styles,
        empty_message="No warnings. All categories are within budget.",
    )