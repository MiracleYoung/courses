# 因为我们要接受参数，所以我们需要引入这个库
# argparse 基于我们的optpars，optparse现在已经不维护了

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

# 我们来打印一下
# print(args)

# 我们先来看看当前路径是不是可行
# python ls.py
# python ls.py -l
# python ls.py -l . / 看到path已经变成一个list了
# python ls.py -lha
# 这就是我们的参数解析，已经ok了，接下来我们来写代码
# 在mac上可以看到是运行的

# 大家想一下ls是不是要先列出我们的目录，怎么办呢？我们ipython里试试
# import pathlib
# p = pathlib.Path('~/Project/workspace')
# p.iterdir() 这是一个生成器，可以列出目录
# item = next(p.iterdir()) 就完成了


# 引入pathlib库

def scan(path: str) -> pathlib.Path:
    # 我们可以不要这个for 循环
    # for item in pathlib.Path(path).iterdir():
    #     yield item
    # yield from pathlib.Path(path).iterdir()

    # 为了处理-a,上面的for循环改成下面的
    yield from (x for x in pathlib.Path(path).iterdir() if args.all or not x.name.startswith('.'))


    # 如果这里只是3个选项我们就完成了，但是还有一个l，所以我们需要一个format函数，控制格式

def time_format(mtime: int) -> str:
    dt = datetime.datetime.fromtimestamp((mtime))
    # 为什么这里不用时间，因为需要满足我们的格式
    return '{:>2} {:>2} {:>2}:{:>2}'.format(dt.month, dt.day, dt.hour, dt.minute)

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
        # 我们来看看ls -l列出来的格式
        return item.name
    # 在ipython里操作，item.stat()，就可以得到我们的mode了，包括我们后面的link，gid，cid都可以得到，所以我们先求出他的stat
    # 这个时候我们有更好的办法，import stat
    # st = item.stat()
    # stat.filemode(item.stat().st_mode)
    # 所以引入stat库
    st = item.stat()
    attr = {
        'mode': stat.filemode(st.st_mode),
        'nlink': st.st_nlink,
        # 我们可以引用pwd，在ipython里写，
        # import pwd
        # st = item.stat()
        # pwd.getpwuid(st.st_uid)
        # pwd.getpwuid(st.st_uid).pw_name
        # 也可以用item.owner()
        'user': pwd.getpwuid(st.st_uid).pw_name,
        # 这里需要引入grp库
        # 也可以用item.group()
        'group': grp.getgrgid(st.st_gid).gr_name,
        # 主要影响的是我们的size，所以需要写一个处理size的函数
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