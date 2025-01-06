from user_interface.ExpenseTrackerApp import ExpenseTrackerApp
import tkinter as tk

def main():
    """
    Main function to run the expense tracker application.

    Provides a menu for users to:
    1. Add an expense.
    2. View a summary of expenses.
    3. View total expenses.
    4. List expenses
    5. Delete an expense
    6. Close database connection

    The application loads existing expenses from a file (if available) and
    saves the data before exiting.
    """
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

    # while True:
    #     print("\nExpense Tracker")
    #     print("1. Add Expense")
    #     print("2. View Summary")
    #     print("3. View Total Expenses")
    #     print("4. List Expenses")
    #     print("5. Delete Expense by ID")
    #     print("6. Close Connection")

    #     choice = input("Choose an option: ")

    #     if choice == "1":
    #         try:
    #             amount = float(input("Enter amount: "))
    #             category = input("Enter category: ")
    #             description = input("Enter description (optional): ")
    #             tracker.add_expense(amount, category, description)
    #         except ValueError:
    #             print("Invalid input. Please enter a valid amount.")
    #     elif choice == "2":
    #         tracker.view_summary()
    #     elif choice == "3":
    #         tracker.total_expenses()
    #     elif choice == "4":
    #         tracker.list_expenses()
    #     elif choice == "5":
    #         try:
    #             expense_id = int(input("Enter the ID of the expense to delete: "))
    #             tracker.delete_expense(expense_id)
    #         except ValueError:
    #             print("Invalid input. Please enter a valid expense ID.")
    #         tracker.delete_expense(expense_id)
    #     elif choice == "6":
    #         tracker.close()
    #         print("Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
