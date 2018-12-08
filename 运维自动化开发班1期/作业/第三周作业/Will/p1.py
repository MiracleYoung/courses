#!/usr/bin/env python
# coding: utf-8

'''
实现ls命令，起码实现 ls -al <path>
python 如何读取参数
python 如何 获取 文件及文件夹
python 如何获取 系统 参数
python ls.py -al /
'''

import os
import sys
import time
import pwd
import grp


def get_fileinfo(filename):
    stat = os.stat(filename)
    permission = oct(stat.st_mode)[-3:]
    link = stat.st_nlink
    uid = stat.st_uid
    gid = stat.st_gid
    user = pwd.getpwuid(uid)
    group = grp.getgrgid(gid)
    size = stat.st_size
    mtime = time.ctime(os.path.getmtime(filename))
    return permission, link, user.pw_name, group.gr_name, size, mtime


def print_fileinfo(flist):
    for f in flist:
        p, link, u, g, size, mtime = get_fileinfo(f)
        print(p, link, u, g, size, mtime, f)


if len(sys.argv) < 3:
    arg = sys.argv[1].strip()
    if arg == '-a':
        print(os.listdir(os.getcwd()))
    if arg == '-l' or arg == '-al':
        print_fileinfo(os.listdir(os.getcwd()))
elif len(sys.argv) == 3:
    arg = sys.argv[1].strip()
    path = sys.argv[2].strip()
    if arg == '-a':
        print(os.listdir(path))
    if arg == '-l' or arg == '-al':
        print_fileinfo(os.listdir(path))
