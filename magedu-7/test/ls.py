#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 上午6:50
# @Author  : MiracleYoung
# @File    : find1.py

import argparse
import stat
import pathlib
import pwd
import grp
import datetime

parser = argparse.ArgumentParser(prog='ls', add_help=False)

# 这里的选项能看懂吗？没看懂的打0哦，没看过文档的打2
parser.add_argument('-l', dest='long_format', help='', action='store_true')

# argparse 大家自己看文档，一定要学会自己看文档
parser.add_argument('-h', dest='human', help='', action='store_true')
# 然后呢，我们再增加一个
parser.add_argument('-a', dest='all', help='', action='store_true')

# argument我们已经增加上去了，现在把他parse出来，当然了，我们这里还少一个东西，path
# 我们的path是可以有多个的，所以是*
parser.add_argument('path', nargs='*', default='.')

# 这样我们就可以来解析我们的参数了

args = parser.parse_args()

print(args)


def scan(path: str) -> pathlib.Path:
    # 我们可以不要这个for 循环
    # for item in pathlib.Path(path).iterdir():
    #     yield item
    # yield from pathlib.Path(path).iterdir()

    # 为了处理-a,上面的for循环改成下面的
    yield from (x for x in pathlib.Path(path).iterdir() if args.all or not x.name.startswith('.'))


def time_format(mtime: int) -> str:
    dt = datetime.datetime.fromtimestamp((mtime))
    # 为什么这里不用时间，因为需要满足我们的格式
    # 这里的 {:>2} 是string format 的格式，表示 长度要大于2，这是为了保证我们格式的统一性
    return '{:>2} {:>2} {:>2}:{:>2}'.format(dt.month, dt.day, dt.hour, dt.minute)


# 需要一个计算文件大小的函数
def size_setup(size: int) -> str:
    if not args.human:
        return str(size)
    units = ['', 'K', 'M', 'G', 'T', 'P', 'B']
    idx = 0
    while size > 1024:
        size /= 1024
        idx += 1
        # 有可能小数点太多，所以需要一个round
    return '{}{}'.format(round(size, 1), units[idx])


def format(item: pathlib.Path) -> str:
    if not args.long_format:
        return item.name
    st = item.stat()
    attr = {
        'mode': stat.filemode(st.st_mode),
        'nlink': st.st_nlink,
        'user': pwd.getpwuid(st.st_uid).pw_name,
        'group': grp.getgrgid(st.st_gid).gr_name,
        # n
        'size': size_setup(st.st_size),
        'mtime': time_format(st.st_mtime),
        'name': item.name
    }
    return '{mode} {nlink} {user} {group} {size} {mtime} {name}'.format(**attr)


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
    # en
