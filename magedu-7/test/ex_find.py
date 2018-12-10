#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/19 5:48
# @Author  : Aries
# @Site    : 
# @File    : find.py
# @Software: PyCharm

# 首先还是少些几个参数
import argparse
import pathlib
import fnmatch
import stat

parser = argparse.ArgumentParser(prog='find')
parser.add_argument('path')
parser.add_argument('-name', dest='name', type=str)
parser.add_argument('-executable', dest='executable', action='store_true')

args = parser.parse_args()

# print(args)

# ipython 进行验证
# python find.py '*'
# python find.py '*' ./
# python find.py -name abc   -executable  '*'

# 所以我们需要先来定义一个walk函数，来递归遍历，因为涉及到目录的递归
# def walk(path):
#     # 来一个深度优先遍历
#     for item in pathlib.Path(path).iterdir():
#         if item.is_dir():
#             yield from walk(item.name)
#         yield item

# 我们先来测试下这个函数是否工作

# FileNotFoundError: [Errno 2] No such file or directory: '.idea'
# 说找不到文件，在包装下：
def _walk(path: pathlib.Path):
    # 来一个深度优先遍历
    for item in path.iterdir():
        if item.is_dir():
            yield from _walk(item)
        yield item

def walk(path):
    yield from _walk(pathlib.Path(path))

def is_name_match(item: pathlib.Path, pattern: str) -> bool:

    # 这里我们要来看看怎么做match哦
    # ipython中，item 若没有，则赋一个，item = pathlib.Path('~/.pyenv/versions')
    # item.glob('*version')
    # 这个是不对的吧返回的结果
    # 所以我们需要用另一个库
    # import fnmatch
    # help(glob.fnmatch)
    # fnmatch.fnmatch(str('magedu/w6/ls.py'), '*.py')
    # fnmatch.fnmatch(str('magedu/w6/ls.py'), '*.pyxx')

    return fnmatch.fnmatch(str(item), pattern)

def is_executable(item: pathlib.Path) -> bool:
    # 要根据我们的符号链接的，所以是lstat不是stat

    # return item.lstat().st_mode()

    # 我们要看下他是否是可执行的
    # ipython，stat.S_IEXEC
    # 需要与一下，stat.S_IEXEC & st.st_mode
    # p = pathlib.Path('ls.py')，
    # stat.S_IEXEC & p.stat().st_mode()
    # shell，附上可执行全行，chmod +x ls.py
    # stat.S_IEXEC & p.stat().st_mode()
    # 为什么会这样呢？因为他是一个可执行文件

    mode = item.lstat().st_mode
    return stat.S_IEXEC & mode > 0

# 再来一个filter，过滤器把
def filter(item: pathlib.Path) -> bool:
    ret = is_name_match(item, args.name)
    # parser.add_argument('-name', dest='name', type=str, default='*') 赋上一个初值,
    # 如果是可执行的，还需要在判断一次
    if args.executable:
        ret = ret and is_executable(item)
    # 如果还有gid，cid都在这里写就好了
    return ret

def main():
    for item in walk(args.path):
        if filter(item):
            print(item)

# main函数就需要修改成
# if __name__ == '__main__':
#     main()

# 我们来实测一把

# python find.py . -name '*.py'
# python find.py . -name '*.py' -executable


if __name__ == '__main__':
    for item in walk(args.path):
        # 测试下，python find.py ..
        # 有了吧，但是我们发现一个问题，他显示的不是全路径
        # print(item.name)

        # 所以修改成全路径
        # ok, 这就是我们的列出目录了, item.resolve()就是输出绝对路径，这里我们就相对路径就好了
        print(item)



# stat.S_IEXEC 这里64怎么来的呢？
# ipython
# import glob
# stat.S_IEXEC
# oct(stat.S_IEXEC)转化成八进制看看
# oct(stat.st_mode)，这样就能看出来了吧？它是通过八进制权限转换出来的
# oct(p.stat().st_mode) ，可以看到低位就是权限位，高位就是其他东西了
# stat.S_   的方法都是判断什么属性的
# 当然了也可以用os模块
# import os
# help(os.access)
# os.access('magedu/w6/', 64)

# 这里主要涉及到一个按位操作
# return stat.S_IEXEC & mode > 0
# bin(stat.S_IEXEC) 和 bin(mode)看看

# 这里离我们的真正的find 还差的很远





