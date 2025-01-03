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

    def create_table(self):
        """
        Creates the expenses table if it doesn't already exist.
        """
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL
                )
            """
            )

    def add_expense(self, amount, category, description=""):
        """
        Adds a new expense to the database.
        """
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO expenses (amount, category, description, date)
                VALUES (?, ?, ?, ?)
            """,
                (amount, category, description, date),
            )
        print("Expense added successfully!")

    def view_summary(self):
        """
        Displays a summary of expenses by category.
        """
        with self.connection:
            cursor = self.connection.execute(
                """
                SELECT category, SUM(amount) as total
                FROM expenses
                GROUP BY category
            """
            )
            print("\nExpense Summary:")
            for row in cursor:
                category, total = row
                print(f"{category}: ${total:.2f}")

    def total_expenses(self):
        """
        Displays the total expenses.
        """
        with self.connection:
            cursor = self.connection.execute(
                """
                SELECT SUM(amount) as total
                FROM expenses
            """
            )
            total = cursor.fetchone()[0] or 0
        return total

    def list_expenses(self):
        """Lists all expenses in the database."""
        with self.connection:
            cursor =self.connection.execute(
                "SELECT id, amount, category, description, date FROM expenses"
            )
            expenses = cursor.fetchall()
            print("\nAll Expenses:")
            for expense in expenses:
                print(expense)

    def delete_expense(self, expense_id):
        """Deletes an expense from the database by ID."""
        with self.connection:
            self.connection.execute("""DELETE FROM expenses WHERE id = ?""", (expense_id,))
        print("Expense deleted successfully!")

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()
