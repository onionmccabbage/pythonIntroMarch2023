import date_util
import write_log
import json
from read_todos import readTodos
from find_completed import findCompleted

def jsonToDict(j):
    return json.loads(j)

if __name__ == '__main__':
    t_j = readTodos()
    # print(t_j)
    t_d = jsonToDict(t_j)
    print(t_d)
    t_completed = findCompleted(t_d)
    print(t_completed)