# loop 

thisdict = {
    "name": "John",
    "age": 25,
    "department": "CSE",
    "color": "white",
    "Is_student": True
}

for x in thisdict:
    print(x) # print keys

for i in thisdict:
    print(thisdict[i]) # print values


# values()
for x in thisdict.values():
    print(x)


# items( - loop both keys and values
for x, y in thisdict.items():
    print(x, y)