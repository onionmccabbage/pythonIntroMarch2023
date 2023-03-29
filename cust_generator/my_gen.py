# recall that generators can yield values without them persisting in memory
even_g = ( num for num in range(0,100,2) )
print(even_g.__next__()) # 0
print(even_g.__next__()) # 2
print(even_g.__next__()) # 4

# we can write our own custom generator to yield values on demand
def genSquareNums(n=0, stop=10, step=1): # sensible defaults
    '''Generate the squares of nubmers from n to 'stop' every 'step' '''
    count = n # begins at zero by default
    stop_at = stop-1 # follow the convention of Python
    while count < stop_at:
        count += step # default to increment by 1
        # by using 'yield' we make this function into a generator
        yield count**2 # yield will return the next value in the series

if __name__ == '__main__':
    g = genSquareNums(stop=101) # we now have an isntance of our generator
    print( g.__next__() ) # 1
    print( g.__next__() ) # 4
    print( g.__next__() ) # 9
    # we can iterate over any generator
    for s in g:
        print(s, end=', ')
    print('\n') # finish with a new line
    # when we run out of generated values, the generator is exhausted
    # print( g.__next__() ) # fails