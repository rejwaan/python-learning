# change list items

thislist = ["apple", "banana", "cherry"]

thislist[0] = "Mango"
print(thislist) # change from apple to Mango

# change a range of item values
thislist[1:3] = ["green", "red"]
print(thislist) # ['Mango', 'green', 'red']

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly


# insert items
thislist.insert(2, "melon")
print(thislist)

# thislist.insert(True, "melon")  - index 1
# thislist.insert(False, "melon")  - index 0

print(len(thislist)) #4