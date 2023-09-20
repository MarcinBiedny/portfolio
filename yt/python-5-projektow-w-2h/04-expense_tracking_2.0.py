expenses = []

months_array = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

expense_types = ["house", "car", "bills", "food", "entertainment"]

def is_integer(value):
    try:
        int(value)
    except Exception:
        return False
    return True

def is_month_within_proper_range(month):
    if 0 <= month <= 12:
        return True
    else:
        print("A year doesn't have that many months.")
    return False

def is_valid_month_input_given_by_user(month):
    if not is_integer(month):
        print("There is no such month.")
        return False
    if not is_month_within_proper_range(int(month)):
        return False
    return True

def is_choice_within_proper_range(choice):
    if 0 <= choice <= 5:
        return True
    else:
        print("There is no such option in the menu.")
    return False

def is_valid_choice_input_given_by_user(choice):
    if not is_integer(choice):
        print("It's not a number.")
        return False
    if not is_choice_within_proper_range(int(choice)):
        return False
    return True

def show_expenses(month):
    print()
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')

def show_expenses_by_type(month):
    expense_totals = {}
    print()
    print("Expenses per category in "+months_array.get(month))
    for expense_amount, expense_type, month in expenses:
        if (expense_type, month) in expense_totals:
            expense_totals[(expense_type, month)] += expense_amount
        else:
            expense_totals[(expense_type, month)] = expense_amount

    for (expense_type,month), total_amount in expense_totals.items():
        print(f"Total expenses for {expense_type} - {total_amount}")

def add_expense(month):
    print()
    while True:
        expense_amount = input("Enter the amount [PLN]: ")
        if is_integer(expense_amount):
            expense_amount = int(expense_amount)
            break
        print()
        print("The cost value must be an integer. Please enter a valid cost value.")
    
    print()
    while True:
        categories = ", ".join(expense_types)
        expense_type = input("Enter the type of expense ("+categories+"): ")

        if expense_type in expense_types:
            break
        else:
            print()
            print("Invalid expense type.")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)

def add_expense_types():
    print()
    print("Expense types available: ")
    print(expense_types)
    new_expense_types = input("Enter a new expense type: ")
    expense_types.append(new_expense_types)

def show_stats(month):
    while True:
        if len(expenses) == 0:
            print()
            print("No expenses have been entered yet.")
            break
        else:    
            total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
            number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
            average_expenses_this_month = total_amount_this_month / number_of_expenses_this_month
            total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
            average_expenses_all = total_amount_all / len(expenses)

            print()
            print("Statistics")
            print("All expenses this month [PLN]: ", total_amount_this_month)
            print("Average spend this month [PLN]: ", average_expenses_this_month)
            print("All expenses [PLN]: ", total_amount_all)
            print("Average spend [PLN]: ", average_expenses_all)
            break

while True:

    while True:
        
        print()
        month = input("Select a month [1-12]. Selecting [0] ends the program. ")
        if is_valid_month_input_given_by_user(month):
            month = int(month)
            break

    if month == 0:
        break

    while True:
        print()
        print("Selected month - "+months_array.get(month))
        print("0. Back to month selection")
        print("1. View all expenses")
        print("2. View expenses by type")
        print("3. Add expense")
        print("4. Add a new expense type")
        print("5. Statistics")
        
        while True:
            print()
            choice = input("Choose an option: ")
            if is_valid_choice_input_given_by_user(choice):
                choice = int(choice)
                break

        if choice == 0:
            break
    
        if choice == 1:
            show_expenses(month)

        if choice == 2:
            show_expenses_by_type(month)

        if choice == 3:
            add_expense(month)

        if choice == 4:
            add_expense_types()

        if choice == 5:
            show_stats(month)
