from datetime import datetime, date, timedelta
from rich import print

def show_spending():
    print("\n1. Show Weekly Spending")
    print("\n2. Show Monthly Spending")

    try:
        option = int(input("\nSelect Option: "))
    except ValueError:
        option = 0

    today = date.today()

    if option == 1:
        start_date = today - timedelta(days=today.weekday())
    else:
        start_date = today.replace(day=1)

    try:
        with open("logs.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("---[!]No Logs Found---")
        return

    totals = {}

    for line in lines:
        parts = line.strip().split(" | ")
        if len(parts) < 3:
            continue
        if "Expense:" not in parts[1]:
            continue

        date_text = parts[0].replace("[dim]", "").replace("[/dim]", "")
        date_text = date_text[:10]
        expense_date = datetime.strptime(date_text, "%m-%d-%Y").date()

        if expense_date >= start_date:
            amount_text = parts[1].replace("[red bold]Expense: -₱ ", "").replace("[/red bold]", "")
            amount = float(amount_text)
            category = parts[2]

            if category in totals:
                totals[category] = totals[category] + amount
            else:
                totals[category] = amount

    print(f"\n---Spending since {start_date.strftime('%b %d, %Y')}---")

    if not totals:
        print("No expenses recorded for this period.")
        return

    all_total = 0.0
    for category in totals:
        print(f"{category}: ₱ {totals[category]:.2f}")
        all_total = all_total + totals[category]

    print(f"\nTotal: ₱ {all_total:.2f}")