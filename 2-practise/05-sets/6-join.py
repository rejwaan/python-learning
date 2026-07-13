# join sets

# union()

set1 = {1,2,3}
set2 = {4,5,6}

set3 = set1.union(set2)
print(set3)

# | operator
setx = {7,8}
sety = {9, 10}

setz = setx | sety
print(setz)


# Join multiple sets
allset = set1.union(set2, setx, sety)
print(allset)

# Using | operator
allset2 = set1 | set2 | setx | sety
print(allset2)



# Join a set and a tuple
x = {1,2}
y = (3,4)
z = x.union(y)
print(z)


# update()
newset1 = {1,3,5}
newset2 = {7,9}

newset1.update(newset2)
print(newset1)


# intersection() - keep only the duplicates

aset = {1,2,3}
bset = {3,4,5}

cset = aset.intersection(bset)
print(cset) # {3}

# the & - same as intersection()
cset2 = aset & bset
print(cset2)

# intersection_update() - 
aset.intersection_update(bset)
print(aset)


# .........................................

# difference()

thisset1 = {1,2,3}
thisset2 = {3,4,5}

thissetend = thisset1.difference(thisset2)
print(thissetend) # {1, 2}


# the (-) operator insted of difference()
thissetend2 = thisset1 - thisset2
print(thissetend2) # {1, 2}

# difference_update() ----***


# symmentric_difference()

theset1 = {1, 2, 3}
theset2 = {3, 4, 5}

thesetend = theset1.symmetric_difference(theset2)
print(thesetend) #{1, 2, 4, 5}

# the (^) operator - same as symmetric_diff...
thesetend2 = theset1 ^ theset2
print(thesetend2)

# also we have - symmetric_difference_update()...