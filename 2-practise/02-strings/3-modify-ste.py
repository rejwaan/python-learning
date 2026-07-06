#modify strings

a = "Hello world"

#uppercase
print(a.upper()) #HELLO WORLD

#lowercase
print(a.lower())

#strip - remove white space from end or start.
print(a.strip())

#replace
print(a.replace("H", "N")) #Nello world

#split
b = "Hello, world"
print(b.split(",")) #['Hello', ' world']


#Concatenation strings

x = "Hello"
y = "World"
c = x+y
print(c) #HelloWorld


#F-String

age = 34
txt = f"My name is x, and I am {age}"
print(txt)

sum = f"the sum is {30+32}"
print(sum)


#Escape charecter example

text = "We are \"Hero\" in hour village"
print(text)