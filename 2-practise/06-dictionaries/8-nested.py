# nested dictionaries

# one way
myfamily = {
    "child1": {
        "name":"Emil",
        "age": 24
    },
    "child2": {
        "name": "Shatomi",
        "age": 21
    },
    "child3": {
        "name": "Linus",
        "age": 20
    }
}

print(myfamily)

# access items..
print(myfamily["child2"]["name"])

# another way
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

member1 = {
    "name": "Shatomi"
}
member2 = {
    "name": "Ishihara"
}
member3 = {
    "name": "Linus"
}

all_members = {
    "member1" : member1,
    "member2" : member2,
    "member3" : member3
}

print(all_members)

# access items
print(all_members["member1"]["name"])