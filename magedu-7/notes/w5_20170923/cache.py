def cache(exp=0):
    def _cache(fn):
        cache = {}
        @functools.wraps(fn)
        def wrap(*args, **kwargs):
            key = []

            # 对默认值进行 预处理
            # 需要把默认值  和 其参数 存储起来
            # names 中存储的是什么？是我们的参数key
            # 默认值不需要存储，因为 可以通过v.default
            names = set()

            # 处理位置参数
            params = inspect.signature(fn).parameters
            for i, arg in enumerate(args):
                name = list(params.keys())[i]
                key.append((name, arg))

                names.add(name)

            # 关键字参数
            # for k, v in kwargs.items():
            #    key.append((k, v))

            key.extend(kwargs.items())
            names.update(kwargs.keys())

            # 如果 参数中 有默认值，就需要 往key中添加一对 k-v 对
            for k, v in params.items():
                if k not in names:
                    key.append((k, v.default))

            key.sort(key=lambda x: x[0])

            key = '&'.join(['{}={}'.format(name, arg) for name, arg in key])

            print(key)


            # TODO key 如何瓶装
            if key in cache.keys():
                # TODO 超时检测
                # key -> 'x=1&y=3&timestamp=12345678'
                ret, timestamp = cache[key]
                if exp == 0 or datetime.datetime.now().timestamp() - timestamp < exp:

                    print('cache hit')
                    return cache[key]
            ret = fn(*args, **kwargs)
            cache[key] = (ret, datetime.datetime.now().timestamp())
            print('cache miss')
            return ret
        return wrap
    return _cache
