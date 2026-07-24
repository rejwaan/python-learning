# Add and Remove Elements from a Set

# Given the following set:

# fruits = {"apple", "banana", "mango"}

# Tasks:
# 1. Add "orange" to the set.
# 2. Remove "banana" from the set.
# 3. Print the updated set.

# Expected Output:

# {'apple', 'mango', 'orange'}

# Note:
# Since sets are unordered, the order of elements in your output may be different. That is still correct.


# code --------------------------

fruits = {"apple", "banana", "mango"}

fruits.add("orange")
fruits.remove("banana")

print(fruits)