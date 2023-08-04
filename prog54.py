'''class person:
    def __init__(self, name):
        self.name = name
    def myname(self):
        print("Name: ", self.name)
p = person("Calx")
p.myname()'''


# WAP to create a class named circle, with attributes radius and two methods that will compute the area and perimeter of the circle

class Circle:
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return 3.14 * self.rad ** 2

    def perim(self):
        return 2 * 3.14 * self.rad


c = Circle(5)
print("Area of the circle:", c.area())
print("Perimeter of the circle:", c.perim())