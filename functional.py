
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
            coll[0]=functions_list[1](coll[0], coll[1])
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
    def func_maker(func, **kwargs):
        return lambda x: func(x, **kwargs)
    ret_func_list = []
    for func in args:
        res = func_maker(func, **kwargs)
        ret_func_list.append(res)
    return ret_func_list
# Реализуйте полный аналог функции print без использования её самой (без аргумента flush).
# В этом деле вам может помочь встроенный модуль sys.
import sys as s 
def personal_print(*args: str, sep=' ', end='\n', file = None):
    if file == None:
        result = ""
        for i in args:
            result += f"{i}{sep}"
        s.stdout.write()
    else: 
        pass

# Print objects to the text stream file, separated by sep and followed by end. sep, end, file, 
# and flush, if present, must be given as keyword arguments.

# All non-keyword arguments are converted to strings like str() does and written to the stream, 
# separated by sep and followed by end. Both sep and end must be strings; they can also be None, 
# which means to use the default values. If no objects are given, print() will just write end.

# The file argument must be an object with a write(string) method; if it is not present or None, 
# sys.stdout will be used. Since printed arguments are converted to text strings, print() 
# cannot be used with binary mode file objects. For these, use file.write(...) instead.

# Whether the output is buffered is usually determined by file, but if the flush keyword argument 
# is true, the stream is forcibly flushed.

# Changed in version 3.3: Added the flush keyword argument.    
