
name = input("Enter your name: ")

while name == "":
  print("You did not enter your name")
  name = input("Enter your name: ")

print(f"hello {name}")





# example 2

food = input("Enter a food name you like (q to quit): ")

while not food == "q":
  print(f"You like {food}")
  food = input("Enter another food name you like (q to quit): ")

print("bye")



#example 3

num = int(input("Enter a Number between 1 - 10: "))

while num < 1 or num > 10:
  print(f"your number {num} is not valid")
  num = int(input("Enter a Number between 1 - 10: "))

print(f"GREAT! Your number is {num}")
