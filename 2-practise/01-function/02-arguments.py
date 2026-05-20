# example 1

def my_func(name):  # parameter
    print("Hello",name)

my_func("rejo")   # argument
my_func("bro")    # argument


# example 2

def func(a, b):
    print(a, b)

# func(3) type error
func(4, 5)


# default parameter

def new(a = 30, b = "name"):
    print(a, b)
new()