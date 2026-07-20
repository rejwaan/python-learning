# Count and Sum Positive Numbers

# Given the following tuple:

# numbers = (10, -5, 20, -8, 15, -2, 30)

# Tasks:
# 1. Count the positive numbers.
# 2. Calculate the sum of all positive numbers.
# 3. Use only one for loop.
# 4. Print both results.

# Expected Output:

# Positive count: 4
# Positive sum: 75


# code --------------------------

numbers = (10, -5, 20, -8, 15, -2, 30)

count_positve = 0
sum_positive = 0

for num in numbers:
    if num > 0:
        count_positve += 1
        sum_positive += num

print("Positive count: ", count_positve)
print("Positive sum: ", sum_positive)
