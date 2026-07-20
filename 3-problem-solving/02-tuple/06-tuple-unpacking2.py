# Tuple Unpacking with *

# Given the following tuple:

# fruits = ("apple", "banana", "mango", "orange", "grape")

# Tasks:
# 1. Unpack the tuple so that:
#    - first contains the first element.
#    - middle contains all the middle elements as a list.
#    - last contains the last element.
# 2. Print all three variables.

# Expected Output:

# First: apple
# Middle: ['banana', 'mango', 'orange']
# Last: grape


# code ------------------------------------

fruits = ("apple", "banana", "mango", "orange", "grape")

first, *middle, last = fruits

print("First: ", first)
print("Middle: ", middle)
print("Last: ", last)