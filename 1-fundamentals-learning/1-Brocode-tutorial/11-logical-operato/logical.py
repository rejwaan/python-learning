# or = at least one condition must be true
# and = both conditions must be true
# not = inverts the condition (not false, not true)

temp = -60
is_raining = False

# if temp > 43 or temp < 0:
#   print("outdoor is dengarous")

# else:
#   print("You can go outside")

# -------------------------------------

# if temp > 43 or is_raining:
#   print("outdoor is dengarous")

# else:
#   print("You can go outside")



# and
roll = 144

if roll > 1 and roll < 10:
  print("He is a good student")

elif roll > 100 and roll < 200:
  print("bad boy")

#---------------------------------
num = 5

if not num > 10:
    print("Number is 10 or smaller")