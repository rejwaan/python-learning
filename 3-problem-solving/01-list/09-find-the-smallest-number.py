# Find the Smallest Number

# Given the following list:

# numbers = [45, 12, 78, 3, 56, 19]

# Tasks:
# 1. Find the smallest number in the list.
# 2. Use a variable named smallest.
# 3. Do not use min() or max().
# 4. Print the smallest number.

# Expected Output:

# Smallest number: 3


# code -------------

numbers = [45, 12, 78, 3, 56, 19]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number: ", smallest)