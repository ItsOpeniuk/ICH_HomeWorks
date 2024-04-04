class BankAccount(object):


    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self.balance = balance


    def deposit(self, dep: float):
        self.balance += dep
        return f'Successfully deposited acount {self.account_number}, balance: {self.balance}'

    def withdraw(self, amount: float):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient funds")
        except ValueError as e:
            return str(e)
        else:
            self.balance -= amount
            return f"Withdrawn from account {self.account_number}. New balance: {self.balance}"


account1 = BankAccount(1235234523, 5564.67)
print(account1.deposit(4000))