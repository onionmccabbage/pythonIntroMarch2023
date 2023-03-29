# Python has global and block scopes
# Anything not in a block of code is in the global scope
# as with all languages, we try to avoid polluting the global scope

g = 'this is in the global scope'

def fn(): # remember: the colon always indicates a block of code
    global g # now we are talking about the same thing, known as 'g'
    g = 'this is in a local block scope'
    print(g)

if __name__ == '__main__':
    fn()
    print(g) # this will print the global g
