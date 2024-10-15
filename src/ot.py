# ot.py
import random

class ObliviousTransfer:
    def __init__(self, choices):
        self.choices = choices

    def sender(self):
        return random.choice(self.choices)

    def receiver(self, index):
        return self.choices[index]
