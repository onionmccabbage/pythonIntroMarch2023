# unlike other languages, the file name bears no relation to the class name

class Person: # brackets are onptional
    '''Explain your class in a docstring
    This class encapsulates Person details
    Parameters: name, age, email
    'age' must be a positve integer'''
    # all methods of a class MUST take 'self' as an argument
    def __init__(self, n, a, e): # init is not a constructor, but is very like one
        # double-underscore will 'mangle' the parameter name
        self.__name = n # we use our mutator method
        self.age   = a
        self.email = e
    # we need a 'setter' method to validate the name
    def setName(self, new_name):
        if type(new_name) == str and new_name !='':
            self.name=new_name
        else: # we could raise an exeption
            self.name  ='default'
    # we also provide a 'getter' method
    def getName(self):
        return self.__name # we return the mangled property

if __name__ == '__main__':
    # we can create intances of our class
    ethel = Person('Ethel', 98, 'ethel@babbage.com')
    grace = Person('Grace', 82, 'grace@nasa.com')
    doh   = Person('', True, {}) # no validation, so this is fine
    # without some work, we can mutate the properties of our class instances
    ethel.setName(True)
    print(f'{ethel.getName()} is {ethel.age}')
    print(f'{doh.getName()}') # default