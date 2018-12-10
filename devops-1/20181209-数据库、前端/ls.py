import argparse, pathlib, stat, pwd, grp, datetime

parser = argparse.ArgumentParser(prog='python version ls.py', add_help=False)
parser.add_argument('-l', dest='long_format', help='', action='store_true')
parser.add_argument('-h', dest='human', help='', action='store_true')
parser.add_argument('-a', dest='all', help='', action='store_true')
parser.add_argument('path', nargs='*', default='.')

args = parser.parse_args()


def scan(path: str) -> pathlib.Path:
    # for item in pathlib.Path(path).iterdir():
    #     yield item

    # yield from pathlib.Path(path).iterdir()
    yield from (x for x in pathlib.Path(path).iterdir() if args.all or not x.name.startswith('.'))


def format(item: pathlib.Path) -> str:
    if not args.long_format:
        return item.name

    st = item.stat()
    attr = {
        'mode': stat.filemode(st.st_mode),
        'nlink': st.st_nlink,
        'user': pwd.getpwuid(st.st_uid).pw_name,
        'group': grp.getgrgid(st.st_gid).gr_name,
        'size': size_setup(st.st_size),
        'mtime': time_format(st.st_mtime),
        'name': item.name
    }
    return '{mode} {nlink} {user} {group} {size:>8} {mtime} {name}'.format(**attr)


def time_format(mtime: int) -> str:
    dt = datetime.datetime.fromtimestamp((mtime))
    return f'{dt.month:>2} {dt.day:>2} {dt.hour:>2}:{dt.minute:>2}'

def size_setup(size: int) -> str:
    if not args.human:
        return str(size)
    units = ['', 'K', 'M', 'G', 'T', 'P', 'B']
    idx = 0
    while size > 1024:
        size /= 1024
        idx += 1
    return f'{round(size, 1)}{units[idx]}'

def main():
    if isinstance(args.path, list):
        for path in args.path:
            print(f'{path}')
            for item in scan(path):
                print(format(item))
            print('')
    else:
        for item in scan(path):
            print(format(item))
        print('')

if __name__ == '__main__':
    main()