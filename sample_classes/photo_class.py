class Photo:
    '''URL must be a non-empty string'''
    ''' we also need an id property, which must be a positive integer'''
    def __init__(self, url, id):
        self.__url = url
        self.__id  = id
    # this time we will use 'decorator syntax' for the property get/set methods
    @property # here we have a 'getter' for the URL
    def url(self):
        return self.__url
    @url.setter
    def url(self, new_url):
        if type(new_url)== str and new_url != '':
            self.__url = new_url
        else:
            self.__url = 'na'
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, new_id):
        if type(new_id)==int and new_id > 0:
            self.__id = new_id
        else:
            self.__id = 999
    # we can override the built in '__str__' method with our own print preference
    def __str__(self):
        return f'Photo id {self.id} url: {self.url}'

if __name__ == '__main__':
    p1 = Photo('https://placehold.co/64', 1)
    print(p1.url, p1.id)
    print(p1) # this will call the __str__ method