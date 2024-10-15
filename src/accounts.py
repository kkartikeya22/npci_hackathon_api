# accounts.py
class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def get_balance(self):
        return self.balance

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def credit(self, amount):
        self.balance += amount
