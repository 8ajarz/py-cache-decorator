from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    res_storage = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Callable:
        fname = func.__name__
        nonlocal res_storage
        inputs = args, kwargs
        if fname not in res_storage or inputs not in [
            el[0] for el in res_storage[fname]
        ]:
            print("Calculating new result")
            res = func(*args, **kwargs)
            res_storage[fname] = res_storage.get(fname, []) + [(inputs, res)]
        else:
            for el in res_storage[fname]:
                if el[0] == inputs:
                    print("Getting from cache")
                    res = el[1]
                    break
        return res
    return inner
