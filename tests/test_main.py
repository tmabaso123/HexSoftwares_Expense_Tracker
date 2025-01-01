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
