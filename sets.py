# create am empty set

s = set()
# add items to the set
s.add(1)
s.add(2)
s.add(3)
s.add(2)  # adding a duplicate item does not change the set
print(s)
# remove an item from the set
s.remove(2)
print(s)
# calculate the length of elements in the set
print(len(s))