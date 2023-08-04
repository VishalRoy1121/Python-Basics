# WAP to that finds all pairs of elements in a list whose sum is equal to a given value.

a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = int(input("Enter sum: "))
pair = set()
for x in a:
    for y in a:
        if x + y == b and x != y:
            pair.add((x, y))
print("The pairs are: ", pair)

