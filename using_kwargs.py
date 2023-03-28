# as well as potional arguments, we may choose to provide keyword argument

def fn( **kwargs ): # by convention we use **kwrgs
    # all keyword arguments will exist in a dictionary
    print(kwargs, type(kwargs))
    
if __name__ == '__main__':
    # keyword arguments are always name=value. they MUST come after positional arguments
    fn(x=3, y=4) # keyword arguments can appearr in any order (following positional args)
    fn(y=4, x=3)