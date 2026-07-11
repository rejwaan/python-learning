# access tuple

mytuple = ("apple", "banana", "mango")

print(mytuple[1])


# negative indexing..
print(mytuple[-1])

# range of indexes...
print(mytuple[1:3])

print(mytuple[:2])

print(mytuple[1:])

# range of negative indexes...
print(mytuple[-3:-1])


# check if item exists...

if "apple" in mytuple:
    print("Yes, 'apple' is in the mytuple")