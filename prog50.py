# WAP to pass a list to a function, now function adds 3 to each and every element of the list and print the updated list inside the function call

def listadd(a):
    new_list = list()
    for i in a:
        new_list.append(i + 3)
    print(new_list)

l1 = [2, 4, 6, 8, 10]
listadd(l1)