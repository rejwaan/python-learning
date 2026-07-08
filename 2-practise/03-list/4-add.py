# add list items

thislist = ["apple", "mango", "cherry", "orange"]

# append()
thislist.append("watermelon")
print(thislist) #add watermelon


# extend()
anotherlist = ["tomato", "potato"]

thislist.extend(anotherlist)
print(thislist)

# add any iterable
thistouple = ("burger", "pizza")

thislist.extend(thistouple)
print(thislist)