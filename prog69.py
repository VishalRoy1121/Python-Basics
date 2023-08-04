# WAP in python with OOP concept to implememnt a user defined stack data structure then demonstarte the push and pop method with a set of elements.(without pre-defined functions)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())  # Output: 3
print(my_stack.pop())  # Output: 2
print(my_stack.pop())  # Output: 1
print(my_stack.pop())  # Output: None