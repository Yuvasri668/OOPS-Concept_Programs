#Hierarchical Inheritance

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance -= amount
            self.display_balance()
        else:
            print("You have insufficient amount in your account")

    def display_balance(self):
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, name, interest_rate):
        temp_interest=interest_rate/100
        super().__init__(name)
        self.interest_rate = temp_interest

    def add_interest(self):
        self.balance*=(1+self.interest_rate)
        super().display_balance()

class CurrentAccount(BankAccount):
    def __init__(self, name, overdraft_limit):
        super().__init__(name)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount<self.balance+self.overdraft_limit:
            self.balance -= amount
            super().display_balance()
        else:
            print("Ovaerdraft limit is exceeded")

SA = SavingsAccount("yuva",10)

SA.deposit(100)
SA.withdraw(30)
SA.add_interest()
SA.display_balance()

c = CurrentAccount("yuva",100)
c.deposit(100)
c.withdraw_with_overdraft(590)
