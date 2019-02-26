# bank account program to practice python classes and objects
# bank account class has a name attribute and functions to deposit, withdraw and show balance

class BankAccount:

    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "This account belongs to: %s. The balance is $%.2f" %(self.name, self.balance)
    
    def show_balance(self):
        print("Current balance: $%.2f" %(self.balance))

    def accept_deposit(self, amount):
        if(amount <= 0):
            print("Error: your deposit must be greater than $0")
            return
        else:
            print("Deposit amount: $%.2f" %(amount))
            self.balance += amount
            self.show_balance()

    def perform_withdraw(self, amount):
        if((amount <= 0) or (amount > self.balance)):
            print("Error: enter a valid withdrawal amount")
        else:
            print("Withdrawal Amount: $%.2f" %(amount))
            self.balance -= amount
            self.show_balance()

my_account = BankAccount("Keegan")
my_account.accept_deposit(2000)
my_account.perform_withdraw(1500)
my_account.perform_withdraw(900)

