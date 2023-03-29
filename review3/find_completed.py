def findCompleted(tasks):
    '''return only those todos that have completed set to True'''
    completed = []
    for task in tasks:
        if task['completed']:
            completed.append(task)
    return completed

if __name__ == '__main__':
    pass