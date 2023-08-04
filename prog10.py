c = []
for i in range(4):
    a = int(input("ENTER mark :"))
    c.append(a)

mark = 0
for i in c:
    mark = mark+i

per = (mark/400)*100

print("total mark : ", mark)
print("percentage : ", per)

grade = 'no grade'
if per >= 90:
    grade = 'o'
elif per >= 80 and per < 90:
    grade = 'e'
elif per >= 70 and per < 80:
    grade = 'a'
elif per >= 60 and per < 70:
    grade = 'b'
elif per >= 50 and per < 60:
    grade = 'c'
elif per >= 40 and per < 50:
    grade = 'd'
else:
    grade = 'fail'

print("grade = ", grade)