# WAP to calculate the simple interest on a given PTR using a function which takes default value for R

def interest(prin, time, rate = 5):
    si = (prin * rate * time) / 100
    print("Simple Interest: ", si)

p = float(input("Enter value of P: "))
t = float(input("Enter value of T: "))
interest(p, t)