# might encapsulate some logic
def validate(value):
    if type(value)==int:
        return 'ok'
    else:
        return 'not ok'
# exercise the code
if __name__ == '__main__':
    print(f'This module is named {__name__}')
    print(validate(-4))
