# functions are declared with the keyword 'def'

def doStuff(x, y): # we can pass arguments into the function
    square_x = x*x
    square_y = y*y
    hypotenuse = ( square_x + square_y )**0.5 # raise to 0.5 will be the square root
    return hypotenuse # Python does not require a 'return' - it will default to zero
    # or return ( x**2 + y**2 )**0.5

# use the code
result = doStuff( -3, 4 ) # expect 5.0
print(result)

# we can ask the user for values
x = input('Value for x: ') # careful - EVERY user input is always a STRING
y = input('Value for y: ')
# we probably need to cast input values to numeric values
if x.isnumeric(): # we should always validate user input
    x_num = int(x)
    print(x_num, type(x_num))
if y.isnumeric():
    y_num = int(y)
    print(y_num, type(y_num))
# calculate the hypotenuse
result = doStuff(x_num, y_num) # we pass in the validated values (NOT the string input values)
print(result)