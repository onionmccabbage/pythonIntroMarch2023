# classes are often used to compose a custom structure from smaller parts
class Geo(object):
    '''encapsulate values for lat and for lon'''
    def __init__(self, lat, lon):
        '''we should validate...'''
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f'latitude:{self.lat:0.2f} longitude:{self.lon:0.2f}'
    
class Address(object):
    '''encapslate values for street and geo'''
    count = 0 # this property can be called on the Class itself
    def __init__(self, street, geo):
        self.street = street
        self.geo = geo
        Address.count += 1 # increase the count every time an Address is instantiated
    def __str__(self):
        return f'Address Street is {self.street} latitude:{self.geo.lat:0.2f} longitude:{self.geo.lon:0.2f}'
    staticmethod
    def showMetaData():
        '''information about this class'''
        return 'Address class developed in March 2023 as part of Python into course'

if __name__ == '__main__':
    # 53.43333 -7.95 is Athlone
    g = Geo(53.43333, -7.95)
    print(g)
    a = Address('high street', g) # composing my address by passing in a geo instance
    a = Address('brawney road', g) # composing my address by passing in a geo instance
    a = Address('blackberry lane', g) # composing my address by passing in a geo instance
    print(a)
    print(Address.count) # 3
    print(Address.showMetaData()) # here we call a static method - it belongs to the class, not to any instance
    # we can always acces a docstring as follows...
    print(Address.__doc__) # works for classes, function etc.

