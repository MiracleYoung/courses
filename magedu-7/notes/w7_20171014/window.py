#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 17:38
# @File    : window.py
# @Software: PyCharm

import datetime
import random
import time
import re
from collections import namedtuple
import queue
import threading

matcher = re.compile(
    r'(?P<remote>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>.*)\] "(?P<request>.*)" (?P<status>\d+) (?P<length>\d+) ".*" "(?P<ua>.*)"')  # 捕获
Request = namedtuple('Request', ['method', 'url', 'version'])
mapping = {
    'length': int,
    'request': lambda x: Request(*x.split()),
    'status': int,
    'time': lambda x: datetime.datetime.strptime(x, '%d/%b/%Y:%H:%M:%S %z'),
}


def extract(line):
    m = matcher.match(line)
    if m:
        ret = m.groupdict()
        return {k: mapping.get(k, lambda x: x)(v) for k, v in ret.items()}
    raise Exception(line)


def read(f):
    for line in f:
        # print(line)
        try:

            yield extract(line)
        except:
            pass

def load(path):
    # print(path)
    with open('./access.log') as f:
        while True:
            yield from read(f)
            time.sleep(1)


def window(source, handler, interval: int, width: int):
    store = []
    # start = datetime.datetime.now()
    start = None

    while True:
        data = next(source)
        # data = source()
        # data = source.get()
        # current = datetime.datetime.now()
        # if data:
        store.append(data)
        current = data['time']

        if start is None:
            start = current

        # 窗口什么时候后移？
        if (current - start).total_seconds() >= interval:
            # TODO 3件事情
            start = current

            try:
                handler(store)
            except:
                pass
            # 窗口如何后移？
            dt = current - datetime.timedelta(seconds=width)
            store = [x for x in store if x['time'] > dt]


def source():
    while True:
        yield {'time': datetime.datetime.now(), 'value': random.randint(0, 100)}
        time.sleep(1)


def handler(items):
    values = [x['value'] for x in items]
    print(sum(values) / len(values))


def despatcher(source):
    analyers = []

    queues = []

    def _source(q):
        while True:
            yield q.get()

    def register(handler, interval, width):

        q = queue.Queue()
        queues.append(q)
        t = threading.Thread(target=window, args=(_source(q), handler, interval, width))

        # analyers.append(window(source, handler, interval, width))
        analyers.append(t)

    def start():
        for t in analyers:
            t.start()
        for item in source:
            # print(item)
            for q in queues:
                q.put(item)

    return register, start


def null_handler(items):
    # print('null handler running')
    pass


def status_handler(items):
    # print('status handler running')
    if len(items) <= 0:
        return
    print(items[0]['time'])

    status = {}
    for x in items:
        if x['status'] not in status.keys():
            status[x['status']] = 0
            status[x['status']] += 1
            total = sum(x for x in status.values())

    for k, v in status.items():
        print('\t{} => {:.2f}'.format(k, v / total * 100))


if __name__ == '__main__':
    import sys
    register, start = despatcher(load(sys.argv[1]))
    register(null_handler, 5, 10)
    register(status_handler, 5, 10)
    start()
