# Given the following list:

# numbers = [2, 4, 6, 8, 10]

# Tasks:
# 1. Create a new list.
# 2. Store each number multiplied by 2 in the new list.
# 3. Do not modify the original list.
# 4. Print both the original list and the new list.

# Expected Output:

# Original: [2, 4, 6, 8, 10]
# New: [4, 8, 12, 16, 20]

# Rules:
# - Use a for loop.
# - Use append().
# - Do not use list comprehension.
# - Do not modify the original list.


# code ---------------------

numbers = [2, 4, 6, 8, 10]

new_list = []

for x in numbers:
    new_list.append(x*2)
   

print("Original: ",numbers)

print("New: ",new_list)