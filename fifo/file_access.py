import time
import random

def writeFile(words):
    '''Given a string of text, commit to a file'''
    try:
        #NB if the file does not yet exist, it will be created. If it exists, it will be appended
        # 'x' will expect exclusive access to the file
        # 'w' will (over)write the file
        fout = open('log.txt', 'a') # 'a' to append (text is the default)
        fout.write(words) # careful - will not append a new line character
        fout.write('\n')  # we may choose to put a new line character at the end
        fout.close() 
    # to handle exceptions, deal with specific ones first, then handle all others at the end
    except FileExistsError as err:
        print(f'The file already exists {err}')
    except Exception as err:
        print(err)
    finally:
        '''we would tidy up here'''

def readFile():
    try:
        fin = open('log.txt', 'r') # 'r' means read. Fails if the file does not exist
        readback = fin.read() # read will read in the whole thing
        print(f'Read in the following from log:\n{readback}')
        fin.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    # commit some information to our text log file
    writeFile('initial text')
    now  = time.time()
    writeFile(f'log written at {now}')
    value = random.randint(0, 100)
    writeFile(f'The value is {value}')
    readFile()



