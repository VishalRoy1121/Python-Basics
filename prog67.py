# WAP to create a class called inventory with attributes like item_id, item_name, stock_count and price. Define suitable methods and constructors to perform the operations like add items, update items, check item details, etc.

class Inventory:
    def __init__(self, item_id, item_name, stock_count, price):
        self.item_id = item_id
        self.item_name = item_name
        self.stock_count = stock_count
        self.price = price

    def add_item(self, quantity):
        self.stock_count += quantity

    def update_item(self, new_name, new_price):
        self.item_name = new_name
        self.price = new_price

    def item_details(self):
        print(f"Item ID: {self.item_id}")
        print(f"Item Name: {self.item_name}")
        print(f"Stock Count: {self.stock_count}")
        print(f"Price: {self.price}")


item1 = Inventory(1, "Apple", 10, 1.50)

item1.add_item(5)
item1.update_item("Orange", 2.00)
item1.item_details()
