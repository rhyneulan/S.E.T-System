from rich import print
from cleaner import clear_console
from set_value import add_value, deduct_value
from report  import total_expense, display_all_expenses, display_log, display_all_budget, total_balance, get_total_balance
from logs import clear_logs
from analysis import comparing_with_budget, show_highest_spending, show_warning
from balance import clear_balance
from expense import clear_expenses
from tracker import show_spending
from rich import print

while True:
    clear_console()
    print("============================================================")
    print(" Welcome to S.E.T SYSTEM: Student Expense Tracker System")
    print("============================================================")
    print(f"Your Total Remaining Balance is: ₱ {get_total_balance():.2f}") 
    print("============================================================")
    print()

    print("Select Option:")
    print("1. Add Budget")
    print("2. Enter Expense")
    print("3. See Expense Summary Report")
    print("4. Tools")
    print("0. Exit")

    try:
        option = int(input("Enter Option: "))
    except ValueError:
        option = -1 

    if option == 1:
        add_value()
        
    elif option == 2: 
        deduct_value()

    elif option == 3:
        select = ["Total Expenses", "Total Budget", "Logs", "Budget vs Expenses", "Highest Spending Category", "Weekly & Monthly Spending", "Warnings"]
        print("\nSelect Option: ")
        for i, select in enumerate(select, start=1):
                print(f"{i}. {select}")
        try:
            option = int(input("\nSelect your report option: "))
        except ValueError:
            option = 0

        if option == 1:
            display_all_expenses()
            print("\n----Total----")
            total_expense()
        elif option == 2:
            display_all_budget()
            print("\n----Total----")
            total_balance()
        elif option == 3:
            display_log()
        elif option == 4:
            comparing_with_budget()
        elif option == 5:
            show_highest_spending()
        elif option == 6:
            show_spending()
        elif option == 7:
            show_warning()
        else:
            print("\nInvalid input please try again.")

    elif option == 4:
        tools = ["Clear Logs", "Reset Budget", "Reset Expenses"]
        print("\nSelect Option: ")
        for i, tools in enumerate(tools, start=1):
                print(f"{i}. {tools}")
        try:
            option = int(input("\nSelect your tool option: "))
        except ValueError:
            option = 0

        if option == 1:
            confirm = input("Do you want to clear all logs? (yes/no): ").strip().lower()
            if confirm == "yes" or confirm == "y":
                clear_logs()
                print("---All logs has been successfuly cleared.---")
            else:
                print("---Action Canceled!---")

        elif option == 2:
            confirm = input("Do you want to reset all budget? (yes/no): ").strip().lower()
            if confirm == "yes" or confirm == "y":
                clear_balance()
                print("---All budget has been successfuly reset.---")
            else:
                print("---Action Canceled!---")

        elif option == 3:
            confirm = input("Do you want to reset all expenses? (yes/no): ").strip().lower()
            if confirm == "yes" or confirm == "y":
                clear_expenses()
                print("---All expenses has been successfuly reset.---")
            else:
                print("---Action Canceled!---")

    elif option == 0:
        print("\n---Thank you for using S.E.T SYSTEM!---")
        print("---Exiting the program---")
        break
        
    else:
        print("\nInvalid input please try again.")

    input("\n---Press Enter to Continue---")