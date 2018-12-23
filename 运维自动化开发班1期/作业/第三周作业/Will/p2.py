#!/usr/bin/env python
# coding: utf-8

from functools import wraps


def cache(func):
    data = {}

    @wraps(func)
    def wrapper(*args):
        if args in data:
            print("in cache")
            return data[args]
        else:
            print("not in cache")
            res = func(*args)
            data[args] = res
            return res

    return wrapper


@cache
def add(x, y):
    return x + y


print(add(1, 2))
print(add(1, 2))
print(add(3, 4))
