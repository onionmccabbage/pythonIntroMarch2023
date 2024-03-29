# generate city/country pairs

def locationGen():
    locations = [ # NB these values DO all exist in memory
        ('Athlone','ie'),
        ('Galway','ie'),
        ('Hull','uk'),
        ('Canberra','aus'),
        ('Berlin','de'),
        ('Madrid','es')
    ]
    index = 0
    while index < len(locations):
        # instead of a return statement, we have a yield statement
        yield locations[index] # yields the next value in the sequence being generated
        index += 1

if __name__ == '__main__':
    inst = locationGen()
    print( inst.__next__() ) # ('Athlone','ie')
    print( inst.__next__() ) # ('Galway','ie')
    print( inst.__next__() ) # ('Hull','uk')