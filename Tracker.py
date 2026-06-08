expenses = []
while True:
    print("\n====EXPENSE TRACKER====")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.View Total Spent")
    print("4.Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        try:
            amount = float(input("Enter expense amount: ₹"))
            expenses.append(amount)
            print("Expense added successfully!")
        except ValueError:
            print("Please enter a valid amount.")

    elif choice =="2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nExpense List:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ₹{expense:.2f}")

    elif choice == "3":
        total = sum(expenses)
        print(f"\nTotal Spent: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice.Please select between 1 and 4.")