
# Expense Tracker - Menu Driven Program

expenses = []   # list of dictionaries

def add_expense():
    date = input("Enter date (DD/MM/YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("===== Expense List =====")
    for idx, item in enumerate(expenses, 1):
        print(f"{idx}. {item['date']} | {item['category']} | {item['description']} | ₹{item['amount']}")
    print()

def total_expense():
    if not expenses:
        print("No expenses to calculate.\n")
        return
    
    total = sum(item["amount"] for item in expenses)
    print(f"Total Expense: ₹{total}\n")

def menu():
    print("==== EXPENSE TRACKER ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expense")
    print("4. Exit")

while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number.\n")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_expense()
    elif choice == 4:
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid option. Please choose between 1–4.\n")
