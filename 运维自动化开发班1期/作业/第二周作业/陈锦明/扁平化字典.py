#!/usr/bin/env python
# encoding: utf-8
# @Time : 2018/11/30 23:02
# author: andy chen

m = {'a': {'b': {'c': 1}, 'd': 2}, 'e': 3}

def flatdict(m,target=None,prefix=''):
    if target is None:
        target = {}
    for k, v in m.items():
        if isinstance(v, dict):
            flatdict(v,target,prefix + k + '.')
        else:
            target[prefix + k] = v
    return target
print(flatdict(m))

