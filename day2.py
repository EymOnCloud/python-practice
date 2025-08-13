students_count = 10
rating = 4.99
is_published = True
print(students_count)

course_name = "Python Programming"
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[1:])
print(course_name[:])

course = "  Python Programming"
print(course.center(80))
print(course.replace("m", "T"))
print(course.strip())
print(course.find("Pro"))
print("pro" in course)
print("Pro" in course)
print("hotdogs" not in course)


hotdogs = """

Tender \nJuicy hotdogs
with a side of ketchup and mayo
"""
print(hotdogs)

first = "Eimiel"
last = "Lantion"
full = first + "" + last
print(full)
fullname = f"{len(first)} {2+2}"
print(fullname)
myname = f"{first} {last}"
print(myname)

x = 1
x = 1.1
x = 1 + 2j # a +bi

print(10 + 3)
print(6 - 2)
print(5 * 2)
print(10 / 5)
print(10 // 3)
print(10 % 4)
print(10 ** 4) 

x = 10
x = x + 3
x += 3

print(round(26.2))
print(abs(-20))

import math

print(math.ceil(60.9))



# int(x)
# float(x)
# bool(x)
# str(x)

size = 57
if size > 58:
    print("big ahh")
    print("anlaki")
elif size > 54:
    print("small ahh")
    print("liit")
print("engk")

age = 12
if age >= 18:
     message = "adult"
else:
     message = "minor"
print(message)

message = "adult" if age >= 18 else "minor" 
print(message)

pogi = True
matalino = True

if pogi and matalino:
    print("10/10")
else:
    print("0/10")

sizee = True
performance = False

if (sizee or performance) and not pogi:
    print("10/10")
else:
    print("0/10")