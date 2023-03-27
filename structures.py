# Python data structures: list, tuple, dictionary and set
# the 'dictionary' structure is a non-indexed mutable collection
# curly-brackets can indicate a dictionary
my_d = {'fn':'Timnit', 'ln':'Gebru', 'admin':True, 'age':42} # key:value pairs
# we can add new members and mutate existing members
my_d['hero'] = True # we must set using the equals sign
my_d['age'] = 38
print(my_d, my_d['fn'])

# we can inspect collection using 'in'
if 'admin' in my_d:
    print(my_d['admin'])
else:
    print('no key for \'admin\' ') # we can use backslash to 'escape' certain characters

# we can use 'in' for other collections
days_l = ['mon', 'tue', 'wed']
print( 'thur' in days_l  ) # False
squares_t = (1, 4, 9, 16, 25)
print( 8 in squares_t )

# tuple...
t = (5,4,3,2) # we canot add members to this tuple (it is immutable)

# the 'set' collection is a mutable collection of unique values of any primitive data type
my_set = {3, 8, True, 'hi', 42, 8, True, t} # we CAN add tuple to a set
my_set.add('additional')
print(my_set)

n = None # can be handy

# Everything in Python is an Object - all types inherit from 'object'


