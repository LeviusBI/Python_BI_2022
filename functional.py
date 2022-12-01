
# sequential_map - функция должна принимать в качестве аргументов любое количество функций 
# (позиционными аргументами, НЕ списком), а также контейнер с какими-то значениями. 
# Функция должна возвращать список результатов последовательного применения переданных функций 
# к значениям в контейнере. 
def sequential_map(*args):
    *functions_list, coll = [*args]
    for i in functions_list:
        coll = list(map(i, coll))
    return coll

print(sequential_map(lambda x: x**2, lambda x: x**(0.5), lambda x: x**3, [1, 2, 3, 4, 5]))

# consensus_filter - функция должна принимать в качестве аргументов любое количество функций 
# (позиционными  аргументами, НЕ списком), возвращающих True или False, а также контейнер с какими-то
#  значениями. Функция должна возвращать список значений, которые при передаче их во все функции 
# дают True.
def consensus_filter(*args):
    *functions_list, coll = [*args]
    for i in functions_list:
        coll = list(filter(i, coll))
    return coll

print(consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]))

# conditional_reduce - функция должна принимать 2 функции, а также контейнер с значениями. 
# Первая функция должна принимать 1 аргумент и возвращать True или False, вторая также принимает 2 
# аргумента и возвращает значение (как в обычной функции reduce). conditional_reduce должна возвращать
#  одно значение - результат reduce, пропуская значения с которыми первая функция выдала False. 
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
print(conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]))              

# func_chain - функция должна принимать в качестве аргументов любое количество функций (позиционными 
#  аргументами, НЕ списком). Функция должна возвращать функцию, объединяющую все переданные 
# последовательным выполнением.
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

# Интеграция func_chain в первую функцию 

def sequential_map_2(*args):
    *functions_list, coll = [*args]
    pipeline = func_chain(*functions_list)
    return pipeline(coll)
print(sequential_map_2(lambda x: x**2, lambda x: x**(0.5), lambda x: x**3, [1, 2, 3, 4, 5]))
# Реализовать функцию  multiple_partial - аналог функции partial, но которая принимает неограниченное 
# число функций в качестве аргументов и возвращает список из такого же числа "частичных функций". 
# Не используйте саму функцию partial. Например: 
# ax1_mean, ax1_max, ax1_sum = multiple_partial(np.mean, np.max, np.sum, axis=1)
def multiple_partial(*args, **kwargs):
    func_list = [*args]
    kwd = {**kwargs}
    ret_func_list = []
    for func in func_list:
        ret_func_list
    return ret_func_list
# Реализуйте полный аналог функции print без использования её самой (без аргумента flush).
# В этом деле вам может помочь встроенный модуль sys.
import sys as s 
def personal_print(*args: str, sep = '', end = '\n', file = s.stdout):
    if file == s.stdout:
        result = ""
        for i in args:
            result += f"{i}{sep}"
        return "result %{end}"
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

# Требования:
# Все функции реализуйте в файле functional.py
# Код вне функций писать не нужно, реализовывать интерфейс для взаимодействия с пользователем 
# тоже не надо
# Использовать любые библиотеки (в том числе встроенные модули) запрещается. 
# Используем только функционал "голого" питона. Для отладки и тестирования можно использовать 
# что угодно, но в финальном скрипте этого быть не должно. 
# P.S. Кроме второго дополнительного задания, там можно использовать модуль sys. 