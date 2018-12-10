#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 上午8:03
# @Author  : MiracleYoung
# @File    : watch.py

import sys
import time
import logging
from watchdog.observers import Observer

# 看到这里，他是一个什么？observer，观察者模式
from watchdog.events import LoggingEventHandler

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except  KeyboardInterrupt:
        observer.stop()
    observer.join()