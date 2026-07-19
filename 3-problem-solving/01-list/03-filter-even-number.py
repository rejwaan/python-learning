# Filter even numbers

# Given the following list:

# numbers = [3, 8, 5, 12, 7, 20]

# Tasks:
# 1. Create a new list.
# 2. Store only the even numbers in the new list.
# 3. Do not modify the original list.
# 4. Print both the original list and the new list.

# Expected Output:

# Original: [3, 8, 5, 12, 7, 20]
# Even: [8, 12, 20]

# Rules:
# - Use a for loop.
# - Use an if statement.
# - Use append().
# - Do not use list comprehension.


# code -------

numbers = [3, 8, 5, 12, 7, 20]

new_even_numbers = []

for num in numbers:
    if num % 2 == 0:
        new_even_numbers.append(num)

print("Original: ", numbers)
print("Even: ", new_even_numbers)