def f1(x):
    return x * x + 1


def f2(x):
    return 1 / (x * x)


def f3(x):
    val = (x * x) - 1
    return val


def f(x):
    if x <= 0:
        return f1(x)
    elif 0 < x < 1:
        return f2(x)
    elif x >= 1:
        return f3(x)
