class BankAccount:
    all_accounts = []
    # Creates a new instance of this class, i.e. a new bank account.
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    # Increases the account balance by the given amount.
    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing ${amount}. Your new balance is ${self.balance}.")
        return self
    
    # Decreases the account balance by the given amount.
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds, your current balance is ${self.balance}. Charging a $5 fee.")
            self.balance -= 5
            print(f"Your new balance is ${self.balance}.")
        else:
            self.balance -= amount
            print(f"Withdrawing ${amount}. Your new balance is ${self.balance}.")
        return self
    
    # Prints the account balance.  
    def display_account_info(self):
        print(f"Your current balance is ${round(self.balance, 0)}.")
        return self
    
    # Increases the account balance by a certain percentage yield.
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
            print(f"Your balance increased by {self.int_rate*100}% to ${round(self.balance, 0)}.")
        else:
            print(f"Cannot provide yield because you have a negative balance of ${self.balance}.")
        return self
    
    # Prints all instances of a bank account's info.
    @classmethod
    def prints_all_instances(cls):
        for account in cls.all_accounts:
            account.display_account_info()
    
# Create 2 bank accounts.
BankAccount1 = BankAccount(0.1, 100)
BankAccount2 = BankAccount(0.05, 50)

# BankAccount1: Make 3 deposits and 1 withdrawals, then yield interest, and display the account's info all in one line of code.
BankAccount1.deposit(70).deposit(20).deposit(40).withdraw(10).yield_interest().display_account_info()
print("=====")
#BankAccount 2: Make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code.
BankAccount2.deposit(25).deposit(25).withdraw(15).withdraw(15).withdraw(15).withdraw(15).yield_interest().display_account_info()
print("=====")
# Bonus: print out all accounts' balance.
BankAccount.prints_all_instances()