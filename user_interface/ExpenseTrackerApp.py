from expensetracker.ExpenseImplementation import ExpenseImplementation

class ExpenseTrackerApp:
    def __init__(self):
        """Initialize the app and create an ExpenseImplementation instance."""
        self.tracker = ExpenseImplementation()

    def run(self):
        """Main loop to interact with the user."""
        while True:
            print("\n--- Expense Tracker ---")
            print("1. Add Expense")
            print("2. List Expenses")
            print("3. View Summary")
            print("4. Total Expenses")
            print("5. Delete Expense")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                self.tracker.add_expense(amount, category, description)
            elif choice == "2":
                self.tracker.list_expenses()
            elif choice == "3":
                self.tracker.view_summary()
            elif choice == "4":
                self.tracker.total_expenses()
            elif choice == "5":
                expense_id = int(input("Enter expense ID to delete: "))
                self.tracker.delete_expense(expense_id)
            elif choice == "6":
                print("Exiting...")
                self.tracker.close()
                break
            else:
                print("Invalid choice. Please try again.")
