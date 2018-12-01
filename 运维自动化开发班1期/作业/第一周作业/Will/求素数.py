#!/usr/bin/env python
# coding: utf-8

"""
求100w以内的素数
质数（Prime number），又称素数，指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数（也可定义为只有1与该数本身两个因数的数）。
简单来说就是，只能除以1和自身的数（需要大于1）就是质数。举个栗子，5这个数，从2开始一直到4，都不能被它整除，只有1和它本身（5）才能被5整除，所以5就是一个典型的质数。
"""

p = []
max_num = 100
for i in range(2, max_num):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        p.append(i)

print(f'{max_num} 以内有 {len(p)}个素数')
