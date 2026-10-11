from balance import budget_storage
from expense import expense_storage
from rich import print

NEAR_LIMIT = 70 
REACHED_LIMIT = 100  # percentage threshold for warnings

def read_amounts(filename):
    amounts = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            name, amount = line.split(":")
            amounts[name] = float(amount)
    return amounts

def get_percent(spend, budget):
    if budget <= 0:
        return 0.0
    return (spend / budget) * 100

def comparing_with_budget():
    remaining = read_amounts(budget_storage)
    spent = read_amounts(expense_storage)

    print("---Budget vs Expenses---\n")
    for category in remaining:
        spent_amount = spent.get(category, 0.0)
        budget = remaining[category] + spent_amount
        percent_spent = get_percent(spent_amount, budget)
        print(f"{category}: [green bold]Budget ₱ {budget:.2f}[/green bold], [red bold]Spent ₱ {spent_amount:.2f}[/red bold] |" 
              f"Remaining ₱ {remaining[category]:.2f} | [blue bold]Used {percent_spent:.2f}%[/blue bold]\n")

def show_highest_spending():
    spent = read_amounts(expense_storage)

    highest_category = ""
    highest_amount = 0.0
    for  category in spent:
        if spent[category] > highest_amount:
            highest_category = category
            highest_amount = spent[category]
    print(f"---Highest Spending Category---")
    if highest_category == "":
        print("No expenses recorded yet.")
    else:
        print(f"Category: [red bold]{highest_category}[/red bold], Amount Spent: [red bold]₱ {highest_amount:.2f}[/red bold]")

def show_warning(category=None):
    remaining = read_amounts(budget_storage)
    spent = read_amounts(expense_storage)
    found_warning = False

    for name in remaining:
        if category is not None and name != category:
            continue   # skip categories we are not checking

        spent_amount = spent.get(name, 0)
        budget = remaining[name] + spent_amount
        percent = get_percent(spent_amount, budget)

        if percent == REACHED_LIMIT:
            print(f"[red bold][!] {name} has reached its budget! ({percent:.0f}% used)[/red bold]")
            found_warning = True
        
        elif percent >= NEAR_LIMIT:
            print(f"[blue bold][!] {name} is near its limit ({percent:.0f}% used)[/blue bold]")
            found_warning = True

    if not found_warning and category is None:
        print("No warnings. All categories are within budget.")