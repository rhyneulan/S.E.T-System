from category import choose_category
from balance import get_initial_balance, save_value
from expense import save_evalue, get_initial_expenses
from logs import logs_tracker
from rich import print

def add_value():
    logs = logs_tracker()
    category = choose_category()
    value = get_initial_balance(category)
    print(f"Your current budget for [blue bold]{category}[/blue bold] is: {value}")

    try:
        added_value = float(input("Please Enter Your Amount: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    value += added_value
    save_value(category, value)
    logs(f"[green bold]Added: +₱ {added_value:.2f} | {category}[/green bold]")
    print()
    print("---Amount is Successfully Added to the Budget---\n")
    print(f"Your current budget for [blue bold]{category}[/blue bold] is: {value}")

def deduct_value():
    logs = logs_tracker()
    category = choose_category()
    value = get_initial_balance(category)
    expense = get_initial_expenses(category)
    print(f"Your current budget for [blue bold]{category}[/blue bold] is: {value}")

    try:
        deducted_value = float(input("Please Enter Your Expense Amount: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    if deducted_value > value:
        print("---[!]Insufficient Budget---")
        return
    else:
        value -= deducted_value
        save_value(category, value)
        expense += deducted_value
        save_evalue(category, expense)
        desc = expense_description()
        logs(f"[red bold]Expense: -₱ {deducted_value:.2f}[/red bold] | {category} | {desc}")
        print()
        print("---Amount is Successfully Deducted to the Budget---\n")
        print(f"Your current budget for [blue bold]{category}[/blue bold] is: {value}")

def expense_description():
    desc = input("Please Enter Your Expense Description: ")
    return desc