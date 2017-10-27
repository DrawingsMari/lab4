from time import sleep
from librip.ctxmngrs import timer

with timer():
    sleep(3)
    print("Проснулся!")
    sleep(1)
    print("Ой, опять заснул!")


