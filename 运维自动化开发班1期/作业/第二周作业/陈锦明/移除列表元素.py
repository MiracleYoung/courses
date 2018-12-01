#!/usr/bin/env python
# encoding: utf-8
# @Time : 2018/11/30 22:28
# author: andy chen


# m = [1, 1, 2, 3, 4, 4, -1, -1]
# n = list(set(m))
# print(n)

m = [1,4,3,3,4,2,3,4,5,6,1]
n = []
[n.append(i)for i in m if not i in n]
print(n)





