import os


def read_file(path):
    ctx = ''
    if os.path.isfile(path):
        with open(path, 'rb') as handlers:
            ctx = handlers.read()
        ctx = ctx.decode()
    return ctx


def write_file(path, ctx):
    if not isinstance(ctx, bytes):
        ctx = str(ctx).encode()
    with open(path, 'wb') as handler:
        handler.write(ctx)

    return True
