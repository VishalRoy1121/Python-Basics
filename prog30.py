# WAP to find out the index of an element in a specified list

l1 = [9, 8, 2, 6, 5, 7, 4, 1]
a = int(input("Enter element you want to find: "))

for i in range(len(l1)):
    if l1[i] == a:
        index = i
        break
    else:
        index = -1
if index >= 0:
    print("Index: ", index)
else:
    print("Element not in list")