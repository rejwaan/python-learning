# Double Only Even Numbers

# Given the following list:

# numbers = [5, 8, 11, 14, 17, 20]

# Tasks:
# 1. Create a new list.
# 2. Store only the even numbers in the new list.
# 3. Before storing, multiply each even number by 2.
# 4. Do not modify the original list.
# 5. Print both the original list and the new list.

# Expected Output:

# Original: [5, 8, 11, 14, 17, 20]
# New: [16, 28, 40]

# Rules:
# - Use a for loop.
# - Use an if statement.
# - Use append().
# - Do not use list comprehension.
# - Do not modify the original list.


# code ---------------

numbers = [5, 8, 11, 14, 17, 20]

new_nums = []

for num in numbers:
    if num % 2 == 0:
        new_nums.append(num*2)

print("Original: ", numbers)
print("New: ", new_nums)