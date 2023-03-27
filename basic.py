# here is a Python comment

# sinple data types
a = 7   # integer
b = 3.2 # float

# but Python is dynamically typed...
a = 'hello' # now it is a string type

# simple maths
c = 5
d = 13
print(c+d) # - * /
print(d%c) # show the remainder (modulo)
print(d//c)# how many times does c go into d
print(d**c)#raise to the power
# data type will change when we use division
print(d/c) # integer division result in a float
print (type(c), type(d/c))

# the string type is an indexed collection of characters
s = "here is a long collection of words making a string" # single, double or triple quotes are fine
print(s[0]) # 'h'
print(s[32])
# all indexed collections allow square-bracket acess like this...
print( s[3:38:2] ) # [start:stop-before:step]
# this is espcially useful for loops
# a colon indicates a block of code
for i in range(0,10): # the range object lets us (start, stop-before, step)
    print(i)
# the code clock will end when we no longer indent
if b>6:
    print(b)
else:
    print('six or less')

# the string type is an immutable collection
# s[0]='H' # this will fail - we CANNOT mutate members of a string

# big numbers - careful - this can use a lot of computing power!!!
# Python is only limited by system resources
g = 10**10000
print(g)

# other data types
t = True # boolean True or False
# square-brackets can indicate an indexed collection of mutable members of any data type
my_list = [6, 5.2, True, 'almost coffee', s, c]
my_list[0] = -6
my_list.append(d+b/c) # add a new mem ber to the end of the list
print(my_list, my_list[3], len(my_list))
my_list.pop() # remove the last member
# round brackets can indicate a tuple: an immutable indexed collection of any data type
my_tuple = (8, 7, 6, 'hi', False, b) # therefore tuple is more efficient
print(my_tuple[0:4])
# careful - a single-member tuple MUST have a trailing comma
other_t = (7,)
print(type(other_t))