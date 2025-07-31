# Class definition

class BankAccount:

    # Method to initialize the account balance
    def __init__(self, account_balance=0):       
        self.account_balance = account_balance

    # Method deposit

    def deposit(self, amount):
        self.account_balance += amount

    # Method withdraw

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
        
    # Method display

    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")

