# WAP to create a class to implement pow(x, n)

class Pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def power(self):
        ans = self.x ** self.n
        return ans


num = float(input("Enter value of x: "))
exp = float(input("Enter value of n: "))
p = Pow(num, exp)
print("pow(x, n) is: ", p.power())