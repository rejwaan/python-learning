# typecasting = the process of converting a variable from one date 
#                type to another str(), int(), float(), bool() .

name = ""
age = 25
gpa = 3.4
is_student = True


print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


# type cast

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(type(age))

name = bool(name)
print(name)