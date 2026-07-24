# Find Positive Numbers and Their Average

# Given the following tuple:

# numbers = (10, -5, 20, -8, 15, -2, 30)

# Tasks:
# 1. Store all positive numbers in a new list.
# 2. Calculate the total sum of the positive numbers.
# 3. Calculate the average of the positive numbers.
# 4. Print all three results.

# Expected Output:

# Positive numbers: [10, 20, 15, 30]
# Sum: 75
# Average: 18.75

# Rules:
# - Do not use sum().
# - Do not use max() or min().
# - Do not use filter().
# - Use a single for loop.
# - You may create a new list.
# - Calculate the average using the sum / count logic.



# code --------------

numbers = (10, -5, 20, -8, 15, -2, 30)

positive_numbers = []
total = 0
average = 0

for num in numbers:
    if num > 0:
        positive_numbers.append(num)
        total += num

        length = len(positive_numbers)
        average = total / length

print("Positive numbers: ", positive_numbers)
print("Sum: ", total)
print("Average: ", average)


