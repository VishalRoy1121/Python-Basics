a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))
e = int(input("Enter 5th number: "))
if (a > b and a > c and a > d and a > e):
 print(a, ' is greatest')
if (b > a and b > c and b > d and b > e):
 print(b, ' is greatest')
if (c > b and c > a and c > d and c > e):
 print(c, ' is greatest')
if (d > b and d > c and d > a and d > e):
 print(d, ' is greatest')
if (e > b and e > c and e > d and e > a):
 print(e, ' is greatest')