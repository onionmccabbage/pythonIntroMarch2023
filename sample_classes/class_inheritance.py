# there are several ways to write a class in Python
class A: # all classes ultimately inherit from 'object'
    pass

class B(): # implicitly inherit from 'object
    pass

class C(object): # explicitly inherit from 'object'
    '''property 'name' must be non-empty string or Exception'''
    def __init__(self, n):
        self.name = n # this will call the setter metod for 'name'
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name.isinstance('str') and new_name != '':
            self.__name = new_name
        else:
            raise Exception('Name must be a non-empty string')

class D(C): # here the 'D' class will inherit everything from the 'C' class
    '''as well as 'name' (from D class) this class will have 'completed' (boolean)'''
    def __init__(self, n, c):
        # we call the __init__ method of the parent class (super)
        super().__init__(n) # this uses the 'name' property of the parent class
        self.completed = c
    @property
    def completed(self):
        return self.__completed
    @completed.setter
    def completed(self, new_completed):
        if new_completed.isinstance(bool):
            self.__completed = new_completed
        else:
            raise Exception('Completed must be boolean')

if __name__ == '__main__':
    c1 = C('Ermintrude')
    d1 = D('Beatrice', True)
    # see if it breaks...
    c1 = C(333) # should raise an exception
