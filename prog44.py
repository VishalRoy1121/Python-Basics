# WAP to multiply all elements present in a dictionary

dic = {1: 5, 2: 10, 3: 4, 4: 2}
prod = 1
for i in dic:
    prod *= dic[i]
print(prod)
