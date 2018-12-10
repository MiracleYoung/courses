#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 上午8:33
# @Author  : MiracleYoung
# @File    : test.py

import threading

def worker(x):
    print('work {}'.format(x))


for x in range(5):
    t = threading.Thread(target=worker, args=(x, ))
    t.start()