import  datetime

# endless generator for date-time
def getDate():
    yield datetime.datetime.now()

# endless generator for time
# def getTime():
#     yield datetime.time()

if __name__ == '__main__':
    d = getDate()
    print( d.__next__() )
    # t = getDate()
    # print( t.__next__() )