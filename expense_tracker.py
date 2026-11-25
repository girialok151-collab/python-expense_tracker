expenses = []


def add_expense():
    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully.")

    except ValueError:
        print("Please enter a valid amount.")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    print("\n--- Expense List ---")

    for number, expense in enumerate(expenses, start=1):
        print(number, ".", expense["category"], "-", expense["amount"])


def show_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total expense is:", total)


while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Thank you for using the Expense Tracker.")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")