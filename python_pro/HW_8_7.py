def cache_results(func):
    cache = {}

    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return inner


@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))  # Обчислюється
print(fibonacci(10))  # Використання кешу
