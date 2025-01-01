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
