# list comprehension

# example: without list comprehension

numbers = []

for i in range(1, 10):
    numbers.append(i)
print(numbers)

# with list comprehension...

nums = [i for i in range(1, 10)]
print(nums)

#example - convert to lowercase
names = ['APPLE', 'MANGO', 'BANANA']

new_names = [name.lower() for name in names]
print(new_names)


#example- even numbers

evennums = [i for i in range(1, 21) if i%2 == 0]
print(evennums)