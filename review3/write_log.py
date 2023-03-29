from date_util import dateGen

def writeCompleted(data_j, dts):
    '''commit the completed tasks to a file'''
    try:
        with open('completed.txt', 'at') as fout:
            fout.write(data_j)
            fout.write('\n')
            fout.write( f'{dts}' ) # or str(dts) to cast datetime object to a string
            fout.write('\n')
    except Exception as err:
        print(err)

if __name__ == '__main__':
    du = dateGen()
    dts = du.__next__()
    writeCompleted('', dts)