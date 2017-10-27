from librip.gens import *

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'},
    {'title': 'Шкаф', 'price': 6500, 'color': None},
    {'title': None, 'price': None, 'color': None}
]

# Реализация задания 1

print(*((str(x) + '\n') for x in field(goods, 'title', 'color')))
print(*(str(x) + '  ' for x in gen_random(2, 5, 10)))

