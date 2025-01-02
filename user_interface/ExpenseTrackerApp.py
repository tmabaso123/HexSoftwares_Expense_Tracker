import tkinter as tk
from tkinter import messagebox
from expensetracker.ExpenseImplementation import ExpenseImplementation

class ExpenseTrackerApp:
    def __init__(self, root):
        """
        Initializes the Expense Tracker GUI and database connection.
        """
        self.tracker = ExpenseImplementation()
        self.root = root
        self.root.title("Expense Tracker")

        # GUI Layout
        tk.Label(root, text="Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)

        tk.Label(root, text="Category:").grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        tk.Label(root, text="Description:").grid(row=2, column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=2, column=1)

        add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        add_button.grid(row=3, column=0, columnspan=2)

        view_button = tk.Button(root, text="View Summary", command=self.view_summary)
        view_button.grid(row=4, column=0, columnspan=2)

        total_button = tk.Button(root, text="Total Expenses", command=self.total_expenses)
        total_button.grid(row=5, column=0, columnspan=2)

        list_button = tk.Button(root, text="List Expenses", command=self.list_expenses)
        list_button.grid(row=6, column=0, columnspan=2)

        delete_button = tk.Button(root, text="Delete Expense", command=self.delete_expense)
        delete_button.grid(row=7, column=0, columnspan=2)

    def add_expense(self):
        """
        Adds an expense to the database.
        """
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()

        if amount and category:
            try:
                self.tracker.add_expense(float(amount), category, description)
                messagebox.showinfo("Success", "Expense added successfully!")
                self.amount_entry.delete(0, tk.END)
                self.category_entry.delete(0, tk.END)
                self.description_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            messagebox.showerror("Error", "Amount and Category are required.")

    def view_summary(self):
        """
        Displays a summary of expenses by category.
        """
        summary = []
        with self.tracker.connection:
            cursor = self.tracker.connection.execute("""
                SELECT category, SUM(amount) as total
                FROM expenses
                GROUP BY category
            """)
            summary = cursor.fetchall()

        if summary:
            summary_text = "\n".join([f"{row[0]}: ${row[1]:.2f}" for row in summary])
            messagebox.showinfo("Expense Summary", summary_text)
        else:
            messagebox.showinfo("Expense Summary", "No expenses found.")

    def total_expenses(self):
        """
        Displays the total expenses.
        """
        with self.tracker.connection:
            cursor = self.tracker.connection.execute("""
                SELECT SUM(amount) as total
                FROM expenses
            """)
            total = cursor.fetchone()[0] or 0
        messagebox.showinfo("Total Expenses", f"Total: ${total:.2f}")

    def list_expenses(self):
        """
        Lists all expenses in a separate window.
        """
        list_window = tk.Toplevel(self.root)
        list_window.title("All Expenses")
        expenses = []

        with self.tracker.connection:
            cursor = self.tracker.connection.execute("""
                SELECT id, amount, category, description, date
                FROM expenses
            """)
            expenses = cursor.fetchall()

        if expenses:
            for expense in expenses:
                tk.Label(list_window, text=f"{expense}").pack()
        else:
            tk.Label(list_window, text="No expenses found.").pack()

    def delete_expense(self):
        """
        Deletes an expense by ID.
        """
        expense_id = tk.simpledialog.askinteger("Delete Expense", "Enter Expense ID to delete:")
        if expense_id:
            self.tracker.delete_expense(expense_id)
            messagebox.showinfo("Success", "Expense deleted successfully!")
