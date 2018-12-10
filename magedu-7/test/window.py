#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 上午6:22
# @Author  : MiracleYoung
# @File    : window.py

import re
import datetime
import threading
from collections import namedtuple
import queue
import time

# 这个时候我的复制粘贴要来了
matcher = re.compile(
    r'(?P<remote>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>.*)\] "(?P<request>.*)" (?P<status>\d+) (?P<length>\d+) ".*" "(?P<ua>.*)"')
# 这个时候我们的matcher对象已经有了
# 接下来是我们的Request，我的复制粘贴又要来了
Request = namedtuple('Request', ['method', 'url', 'version'])

mapping = {
    'length': int,
    'request': lambda x: Request(*x.split()),
    'status': int,
    'time': lambda x: datetime.datetime.strptime(x, '%d/%b/%Y:%H:%M:%S %z'),

}


# 这是我们的提取函数
def extract(line):
    regex = r'(?P<remote>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>.*)\] "(?P<request>.*)" (?P<status>\d+) (?P<length>\d+) ".*" "(?P<ua>.*)"'
    m = re.match(regex, line)
    if m:
        ret = m.groupdict()
        return {k: mapping.get(k, lambda x: x)(v) for k, v in ret.items()}
    raise Exception(line)


## 写一个read函数
def read(f):
    for line in f:

        try:
            yield extract(line)
        except:
            pass


def load(path):
    with open(path) as f:
        while True:
            yield from read(f)
            time.sleep(1)


# 我们的window函数
def window(source, handler, interval: int, width: int):
    store = []
    start = None

    while True:
        data = next(source)

        store.append(data)
        current = data['time']

        if start is None:
            start = current

        if (current - start).total_seconds() >= interval:
            start = current

            # n
            # handler(store)
            try:
                handler(store)
            except:
                pass
            # en

            dt = current - datetime.timedelta(seconds=width)
            store = [x for x in store if x['time'] > dt]


# 我们的despatcher
def despatcher(source):
    analyers = []
    queues = []

    # n
    def _source(q):
        while True:
            yield q.get()

    # en

    def register(handler, interval, width):
        q = queue.Queue()
        queues.append(q)
        t = threading.Thread(target=window, args=(_source(q), handler, interval, width))
        analyers.append(t)

    def start():
        for t in analyers:
            t.start()
        for item in source:
            # print(item)
            for q in queues:
                q.put(item)

    return register, start


# 最后只要写一些处理函数
def null_handler(items):
    # print('null handler running')
    pass


# 这里的handler可以是任意多个handler
# 这里演示一个状态码的handler

def status_handler(items):
    # n
    if len(items) <= 0:
        return
    print(items[0]['time'])
    # en

    status = {}
    for x in items:
        if x['status'] not in status.keys():
            status[x['status']] = 0
            status[x['status']] += 1
            total = sum(x for x in status.values())
    for k, v in status.items():
        # n
        # print('{} => {}'.format(k, v / total * 100))
        print('\t{} => {:.2f}'.format(k, v / total * 100))
        # en


if __name__ == '__main__':
    import sys

    register, start = despatcher(load(sys.argv[1]))
    # 5秒钟分析一次，分析前10秒的东西
    register(null_handler, 5, 10)
    register(status_handler, 5, 10)
    start()
