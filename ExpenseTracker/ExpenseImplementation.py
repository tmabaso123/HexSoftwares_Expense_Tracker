import sqlite3
from datetime import datetime

class ExpenseImplementation:
    """
    A simple expense tracker to manage and categorize expenses, 
    view summaries, and save/load expense data to/from a file.
    """
    def __init__(self, db_name="expenses.db"):
        """
        Initializes the ExpenseImplementation with a SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def add_expense(self, amount, category, description=""):
        """
        Adds a new expense to the tracker.

        Parameters:
        amount (float): The amount of the expense.
        category (str): The category of the expense (e.g., food, rent).
        description (str): A brief description of the expense (optional).
        """
        self.expenses.append({"amount": amount, "category": category, "description": description})
        print("Expense added successfully!")

    def view_summary(self):
        """
        Displays a summary of expenses categorized by their categories.
        """
        summary = {}
        for expense in self.expenses:
            category = expense["category"]
            summary[category] = summary.get(category, 0) + expense["amount"]
        print("\nExpense Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")

    def total_expenses(self):
        """
        Displays the total amount of all expenses.
        """
        total = sum(expense["amount"] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

    def save_to_file(self, filename="expenses.json"):
        """
        Saves the list of expenses to a JSON file.

        Parameters:
        filename (str): The name of the file to save the expenses (default is 'expenses.json').
        """
        with open(filename, "w") as file:
            json.dump(self.expenses, file)
        print("Expenses saved to file!")

    def load_from_file(self, filename="expenses.json"):
        """
        Loads the list of expenses from a JSON file.

        Parameters:
        filename (str): The name of the file to load the expenses from (default is 'expenses.json').

        If the file does not exist, starts with an empty tracker.
        """
        try:
            with open(filename, "r") as file:
                self.expenses = json.load(file)
            print("Expenses loaded from file!")
        except FileNotFoundError:
            print("File not found. Starting with an empty tracker.")
