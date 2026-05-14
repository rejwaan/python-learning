# python weight converter

weight = float(input("Enter weight in kg or pounds: "))

unit = input ("pounds or kg (p/k): ")

if unit == "p":
    converted = weight * 0.45
    print(f"{weight} pounds is {converted} kg")
elif unit == "k":
    converted = weight / 0.45
    print(f"{weight} kg is {converted} pounds")
else:
     print("Invalid unit")  