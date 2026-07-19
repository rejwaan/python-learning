#  Remove Negative Numbers

# Given the following list:

# numbers = [10, -5, 20, -8, 15, -2, 30]

# Task:
# Create a new list that contains only positive numbers and zero.
# Remove all negative numbers.

# Print both the original list and the new list.

# Expected Output:

# Original: [10, -5, 20, -8, 15, -2, 30]
# New: [10, 20, 15, 30]

# code --------------

numbers = [10, -5, 20, -8, 15, -2, 30]

positive_nums = []

for num in numbers:
    if num >= 0:
        positive_nums.append(num)
        
print("Original: ", numbers)
print("New: ", positive_nums)