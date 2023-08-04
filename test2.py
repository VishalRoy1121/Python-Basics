number = int(input("Enter a 3 digit number: "))
digit_list = []
for i in range(3):
    digit = number % 10
    digit_list.insert(0, digit)
    number = number // 10

print((100*digit_list[0])+(10*digit_list[1])+digit_list[2])
print((100*digit_list[1])+(10*digit_list[0])+digit_list[2])
print((100*digit_list[2])+(10*digit_list[1])+digit_list[0])