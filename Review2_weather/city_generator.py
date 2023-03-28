def cityGen():
    cities = [
        ('Athlone'),
        ('Galway'),
        ('Hull'),
        ('Canberra'),
        ('Berlin'),
        ('Madrid')
    ]
    index = 0
    while index < len(cities):
        # instead of a return statement, we have a yield statement
        yield cities[index] # yields the next value in the sequence being generated
        index += 1

if __name__ == '__main__':
    inst = cityGen()
    print( inst.__next__() )
    print( inst.__next__() )
    print( inst.__next__() )