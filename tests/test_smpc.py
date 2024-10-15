# test_smpc.py
import unittest
from src.smpc import smpc_split, smpc_reconstruct

class TestSMPC(unittest.TestCase):
    def test_smpc_split(self):
        secret = 100
        shares = smpc_split(secret)
        self.assertEqual(smpc_reconstruct(shares), secret)

if __name__ == "__main__":
    unittest.main()
