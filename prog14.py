# 7 WAP to check if the given number is armstrong number or not.
a = input('enter a number: ')
length = int(len(a))
last = int(0)
sum = int(0)
a = int(a)
temp=a
while (a > 0):
    last = a % 10
    sum = sum + pow(last, length)
    a = a//10
if (sum == temp):
    print('number is armstrong')
else:
    print('number is not armstrong')