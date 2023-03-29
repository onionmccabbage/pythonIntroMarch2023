# we can write tests within the docstring by using doctest
import doctest

def cube(x):
    '''This function will take a nubmer and return the cube of that number
    >>> cube(3)
    27
    >>> cube(-3)
    -27
    >>> cube(999)
    997002999
    '''
    return x*x*x # or x**3

if __name__ == '__main__':
    # r = cube(3) # 27
    # print(r)
    #doctetst will run any tests writtetn within the docstring
    doctest.testmod(verbose=True) # we will see more details