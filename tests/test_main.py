import unittest
from unittest.mock import patch
from expensetracker.ExpenseImplementation import ExpenseImplementation

class TestExpenseImplementation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create a new ExpenseImplementation instance for testing."""
        cls.tracker = ExpenseImplementation(db_name=":memory:")
