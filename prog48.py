# WAP to convert a dictionary into list of lists

dic = {'a': 5, 'b': 10, 'c': 4, 'd': 4}
new_list = list()
for i in dic:
    new_list.append((i, dic[i]))
print("List: ", new_list)