def fn():
    '''Good idea to write a docstring for our functions
    The docstring can explain the purpose of this function'''
    # ask the user for a non-empty string
    s = ''
    while s == '':
        try:
            u = input('Please type something')
            # is it an empty string?
            if u == '':
                raise Exception('cannot be empty string')
            else:
                s = u
        except Exception as err: # this block iwll catch all exceptions
            print(err)
        finally: # this always runs, whether or not there is an exception
            print(f'Thank you for entering {s}')

if __name__ == '__main__':
    '''here we execute the local function'''
    fn()