# how to handle bytes
b = bytes(b'hello') # b converts the string to bytes
print(b) # this converts the bytes back to text

c = bytes( range(0,255) )
# print(c)

def writeBytes():
    '''we can write files using byte data'''
    try:
        # remember, we have file access objects - a means to access the actual file
        fout = open('bfile', 'wb') # 'w' (over)write 'b' bytes
        fout.write(c)
        fout.close()
    except Exception as err:
        print(err)

def readBytes():
    '''we can read back byte data'''
    try:
        fin = open('bfile', 'rb') # 'rb' will read bytes
        r = fin.read()
        fin.close()
        print(r) # print will try to render anything, even bytes
    except Exception as err:
        print(err)

if __name__ == '__main__':
    writeBytes()
    readBytes()