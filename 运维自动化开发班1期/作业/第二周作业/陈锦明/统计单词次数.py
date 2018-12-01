#!/usr/bin/env python
# encoding: utf-8
# @Time : 2018/11/30 22:49
# author: andy chen

import collections
str1=['ab','ab','c','cccc','ccc','cccc']
m = collections.Counter(str1)

#print(str1)
#print(m)
print('ab:',m['ab'])
print('c:',m['c'])
print('cccc:',m['cccc'])
print('ccc:',m['ccc'])