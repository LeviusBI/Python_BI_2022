# sequential_map - функция должна принимать в качестве аргументов любое количество функций 
# (позиционными аргументами, НЕ списком), а также контейнер с какими-то значениями. 
# Функция должна возвращать список результатов последовательного применения переданных функций 
# к значениям в контейнере. Например, 
# sequential_map(np.square, np.sqrt, lambda x: x**3, [1, 2, 3, 4, 5]) -> [1, 8, 27, 64, 125]
# 
# consensus_filter - функция должна принимать в качестве аргументов любое количество функций 
# (позиционными  аргументами, НЕ списком), возвращающих True или False, а также контейнер с какими-то
#  значениями. Функция должна возвращать список значений, которые при передаче их во все функции 
# дают True. Например: consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, 
# [-2, 0, 4, 6, 11]) -> [6]
# 
# conditional_reduce - функция должна принимать 2 функции, а также контейнер с значениями. 
# Первая функция должна принимать 1 аргумент и возвращать True или False, вторая также принимает 2 
# аргумента и возвращает значение (как в обычной функции reduce). conditional_reduce должна возвращать
#  одно значение - результат reduce, пропуская значения с которыми первая функция выдала False. 
# Например, conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) -> 4
# 
# func_chain - функция должна принимать в качестве аргументов любое количество функций (позиционными 
#  аргументами, НЕ списком). Функция должна возвращать функцию, объединяющую все переданные 
# последовательным выполнением. Например, 
# my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4)). my_chain(37) -> (9.75, 9). 
# +2 дополнительных балла за интеграцию этой функции в 1 задание.

# Реализовать функцию  multiple_partial - аналог функции partial, но которая принимает неограниченное 
# число функций в качестве аргументов и возвращает список из такого же числа "частичных функций". 
# Не используйте саму функцию partial. Например: 
# ax1_mean, ax1_max, ax1_sum = multiple_partial(np.mean, np.max, np.sum, axis=1)

# Реализуйте полный аналог функции print без использования её самой (без аргумента flush).
# В этом деле вам может помочь встроенный модуль sys.

# Требования:
# Все функции реализуйте в файле functional.py
# Код вне функций писать не нужно, реализовывать интерфейс для взаимодействия с пользователем 
# тоже не надо
# Использовать любые библиотеки (в том числе встроенные модули) запрещается. 
# Используем только функционал "голого" питона. Для отладки и тестирования можно использовать 
# что угодно, но в финальном скрипте этого быть не должно. 
# P.S. Кроме второго дополнительного задания, там можно использовать модуль sys. 