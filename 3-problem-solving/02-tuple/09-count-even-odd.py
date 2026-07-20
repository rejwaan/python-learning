# Count Even and Odd Numbers

# Given the following tuple:

# numbers = (12, 7, 25, 18, 3, 40, 9, 16)

# Tasks:
# 1. Count how many even numbers are in the tuple.
# 2. Count how many odd numbers are in the tuple.
# 3. Print both counts.

# Expected Output:

# Even count: 4
# Odd count: 4


# code -----------------------------

numbers = (12, 7, 25, 18, 3, 40, 9, 16)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count: ", even_count)
print("Odd count: ", odd_count)