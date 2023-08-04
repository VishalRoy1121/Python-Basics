# bank -> customer

class Bank:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def show_customers(self):
        print("Customers of {}:".format(self.name))
        for customer in self.customers:
            print(customer.name)

class Customer(Bank):
    def __init__(self, name, address, phone, account_number, balance):
        super().__init__(name, address, phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)

bank = Bank("SBI", "Mumbai", "855-688688")
customer1 = Customer("A", "Kolkata", "9824019189", "001", 1000)
customer2 = Customer("B", "Mumbai", "8917245622", "002", 500)

bank.add_customer(customer1)
bank.add_customer(customer2)

bank.show_customers()

customer1.display_balance()
customer2.display_balance()