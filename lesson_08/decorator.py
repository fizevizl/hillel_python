
import time
from datetime import datetime
from random import randint as rnd

def decorator(func):
    def inner():
        print('-'*10, func.__name__, '-'*10)
        now = datetime.now()
        func()
        print(f" час виконання функції: {datetime.now() - now}")
        print("-"*40, '\n')
    return inner

@decorator
def gen_list():
    time.sleep(rnd(1, 3))
    c = [ c * 3 for c in "list"]
    print("", c)

@decorator
def random_num():
    time.sleep(rnd(1, 3))
    s = rnd(1, 10)
    print("", s)

gen_list()
random_num()