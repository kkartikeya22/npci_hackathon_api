# test_accounts.py
import unittest
from src.accounts import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("test123", 100)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_debit_success(self):
        self.assertTrue(self.account.debit(50))
        self.assertEqual(self.account.get_balance(), 50)

    def test_debit_failure(self):
        self.assertFalse(self.account.debit(200))
        self.assertEqual(self.account.get_balance(), 100)

    def test_credit(self):
        self.account.credit(100)
        self.assertEqual(self.account.get_balance(), 200)

if __name__ == "__main__":
    unittest.main()
