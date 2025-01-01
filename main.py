import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from expensetracker.ExpenseImplementation import ExpenseImplementation


def main():
    """
    Main function to run the expense tracker application.

    Provides a menu for users to:
    1. Add an expense.
    2. View a summary of expenses.
    3. View total expenses.
    4. Close database connection
    5. Exit the application.

    The application loads existing expenses from a file (if available) and
    saves the data before exiting.
    """
    tracker = ExpenseImplementation()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. View Total Expenses")
        print("4. Close Connection")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "2":
            tracker.view_summary()
        elif choice == "3":
            tracker.total_expenses()
        elif choice == "4":
            tracker.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()