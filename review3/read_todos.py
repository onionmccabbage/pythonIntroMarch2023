def readTodos():
    try:
        fin = open('./review3/todos.json', 'rt')
        tasks = fin.read()
        return tasks
    except Exception as err:
        print(err)

if __name__ == '__main__':
    readTodos()