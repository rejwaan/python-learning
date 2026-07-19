# Count positive numbers

# Given the following list:

# numbers = [-5, 10, -2, 8, 0, 15, -7]

# Tasks:
# 1. Create a variable named count and initialize it to 0.
# 2. Use a for loop.
# 3. If a number is greater than 0, increase count by 1.
# 4. Print the total number of positive numbers.

# Expected Output:

# Positive numbers: 3

# Rules:
# - Use a for loop.
# - Use an if statement.
# - Use count += 1.
# - Do not use the count() method.


# code -------------

numbers = [-5, 10, -2, 8, 0, 15, -7]

count = 0

for num in numbers:
    if num > 0:
        count = count + 1

print("Positive numbers: ",count)