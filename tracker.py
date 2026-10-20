from monthly import CATEGORIES, get_current_month, get_month_label, read_monthly, get_budget_and_expense
from table_view import print_table, peso


def show_spending():
    records = read_monthly()

    # Table 1: one row per month
    month_budget = {}
    month_expense = {}

    for month, category, budget, expense in records:
        month_budget[month] = month_budget.get(month, 0.0) + budget
        month_expense[month] = month_expense.get(month, 0.0) + expense

    rows = []
    styles = {}
    total_budget = 0.0
    total_expense = 0.0

    for month in sorted(month_budget):
        budget = month_budget[month]
        expense = month_expense[month]
        savings = budget - expense

        if savings < 0:
            styles[len(rows)] = "red"

        rows.append([get_month_label(month), peso(budget), peso(expense), peso(savings)])
        total_budget += budget
        total_expense += expense

    print_table(
        "MONTHLY SPENDING",
        ["Month", "Budget", "Expenses", "Savings"],
        rows,
        ["<", ">", ">", ">"],
        total=["Total", peso(total_budget), peso(total_expense), peso(total_budget - total_expense)],
        styles=styles,
        empty_message="No budget or expenses recorded yet.",
    )

    # Table 2: where this month's money went
    this_month = get_current_month()
    spent = []
    month_total = 0.0

    for category in CATEGORIES:
        budget, expense = get_budget_and_expense(records, this_month, category)
        if expense > 0:
            spent.append([category, expense])
            month_total += expense

    category_rows = []
    for category, expense in spent:
        category_rows.append([category, peso(expense), f"{expense / month_total * 100:.0f}%"])

    print_table(
        f"SPENDING BY CATEGORY ({get_month_label(this_month)})",
        ["Category", "Spent", "Share"],
        category_rows,
        ["<", ">", ">"],
        total=["Total", peso(month_total), "100%"],
        empty_message="No expenses recorded this month.",
    )
