# sort list

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["m", "r", "w", "c", "k", "t"]
thislist.sort()
print(thislist)

nums = [4,32,5,4,3,2,4,32,2,3,3]
nums.sort()
print(nums)

# sort descending
fruits = ["apple", "mango", "cherry", "blueberry"]
fruits.sort(reverse=True)
print(fruits)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# the solution is:

thelist = ["a", "K", "C", "r", "b"]
thelist.sort(key= str.lower)
print(thelist)


# reverse order

numberlist = [3,4,5,2,23,4,2,1,12,2]
numberlist.reverse()
print(numberlist)