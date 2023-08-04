a = int(input('Enter a three digit number: '))
b = a % 10
c = (a//10) % 10
d = ((a//10)//10) % 10
sum = d+c*10+b*100
print(sum == a)