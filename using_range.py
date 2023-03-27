# the 'range' object is useful for ranges of values
r = range(-5, 6, 2) # start, stop-before, step
# use our range to populate a list
l = list(r) # make our range into a list
print(l)
# we can populate a structure at the same time as making a range
odd_l = list(range(1, 8, 2))
print(odd_l)

# it is legal to step BACKWARDS through a collection
s = 'is it time for lunch?'
#we can have defaults in a step [::]
print( s[::-1] ) # step -1 so it goes backwards through ANY indexed collection