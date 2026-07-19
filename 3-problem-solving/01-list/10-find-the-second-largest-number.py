# Find the Second Largest Number

# Given the following list:

# numbers = [12, 45, 7, 89, 23, 67]

# Task:
# Find the second largest number in the list.

# Expected Output:

# Second largest number: 67

# Rules:
# - Do not use sort().
# - Do not use max() or min().
# - Do not create a new list.
# - Use a for loop.
# - Solve it using logic.


# code --------------------

numbers = [12, 45, 7, 89, 23, 67]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    
    elif largest > num > second_largest:
        second_largest = num
        

print("Second largest number: ",second_largest)
