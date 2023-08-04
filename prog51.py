# WAP to pass a number to a function, then print 1 2 3 ... upto n using recursion

def printn(n):
    if n > 0:
        printn(n-1)
        print(n, end=' ')

num = int(input("Enter value: "))
printn(num)