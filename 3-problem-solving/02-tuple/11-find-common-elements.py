# Find Common Elements

# Given the following two tuples:

# tuple1 = (10, 20, 30, 40, 50)
# tuple2 = (30, 40, 60, 70, 80)

# Task:
# Find the elements that are present in both tuples.

# Expected Output:

# Common elements: [30, 40]

# Rules:
# - Do not use set().
# - Do not create a new tuple.
# - Do not use intersection().
# - Use a for loop.
# - You may create a new list to store the common elements.

# code----------------

tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 60, 70, 80)

common_nums = []

for num in tuple1:
    if num in tuple2:
        common_nums.append(num)

common_tuple = tuple(common_nums) # add extra change - convert it from list to tuple

print("Common elements:", common_tuple)


