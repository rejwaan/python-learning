# Separate Even and Odd Numbers

# Given the following list:

# numbers = [3, 8, 5, 12, 7, 20, 15, 18]

# Tasks:
# 1. Create two new lists:
#    - even_numbers
#    - odd_numbers
# 2. Using a single loop, separate the numbers into the correct list.
# 3. Print the original list, the even numbers list, and the odd numbers list.

# Expected Output:

# Original: [3, 8, 5, 12, 7, 20, 15, 18]
# Even: [8, 12, 20, 18]
# Odd: [3, 5, 7, 15]


# code ------------

numbers = [3, 8, 5, 12, 7, 20, 15, 18]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Original: ",numbers)
print("Even: ", even_numbers)
print("Odd: ", odd_numbers)