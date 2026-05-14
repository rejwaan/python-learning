# Python calculator

operator = input("Enter operator (+, -, *, /): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = round(num1 / num2, 2)
    else:
        result = "Error: Division by zero"

else:
    result = "Error: Invalid operator"

print("Result:", result)