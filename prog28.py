# WAP to get the second smallest and second largest element of a list

l1 = [2, 5, 7, 8, 1, 9]
ss = float('inf')
sl = float('-inf')
sml = float('inf')
lrg = float('-inf')
for num in l1:
    if num < sml:
        ss = sml
        sml = num
    elif num < ss:
        ss = num

    if num > lrg:
        sl = lrg
        lrg = num
    elif num > sl:
        sl = num
print("2nd smallest element: ", ss)
print("2nd largest element: ", sl)