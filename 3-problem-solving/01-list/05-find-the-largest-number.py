# Find the Largest Number

# numbers = [12, 45, 7, 89, 23, 67]

# Tasks:
# 1. Create a variable named largest.
# 2. Initialize it with the first element of the list.
# 3. Use a for loop to iterate through the list.
# 4. If a number is greater than largest, update largest.
# 5. Print the largest number.

# Expected Output:

# Largest number: 89

# Rules:
# - Use a for loop.
# - Use an if statement.
# - Do not use max().


# code -- ---- - -

numbers = [12, 45, 7, 89, 23, 67]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number: ", largest)