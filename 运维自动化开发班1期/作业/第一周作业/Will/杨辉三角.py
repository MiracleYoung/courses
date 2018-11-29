#!/usr/bin/env python
# encoding: utf-8

"""
求杨辉三角第n行，第k列的值
　　　　　　　　１
　　　　　　　１　１
　　　　　　１　２　１
　　　　　１　３　３　１
　　　　１　４　６　４　１
　　　１　５　10　10　５　１
　　１　６　15　20　15　６　１
　１　７　21　35　35　21　７　１
１　８　28　56　70　56　28　８　１
"""

n = int(input('输入第几行：>>>'))
k = int(input('输入第几列：>>>'))
print(f'n={n},k={k}')
triangle = [[1], [1, 1]]
for i in range(2, n):
    tmp = triangle[-1]
    cul = [1] * (i + 1)
    for j in range(i // 2):
        cul[j + 1] = tmp[j] + tmp[j + 1]
        if i != 2j:
            cul[-j - 2] = cul[j + 1]
    triangle.append(cul)
print(triangle)
print(f'第{n}行，第{k}列的数据是{triangle[k]}')
