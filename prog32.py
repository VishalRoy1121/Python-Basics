# WAP to change the position of every nth element with n + 1 th element

a = [2, 4, 6, 8, 10, 12, 14]
n = len(a)
if n % 2 == 1:
    n -= 1
for i in range(0, n, 2):
    t = a[i]
    a[i] = a[i+1]
    a[i+1] = t
print("New list:",a)