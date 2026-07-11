# update tuples

mytuple = ("apple", "banana", "mango")


# change tuple values
# tuple is unchangeable but there is a technic

mylist = list(mytuple)
mylist[0] = "cherry"
mytuple = tuple(mylist)

print(mytuple)


# Add items
# tuple are immutable and not have append() but there is a way:

mylist1 = list(mytuple)
mylist1.append("orange")
mytuple = tuple(mylist1)

print(mytuple)


# add tuple to a tuple
newt = ("lemon",)

mytuple += newt

print(mytuple)


# remove tuple items
# there is no in built way but there  is 

newlist2 = list(mytuple)
newlist2.remove("banana")
mytuple = tuple(newlist2)

print(mytuple)


# the del keyword can delete the tuple completely

atuple = (3,4,3,2,3,1)
del atuple
# print(atuple) NameError: name 'atuple' is not defined.