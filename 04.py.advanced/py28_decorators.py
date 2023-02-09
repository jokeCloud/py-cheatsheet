from functools import wraps
from time import time
import functools


def performance(func):

    @functools.wraps
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Took: {t2 - t1} ms')
        return result
    return wrapper


@performance
def long_time():
    print(sum(i*i for i in range(10000)))


def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **args)
    return out


@debug
def add(x, y):
    return x + y
