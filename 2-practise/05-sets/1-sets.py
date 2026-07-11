# Pyhton sets
# set items are unchangeable.
# sets are unordered

myset = {"apple", "banana", "cherry"}
print(myset)


# duplicates not allowed
thisset = {"a", "b", "c", "a"}
print(thisset) # {'b', 'a', 'c'}

# true and 1
st = {True, 1}
print(st) # {True}

st2 = {0, False}
print(st2) # {0}


# len()
print(len(myset)) # 3

# type()
print(type(myset)) # <class 'set'>

# set() constructor to make a set
sets = set((2,4,5,6))
print(sets)