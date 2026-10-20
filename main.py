from rich import print
from cleaner import clear_console
from set_value import add_value, deduct_value
from report import display_log, show_total_expenses, show_total_budget
from logs import clear_logs
from analysis import show_expense_vs_budget
from monthly import get_total_remaining, reset_budgets, reset_expenses
from tracker import show_spending


def ask_number(message):
    try:
        return int(input(message))
    except ValueError:
        return -1


def confirm(question):
    answer = input(f"{question} (yes/no): ").strip().lower()
    return answer == "yes" or answer == "y"


while True:
    clear_console()
    print("============================================================")
    print(" Welcome to S.E.T SYSTEM: Student Expense Tracker System")
    print("============================================================")
    print(f"Your Total Remaining Balance is: ₱ {get_total_remaining():,.2f}")
    print("============================================================")
    print()

    print("Select Option:")
    print("1. Add Budget")
    print("2. Enter Expense")
    print("3. See Expense Summary Report")
    print("4. Tools")
    print("0. Exit")

    option = ask_number("Enter Option: ")

    if option == 1:
        add_value()

    elif option == 2:
        deduct_value()

    elif option == 3:
        report_options = ["Total Expenses", "Total Budget", "Logs", "Expense vs. Budget", "Monthly Spending"]
        print("\nSelect Option: ")
        for number, name in enumerate(report_options, start=1):
            print(f"{number}. {name}")

        report = ask_number("\nSelect your report option: ")

        if report == 1:
            show_total_expenses()
        elif report == 2:
            show_total_budget()
        elif report == 3:
            display_log()
        elif report == 4:
            show_expense_vs_budget()
        elif report == 5:
            show_spending()
        else:
            print("\nInvalid input please try again.")

    elif option == 4:
        tool_options = ["Clear Logs", "Reset Budget", "Reset Expenses"]
        print("\nSelect Option: ")
        for number, name in enumerate(tool_options, start=1):
            print(f"{number}. {name}")

        tool = ask_number("\nSelect your tool option: ")

        if tool == 1:
            if confirm("Do you want to clear all logs?"):
                clear_logs()
                print("---All logs has been successfuly cleared.---")
            else:
                print("---Action Canceled!---")

        elif tool == 2:
            if confirm("Do you want to reset all budget?"):
                reset_budgets()
                print("---All budget has been successfuly reset.---")
            else:
                print("---Action Canceled!---")

        elif tool == 3:
            if confirm("Do you want to reset all expenses?"):
                reset_expenses()
                print("---All expenses has been successfuly reset.---")
            else:
                print("---Action Canceled!---")

        else:
            print("\nInvalid input please try again.")

    elif option == 0:
        print("\n---Thank you for using S.E.T SYSTEM!---")
        print("---Exiting the program---")
        break

    else:
        print("\nInvalid input please try again.\n")

    input("\n---Press Enter to Continue---")