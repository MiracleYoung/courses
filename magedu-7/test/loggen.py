#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 上午6:38
# @Author  : MiracleYoung
# @File    : loggen.py

import sys
import time

with open(sys.argv[1]) as r:
    with open(sys.argv[2], 'w') as w:
        for line in r:
            w.write(line)
            w.flush()
            time.sleep(1)



