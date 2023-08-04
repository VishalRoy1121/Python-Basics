#WAP to create a class named student, with two instances student1 and student2, declare suitable data members, attributes and member functions to initialize and display the values of the attributes

class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No.:", self.roll_no)


student1 = Student("Amit", 20, "20051245")
student2 = Student("Mia", 19, "2005094")
student1.display()
print("")
student2.display()
