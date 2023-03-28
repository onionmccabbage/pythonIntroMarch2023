# we can use the requests library to access external data from an API
import requests # remember - we may need to 'pip install requests'
# we need to import our classes
from photo_class import Photo
from todo_class  import ToDo

def getData(category, id):
    '''get data using the category and id provided'''
    # this URL will return JSON data
    dataUrl = f'https://jsonplaceholder.typicode.com/{category}/{id}'
    # remember, all internet requests use http(s)
    # 'get' is by far the mpst common eay to acces URL data
    response = requests.get(dataUrl) # this will call the API and access the returned data
    # the response includes the code, the headers etc.... and our data
    # we can easily convert the JSON into a dictionary
    response_dict = response.json() # or .text or .html or .xml ....
    return response_dict

if __name__ == '__main__':
    '''we can call our requests method to get data'''
    result = getData('todos', 77)
    # print( result )
    # careful - we have single quotes inside double quotes
    print( f"We received {result['title']} with id {result['id']} completed {result['completed']}" )
    # we can get photo data
    photo_result = getData('photos', 1234)
    print(photo_result)
    # we can populate our classes from the retrieved data
    todo1  = ToDo(result['title'], result['id'])
    photo1 = Photo(photo_result['url'], photo_result['id'])
    print(todo1, photo1) # use the __str__