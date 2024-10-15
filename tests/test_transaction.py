# test_transaction.py
import unittest
from src.transaction import Transaction
from src.accounts import Account

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.sender = Account("sender", 100)
        self.receiver = Account("receiver", 50)
        self.transaction = Transaction(self.sender, self.receiver, 50)

    def test_execute_success(self):
        success = self.transaction.execute()
        self.assertTrue(success)
        self.assertEqual(self.sender.get_balance(), 50)
        self.assertEqual(self.receiver.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()
