#5 WAP to enter a number from the keyboard and find out reverse of each.
a = int(input('enter a three digit number: '))
b = a % 10
c = (a//10) % 10
d = ((a//10)//10) % 10
sum = d+c*10+b*100
print(b)
print(c)
print(d)
print(sum)