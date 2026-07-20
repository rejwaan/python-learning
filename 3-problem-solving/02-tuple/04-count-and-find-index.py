#  Count and Find Index

# Given the following tuple:

# fruits = ("apple", "banana", "mango", "banana", "orange", "banana")

# Tasks:
# 1. Find how many times "banana" appears.
# 2. Find the index of the first occurrence of "mango".
# 3. Print both results.

# Expected Output:

# Banana count: 3
# Mango index: 2

# code --------------------

fruits = ("apple", "banana", "mango", "banana", "orange", "banana")

count_banana = fruits.count("banana")
index_mango = fruits.index("mango")

print("Banana count: ", count_banana)
print("Mango index: ", index_mango)