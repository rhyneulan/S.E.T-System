def choose_category():
#    This function displays a list of expense categories and prompts the user to select one.
    category = ["Foods", "Bills", "Transportation", "Entertainment", "Health", "Supplies", "Shopping"]
    print("\n---Expense Categories---")

    for i, category in enumerate(category, start=1):
        print(f"{i}. {category}")
    try:
        option = int(input("Select your expense category: "))
    except ValueError:
        option = 0

    if option == 1:
        return "Foods"
    elif option == 2:
        return "Bills"
    elif option == 3:
        return "Transportation"
    elif option == 4:
        return "Entertainment"
    elif option == 5:
        return "Health"
    elif option == 6:
        return "Supplies"
    elif option == 7:
        return "Shopping"
    else:
        print("Invalid option. Please try again.")
        return choose_category() 