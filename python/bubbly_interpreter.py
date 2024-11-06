environment = {}


def start(arg):
    return arg


def let(name):
    def inner(arg):
        environment[name] = arg

    return inner


def return_(arg):
    return arg


def add(a):
    def inner(b):
        return a + b

    return inner


def sub(a):
    def inner(b):
        return a - b

    return inner


def mul(a):
    def inner(b):
        return a * b

    return inner


def div(a):
    def inner(b):
        return a // b

    return inner
