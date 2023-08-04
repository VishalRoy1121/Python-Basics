'''# typecasting
a = "1"
b = "2"
print(a+b)
print(int(a)+int(b))
c = 1.8
d = 4
print(c+d)

# user input (by default input is string

e = input("Enter name: ")
print("Name: ", e)
f = (input("Enter num1: "))
g = (input("Enter num2: "))
print(f+g)
print(int(f)+int(g))

# string

ms = """This is a
multiline
string"""
print(ms)
h = "w ut"
print(h[0])
print(h[1])
print(h[2])
for character in h:
    print(character, end=" ")

# slicing
g = "What the hell is going on"
gl = len(g)
print(gl)
print(g[:5])  # start value automatically 0, end value length
print(g[0:-3])
print(g[-5:-1]) '''


# string methods

j = "!!! hElLo !!!"  # string is immutable (cannot be changed)
print(j)
print(j.upper())
print(j.lower())
print(j.rstrip("!"))  # only removes from the end
print(j.replace("HeLlO", "Wow"))  # replaces all occurrences
print(j.split(" "))  # splits string into list
k = "Hello beaches"
print(k.capitalize())
print(k.center(25))
print(k.count("e"))
print(k.endswith("es"))
print(k.endswith("o", 1, 5))
print(k.find("ea"))  # finds first occurrence, returns -1 if not found
print(k.index("ea"))  # same as find but it returns error if not found
print(k.isalnum())
print(k.isalpha())
print(k.islower())
print(k.isprintable())  # returns false if \n, \t etc etc exits
print(k.isspace())
print(k.istitle())  # checks if first alpha is cap or not
print(k.swapcase())
print(k.title())  # changes all word first letter to cap