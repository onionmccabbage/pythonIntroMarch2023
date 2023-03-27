# we can import code from other modules
from using_functions import * 

# careful EVERY BIT of the imported module will RUN when imported
if __name__ == '__main__':
    # keep asking until we have int values
    x_invalid = True
    while x_invalid: # careful - a 'while' block will run forever (unless we break out)
        # ask the user for x
        x_str = input('X: ')
        if x_str.isdecimal():
            x_int = int(float(x_str)) # safest validation
            break # this will end our while block
    y_invalid = True
    while y_invalid:
        y_str = input('Y ')
        if y_str.isnumeric(): # isnumeric only allows digits. No '-' or '.' is permitted
            y_int = int(float(y_str))
            y_invalid = False # another way of stopping the while loop

    # use the imported function
    h = doStuff(x_int, y_int) # here we call the imported function
    print(f'Given {x_int} and {y_int} the hypotenuse is {h}')