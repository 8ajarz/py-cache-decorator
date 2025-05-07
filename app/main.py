from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    res_storage = {}
    @wraps(func)
    def inner(*args, **kwargs):
        funcname = func.__name__
        nonlocal res_storage
        if funcname not in res_storage:
            print("Calculating new result")
            res = func(*args, **kwargs)
            res_storage[funcname] = res_storage.get(funcname, []) + [(args, res)]
        else:
            args_in = False
            for el in res_storage[funcname]:
                if el[0] == args:
                    print("Getting from cache")
                    res = el[1]
                    args_in = True
                    break
            if not args_in:
                print("Calculating new result")
                res = func(*args, **kwargs)
                res_storage[funcname] = res_storage.get(funcname, []) + [(args, res)]
        return res
    return inner

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
