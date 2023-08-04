# WAP to check if an entered value is present in the set or not.

a = {1, 2, 4, 7, 11}
b = int(input("Enter a value:"))
if b in a:
    print("Element is present")
else:
    print("Element is not present")

#count = 0
#for i in a:
#    if i == b:
#        count += 1
#        break
#if count > 0:
#    print("Element is present")
#else:
#    print("Element is not present")