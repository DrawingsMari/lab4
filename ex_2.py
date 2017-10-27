#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ["AAA", "aaa", "bb", "c", "c", "D"]
data4 = [1,1,2,3,4,4,4,3,5]

print(*Unique(data4, ignore_case=False))
# Реализация задания 2
print(*Unique(data1,False))
print(*(x for x in Unique(data1, False)))
print(*(x for x in Unique(list(data2), False)))
print(*(x for x in Unique(data3, False)))

