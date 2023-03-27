# might contain some utilities
def setLowercase(words):
    return words.lower()

# exercise this code
if __name__ == '__main__': # exactly this...
    # so just what is the name of this module?
    print(f'This module is named {__name__}')
    print( setLowercase('HELLO') )