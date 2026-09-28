class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True


class CryptoWallet:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def receive(self, amount):
        self.balance += amount
