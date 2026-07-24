# Find Set Length and Loop Through Elements

# Given the following set:

# numbers = {10, 20, 30, 40, 50}

# Tasks:
# 1. Find the total number of elements in the set.
# 2. Use a for loop to print each element in the set.
# 3. Print "Number:" before each element.

# Expected Output Format:

# Length: 5
# Number: 10
# Number: 20
# Number: 30
# Number: 40
# Number: 50

# Note:
# Since sets are unordered, the order of the numbers may be different.


# code-----------------------

numbers = {10, 20, 30, 40, 50}

print("Length: ",len(numbers))

for num in numbers:
    print("Number: ", num)
