def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def swapprimes(lst):
    for i in range(len(lst)-1):
        if is_prime(lst[i]) and is_prime(lst[i+1]):
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

A = list(map(int, input("Enter the elements of list A separated by spaces: ").split()))
B = list(map(int, input("Enter the elements of list B separated by spaces: ").split()))

C = []
for i in range(len(A)):
    C.append(A[i] ** B[i])

print("New List :", C)
print("Updated List: ", swapprimes(C))
