def rect1(x, y):
    print('*' * x)
    for i in range(y - 2):
        print('*', ' ' * (x - 2), '*', sep='')
    print('*' * x)


rect1(4, 5)
