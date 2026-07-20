# Find the Largest and Smallest Number in a Tuple

# Given the following tuple:

# numbers = (12, 45, 7, 89, 23, 67, 5)

# Tasks:
# 1. Find the largest number.
# 2. Find the smallest number.

# Rules:
# - Do not use max().
# - Do not use min().
# - Do not convert the tuple into a list.
# - Use a single for loop if possible.

# Expected Output:

# Largest: 89
# Smallest: 5


# code ---------------------------------

numbers = (12, 45, 7, 89, 23, 67, 5)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest: ", largest)
print("Smallest: ", smallest)
     