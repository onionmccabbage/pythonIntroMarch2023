class Photo:
    '''URL must be a non-empty string'''
    ''' we also need an id property, which must be a positive integer'''
    def __init__(self, url):
        self.__url = url
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

if __name__ == '__main__':
    p1 = Photo('https://placehold.co/64')
    print(p1.url)