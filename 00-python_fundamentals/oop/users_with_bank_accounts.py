# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

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
            
            
class User:
    def __init__(self, name, email, account_number):
        self.name = name
        self.email = email
        self.account_number = account_number
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount, account_number):
        if account_number == "1":
            self.account.deposit(amount)
        
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        self.account.display_account_info()
            

# User1.display_user_balance()
# User1.make_deposit(100)
# User1.display_user_balance()
# User1.make_withdrawal(35)
# User1.display_user_balance()

User1 = User("Henry Chen", "henrychen14505@gmail.com", "1")
User2 = User("Henry Chen", "henrychenphotography@gmail.com", "2")