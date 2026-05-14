unit = input("Is this temperature in celsius or fahrenheit (C/F): ")

temp = float(input("Enter the temperature: "))

if unit == "C":
  fn = round((9 * temp) / 5 + 32, 1)
  print(f"from celsius {temp} is {fn}F")

elif unit == "F":
  cl = round((temp - 32) * 5/9, 1)
  print(f"from Fahrenheit {temp} is {cl}C")

else:
  print(f"{unit} is Invalid Input")