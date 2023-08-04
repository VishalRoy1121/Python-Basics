'''a = int(input("Enter age:"))
if a > 18:
    print("Drive crow")
else:
    print("Mat crow")

num = int(input())
if num >= 1:
    print("+")
elif num == 0:
    print("0")
else:
    print("-")


num = 18
if num < 0:
    print("Number is negative.")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif num > 10 and num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")



x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)


# for loop

name = 'Abhishek'
for i in name:
   print(i)
   if i =="b":
    print("This is something special!")


for i in range(1, 10, 2): #first arg is start, 2nd is end (not inclusive, 3rd is step value
    print(i)


# while loop

i = int(input("Enter the number: "))              #do while loop simulation
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")

count = 5
while (count > 0):
   print(count)
   count -= 1
else: # else can be used with while, enters else if the condition is not met
   print("I am inside else")


#do while loop

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break

# break continue

for i in range(12):
   if(i == 10):
     print("Skip the iteration")
     continue
   print("5 X", i, "=", 5 * i)

i = 0
while True:
    print(i)
    i = i + 1
    if (i % 5 == 0):
        break



# function

def calcAvg(a, b):
    avg = (a + b) / 2
    print(avg)
def isGreater(a, b):
    pass # ignore function def for now
c = 5
d = 6
calcAvg(c, d)
e = 7
f = 8
calcAvg(e, f)

# def sum(a = 5, b= 9) default argument
# sum(6) puts 6 in a, 9 in b
# sum(b = 6) puts 5 in a, 6 in b

# sum(b = 2, a = 3) keyword arguments, can change order

# def prod(a, b, c=1)  a, b are required arguments, otherwise error
'''
def average(*numbers):   # takes input in tuple
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  #print("Average is: ", sum / len(numbers))
  return sum / len(numbers)


c = average(4,5,6,7,8) #can be any amt of numbers
print(c)