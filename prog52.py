# WAP to generate a multiplication table of any number using lambda function

mul = lambda n, c: n * c
num = int(input("Enter value: "))
for i in range(1, 11):
    print(num, "*", i, "=", mul(num, i))