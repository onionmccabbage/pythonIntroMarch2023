# we can have default values for function arguments
def pow(a=2, b=3):
    '''return a raised the to the power of b'''
    return a**b

# if we wish, we can collect together ALL the positional arguments of a function
def posArgs( *args ): # *args wil collect all the posituional arguments into a tuple
    print( args, type(args) ) # a tuple
    # we can use args in place of overloads
    if len(args)==0:
        # we have no arguments
        print('no arguments were provided')
    elif len(args)==1:
        # we have a single argument
        print(f'Received {args[0]}')
    elif len(args)==2:
        return args[0]**args[1]
    else:
        return f'Recieved several arguments: {args}'

if __name__ == '__main__':
    print( pow(3, 2) ) # 9 we override the default values with our own values
    print( pow() ) # this will use the default values i.e return 8
    # use our multi-armument function
    posArgs()
    posArgs(True)
    posArgs(3,4)
    posArgs(3, 6, 'lunch', {'id':5}, True)