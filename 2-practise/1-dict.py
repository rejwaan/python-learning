# Python dictionaries

thisdict = {
#    key: value

    "brand": "xiaomi",
    "model": "xiaomi 11i",
    "price": 30000
}

print(thisdict)

print(thisdict["model"])
print(thisdict.get("price"))

# duplicates are not allowed

print(len(thisdict)) # 3

# we can put set tuple list data types in dictionaries

dicts = {
    "number": [1, 2, 3],
    "color": ("red", "blue"),
    "value": {True, False, 3}
}

print(dicts)
print(dicts.get("color"))

print(type(dicts))


# dict() constructor...
newdict = dict(name = "Jhon", age = 30)
print(newdict)