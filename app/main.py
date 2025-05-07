from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    res_storage = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Callable:
        fname = func.__name__
        nonlocal res_storage
        if fname not in res_storage or args not in [
            el[0] for el in res_storage[fname]
        ]:
            print("Calculating new result")
            res = func(*args, **kwargs)
            res_storage[fname] = res_storage.get(fname, []) + [(args, res)]
        else:
            for el in res_storage[fname]:
                if el[0] == args:
                    print("Getting from cache")
                    res = el[1]
                    break
        return res
    return inner
