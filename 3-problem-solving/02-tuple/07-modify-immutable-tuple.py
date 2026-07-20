# Modify an Immutable Tuple

# Given the following tuple:

# colors = ("red", "green", "blue")

# Tasks:
# 1. Convert the tuple into a list.
# 2. Replace "green" with "yellow".
# 3. Convert the list back into a tuple.
# 4. Print the new tuple.

# Expected Output:

# ('red', 'yellow', 'blue')


# code -----------------------------

colors = ("red", "green", "blue")

color_list = list(colors)

color_list[1] = "yellow"

colors = tuple(color_list)

print(colors)