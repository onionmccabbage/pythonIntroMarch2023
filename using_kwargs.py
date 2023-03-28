# as well as potional arguments, we may choose to provide keyword argument

def fn( **kwargs ): # by convention we use **kwrgs
    # all keyword arguments will exist in a dictionary
    print(kwargs, type(kwargs))

# we can choose to handle args and kwargs all together
def handleBoth(*args, **kwargs):
    print(args, kwargs)

if __name__ == '__main__':
    # keyword arguments are always name=value. they MUST come after positional arguments
    fn(x=3, y=4) # keyword arguments can appearr in any order (following positional args)
    fn(y=4, x=3)
    handleBoth() # no args or kwargs
    handleBoth(1, 5, True, []) # positional args but no keyword args
    handleBoth(n='Bertha', a=42, flag=False) # keyword args no postional args
    handleBoth(4, {}, q='Athlone', done=True) # positonal and keyword args