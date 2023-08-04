# WAP to check if an instance belongs to a particular class or not, or if it is a subclass of a particular class or not

class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


my_dog = Dog()
my_cat = Cat()
print(isinstance(my_dog, Dog))
print(isinstance(my_cat, Dog))

print(issubclass(Dog, Animal))
print(issubclass(Cat, Animal))
print(issubclass(Animal, Dog))
