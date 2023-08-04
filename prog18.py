# WAP to print the following number series n n-2 n-4 ...

a = int(input("Enter value of n:"))
for i in range(a, 0, -2):
    print(i, end=" ")

