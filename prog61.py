# WAP to create a class named bankaccount with attributes like account_no, balance, customer_name and methods like deposit, withdraw and check_balance and also print the values

class BankAccount:
    Cname = ""
    AccountNo = 0
    balance = 0

    def __init__(self, Cname, balance, AccountNo=101):
        self.Cname = Cname
        self.AccountNo = AccountNo
        self.balance = balance

    def deposit(self):
        x = float(input("Enter the amount you want to deposit"))
        self.balance += x
        print("Updated balance is : ", self.balance)

    def withdraw(self):
        x = float(input("Enter the amount you want to withdraw"))
        self.balance -= x
        print("Updated balance is : ", self.balance)

    def checkBalance(self):
        print("Current balance is : ", self.balance)

    def details(self):
        print("")


Acc = BankAccount("Harry", 500)
Acc.checkBalance()