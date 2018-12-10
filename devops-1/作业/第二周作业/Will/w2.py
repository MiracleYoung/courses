#!/usr/bin/env python
# coding: utf-8

# W 2
# 1.移除列表中的重复元素，并保持新列表和元列表的顺序一致 [1, 1, 2, 3, 4, 4, -1, -1] => [1, 2, 3, 4, -1]
l1 = [2, 2, 1, 3, 1, 1, 4, -1, -1]
# l1=['b','c','a','b','d','c','a']
l2 = list(set(l1))
n = []
[n.append(i) for i in l1 if not i in n]
print(n)

# 2.统计文本中各单词出现的次数 'ab ab c cccc ccc cccc'
# s='ab ab c cccc ccc cccc'
s = 'ab c fk ccc cccc fk that shit damn it it damn shit shit shit ab cccc c ccc d'

ns = s.split(' ')

r = {}
for i in range(len(ns)):
    # print(f'{ns[i]}= {ns.count(ns[i])}')
    c = ns.count(ns[i])
    r[ns[i]] = c

print(r)

# 3.扁平化字典 {'a': {'b': {'c': 1}, 'd': 2}, 'e': 3} => {'a.b.c': 1, 'a.d': 2, 'e': 3}
s = {'a': {'b': {'c': 1}, 'd': 2}, 'e': 3}
t = {}


def flatdic(srcDic, targetKey=''):
    for k, v in srcDic.items():
        if isinstance(v, dict):
            flatdic(v, targetKey=targetKey + k + '.')
        else:
            t[targetKey + k] = v


flatdic(s)
print(t)
