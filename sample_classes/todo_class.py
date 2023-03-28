class ToDo:
    ''' ToDo will have 'title' as a non-empty string property '''
    ''' we also need an id property, which must be a positive integer'''
    def __init__(self, title):
        self.__title = title # mangle the property to avoid direct access
    # we can validate properies by writing setter and getter methods
    def getTitle(self): # remember, every method of a class must have 'self' as an argument
        return self.__title
    def setTitle(self, new_title):
        if type(new_title)==str and new_title !='':
            self.__title = new_title
        else:
            self.__title = 'Default' # or raise exception
    # we can declare the get/set methods as a property
    title = property(getTitle, setTitle)

if __name__ == '__main__':
    '''e can instantiate our class'''
    t1 = ToDo('Learn Python') # every time we create an instance, the __init__ method will be called
    t1.setTitle(99)
    t1.getTitle()
    # we can access the getTtiel and setTitle as if they are one property, called 'title'
    t1.title = 'Done' # use the set title method
    print(t1.title) # use the getTitle method