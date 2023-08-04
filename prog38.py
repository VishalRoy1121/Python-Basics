# WAP to check the frequency of a specific element within a tuple

a = (1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7)
b = int(input("Enter a number "))
count = 0
for i in a:
    if i == b:
        count = count + 1
print(count)