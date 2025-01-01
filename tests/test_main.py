import unittest
from unittest.mock import patch
from expensetracker.ExpenseImplementation import ExpenseImplementation

class TestExpenseImplementation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create a new ExpenseImplementation instance for testing."""
        cls.tracker = ExpenseImplementation(db_name=":memory:")

    def setUp(self):
        """Reset the table before each test."""
        with self.tracker.connection:
            self.tracker.connection.execute("DELETE FROM expenses")

    def test_add_expense(self):
        """Test adding an expense."""
        self.tracker.add_expense(50.0, "Food", "Lunch")
        with self.tracker.connection:
            cursor = self.tracker.connection.execute("SELECT COUNT(*) FROM expenses")
            count = cursor.fetchone()[0]
        self.assertEqual(count, 1)

    def test_view_summary(self):
        """Test viewing the summary of expenses by category."""
        self.tracker.add_expense(50.0, "Food", "Lunch")
        self.tracker.add_expense(30.0, "Food", "Snack")
        self.tracker.add_expense(20.0, "Transport", "Bus fare")
        
        with patch("builtins.print") as mock_print:
            self.tracker.view_summary()
            mock_print.assert_any_call("Food: $80.00")
            mock_print.assert_any_call("Transport: $20.00")

    def test_total_expenses(self):
        """Test calculating total expenses."""
        self.tracker.add_expense(50.0, "Food", "Lunch")
        self.tracker.add_expense(30.0, "Food", "Snack")
        
        with patch("builtins.print") as mock_print:
            self.tracker.total_expenses()
            mock_print.assert_any_call("Total Expenses: $80.00")

    def test_list_expenses(self):
        """Test listing all expenses."""
        self.tracker.add_expense(50.0, "Food", "Lunch")
        self.tracker.add_expense(30.0, "Transport", "Bus fare")
        
        with patch("builtins.print") as mock_print:
            self.tracker.list_expenses()
            mock_print.assert_any_call((1, 50.0, "Food", "Lunch", ""))
            mock_print.assert_any_call((2, 30.0, "Transport", "Bus fare", ""))

    def test_delete_expense(self):
        """Test deleting an expense."""
        self.tracker.add_expense(50.0, "Food", "Lunch")
        self.tracker.add_expense(30.0, "Food", "Snack")
        
        with self.tracker.connection:
            cursor = self.tracker.connection.execute("SELECT COUNT(*) FROM expenses")
            count_before = cursor.fetchone()[0]
        self.tracker.delete_expense(1)  # Delete expense with ID 1
        
        with self.tracker.connection:
            cursor = self.tracker.connection.execute("SELECT COUNT(*) FROM expenses")
            count_after = cursor.fetchone()[0]
        self.assertEqual(count_before - 1, count_after)

    @classmethod
    def tearDownClass(cls):
        """Close the database connection after all tests."""
        cls.tracker.close()
