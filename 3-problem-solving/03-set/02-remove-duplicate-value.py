# Remove Duplicate Values

# Given the following list:

# numbers = [10, 20, 10, 30, 20, 40, 30, 50]

# Tasks:
# 1. Remove all duplicate values from the list.
# 2. Store the result as a set.
# 3. Print the set.

# Expected Result:

# {10, 20, 30, 40, 50}

# Note:
# Since sets are unordered, the order of elements in the output may be different.


# code ----------------------------------

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

set_numbers = set(numbers)

print(set_numbers)