#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 上午7:38
# @Author  : MiracleYoung
# @File    : find.py

import argparse
import pathlib
import fnmatch
import stat

parser = argparse.ArgumentParser(prog='find')
parser.add_argument('path')
parser.add_argument('-name', dest='name', type=str)
parser.add_argument('-executable', dest='executable', action='store_true')

args = parser.parse_args()

def _walk(path: pathlib.Path):
    # 来一个深度优先遍历
    for item in path.iterdir():
        if item.is_dir():
            yield from _walk(item)
        yield item

def walk(path):
    yield from _walk(pathlib.Path(path))

if __name__ == '__main__':
    for item in walk(args.path):
        print(item)