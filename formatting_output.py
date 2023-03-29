# sometimes we need to represent values with a certain number of decimal places
def show2dp(num):
    '''return a string from a floating point number, showing only 2 decimal places'''
    if type(num) == int or type(num)==float:
        # the precision of the number is preserved, only the string renders imprecision
        # return f'{num:0.2f}' # this will round the numeric value to 2dp
        return '{:0.2f}'.format(num) # this will round the numeric value to 2dp
    else:
        raise Exception('Only numeric values are accepted')

if __name__ == '__main__':
    v = 3.43678# 3.45678
    result = show2dp(v) # expect 3.44
    print( f'The numeric value {v} is rounded to {result}' )