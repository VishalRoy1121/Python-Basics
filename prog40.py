# WAP to check if any common element is present in two sets or not.

a = {1, 2, 4, 7, 11}
b = {11, 12, 14, 17,}

if a.intersection(b):
    print("Common elements are present")
else:
    print("Common elements are not present")