# transaction.py
from .zk_proof import ZeroKnowledgeProof
from .smpc import TransactionProcessor

class Account:
    def __init__(self, balance):
        self.balance = balance

class Transaction:
    def __init__(self, sender: Account, receiver: Account, amount: int):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def execute(self):
        if self.sender.balance >= self.amount:  # Compare balances
            self.sender.balance -= self.amount
            self.receiver.balance += self.amount
            return True
        return False
