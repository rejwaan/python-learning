#  Access Tuple Elements

# Given the following tuple:

# fruits = ("apple", "banana", "mango", "orange")

# Tasks:
# 1. Print the second element.
# 2. Print the last element.
# 3. Print the total number of elements in the tuple.

# Expected Output:

# Second: banana
# Last: orange
# Length: 4


# code ------------

fruits = ("apple", "banana", "mango", "orange")

second_word = fruits[1]
last_word = fruits[-1] 
length = len(fruits)

print("Second: ",second_word)
print("Last: ",last_word)
print("Length: ",length)