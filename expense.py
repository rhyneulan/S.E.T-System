expense_storage = "expense.txt"

def save_evalue(category, value, filename=expense_storage):
    budgets = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                category_name, amount = line.strip().split(":")
                budgets[category_name] = float(amount)
    except FileNotFoundError:
        pass

    budgets[category] = value

    with open(filename, "w") as file:
        for category_name, amount in budgets.items():
            file.write(f"{category_name}: {amount}\n")

def load_evalue(filename=expense_storage):
    with open(filename, "r") as file:
        return file.read()

def get_initial_expenses(category, filename=expense_storage):
    try:
        with open(filename, "r") as file:
            for line in file:
                category_name, amount = line.strip().split(":")

                if category_name == category:
                    return float(amount)
    except FileNotFoundError:
        pass
        
    return 0.0

def clear_expenses(filename="expense.txt"):
    with open(filename, "w") as file:
        file.write("")