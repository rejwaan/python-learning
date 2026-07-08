# remove list items

thislist = ["apple", "banana", "cherry"]

# remove()
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurrence


# pop()
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item

#....................
thislist[1:]=("orange", "lemon", "mango")
print(thislist)
#.....................


# del()
del thislist[1]
print(thislist)

# The del keyword can also delete the list completely.
# del thislist (example)


# clear()
thislist.clear()
print(thislist)  # []