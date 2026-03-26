expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append([name, amount])
    print("Expense added successfully!\n")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.\n")
    else:
        print("\nYour Expenses:")
        total = 0
        for i in range(len(expenses)):
            print(i+1, ".", expenses[i][0], "-", expenses[i][1])
            total = total + expenses[i][1]
        print("Total =", total, "\n")

def delete_expense():
    view_expenses()
    if len(expenses) == 0:
        return
    num = int(input("Enter expense number to delete: "))
    if num > 0 and num <= len(expenses):
        expenses.pop(num - 1)
        print("Expense deleted!\n")
    else:
        print("Invalid number.\n")

while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.\n")
