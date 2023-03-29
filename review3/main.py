from date_util import dateGen
from write_log import writeCompleted
from json_util import jsonToStruct
from json_util import structToJson
from read_todos import readTodos
from find_completed import findCompleted

def main():
    t_j = readTodos()
    t_d = jsonToStruct(t_j)
    du = dateGen()
    dts = du.__next__()
    t_completed = findCompleted(t_d)
    t_completed_j = structToJson(t_completed)
    writeCompleted(t_completed_j, dts)

if __name__ == '__main__':
    main()