#10 WAP to generarte the following pattern -
#  1
#  23
#  456
#  78910
num=int(1)
for i in range(4):
    for j in range(i+1):
        print(num, end=' ')
        num += 1
    print()