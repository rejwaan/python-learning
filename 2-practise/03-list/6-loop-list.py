# loop list

# using for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# using range() and len()
newlist = ["apple", "banana", "cherry"]
for i in range(len(newlist)):
    print(newlist[i])


# using while loop 
# looping using list comprehension


# create list using for loop................

# example
#even numbers
even = []
for i in range(1, 20):
    if i%2 == 0:
        even.append(i)
print(even)

# 1 - copy
numbers = [1, 2, 3, 4]

new_list = []

for num in numbers:
    new_list.append(num)
print(new_list)


# 2 - modify

numberlist = [1, 2, 3, 4, 5]

square = []

for n in numberlist:
    square.append(n*n)
print(square)


# 3 - filter - condition

nums = [1, 3, 4,54,234,42,35,2,2,11,33,454,3]

even = []

for e in nums:
    if e % 2 == 0:
        even.append(e)
print(even)