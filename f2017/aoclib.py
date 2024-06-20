def list2string(lst):
    result = ''
    for row in lst:
        for col in row:
            result += str(col)
        result += '\n'
    return result

def string2list(str_):
    result = str_.split("\n")
    for r in result:
        result[result.index(r)] = list(r)
    return result

def printlistasstr(lst):
    result = list2string(lst)
    print(result)

def datato2dlist(str_):
    grid = [[char for char in row] for row in str_.splitlines()]
    return grid