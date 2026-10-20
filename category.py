from monthly import CATEGORIES


def choose_category():
    # Displays the list of expense categories and asks the user to pick one.
    while True:
        print("\n---Expense Categories---")

        for number, name in enumerate(CATEGORIES, start=1):
            print(f"{number}. {name}")

        try:
            option = int(input("Select your expense category: "))
        except ValueError:
            option = 0

        if 1 <= option <= len(CATEGORIES):
            return CATEGORIES[option - 1]

        print("Invalid option. Please try again.")
