import  datetime

# endless generator for date-time values
def dateGen():
    yield datetime.datetime.now()

# endless generator for time
# def getTime():
#     yield datetime.time()

if __name__ == '__main__':
    d = dateGen()
    print( d.__next__() )
    # t = getDate()
    # print( t.__next__() )