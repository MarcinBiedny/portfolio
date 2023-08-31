"""
- translate into English - check
- displaying the month name, not the number - check
- month selection validation (only numbers from 1 to 12, 0 - exit from the program)
- selecting a cost category, adding new cost categories - check
- validation of the choice of cost category - check
- validation of selection in the menu (letters)
- summary of expenses by type (change layout from amount/type to type/amount)
"""

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

def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')

def add_expense(month):
    print()
    expense_amount = int(input("Enter the amount [zł]: "))
    
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
    total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    average_expenses_this_month = total_amount_this_month / number_of_expenses_this_month
    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    average_expenses_all = total_amount_all / len(expenses)

    print()
    print("Statistics")
    print("All expenses this month [zł]: ", total_amount_this_month)
    print("Average spend this month [zł]: ", average_expenses_this_month)
    print("All expenses [zł]: ", total_amount_all)
    print("Average spend [zł]: ", average_expenses_all)

while True:
    print()
    month = int(input("Select a month [1-12]. Selecting [0] ends the program. "))

    if month == 0:
        break

    while True:
        print()
        print("Selected month - "+months_array.get(month))
        print("0. Back to month selection")
        print("1. View all expenses")
        print("2. Add expense")
        print("3. Add a new expense type")
        print("4. Statistics")
        choice = int(input("Choose an option: "))

        if choice == 0:
            break
    
        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)

        if choice == 3:
            add_expense_types()

        if choice == 4:
            show_stats(month)