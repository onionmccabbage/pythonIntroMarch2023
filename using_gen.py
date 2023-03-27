# sometimes we need a lot of values
# e.g. we can create a large quantity of numbers
num_l = [ num for num in range(0, 10000, 5) ] # all these values exist in the list in memory
print(num_l)

# we can do something similar without persisting the values in memory
num_g = ( num for num in range(0, 10000, 5) ) 
print(type(num_g)) # this is a generator object
# we can access each member of the generator in sequence
print( num_g.__next__() ) # 0
print( num_g.__next__() ) # 5
print( num_g.__next__() ) # 10

# here's a realistic example
odd_g = (num for num in range(0, 18) if num%2 == 1) # or range(1, 100000, 2)
print( odd_g.__next__() ) # 1
print( odd_g.__next__() ) # 3
print( odd_g.__next__() ) # 5

# we can iterate over a generator
for n in odd_g: # stops when the generator is exhausted
    print( n, end=', ' ) # end makes the print use a cutom separator