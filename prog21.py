# WAP to check if the given string is a palindrome or not

a = input("Enter a string:")
count = 0
for i in a:
    count += 1
l = count//2
count -= 1
f = 0
for i in range(0,l):
    if a[i] == a[count]:
        count -= 1
        continue
    else:
        print("Not a palindrome")
        f += 1
        break
if f == 0:
        print("Palindrome")
