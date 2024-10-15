# test_ot.py
import unittest
from src.ot import ObliviousTransfer

class TestObliviousTransfer(unittest.TestCase):
    def setUp(self):
        # Set up with two choices for simplicity
        self.choices = ["Choice 1", "Choice 2"]
        self.ot = ObliviousTransfer(self.choices)

    def test_sender(self):
        # Test that the sender randomly chooses one of the available choices
        choice = self.ot.sender()
        self.assertIn(choice, self.choices)

    def test_receiver(self):
        # Test that the receiver correctly selects the index of the choice
        index = 1
        chosen_value = self.ot.receiver(index)
        self.assertEqual(chosen_value, self.choices[index])

    def test_invalid_receiver(self):
        # Test that providing an invalid index raises an error
        with self.assertRaises(IndexError):
            self.ot.receiver(10)  # Invalid index

if __name__ == "__main__":
    unittest.main()