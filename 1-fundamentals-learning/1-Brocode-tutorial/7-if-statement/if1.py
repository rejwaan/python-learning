# if = do some code if some condition is true
#      else do someting else

age = int(input("Enter your age: "))

if age > 60:
    print("You are a senior citizen")

elif age >= 18:
    print("You are an adult")

elif 0 <= age <= 2:
    print("You are a baby")

elif age < 0:
    print("You haven't been born yet")

else:
    print("You are a child")