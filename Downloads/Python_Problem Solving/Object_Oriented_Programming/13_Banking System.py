class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc

    def debit(self, amount):
        self.balance -= amount
        print(f"Debited {amount} from account {self.account_number}")
        # print(f"New balance: {self.get_balance()}")
        print(f"New balance: {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount} to account {self.account_number}")
        print(f"New balance: {self.get_balance()}")

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 123456789)
acc1.debit(1000)
acc1.credit(2000)
