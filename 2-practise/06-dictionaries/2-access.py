# Access dictionary items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
print(x)

# get() - same result..
y = thisdict.get("model")
print(y)


# keys()
z = thisdict.keys()
print(z)  # dict_keys(['brand', 'model', 'year'])

thisdict["color"] = "white"
print(z)



# values()
a = thisdict.values()
print(a)

thisdict["is_ready"] = True
print(a)


# items()
b = thisdict.items()
print(b)


# check if key exists

if "model" in thisdict:
    print("yes, 'model' exist")