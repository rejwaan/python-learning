# Sum All Numbers in a Tuple

# Given the following tuple:

# numbers = (10, 20, 30, 40, 50)

# Tasks:
# 1. Use a for loop to calculate the sum of all numbers.
# 2. Do not use the sum() function.
# 3. Print the total.

# Expected Output:

# Total: 150


# code -------------------------------

numbers = (10, 20, 30, 40, 50)

sum_of_numbers = 0

for num in numbers:
    sum_of_numbers += num

print("Total: ", sum_of_numbers)