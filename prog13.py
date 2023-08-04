# 6 WAP to check if the given number is perfect number or not.
a = int(input('enter a number: '))
sum = int(0)
values = range(a-1)
for i in values:
    if (a % (i+1) == 0):
        sum = sum+(i+1)
if (sum == a):
    print('number is perfect')
else:
    print('number is not perfect')