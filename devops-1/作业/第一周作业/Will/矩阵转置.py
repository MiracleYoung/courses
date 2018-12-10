#!/usr/bin/env python
# encoding: utf-8

"""
矩阵转置
m*n
2行3列转成3行2列
[1,2,3]     ->  [1,4]
[4,5,6]         [2,5]
                [3,6]
"""

# 方法1：
# def tf(m):
#     return zip(*m)
#
# m = [[1, 2], [3, 4],[5, 6]]
# m = [[1, 2, 3], [4, 5, 6]]
# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = tf(m)
# for i in res:
#   print(i)

# 方法2：
# m=[[1,2,3],[4,5,6],[7,8,9]]
m = [[1, 2, 3], [4, 5, 6]]
print(f'original:{m}')
print('new:    ', [[j[i] for j in m] for i in range(len(m[0]))])
