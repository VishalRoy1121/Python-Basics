# WAP to input 3 strings and try to delete one of the strings, also check the types of the strings and the address of the strings

a = input("Enter first string:")
b = input("Enter second string:")
c = input("Enter third string:")
del c
print(type(a), id(a))
print(type(b), id(b))
print(type(c), id(c))