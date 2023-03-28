def checkCity(city):
    if isinstance(city, str) and len(city)>2:
        return False
    else:
        return True