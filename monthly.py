from datetime import datetime

monthly_storage = "monthly.txt"

# Single list of categories used by the whole program (category.py imports it from here)
CATEGORIES = ["Foods", "Bills", "Transportation", "Entertainment", "Health", "Supplies", "Shopping"]

# monthly.txt is the ONLY place where budgets and expenses are stored.
# Every line is one month + one category:
#
#   month,category,budget,expense
#   2026-10,Foods,200.00,100.00
#
# In the program, every line becomes a list like this:
#   ["2026-10", "Foods", 200.0, 100.0]
# and all the lines together are a list of those lists (called "records").


def get_current_month():
    return datetime.now().strftime("%Y-%m")


def get_month_label(month):
    # "2026-10" becomes "Oct 2026"
    return datetime.strptime(month, "%Y-%m").strftime("%b %Y")


def read_monthly():
    records = []

    try:
        with open(monthly_storage, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                try:
                    month, category, budget, expense = line.split(",")
                    records.append([month, category, float(budget), float(expense)])
                except ValueError:
                    continue  # skip a damaged line instead of crashing the program
    except FileNotFoundError:
        pass

    return records


def save_monthly(records):
    with open(monthly_storage, "w") as file:
        for month, category, budget, expense in records:
            file.write(f"{month},{category},{budget:.2f},{expense:.2f}\n")


def get_budget_and_expense(records, month, category):
    # Looks for one month + category. If it is not there, both are 0.
    for row_month, row_category, budget, expense in records:
        if row_month == month and row_category == category:
            return budget, expense

    return 0.0, 0.0


def get_remaining(category):
    # Money left in a category = all budget ever added - all expenses ever made.
    # (Unused budget carries over to the next month, same as the old budgets.txt did.)
    left = 0.0

    for row_month, row_category, budget, expense in read_monthly():
        if row_category == category:
            left += budget - expense

    return round(left, 2)


def get_total_remaining():
    left = 0.0

    for row_month, row_category, budget, expense in read_monthly():
        left += budget - expense

    return round(left, 2)


def add_to_monthly(category, budget_amount, expense_amount):
    # Adds to this month's line of the category. Creates the line if it is not there yet.
    # Returns the month that was used.
    month = get_current_month()
    records = read_monthly()

    new_records = []
    found = False

    for row_month, row_category, budget, expense in records:
        if row_month == month and row_category == category:
            budget = budget + budget_amount
            expense = expense + expense_amount
            found = True
        new_records.append([row_month, row_category, budget, expense])

    if found == False:
        new_records.append([month, category, budget_amount, expense_amount])

    save_monthly(new_records)
    return month


def add_budget(category, amount):
    return add_to_monthly(category, amount, 0.0)


def add_expense(category, amount):
    return add_to_monthly(category, 0.0, amount)


def reset_budgets():
    # Sets every budget to 0 and keeps the expenses.
    records = read_monthly()
    new_records = []

    for month, category, budget, expense in records:
        if expense > 0:  # a line with nothing left in it is dropped
            new_records.append([month, category, 0.0, expense])

    save_monthly(new_records)


def reset_expenses():
    # Sets every expense to 0 and keeps the budgets.
    records = read_monthly()
    new_records = []

    for month, category, budget, expense in records:
        if budget > 0:
            new_records.append([month, category, budget, 0.0])

    save_monthly(new_records)
