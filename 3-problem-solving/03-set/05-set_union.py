# Combine Two Sets
#
# Given the following two sets:
#
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
#
# Task:
# Create a new set containing all unique elements
# from both sets.
#
# Expected Result:
#
# {10, 20, 30, 40, 50, 60}
#
# Note:
# Since sets are unordered, the order of elements
# in the output may be different.


# code-----------------------

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

new_set = set1.union(set2)

print(new_set)