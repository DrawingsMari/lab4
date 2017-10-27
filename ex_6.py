#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = "data_light_cp1251.json"

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    # Отсортированный без повторений Список названий профессий
    return sorted((x for x in unique(list(field(data, "job-name")), ignore_case=True)))


@print_result
def f2(arg):
    # Все профессии начинающиеся с "Программист"
    return list(filter(lambda x: x.startswith("Программист"), arg))


@print_result
def f3(arg):
    # Добавить строку " с опытом Python", map - обработка каждого элеммента массива
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    salaries = list(gen_random(100000, 200000, len(arg)))
    for name, salary in zip(arg, salaries):
        print(name, ", зарплата ", salary, "руб. ")


with timer():
    f4(f3(f2(f1(data))))