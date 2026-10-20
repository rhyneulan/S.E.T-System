from logs import logs_tracker, parse_log_line
from monthly import CATEGORIES, get_current_month, get_month_label, read_monthly, get_budget_and_expense
from table_view import print_table, peso


# Displaying Logs as a table
def display_log():
    logs = logs_tracker()
    rows = []
    styles = {}

    for log in logs():
        parsed = parse_log_line(log)

        if parsed is None:
            continue  # damaged line, nothing to show

        timestamp, kind, amount, category, description = parsed

        if len(description) > 30:
            description = description[:27] + "..."

        if kind == "Expense":
            sign = "-"
            styles[len(rows)] = "red"
        else:
            sign = "+"
            styles[len(rows)] = "green"

        rows.append([timestamp, kind, f"{sign}{peso(amount)}", category, description])

    print_table(
        "RECORDED LOGS",
        ["Date & Time", "Type", "Amount", "Category", "Description"],
        rows,
        ["<", "<", ">", "<", "<"],
        styles=styles,
        empty_message="No Recorded Transactions Yet.",
    )

# Total Expenses and Total Budget as tables (this month)

def print_amount_table(title, column_name, amounts, empty_message):
    # amounts is a list like [["Foods", 31.0], ["Bills", 135.0]]
    total = 0.0
    rows = []

    for category, amount in amounts:
        total += amount
        rows.append([category, peso(amount)])

    print_table(
        title,
        ["Category", column_name],
        rows,
        ["<", ">"],
        total=["Total", peso(total)],
        empty_message=empty_message,
    )

def show_total_expenses():
    month = get_current_month()
    records = read_monthly()

    amounts = []
    for category in CATEGORIES:
        budget, expense = get_budget_and_expense(records, month, category)
        if expense > 0:
            amounts.append([category, expense])

    print_amount_table(f"TOTAL EXPENSES ({get_month_label(month)})", "Expense", amounts, "No expenses recorded this month.")


def show_total_budget():
    month = get_current_month()
    records = read_monthly()

    amounts = []
    for category in CATEGORIES:
        budget, expense = get_budget_and_expense(records, month, category)
        if budget > 0:
            amounts.append([category, budget])

    print_amount_table(f"TOTAL BUDGET ({get_month_label(month)})", "Budget", amounts, "No budget set this month.")