# WAP to define a function with an argument which can take n number of keyword arguments

def keyarg(**a):
    print(a)

keyarg(n1 = 1, n2 = 2, n3 = 4, n4 =6)