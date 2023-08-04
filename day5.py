# lists

'''l = [2, 3, 4, 5, 9, 8, 7, 1]
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[-2])
print(l[1:6:2])  #jump index of 2
if 7 in l:
    print("Yes")
else:
    print("No")
print(l[1:-1])
'''

lst = [i*i for i in range(5)]
print(lst)
lst = [i*i for i in range(5) if i%2 == 0]
print(lst)