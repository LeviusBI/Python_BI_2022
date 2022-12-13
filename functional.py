
def sequential_map_2(*args):
    *functions_list, coll = [*args]
    #for i in functions_list:
    #    coll = list(map(i, coll)) это был код до того, как я реализовал func_chain
    #return coll
    pipeline = func_chain(*functions_list) #тут уже интегрирована функция, которая дальше по заданию
    return pipeline(coll)

def consensus_filter(*args):
    *functions_list, coll = [*args]
    for i in functions_list:
        coll = list(filter(i, coll))
    return coll

def conditional_reduce(*args):
    *functions_list, coll = [*args]
    coll = list(filter(functions_list[0], coll))
    if len(coll) > 1:
        while len(coll) != 1:
            coll[0] = functions_list[1](coll[0], coll[1])
            del coll[1]
        return coll
    else:
        return coll
         
def func_chain(*args):
    def run_pipe(x: int):
        if type(x) == int or type(x) == float:
            res = x
            for f in args:
                res = f(res)
            return res
        elif type(x) == list: #чтоб работала на списках наверняка
            res = x
            for i in range(0, len(x)):
                for f in args:
                    res[i] = f(res[i])
            return res
    return run_pipe


def multiple_partial(*args, **kwargs):
    def func_maker(f, **kwargs):
        return lambda x: f(x, **kwargs)
    ret_func_list = []
    for f in args:
        res = func_maker(f, **kwargs)
        ret_func_list.append(res)
    return ret_func_list

import sys 
def personal_print(*args: str, sep=' ', end='\n', file = None):
    if file == None:
        result = ""
        for i in args:
            result += f"{i}{sep}"
        result+=f"{end}"
        sys.stdout.write(result)
    else:
        with open(file, 'w') as sys.stdout:
            personal_print(*args, sep, end)
