# Access set items
# we cannot access items in a set by an index or key.
# but we can use "for" and "in" 

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# check if
print("banana" in thisset) # True

# if not
print("banana" not in thisset) # False
