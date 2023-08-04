#8 WAP to genetrate fibonacci series upto n terms.
a=int(0)
b=int(1)
n=int(input('enter n terms: '))
print(a,end=' '), print(b, end=' ')
for i in range(n):
    sum=a+b
    print(sum, end=' ')
    a=b
    b=sum