"""
Реалізуйте свій аналог генераторної функції range().
"""
def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    current = start
    while current < stop:
        yield current
        current += step


for item in my_range(10):
    print(item)


