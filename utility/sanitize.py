# we may need to validate generic data
def checkType(value):
    '''Take a value and check if it is an integer, float or boolean
    Return the integer part of the value'''
    simpleTypes   = {int, float, bool}
    complexTypes  = {set, list, tuple, dict}
    # if type(value)==int or type(value)==float or type(value)==bool:
    if type(value) in complexTypes:
        return 0
    if type(value) in simpleTypes or value.isnumeric():
        return int(float(value)) 

if __name__ == '__main__':
    print( checkType(3) )     # pass in a value to be validated
    print( checkType(4.567))  # 4
    print( checkType(False) ) # 0
    print( checkType([]) )    # 0
    print( checkType('99') )  # 99