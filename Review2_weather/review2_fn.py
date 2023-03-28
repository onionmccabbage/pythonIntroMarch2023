import requests
from sanitize import checkCity
from weather_class import Weather

def getWeather():
    '''get weather for a specific city'''
    flag = True
    while flag:
        city = input('Please enter a city name ')
        # use the imported utility to validate the city
        flag = checkCity(city)
    weatherUrl = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'
    response = requests.get(weatherUrl)
    response_dict = response.json()
    return response_dict

def main():
    w = getWeather()
    print(w)
    # or use a class
    c = w['name']
    d = w['weather'][0]['description']
    t = w['main']['temp']
    report = Weather(c, d, t)
    print(report)

if __name__ == '__main__':
    main()