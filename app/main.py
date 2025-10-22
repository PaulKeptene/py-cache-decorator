from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_immutable_values = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Callable:
        cache_key = (func, args, tuple(kwargs.items()))
        mutable_flag = False

        if not mutable_flag:
            for arguments in args:
                if type(arguments) in (dict, list, set):
                    mutable_flag = True
                    break

        if not mutable_flag:
            for key, value in kwargs.items():
                if type(value) in (dict, list, set):
                    mutable_flag = True
                    break

        if mutable_flag:
            print("Arguments must be immutable")
            return func(*args, **kwargs)
        elif cache_key in cache_immutable_values:
            print("Getting from cache")
            return cache_immutable_values[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_immutable_values[cache_key] = result
            return result
    return inner
