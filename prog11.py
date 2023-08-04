# 4 Solve Q3 using switch case.
a = int(input("enter marks in english: "))
b = int(input("enter marks in maths: "))
c = int(input("enter marks in hindi: "))
d = int(input("enter marks in physics: "))
total = a+b+c+d
print("total marks is ", total, '/ 400')
per = (total/400)*100
gpa = per//10
print("your percentage is ", per)
match gpa:
    case 10:
        print('your grade is: O')
    case 9:
        print('your grade is: E')
    case 8:
        print('your grade is: A')
    case 7:
        print('your grade is: B')
    case 6:
        print('your grade is: C')
    case 5:
        print('your grade is: D')
    case 4:
        print('your grade is: E')
    case default:
        print('FAIL')