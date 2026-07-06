# Must know 
# lower()
# upper()
# strip()
# split()
# join()
# replace()
# find()
# startswith()
# endswith()
# count()
#.................................

a = "Hello world"

# lower()
print(a.lower())

# upper()
print(a.upper())

#strip()
print(a.strip())

#split()
print(a.split()) # ['Hello', 'world']

#join()
fruits = ["apple", "banana", "mango"]
print(", ".join(fruits)) # apple, banana, mango

#replace()
print(a.replace("Hello", "Hi")) # Hi world

#find()
print(a.find("o")) #4

#startswith()
print(a.startswith("Hel")) #True

#endswith()
print(a.endswith("wow")) #False

#count()
print(a.count("l")) #3
print(a.count("o")) #2