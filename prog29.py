# WAP to remove all duplicates from a list

l1 = [1, 4, 6, 9, 4, 6, 1, 8, 7, 8]
new_list = []
for num in l1:
    if num not in new_list:
        new_list.append(num)
print(new_list)