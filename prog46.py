# WAP to sort the dictionary by key

dic = {'b': 10, 'a': 5, 'd': 4, 'c': 2}
s_dic = {}
for i in sorted(dic):
    s_dic[i] = dic[i]
print("Sorted dictionary: ", s_dic)
