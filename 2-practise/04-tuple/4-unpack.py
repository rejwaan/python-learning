# unpack tuples

# this is packing..
# fruits = ("apple", "banana", "cherry")

# now unpacking....

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) # apple
print(yellow) # banana
print(red) # cherry

# note: variable number should be equal to values


# using Asterisk (*)

newfruits =  ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = newfruits

print(green)
print(yellow)
print(red) # ['cherry', 'strawberry', 'raspberry']


newfruits2 =  ("apple", "banana","orange","Mango", "cherry")

(green, *yellow, red) = newfruits2

print(green)
print(yellow) # ['banana', 'orange', 'Mango']
print(red)