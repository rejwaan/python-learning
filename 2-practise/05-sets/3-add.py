# add set items

# we cannot change sets items but we can add new items.

# example

thisset = {"a", "b", "c"}
thisset.add("d")
print(thisset)


# update()
newsets = {2,3,4}

thisset.update(newsets)

print(thisset)


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# example. 
mylist = [True, False]

thisset.update(mylist)

print(thisset)