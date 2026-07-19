# Given the following list:
# numbers = [10, 20, 30, 40, 50]
#
# Tasks:
# 1. Add 60 to the end of the list.
# 2. Insert 25 at index 2.
# 3. Remove the value 40 from the list.
# 4. Print the length of the list.
# 5. Print the final list.
#
# Expected Output:
# Length: 6
# [10, 20, 25, 30, 50, 60]
#
# Rules:
# - Do not use a for loop.
# - Use only essential list methods.


# code ------

numbers = [10, 20, 30, 40, 50]

numbers.append(60)

numbers.insert(2, 25)

numbers.remove(40)

print("length:", len(numbers))
print(numbers)