class Weather(object):
    def __init__(self, city, description, temperature):
        self.city        = city
        self.description = description
        self.temperature = temperature
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        if isinstance(new_city, str) and len(new_city) >2:
            self.__city = new_city
        else:
            raise Exception('city must be a string of 3 or more characters')
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str) and len(new_description) >2:
            self.__description = new_description
        else:
            raise Exception('description must be a non-empty string')
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, new_temperature):
        if isinstance(new_temperature, float) or isinstance(new_temperature, int):
            self.__temperature = new_temperature
        else:
            raise Exception('temperature must be a numeric value')
    def __str__(self):
        return f'the weather in {self.city} is {self.description} and {self.temperature} degrees'