def myfunc(*args):

    sum = 0
    for arg in args:
        if isinstance(arg, int) and arg % 2 == 0:
            sum += arg
    return sum
myfunc(1, 2, 'Hello', 4, 3)