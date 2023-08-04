# WAP to merge two dictionaries

a = {'a': 1, 'b': 2, 'c': 4}
b = {'d': 5, 'e': 6, 'f': 7}

for i in b:
    a[i] = b[i]
print(a)