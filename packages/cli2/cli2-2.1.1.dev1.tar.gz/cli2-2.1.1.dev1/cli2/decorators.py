

def cmd(**overrides):
    def wrap(cb):
        cb.cli2 = overrides
        return cb
    return wrap


def arg(name, **overrides):
    def wrap(cb):
        setattr(cb, 'cli2_' + name, overrides)
        return cb
    return wrap
