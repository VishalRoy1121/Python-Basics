# WAP to input a string and display reverse of it

a = input("Enter a string:")
for i in range(len(a)-1, -1, -1):
    print(a[i], end="")