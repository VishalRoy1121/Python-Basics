#wap in python to initialize a three digit num and display reverse of it

a = 157
b = a%10
a = a//10
c = a%10
a = a//10
t = (100*b)+(10*c)+a
print("Reverse:\n")
print(t)