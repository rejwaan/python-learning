# remove items

thisdict = {
    "name": "John",
    "age": 25,
    "department": "CSE",
    "color": "white",
    "Is_student": True
}


# pop() - removes the item with the specified key name
thisdict.pop("color")
print(thisdict)


# popitem()  - emoves the last inserted item
thisdict.popitem()
print(thisdict)


# del  - removes the item with the specified key name
del thisdict["department"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
# del thisdict

# clear() - empties the dictionary
thisdict.clear()
print(thisdict) # {}