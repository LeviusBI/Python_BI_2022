
# sequential_map - функция должна принимать в качестве аргументов любое количество функций 
# (позиционными аргументами, НЕ списком), а также контейнер с какими-то значениями. 
# Функция должна возвращать список результатов последовательного применения переданных функций 
# к значениям в контейнере. Например, 
# sequential_map(np.square, np.sqrt, lambda x: x**3, [1, 2, 3, 4, 5]) -> [1, 8, 27, 64, 125]
def sequential_map(*args):
    *functions_list, coll = [*args]
    for i in functions_list:
        coll = list(map(i, coll))
    return coll
    
    

# consensus_filter - функция должна принимать в качестве аргументов любое количество функций 
# (позиционными  аргументами, НЕ списком), возвращающих True или False, а также контейнер с какими-то
#  значениями. Функция должна возвращать список значений, которые при передаче их во все функции 
# дают True. Например: consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, 
# [-2, 0, 4, 6, 11]) -> [6]
def consensus_filter(*args):
    *functions_list, coll = [*args]
    for i in functions_list:
        coll = list(filter(i, coll))
    return coll


# conditional_reduce - функция должна принимать 2 функции, а также контейнер с значениями. 
# Первая функция должна принимать 1 аргумент и возвращать True или False, вторая также принимает 2 
# аргумента и возвращает значение (как в обычной функции reduce). conditional_reduce должна возвращать
#  одно значение - результат reduce, пропуская значения с которыми первая функция выдала False. 
# Например, conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) -> 4
def conditional_reduce(*args):
    *functions_list, coll = [*args]
    coll = list(filter(functions_list[0], coll))
    while len(coll) != 1:
        coll[0]=functions_list[1](coll[0], coll[1])
        del coll[1]
    return coll
       
res = conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10])
print(res)        
    


# func_chain - функция должна принимать в качестве аргументов любое количество функций (позиционными 
#  аргументами, НЕ списком). Функция должна возвращать функцию, объединяющую все переданные 
# последовательным выполнением. Например, 
# my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4)). my_chain(37) -> (9.75, 9). 
# +2 дополнительных балла за интеграцию этой функции в 1 задание.
def func_chain(*args):
    def run_pipe(x: int):
        res = x
        for f in args:
            res = f(res)
        return res
    return run_pipe
    
    


# Реализовать функцию  multiple_partial - аналог функции partial, но которая принимает неограниченное 
# число функций в качестве аргументов и возвращает список из такого же числа "частичных функций". 
# Не используйте саму функцию partial. Например: 
# ax1_mean, ax1_max, ax1_sum = multiple_partial(np.mean, np.max, np.sum, axis=1)
def multiple_partial(*args, **kwargs):
    def func_maker(*args, **kwargs):
        func_list = [*args]
        kwd = {**kwargs}
        ret_func_list = []
        for func in func_list:
            return func(**kwargs)
    return func_maker
# Реализуйте полный аналог функции print без использования её самой (без аргумента flush).
# В этом деле вам может помочь встроенный модуль sys.
def personal_print(*args, sep = ' ', end = '\n', file = None):
    if file == None:
        return f"{sep}".join([*args])+f"{end}"
    
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