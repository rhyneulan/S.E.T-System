from expense import expense_storage
from logs import logs_tracker
from balance import budget_storage
from rich import print

# Function for the expense
def display_all_expenses():
    print("\n---Your Expenses---")

    try: 
        with open(expense_storage, "r") as file:
            for line in file:
                category, amount = line.strip().split(":")
                print(f"{category}: P{amount}")

    except FileNotFoundError:
        print("---[!]No Expenses Found---")

def total_expense():
    total = 0.0

    try:
        with open(expense_storage, "r") as file:
            for line in file:
                category, amount = line.strip().split(":")
                total += float(amount)
        print(f"P{total:.2f}")
    except FileNotFoundError:
         print("---[!]No Expenses Found---")

# Displaying Logs
def display_log():
    logs = logs_tracker()
    print("\n---Recorded Logs---\n")
    current_logs = logs()
    if not current_logs:
        print("No Recorded Transactions Yet.")
    else:
        for log in current_logs:
            print(log)
            print()

# Functions for the Budget
def display_all_budget():
    print("\n---Your Balance---")

    try: 
        with open(budget_storage, "r") as file:
            for line in file:
                category, amount = line.strip().split(":")
                print(f"{category}: P{amount}")

    except FileNotFoundError:
        print("---[!]No budget Found---")

def total_balance():
    total = 0.0

    try:
        with open(budget_storage, "r") as file:
            for line in file:
                category, amount = line.strip().split(":")
                total += float(amount)
        print(f"P{total:.2f}")
    except FileNotFoundError:
         print("---[!]No budget Found---")