#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 9:18
# @Site    : 
# @File    : ls.py
# @Software: PyCharm


import argparse

import pathlib
import stat
import datetime

parser = argparse.ArgumentParser(prog='ls', add_help=False)

parser.add_argument('-l', dest='long_format', help='', action='store_true')

parser.add_argument('-h', dest='human', help='', action='store_true')

parser.add_argument('-a', dest='all', help='', action='store_true')

parser.add_argument('path', nargs='*', default='.')

args = parser.parse_args() # 把参数解析出来了

# print(args.all)

def scan(path: str) -> pathlib.Path:
    # for item in pathlib.Path(path).iterdir():
    #     yield item

    yield from (x for x in pathlib.Path(path).iterdir() if args.all or not x.name.startswith('.'))

def format(item: pathlib.Path) -> str:
    if not args.long_format:
        return item.name
    # TODO
    # 如果有-l 参数
    st = item.stat()
    attr = {
        'mode': stat.filemode(item.stat().st_mode),
        'nlink': st.st_nlink,
        'user': item.owner(),
        'group': item.group(),
        'size': size_setup(st.st_size),
        'mtime': time_format(st.st_mtime),
        'name': item.name
    }
    return '{mode} {nlink} {user} {group} {size} {mtime} {name}'.format(**attr)

def time_format(mtime: int) -> str:
    dt = datetime.datetime.fromtimestamp(mtime)

    return '{:>2} {:>2} {:>2}:{:>2}'.format(dt.month, dt.day, dt.hour, dt.minute)


def size_setup(size: int) -> str:
    if not args.human:
        return str(size)

    units = ['', 'K', 'M', 'G', 'T', 'P', 'B']
    idx = 0
    while size > 1024:
        size /= 1024
        idx += 1
    return '{}{}'.format(round(size, 1), units[idx])



def main():
    if isinstance(args.path, list):
        for path in args.path:
            print('{}'.format(path))
            for item in scan(path):
                print(format(item))
            print()
    else:
        for item in scan(args.path):
            print(format(item))

if __name__ == '__main__':
    main()