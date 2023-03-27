# we can import stuff
import util # this will import the whole module
import other

# use the code
t = 'Mixed Case soME lOwEr...'
v = 1.0

if __name__ == '__main__':
    print(f'This module is named {__name__}')
    # what name does Python give to the imported modules?
    print(f'The imported modules are named {util.__name__} and {other.__name__}')
    print( util.setLowercase(t) )
    print( other.validate(v))
