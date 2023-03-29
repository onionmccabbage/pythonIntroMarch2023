def readTodos():
    fin = open('todos.json', 'rt')
    tasks = fin.read()
    return tasks

if __name__ == '__main__':
    pass